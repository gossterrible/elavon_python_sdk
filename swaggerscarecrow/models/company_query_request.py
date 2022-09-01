# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class CompanyQueryRequest(object):

    """Implementation of the 'CompanyQueryRequest' model.

    TODO: type model description here.

    Attributes:
        country_code (string): TODO: type description here.
        registration_number (string): TODO: type description here.
        business_name (string): TODO: type description here.
        post_code (string): TODO: type description here.
        vat_id_number (string): TODO: type description here.
        ownership_type (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "country_code": 'countryCode',
        "registration_number": 'registrationNumber',
        "business_name": 'businessName',
        "post_code": 'postCode',
        "vat_id_number": 'vatIDNumber',
        "ownership_type": 'ownershipType'
    }

    _optionals = [
        'country_code',
        'registration_number',
        'business_name',
        'post_code',
        'vat_id_number',
        'ownership_type',
    ]

    def __init__(self,
                 country_code=APIHelper.SKIP,
                 registration_number=APIHelper.SKIP,
                 business_name=APIHelper.SKIP,
                 post_code=APIHelper.SKIP,
                 vat_id_number=APIHelper.SKIP,
                 ownership_type=APIHelper.SKIP):
        """Constructor for the CompanyQueryRequest class"""

        # Initialize members of the class
        if country_code is not APIHelper.SKIP:
            self.country_code = country_code 
        if registration_number is not APIHelper.SKIP:
            self.registration_number = registration_number 
        if business_name is not APIHelper.SKIP:
            self.business_name = business_name 
        if post_code is not APIHelper.SKIP:
            self.post_code = post_code 
        if vat_id_number is not APIHelper.SKIP:
            self.vat_id_number = vat_id_number 
        if ownership_type is not APIHelper.SKIP:
            self.ownership_type = ownership_type 

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

        country_code = dictionary.get("countryCode") if dictionary.get("countryCode") else APIHelper.SKIP
        registration_number = dictionary.get("registrationNumber") if dictionary.get("registrationNumber") else APIHelper.SKIP
        business_name = dictionary.get("businessName") if dictionary.get("businessName") else APIHelper.SKIP
        post_code = dictionary.get("postCode") if dictionary.get("postCode") else APIHelper.SKIP
        vat_id_number = dictionary.get("vatIDNumber") if dictionary.get("vatIDNumber") else APIHelper.SKIP
        ownership_type = dictionary.get("ownershipType") if dictionary.get("ownershipType") else APIHelper.SKIP
        # Return an object of this model
        return cls(country_code,
                   registration_number,
                   business_name,
                   post_code,
                   vat_id_number,
                   ownership_type)