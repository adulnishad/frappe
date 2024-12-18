frappe.ui.form.on('Stock Log', {
    before_save: function (frm) {
        // Fetch Quantity value from a linked Doctype
        frappe.call({
            method: 'frappe.client.get',
            args: {
                doctype:'Article', // Replace with the linked Doctype name
                name: frm.doc.article_id// Replace 'article_id' with the actual field name
            },
            callback: function (response) {
                if (response.message) {
                    const quantity = response.message.quantity; // Adjust the field name as needed
                    // Update a custom HTML field in the form
                    frm.doc.set_db('Stock Log',quantity);
                }
            }
        });
    }
});
