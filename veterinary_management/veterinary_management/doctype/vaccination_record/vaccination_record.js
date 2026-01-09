// Copyright (c) 2025, Solufy and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vaccination Record", {
    after_save(frm) {
        if(frm.doc.status == "Vaccinated" && frm.doc.appointment) {
            frappe.call({
                method: "frappe.client.get",
                args: {
                    doctype: "Appointment",
                    name: frm.doc.appointment
                },
                callback: function(r) {
                    if(r.message) {
                        let appointment_doc = r.message;
                        appointment_doc.status = "Completed"; 
                        frappe.call({
                            method: "frappe.client.save",
                            args: {
                                doc: appointment_doc
                            },
                            callback: function(save_response) {
                                if(save_response.message) {
                                    frappe.msgprint("Appointment Completed.");
                                }
                            }
                        });
                    }
                }
            });
        }
    }
});
