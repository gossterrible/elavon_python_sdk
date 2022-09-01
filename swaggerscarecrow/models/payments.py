# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class Payments(object):

    """Implementation of the 'Payments' model.

    TODO: type model description here.

    Attributes:
        pms_vendor_pas (string): TODO: type description here.
        number_of_providers (string): TODO: type description here.
        sales_rep_phone_number (string): TODO: type description here.
        integrator_notes (string): TODO: type description here.
        has_payment_plans (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pms_vendor_pas": 'pmsVendorPas',
        "number_of_providers": 'numberOfProviders',
        "sales_rep_phone_number": 'salesRepPhoneNumber',
        "integrator_notes": 'integratorNotes',
        "has_payment_plans": 'hasPaymentPlans'
    }

    _optionals = [
        'pms_vendor_pas',
        'number_of_providers',
        'sales_rep_phone_number',
        'integrator_notes',
        'has_payment_plans',
    ]

    def __init__(self,
                 pms_vendor_pas=APIHelper.SKIP,
                 number_of_providers=APIHelper.SKIP,
                 sales_rep_phone_number=APIHelper.SKIP,
                 integrator_notes=APIHelper.SKIP,
                 has_payment_plans=APIHelper.SKIP):
        """Constructor for the Payments class"""

        # Initialize members of the class
        if pms_vendor_pas is not APIHelper.SKIP:
            self.pms_vendor_pas = pms_vendor_pas 
        if number_of_providers is not APIHelper.SKIP:
            self.number_of_providers = number_of_providers 
        if sales_rep_phone_number is not APIHelper.SKIP:
            self.sales_rep_phone_number = sales_rep_phone_number 
        if integrator_notes is not APIHelper.SKIP:
            self.integrator_notes = integrator_notes 
        if has_payment_plans is not APIHelper.SKIP:
            self.has_payment_plans = has_payment_plans 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        pms_vendor_pas = dictionary.get("pmsVendorPas") if dictionary.get("pmsVendorPas") else APIHelper.SKIP
        number_of_providers = dictionary.get("numberOfProviders") if dictionary.get("numberOfProviders") else APIHelper.SKIP
        sales_rep_phone_number = dictionary.get("salesRepPhoneNumber") if dictionary.get("salesRepPhoneNumber") else APIHelper.SKIP
        integrator_notes = dictionary.get("integratorNotes") if dictionary.get("integratorNotes") else APIHelper.SKIP
        has_payment_plans = dictionary.get("hasPaymentPlans") if "hasPaymentPlans" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(pms_vendor_pas,
                   number_of_providers,
                   sales_rep_phone_number,
                   integrator_notes,
                   has_payment_plans)