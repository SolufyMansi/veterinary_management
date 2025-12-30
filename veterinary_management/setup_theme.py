import frappe


@frappe.whitelist()
def setup_veterinary_theme():
    """Create/Update a 'Veterinary Theme' Website Theme and set it in Website Settings,
    also attach the veterinary app logo so it appears in Website Settings.
    """
    theme_name = "Veterinary Theme"
    scss_path = "veterinary_management/public/scss/website"

    # Ensure Website Theme doc exists
    if frappe.db.exists("Website Theme", theme_name):
        theme = frappe.get_doc("Website Theme", theme_name)
    else:
        theme = frappe.new_doc("Website Theme")
        theme.theme = theme_name

    # Set SCSS path (field name is theme_scss in recent versions)
    try:
        theme.theme_scss = scss_path
    except Exception:
        # Fallback for older schemas
        try:
            theme.scss = scss_path
        except Exception:
            pass

    theme.save(ignore_permissions=True)

    # Update Website Settings
    ws = frappe.get_single("Website Settings")
    meta = ws.meta
    fieldnames = {df.fieldname for df in meta.fields}

    # Link the theme
    if "website_theme" in fieldnames:
        ws.website_theme = theme_name

    # Set logo fields to our app logo asset
    logo_path = "/assets/veterinary_management/logo.svg"
    for field in ("logo", "brand_logo", "brand_image", "app_logo"):
        if field in fieldnames:
            ws.set(field, logo_path)

    ws.save(ignore_permissions=True)
    frappe.db.commit()

    return "Veterinary theme and logo configured in Website Settings."