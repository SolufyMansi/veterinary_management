import frappe

def on_submit(doc, method=None):
    if not doc.custom_surgery:
        return

    surgery = frappe.get_doc("Surgery", doc.custom_surgery)
    if doc.outstanding_amount == 0:
        surgery.db_set(
            "status",
            "Hold",
            update_modified=True
        )
    else:
        surgery.db_set(
            "status",
            "Waiting for Payment",
            update_modified=True
        )
