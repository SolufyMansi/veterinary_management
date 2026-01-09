// Copyright (c) 2025, Solufy and contributors
// For license information, please see license.txt

frappe.ui.form.on("Appointment", {
    refresh(frm) {
        if (frm.doc.lead) {
            frm.remove_custom_button(__(frm.doc.lead));
        }
        frm.remove_custom_button(__(frm.doc.calendar_event));
        let apr_btn = null;
        let check_btn = null;

        if (frm.doc.custom_reason == "Vaccination") {
            apr_btn = frm.add_custom_button(__('Vaccination'), function () {
                let d = new frappe.ui.Dialog({
                    title: 'Vaccination',
                    fields: [
                        {
                            label: 'Patient Name',
                            fieldname: 'animal',
                            fieldtype: 'Link',
                            options: 'Patient',
                            default: frm.doc.custom_pet,
                            read_only: 1
                        },
                        {
                            label: 'Vaccine',
                            fieldname: 'vaccine',
                            fieldtype: 'Link',
                            options: 'Item',
                            reqd: 1
                        },
                        {
                            label: 'Date Administered',
                            fieldname: 'date_administered',
                            fieldtype: 'Date',
                            reqd: 1
                        },
                        {
                            label: 'Next Due Date',
                            fieldname: 'next_due_date',
                            fieldtype: 'Date',
                        },
                    ],
                    primary_action_label: 'Create Vaccination Record',
                    primary_action(values) {
                        frappe.call({
                            method: "frappe.client.insert",
                            args: {
                                doc: {
                                    doctype: "Vaccination Record",
                                    animal: values.animal,
                                    vaccine: values.vaccine,
                                    date_administered: values.date_administered,
                                    next_due_date: values.next_due_date,
                                    appointment: frm.doc.name
                                }
                            },
                            callback: function (r) {
                                if (r.message) {
                                    frappe.set_route("Form", "Vaccination Record", r.message.name);
                                    frappe.msgprint('Vaccination Record submitted successfully.')
                                    d.hide();
                                }
                                frm.set_value("status", "Completed")
                                frm.save()
                            }
                        });
                    }
                });

                d.show();
            });

            if (apr_btn) {
                apr_btn.css({
                    "background-color": "black",
                    "color": "white",
                    "font-weight": "bold"
                });
            }
        } else if (frm.doc.custom_reason == "Consultation" && !frm.is_new()) {

            apr_btn = frm.add_custom_button(__('Consultation'), function () {
                frappe.route_options = {
                    "appointment": frm.doc.name,
                    "patient": frm.doc.custom_pet,
                    "doctor": frm.doc.custom_doctor
                };
                frappe.set_route("Form", "Consultation", "new-consultation");
            });

            if (apr_btn) {
                apr_btn.css({
                    "background-color": "black",
                    "color": "white",
                    "font-weight": "bold"
                });
            }
        } else if (frm.doc.custom_reason == "Check-Up" && !frm.is_new()){
            check_btn = frm.add_custom_button(__('Check-Up'), function () {
                frappe.route_options = {
                    "patient": frm.doc.custom_pet,
                    "appointment": frm.doc.name,
                    "status": "Completed",

                };
                frappe.set_route("Form", "Check-Up Record", "new-Check-Up Record");
            });

            if (check_btn) {
                check_btn.css({
                    "background-color": "black",
                    "color": "white",
                    "font-weight": "bold"
                });
            }
        }
        // else if (frm.doc.custom_reason == "Surgery" && !frm.is_new()){
        //     check_btn = frm.add_custom_button(__('Surgery'), function () {
        //         frappe.route_options = {
        //             "patient": frm.doc.custom_pet,
        //             "appointment": frm.doc.name,
        //             "status": "Completed",

        //         };
        //         frappe.set_route("Form", "Check-Up Record", "new-Check-Up Record");
        //     });

        //     if (check_btn) {
        //         check_btn.css({
        //             "background-color": "black",
        //             "color": "white",
        //             "font-weight": "bold"
        //         });
        //     }
        // }
    }
});

frappe.ui.form.on('Appointment', {
    custom_duration: function(frm) {
        if (frm.doc.custom_scheduled_date && frm.doc.custom_schedule_time && frm.doc.custom_duration) {
            let startTime = moment(frm.doc.custom_scheduled_date + ' ' + frm.doc.custom_schedule_time, 'YYYY-MM-DD HH:mm');
            let endTime = startTime.add(frm.doc.custom_duration, 'minutes');
            let formattedEndTime = endTime.format('HH:mm:ss');
            frm.set_value('custom_scheduled_end_time', formattedEndTime);
        }
    },

    custom_schedule_time: function(frm) {
        if (frm.doc.custom_scheduled_date && frm.doc.custom_schedule_time && frm.doc.custom_duration) {
            let startTime = moment(frm.doc.custom_scheduled_date + ' ' + frm.doc.custom_schedule_time, 'YYYY-MM-DD HH:mm');
            let endTime = startTime.add(frm.doc.custom_duration, 'minutes');
            let formattedEndTime = endTime.format('HH:mm:ss');
            frm.set_value('custom_scheduled_end_time', formattedEndTime);
        }
    },

    custom_scheduled_date: function(frm) {
        if (frm.doc.custom_scheduled_date && frm.doc.custom_schedule_time && frm.doc.custom_duration) {
            let startTime = moment(frm.doc.custom_scheduled_date + ' ' + frm.doc.custom_schedule_time, 'YYYY-MM-DD HH:mm');
            let endTime = startTime.add(frm.doc.custom_duration, 'minutes');
            let formattedEndTime = endTime.format('HH:mm:ss');
            frm.set_value('custom_scheduled_end_time', formattedEndTime);
        }
    }
});
