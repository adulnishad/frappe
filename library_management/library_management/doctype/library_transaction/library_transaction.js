
// frappe.ui.form.on('Library Transaction', {
//     after_save: function (frm) {
//         if (frm.doc.article) {
//             // Create a To-Do entry
//             frappe.call({
//                 method: "frappe.client.insert",
//                 args: {
//                     doc: {
//                         doctype: "ToDo",
//                         description: `Follow up on Article: ${frm.doc.article}`,
//                         assigned_by: frappe.session.user,
//                         reference_type: "Library Transaction",
//                         reference_name: frm.doc.name,
//                         date: frappe.datetime.nowdate(),  // Optional: Set a due date
//                         owner: frm.doc.member // Assign to the member if relevant
//                     },
//                 },
//                 callback: function (response) {
//                     if (!response.exc) {
//                         frappe.msgprint(__('To-Do created for the article: ' + frm.doc.article_name));
//                     }
//                 },
//             });
//         }
//     }
// });
