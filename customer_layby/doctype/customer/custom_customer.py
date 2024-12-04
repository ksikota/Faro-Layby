from erpnext.selling.doctype.customer.customer import Customer
import frappe

class CustomCustomer(Customer):
    def validate(self):
        """
        Override the validate method to calculate and save Lay-By eligibility status.
        """
        super().validate()

        # Calculate Lay-By eligibility and store the result in the database
        self.allowed_for_layby = self.calculate_lay_by_eligibility()

    def calculate_lay_by_eligibility(self):
        """
        Check the eligibility for Lay-By based on customer data.
        Returns True if eligible, otherwise False.
        """
        # Check for required identification details
        if not self.is_identification_valid():
            return False
        
        # Check for a valid mobile number
        if not self.mobile_no:
            frappe.throw("A primary mobile number is required for Lay-By eligibility.")

        return True

    def is_identification_valid(self):
        """
        Check if the identification details (ID Number or Passport) are valid.
        Returns True if valid, otherwise False.
        """
        if self.identification_type == "ID Number":
            if not self.id_number:
                frappe.throw("ID Number is required for Lay-By eligibility.")
                return False
        elif self.identification_type == "Passport":
            if not self.passport_number or not self.passport_country_of_origin:
                frappe.throw("Passport Number and Country of Origin are required for Lay-By eligibility.")
                return False
        return True
