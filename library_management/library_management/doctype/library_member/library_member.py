# Copyright (c) 2024, Adul Nishad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
    #this method will run every time a document is saved
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'





@frappe.whitelist()
def get_member_details(member_id):
    try:
        # Fetch the Library Member document by member_id
        member = frappe.get_doc("Library Member", member_id)
        
        # Prepare the data to send back
        data = {
            "name": member.full_name,
            "email": member.email_address,
            
            "phone": member.phone
        }
        
        return {"success": True, "data": data}
    except frappe.DoesNotExistError:
        return {"success": False, "message": "Member not found."}
    except Exception as e:
        return {"success": False, "message": str(e)}

