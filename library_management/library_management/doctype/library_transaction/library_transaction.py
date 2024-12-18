import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryTransaction(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            # set the article status to be Issued
            article = frappe.get_doc("Article", self.article)
            article.quantity = article.quantity - 1
            if article.quantity == 0:
                article.status = "Issued"    
            article.save()
        elif self.type == "Return":
            self.validate_return()
            # set the article status to be Available
            article = frappe.get_doc("Article", self.article)
            article.quantity = article.quantity + 1
            if article.quantity == 1:
                article.status = "Available"
            article.save()

    def after_insert(self):
        # Create a To-Do entry
        self.create_todo_entry()

    def create_todo_entry(self):
        # Fetch the article name from the transaction
        article = self.article  # Assuming article_name is a field in Library Transaction

        # Create a new ToDo entry
        todo = frappe.get_doc({
            "doctype": "ToDo",
            "description": f"{article}",
            "assigned_by": frappe.session.user,
            "reference_type": "Library Transaction",
            "reference_name": self.name,  # Link to the current transaction
            "priority": "Medium",  # Optional: Set priority
            "status": "Open"  # Default status
        })
        todo.insert(ignore_permissions=True)  # Ignore permissions to allow creation
        frappe.db.commit()  # Commit the transaction

    def validate_issue(self):
        self.validate_membership()
        article = frappe.get_doc("Article", self.article)
        # article cannot be issued if it is already issued
        if article.status == "Issued":
            frappe.throw("Article is already issued by another member")

    def validate_return(self):
        article = frappe.get_doc("Article", self.article)
        # article cannot be returned if it is not issued first
        if article.status == "Available":
            frappe.throw("Article cannot be returned without being issued first")

    def validate_membership(self):
        # check if a valid membership exist for this library member
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                "from_date": ("<", self.date),
                "to_date": (">", self.date),
            },
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")

