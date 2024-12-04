from erpnext.selling.doctype.customer.customer import Customer
import frappe

class CustomCustomer(Customer):
    def validate(self):
        """
        Override the validate method to check Lay-By eligibility.
        """
        super().validate()

        # Default to False to ensure initialization
        self.allowed_for_layby = False

        # Run eligibility check and update field
        self.allowed_for_layby = self.check_lay_by_eligibility()

    def check_lay_by_eligibility(self):
        """
        Validate the customer's fields to determine Lay-By eligibility.
        """
        # Ensure Identification Type is set
        if not hasattr(self, "identification_type") or not self.identification_type:
            frappe.throw("Identification Type is required for Lay-By eligibility.")

        # Validate ID Number or Passport details
        if self.identification_type == "ID Number":
            if not self.id_number:
                frappe.throw("ID Number is required for Lay-By eligibility.")
        elif self.identification_type == "Passport":
            if not self.passport_number or not self.passport_country_of_origin:
                frappe.throw("Passport Number and Country of Origin are required for Lay-By eligibility.")

        # Validate Mobile Number
        if not hasattr(self, "mobile_no") or not self.mobile_no:
            frappe.throw("A primary mobile number is required for Lay-By eligibility.")

        # All checks passed, eligible for Lay-By
        return True
