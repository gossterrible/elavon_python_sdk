# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.phone_number import PhoneNumber


class ProviderInfo(object):

    """Implementation of the 'ProviderInfo' model.

    TODO: type model description here.

    Attributes:
        representative_name (string): TODO: type description here.
        representative_email (string): TODO: type description here.
        representative_sales_code (string): TODO: type description here.
        representative_contact_number (PhoneNumber): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "representative_name": 'representativeName',
        "representative_email": 'representativeEmail',
        "representative_sales_code": 'representativeSalesCode',
        "representative_contact_number": 'representativeContactNumber'
    }

    _optionals = [
        'representative_name',
        'representative_email',
        'representative_sales_code',
        'representative_contact_number',
    ]

    def __init__(self,
                 representative_name=APIHelper.SKIP,
                 representative_email=APIHelper.SKIP,
                 representative_sales_code=APIHelper.SKIP,
                 representative_contact_number=APIHelper.SKIP):
        """Constructor for the ProviderInfo class"""

        # Initialize members of the class
        if representative_name is not APIHelper.SKIP:
            self.representative_name = representative_name 
        if representative_email is not APIHelper.SKIP:
            self.representative_email = representative_email 
        if representative_sales_code is not APIHelper.SKIP:
            self.representative_sales_code = representative_sales_code 
        if representative_contact_number is not APIHelper.SKIP:
            self.representative_contact_number = representative_contact_number 

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

        representative_name = dictionary.get("representativeName") if dictionary.get("representativeName") else APIHelper.SKIP
        representative_email = dictionary.get("representativeEmail") if dictionary.get("representativeEmail") else APIHelper.SKIP
        representative_sales_code = dictionary.get("representativeSalesCode") if dictionary.get("representativeSalesCode") else APIHelper.SKIP
        representative_contact_number = PhoneNumber.from_dictionary(dictionary.get('representativeContactNumber')) if 'representativeContactNumber' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(representative_name,
                   representative_email,
                   representative_sales_code,
                   representative_contact_number)