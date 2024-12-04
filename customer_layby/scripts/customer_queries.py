
import frappe

"""
This script runs through customers and pritns the one that are eligible for layby
"""
def get_eligible_customers():
    eligible_customers = frappe.get_all(
        "Customer",
        filters={"allowed_for_layby": 1},
        fields=["name", "mobile_no"]
    )
    print(eligible_customers)
