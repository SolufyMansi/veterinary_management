frappe.ui.form.on("Check-Up Record", {
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
                                reference_doctype: "Check-Up Record",  
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
        if (frm.doc.need_for_consultation){
            // console.log("::::::::::::")
            check_btn = frm.add_custom_button(__('Consultation'), function () {

                frappe.route_options = {
                    "patient": frm.doc.patient,
                    "appointment": frm.doc.appointment
                };
                frappe.set_route("Form", "Consultation", "new-Consultation");
            });

            if (check_btn) {
                check_btn.css({
                    "background-color": "black",
                    "color": "white",
                    "font-weight": "bold"
                });
            }
        }
    }
    
});
