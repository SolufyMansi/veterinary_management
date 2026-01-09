// Copyright (c) 2026, Solufy and contributors
// For license information, please see license.txt

frappe.ui.form.on('Patient', {
    dob: function (frm) {
        if (frm.doc.dob) {
            let today = frappe.datetime.get_today();
            let dob = frm.doc.dob;
            let birthDate = new Date(dob);
            let currentDate = new Date(today);
            let diff = currentDate - birthDate;
            let age = Math.floor(diff / (1000 * 60 * 60 * 24 * 365.25));

            frm.set_value('age', age);
        } else {
            frm.set_value('age', '');
        }
    },
refresh: function (frm) {
    let apr_btn = frm.add_custom_button(__('Book Appointment'), function () {

        let d = new frappe.ui.Dialog({
            title: 'Book Appointment',
            fields: [
                {
                    label: 'Pet',
                    fieldname: 'pet',
                    fieldtype: 'Link',
                    options: 'Pet',
                    default: frm.doc.name,
                    read_only: 1
                },
                {
                    label: 'Pet Owner',
                    fieldname: 'pet_owner',
                    fieldtype: 'Link',
                    options: 'Customer',
                    default: frm.doc.customer,
                    read_only: 1
                },
                {
                    label: 'Status',
                    fieldname: 'status',
                    fieldtype: 'Select',
                    options: ['Scheduled','Completed','Cancelled'],
                    default: "Scheduled",
                    read_only: 1
                },
                {
                    label: 'Appointment Date',
                    fieldname: 'scheduled_date',
                    fieldtype: 'Date',
                    reqd: 1,
                    default:"Today",
                },
                 {
                    label: 'Appointment Time',
                    fieldname: 'schedule_time',
                    fieldtype: 'Time',
                    reqd: 1,
                },
                {
                    label: 'Doctor',
                    fieldname: 'doctor',
                    fieldtype: 'Link',
                    options:'Employee'
                },
                {
                    label: 'Reason',
                    fieldname: 'reason',
                    fieldtype: 'Select',
                    options: ['Check-Up','Consultation','Vaccination']
                                },
            ],
            primary_action_label: 'Create Appointment',
            primary_action(values) {
                frappe.call({
                    method: "frappe.client.insert",
                    args: {
                        doc: {
                            doctype: "Appointment",
                            custom_pet: values.pet,
                            custom_pet_owner: values.pet_owner,
                            custom_schedule_time: values.schedule_time,
                            status :values.status,
                            custom_doctor:values.doctor,
                            custom_scheduled_date:values.scheduled_date,
                            custom_reason:values.reason
                        }
                    },
                    callback: function (r) {
                        if (r.message) {
                            frappe.set_route("Form", "Appointment", r.message.name);
                            frappe.msgprint("Appointment created successfully")
                            d.hide();
                        }
                    }
                });
            }
        });

        d.show();
    });

    apr_btn.css({
        "background-color": "black",
        "color": "white",
        "font-weight": "bold"
    });
}

    
});