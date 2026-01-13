// Copyright (c) 2025, Solufy and contributors
// For license information, please see license.txt
frappe.ui.form.on("Consultation", {
    refresh(frm) {
        if (frm.doc.lab_test_required) {
            let apr_btn = frm.add_custom_button(__('Lab Test'), function () {
                let d = new frappe.ui.Dialog({
                    title: 'Lab Test Report For',
                    fields: [
                        {
                            label: 'Test Type',
                            fieldname: 'test_type',
                            fieldtype: 'MultiSelect',
                            options: 'Blood\nUrine\nFecal\nX-Ray\nUltrasound\nHeartworm\nSkin Scraping\nBlood Pressure Measurement\nBiopsy\nAllergy\nParasite\nLiver Function\nKidney Function\nElectrocardiogram (ECG)\nCholesterol\nGlucose\nThyroid\nBacterial Culture\nVirus\nVaccination Records\nImmunization Titers\nCytology'
                        }
                    ],
                    primary_action_label: 'Create Lab Test Report',
                    primary_action(values) {
                        let selected_test_types = values.test_type.split('\n').join(',');
                        console.log("Selected Test Types: ", selected_test_types);
                        frm.call({
                            method: 'create_lab_test_result',
                            doc: frm.doc,
                            args: {
                                patient: frm.doc.patient,
                                test_types: selected_test_types, 
                                appointment: frm.doc.appointment, 
                                reference_doctype: "Consultation",  
                                reference_name: frm.doc.name
                            },
                            callback: function(response) {
                                if (response.message) {
                                    frappe.msgprint(response.message);  
                                    d.hide();  
                                }
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
        }
        else if (frm.doc.surgery_required && !frm.is_new()){
                // let apr_btn = frm.add_custom_button(__('Book Surgery Appointment'), function () {

                //     let d = new frappe.ui.Dialog({
                //         title: 'Book Surgery Appointment',
                //         fields: [
                //             {
                //                 label: 'Pet Id',
                //                 fieldname: 'pet',
                //                 fieldtype: 'Link',
                //                 options: 'Pet',
                //                 default: frm.doc.patient,
                //                 read_only: 1
                //             },
                //              {
                //                 label: 'Pet Name',
                //                 fieldname: 'pet_name',
                //                 fieldtype: 'Data',
                //                 default: frm.doc.patient_name,
                //                 read_only: 1
                //             },
                //             // {
                //             //     label: 'Pet Owner',
                //             //     fieldname: 'pet_owner',
                //             //     fieldtype: 'Link',
                //             //     options: 'Customer',
                //             //     default: frm.doc.customer,
                //             //     read_only: 1
                //             // },
                //             {
                //                 label: 'Status',
                //                 fieldname: 'status',
                //                 fieldtype: 'Select',
                //                 options: ['Scheduled','Completed','Cancelled'],
                //                 default: "Scheduled",
                //                 read_only: 1
                //             },
                //             // {
                //             //     label: 'Appointment Date',
                //             //     fieldname: 'scheduled_date',
                //             //     fieldtype: 'Date',
                //             //     reqd: 1
                //             // },
                //             //                             {
                //             //     label: 'Time',
                //             //     fieldname: 'scheduled_time',
                //             //     fieldtype: 'Time',
                //             //     reqd: 1
                //             // },
                //             {
                //                 label: 'Surgery Type',
                //                 fieldname: 'surgery_type',
                //                 fieldtype: 'Link',
                //                 options:'Surgery Type',
                //                 reqd: 1
                //             },
                //             {
                //                 label: 'Doctor',
                //                 fieldname: 'doctor',
                //                 fieldtype: 'Link',
                //                 options:'Employee'
                //             },
                //             {
                //                 label: 'Reason',
                //                 fieldname: 'reason',
                //                 fieldtype: 'Select',
                //                 options: ['Check-Up','Consultation','Vaccination','Surgery'],
                //                 default:"Surgery"
                //                             },
                //         ],
                //         primary_action_label: 'Send Appointment Dr Approval',
                //         primary_action(values) {
                //             frappe.call({
                //                 method: "frappe.client.insert",
                //                 args: {
                //                     doc: {
                //                         doctype: "Appointment",
                //                         custom_pet: values.pet,
                //                         // custom_scheduled_date: values.scheduled_date,
                //                         // custom_schedule_time: values.scheduled_time,
                //                         // custom_pet_owner: values.pet_owner,
                //                         status :values.status,
                //                         custom_doctor:values.doctor,
                //                         custom_reason:values.reason,
                //                         custom_surgery_type:values.surgery_type
                //                     }
                //                 },
                //                 callback: function (r) {
                //                     if (r.message) {
                //                         frappe.set_route("Form", "Appointment", r.message.name);
                //                         frappe.msgprint("Appointment created successfully")
                //                         d.hide();
                //                     }
                //                 }
                //             });
                //         }
                //     });

                //     d.show();
                // });
            let apr_btn = frm.add_custom_button(__('Sent Appointment'), function () {
                    let d = new frappe.ui.Dialog({
                        title: 'Send for Doctor Approval',
                        fields: [
                            {
                                label: 'Doctor',
                                fieldname: 'doctor',
                                fieldtype: 'Link',
                                options: 'Employee'
                            },
                           {
                                label: 'Priority',
                                fieldname: 'priority',
                                fieldtype: 'Select',
                                options: ['Low','Medium','High'],
                                default: 'Medium'
                            },
                            {
                                label: 'Description',
                                fieldname: 'description',
                                fieldtype: 'Small Text'
                            },
                        ],
                        primary_action_label: 'Send Appointment Dr Approval',
                        primary_action(values) {
                            frappe.call({
                                method: "frappe.client.insert",
                                args: {
                                    doc: {
                                        doctype: "ToDo",
                                        status: "Open",
                                        priority:values.priority,
                                        description: values.description,
                                        custom_doctor:values.doctor,
                                        reference_type: "Consultation",
                                        reference_name: frm.doc.name,
                                        custom_patient: frm.doc.patient
                                    }
                                },
                                callback: function (r) {
                                    if (r.message) {
                                        frappe.set_route("Form", "ToDo", r.message.name);
                                        frappe.msgprint("Send For Approval successfully")
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
