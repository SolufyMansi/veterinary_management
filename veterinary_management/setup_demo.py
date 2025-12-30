import frappe


def _get_or_create_customer(name: str) -> str:
    doc = frappe.db.get_value("Customer", {"customer_name": name}, "name")
    if doc:
        return doc
    customer = frappe.get_doc({
        "doctype": "Customer",
        "customer_name": name,
        "customer_type": "Individual"
    }).insert(ignore_permissions=True)
    return customer.name


def _get_or_create_item(item_code: str, item_name: str, item_group: str = "All Item Groups") -> str:
    doc = frappe.db.get_value("Item", {"item_code": item_code}, "name")
    if doc:
        return doc
    item = frappe.get_doc({
        "doctype": "Item",
        "item_code": item_code,
        "item_name": item_name,
        "item_group": item_group,
        "is_stock_item": 0
    }).insert(ignore_permissions=True)
    return item.name


@frappe.whitelist()
def create_demo_records():
    """Create 4-5 demo records in all veterinary_management doctypes.

    Safe to run multiple times; uses simple naming to avoid duplicates.
    """
    frappe.flags.mute_messages = True

    customer_name = _get_or_create_customer("Vet Demo Customer")
    vaccine_item = _get_or_create_item("VACCINE-DEMO", "Demo Vaccine")
    med_item = _get_or_create_item("MED-DEMO", "Demo Medicine")

    # HERDS
    herds = []
    herd_specs = [
        ("Demo Herd A", "Cattle", "North Farm", 25),
        ("Demo Herd B", "Sheep", "South Farm", 40),
    ]
    for herd_name, species, location, count in herd_specs:
        existing = frappe.db.get_value("VM Herd", {"herd_name": herd_name}, "name")
        if existing:
            herds.append(existing)
            continue
        herd = frappe.get_doc({
            "doctype": "VM Herd",
            "herd_name": herd_name,
            "species": species,
            "location": location,
            "count": count,
        }).insert(ignore_permissions=True)
        herds.append(herd.name)

    # ANIMALS
    animals = []
    animal_specs = [
        ("Bella", "Dog", "Labrador", "Female"),
        ("Max", "Dog", "Beagle", "Male"),
        ("Molly", "Cat", "Persian", "Female"),
        ("Rocky", "Cattle", "Holstein", "Male"),
        ("Luna", "Sheep", "Merino", "Female"),
    ]
    for idx, (animal_name, species, breed, sex) in enumerate(animal_specs, start=1):
        existing = frappe.db.get_value("VM Animal", {"animal_name": animal_name, "customer": customer_name}, "name")
        if existing:
            animals.append(existing)
            continue
        herd = herds[(idx - 1) % len(herds)] if herds else None
        animal = frappe.get_doc({
            "doctype": "VM Animal",
            "animal_name": animal_name,
            "species": species,
            "breed": breed,
            "sex": sex,
            "customer": customer_name,
            "herd": herd,
        }).insert(ignore_permissions=True)
        animals.append(animal.name)

    # APPOINTMENTS
    appointments = []
    statuses = ["Scheduled", "Completed", "Scheduled", "Completed", "Cancelled"]
    for i, status in enumerate(statuses, start=1):
        animal = animals[(i - 1) % len(animals)] if animals else None
        key = f"DEMO-APT-{i}"
        existing = frappe.db.get_value("VM Appointment", {"name": ("like", f"APT-%")}, "name")
        # Not strictly idempotent by name, so just create a few if none exist
        if existing and i <= 2:
            # avoid too many duplicates if already populated
            continue
        appt = frappe.get_doc({
            "doctype": "VM Appointment",
            "customer": customer_name,
            "vm_animal": animal,
            "doctor": frappe.session.user or "Administrator",
            "appointment_date": frappe.utils.now_datetime(),
            "status": status,
        }).insert(ignore_permissions=True)
        appointments.append(appt.name)

    # MEDICAL PROCEDURES
    procedure_names = [
        "Spay/Neuter",
        "Vaccination",
        "Dental Cleaning",
        "General Surgery",
    ]
    for i, proc_name in enumerate(procedure_names, start=1):
        animal = animals[(i - 1) % len(animals)] if animals else None
        existing = frappe.db.get_value("VM Medical Procedure", {"procedure_name": proc_name, "animal": animal}, "name")
        if existing:
            continue
        frappe.get_doc({
            "doctype": "VM Medical Procedure",
            "animal": animal,
            "procedure_name": proc_name,
            "surgeon": frappe.session.user or "Administrator",
        }).insert(ignore_permissions=True)

    # CONSULTATIONS + PRESCRIPTIONS CHILD TABLE
    for i, appt_name in enumerate(appointments[:4], start=1):
        existing = frappe.db.get_value("VM Consultation", {"appointment": appt_name}, "name")
        if existing:
            continue
        consult = frappe.get_doc({
            "doctype": "VM Consultation",
            "appointment": appt_name,
            "symptoms": "Demo symptoms for consultation #{0}".format(i),
            "diagnosis": "Demo diagnosis #{0}".format(i),
            "treatment_plan": "Demo treatment plan #{0}".format(i),
            "prescriptions": [
                {
                    "doctype": "VM Prescription",
                    "item_code": med_item,
                    "dosage": "1 tablet twice daily",
                    "quantity": 5,
                }
            ],
        }).insert(ignore_permissions=True)

    # VACCINATION RECORDS
    for i, animal in enumerate(animals[:5], start=1):
        existing = frappe.db.get_value("VM Vaccination Record", {"animal": animal}, "name")
        if existing:
            continue
        frappe.get_doc({
            "doctype": "VM Vaccination Record",
            "animal": animal,
            "vaccine": vaccine_item,
            "date_administered": frappe.utils.nowdate(),
            "next_due_date": frappe.utils.add_days(frappe.utils.nowdate(), 365),
        }).insert(ignore_permissions=True)

    frappe.db.commit()
    return "Demo records created for veterinary_management doctypes."
