// Copyright (c) 2026, Solufy and contributors
// For license information, please see license.txt
// frappe.ui.form.on("Lab Test Result", {
//     lab_test_template: function(frm) {
//         if(frm.doc.lab_test_template) {
//             frappe.call({
//                 method: "frappe.client.get",
//                 args: {
//                     doctype: "Lab Test Template",
//                     name: frm.doc.lab_test_template
//                 },
//                 callback: function(r) {
//                     if(r.message) {
//                         frm.clear_table("results");

//                         let template_parameters = r.message.parameters || [];

//                         template_parameters.forEach(function(param) {
//                             let row = frm.add_child("results");
//                             row.parameter = param.parameter_name;
//                             row.unit = param.unit;
//                             row.normal_min = param.normal_min;
//                             row.normal_max = param.normal_max;
//                             row.result = ""; 
//                         });

//                         frm.refresh_field("results");
//                     }
//                 }
//             });
//         }
//     }
// });

frappe.ui.form.on('Lab Test Result Item', {
    result(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.result < row.normal_min) row.flag = "Low";
        else if (row.result > row.normal_max) row.flag = "High";
        else row.flag = "Normal";
        frm.refresh_field("results");
    }
});