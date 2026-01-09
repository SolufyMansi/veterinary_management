// Copyright (c) 2026, Solufy and contributors
// For license information, please see license.tx
frappe.query_reports["Appointment"] = {
	"filters": [
		{
			fieldname: "employee",
			label: "Employee",
			fieldtype: "Link",
			options: "Employee"
		},
		{
			fieldname: "scheduled_time",
			label: "Appointment Date",
			fieldtype: "Datetime"
		},
		{
			fieldname: "status",
			label: "Status",
			fieldtype: "Select",
			options: [
				"",
				"Scheduled", 
				"Completed", 
				"Cancelled", 
				"In Process"
			].join("\n")
		},
		{
			fieldname: "custom_reason",
			label: "Appointment Type",
			fieldtype: "Select",
			options: ['','Check-Up','Consulation','Vaccination','Surgery']
		},

	]
};
