frappe.ui.form.on('ToDo', {
    refresh(frm) {

        if (frm.doc.status === "Open" && !frm.is_new()) {
                let apr_btn = frm.add_custom_button(__('Book Appointment'), function () {
                    let d = new frappe.ui.Dialog({
                        title: 'Book Surgery Appointment',
                        fields: [
                            {
                                label: 'Doctor',
                                fieldname: 'doctor',
                                fieldtype: 'Link',
                                options: 'Employee',
                                default:frm.doc.custom_doctor,
                            },
                           {
                                label: 'Scheduled Date',
                                fieldname: 'scheduled_date',
                                fieldtype: 'Date',
                                default:frm.doc.date
                            },
                            {
                                label: 'Time',
                                fieldname: 'scheduled_time',
                                fieldtype: 'Time',
                                default:frm.doc.custom_surgery_time
                            },
                            {
                                label: 'Surgery Type',
                                fieldname: 'surgery_type',
                                options: 'Surgery Type',
                                fieldtype: 'Link'
                            },
                        ],
                        primary_action_label: 'Book Appointment',
                        primary_action(values) {
                            frappe.call({
                                method: "frappe.client.insert",
                                args: {
                                    doc: {
                                        doctype: "Appointment",
                                        custom_scheduled_date: values.scheduled_date,
                                        status: "Scheduled",
                                        custom_schedule_time: values.scheduled_time,
                                        custom_surgery_type: values.surgery_type,
                                        custom_doctor:values.doctor,
                                        description: frm.doc.description,
                                        custom_pet: frm.doc.custom_patient,
                                        custom_reason: "Surgery"
                                    }
                                },
                                callback: function (r) {
                                    if (r.message) {
                                        frappe.set_route("Form", "Appointment", r.message.name);
                                        frappe.msgprint("Appointment Cretaed successfully")
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
    }
});
