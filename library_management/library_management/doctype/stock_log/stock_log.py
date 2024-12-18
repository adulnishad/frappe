from frappe.model.document import Document
import frappe

class StockLog(Document):
   
    def on_update(self):
        # You can update the Article when Stock Log is updated as well
        if self.article_id:
            article = frappe.get_doc("Article", self.article_id)
            
            # Update the Article based on your logic
            article.quantity = article.quantity + self.quantity
            article.save()
    