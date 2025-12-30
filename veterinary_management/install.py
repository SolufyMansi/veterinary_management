import frappe


def setup_veterinary_management_dashboard():
    dashboard_name = "Veterinary Management Dashboard"

    # 1. Define dashboard charts (spec only)
    charts = [
        {
            "doctype": "Dashboard Chart",
            "chart_name": "Appointments by Status",
            # Use Group By chart type with Count aggregation on status
            "chart_type": "Group By",
            "document_type": "Appointment",
            "group_by_based_on": "status",
            "group_by_type": "Count",
            "filters_json": "[]",
            "type": "Bar",
            "module": "Veterinary Management",
        },
        {
            "doctype": "Dashboard Chart",
            "chart_name": "Patients by Species",
            # Use Group By chart type with Count aggregation on species
            "chart_type": "Group By",
            "document_type": "Patient",
            "group_by_based_on": "species",
            "group_by_type": "Count",
            "filters_json": "[]",
            "type": "Bar",
            "module": "Veterinary Management",
        },
        {
            "doctype": "Dashboard Chart",
            "chart_name": "Revenue by Treatment",
            # Use Group By chart type with Sum aggregation on amount by treatment_type
            "chart_type": "Group By",
            "document_type": "Treatment",
            "group_by_based_on": "treatment_type",
            "group_by_type": "Sum",
            "aggregate_function_based_on": "amount",
            "filters_json": "[]",
            "type": "Bar",
            "module": "Veterinary Management",
        },
    ]

    # 2. Ensure all charts exist and collect their names
    chart_names = []
    for chart in charts:
        chart_name = chart["chart_name"]

        # Skip charts whose target DocType does not exist yet
        doc_type = chart.get("document_type")
        if doc_type and not frappe.db.exists("DocType", doc_type):
            continue

        if not frappe.db.exists("Dashboard Chart", {"chart_name": chart_name}):
            chart_doc = frappe.get_doc(chart)
            chart_doc.insert(ignore_permissions=True)
            frappe.db.commit()

        chart_names.append(chart_name)

    # 3. Ensure the dashboard exists and link charts to it
    if not frappe.db.exists("Dashboard", {"dashboard_name": dashboard_name}):
        dashboard = frappe.get_doc({
            "doctype": "Dashboard",
            "dashboard_name": dashboard_name,
            "module": "Veterinary Management",
            "charts": [
                {
                    "doctype": "Dashboard Chart Link",
                    "chart": name,
                    "width": "Half",
                }
                for name in chart_names
            ],
        })
        dashboard.insert(ignore_permissions=True)
        frappe.db.commit()


def after_install():
    """Hook called after app install to set up dashboard and charts."""
    setup_veterinary_management_dashboard()
