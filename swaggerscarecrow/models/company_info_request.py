# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class CompanyInfoRequest(object):

    """Implementation of the 'CompanyInfoRequest' model.

    TODO: type model description here.

    Attributes:
        company_id (string): TODO: type description here.
        ownership_type (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "company_id": 'companyId',
        "ownership_type": 'ownershipType'
    }

    _optionals = [
        'company_id',
        'ownership_type',
    ]

    def __init__(self,
                 company_id=APIHelper.SKIP,
                 ownership_type=APIHelper.SKIP):
        """Constructor for the CompanyInfoRequest class"""

        # Initialize members of the class
        if company_id is not APIHelper.SKIP:
            self.company_id = company_id 
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

        company_id = dictionary.get("companyId") if dictionary.get("companyId") else APIHelper.SKIP
        ownership_type = dictionary.get("ownershipType") if dictionary.get("ownershipType") else APIHelper.SKIP
        # Return an object of this model
        return cls(company_id,
                   ownership_type)
