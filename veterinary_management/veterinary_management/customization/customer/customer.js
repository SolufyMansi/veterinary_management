// frappe.ui.form.on("Customer", {
//     refresh: function(frm) {
//         // Remove standard buttons
//         frm.remove_custom_button("Create");
//         frm.remove_custom_button("View");
//         frm.remove_custom_button("Actions");
//         frm.remove_custom_button("Accounts Receivable");
//         frm.remove_custom_button("Accounting Ledger");
//     }
// });
frappe.ui.form.on("Customer", {
    refresh: function(frm) {
        frm.page.wrapper.find(".page-actions .dropdown-toggle").hide();
        frm.page.wrapper.find(".page-actions .btn").hide();           
        frm.page.wrapper.find(".standard-actions").hide();          
    }
});
