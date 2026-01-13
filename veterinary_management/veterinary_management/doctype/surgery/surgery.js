// Copyright (c) 2026, Solufy and contributors
// For license information, please see license.txt

frappe.ui.form.on("Surgery", {
	refresh(frm) {
        invoice_btn=frm.add_custom_button(__('Sales Invoice'), function () {
            frappe.route_options = {
                    "customer": frm.doc.pet_owner,
                    "custom_surgery":frm.doc.name,
                    "due_date":frm.doc.surgery_date

                };
                frappe.set_route("Form", "Sales Invoice", "new-sales invoice Record");
 
	},"Create");
        // invoice_btn.css({
        //    "background-color": "black",
        //     "color": "white",
        //     "font-weight": "bold"
        // });
    
}
});
