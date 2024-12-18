frappe.ui.form.on('Library Member', {
    refresh: function(frm) {
        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Library Membership', {
                library_member: frm.doc.name
            });
        });
        frm.add_custom_button('Create Transaction', () => {
            frappe.new_doc('Library Transaction', {
                library_member: frm.doc.name
            });
        });
    }
});

frappe.ui.form.on('Library Member', {
    refresh: function(frm) {
        frm.add_custom_button("Get Member Details", function() {
            frappe.prompt(
                {
                    fieldname: 'member_id',
                    fieldtype: 'Data',
                    label: 'Member ID',
                    reqd: 1
                },
                function(values) {
                    frappe.call({
                        method: "library_management.library_management.doctype.library_member.library_member.get_member_details",
                        args: {
                            member_id: values.member_id
                        },
                        callback: function(response) {
                            if (response.message.success) {
                                const data = response.message.data;
                                // Correct string concatenation using backticks for template literals
                                const message = `
                                    Name: ${data.name} <br>
                                    Email: ${data.email} <br>
                                    Phone: ${data.phone}
                                `;
                                frappe.msgprint(message);
                            } else {
                                frappe.msgprint(response.message.message || "Error fetching member details.");
                            }
                        }
                    });
                },
                'Enter Member ID',
                'Get Details'
            );
        });
    }
});
