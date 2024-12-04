import frappe

"""
This script runs through all customers checks if they are legible for layby and does the action.
Execute with : bench execute customer_layby.scripts.backfill_layby.backfill_layby_field
"""

def backfill_layby_field():
    customers = frappe.get_all("Customer", fields=["name", "identification_type", "id_number", "passport_number", "passport_country_of_origin", "mobile_no"])
    for customer in customers:
        allowed_for_layby = False
        if customer.identification_type == "ID Number" and customer.id_number:
            allowed_for_layby = True
        elif customer.identification_type == "Passport" and customer.passport_number and customer.passport_country_of_origin:
            allowed_for_layby = True
        if allowed_for_layby and not customer.mobile_no:
            allowed_for_layby = False

        frappe.db.set_value("Customer", customer.name, "allowed_for_lay_by", allowed_for_layby)
    frappe.db.commit()