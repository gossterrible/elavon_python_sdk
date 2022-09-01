# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class AdditionalLocationInfo(object):

    """Implementation of the 'AdditionalLocationInfo' model.

    TODO: type model description here.

    Attributes:
        central_mid (string): Merchant Id of existing business
        central_legal_name (string): Legal Name of existing business
        central_tax_id (string): Tax Id of existing busines, required in cases
            where Central Legal Name not present

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "central_mid": 'centralMid',
        "central_legal_name": 'centralLegalName',
        "central_tax_id": 'centralTaxId'
    }

    _optionals = [
        'central_tax_id',
    ]

    def __init__(self,
                 central_mid=None,
                 central_legal_name=None,
                 central_tax_id=APIHelper.SKIP):
        """Constructor for the AdditionalLocationInfo class"""

        # Initialize members of the class
        self.central_mid = central_mid 
        self.central_legal_name = central_legal_name 
        if central_tax_id is not APIHelper.SKIP:
            self.central_tax_id = central_tax_id 

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

        central_mid = dictionary.get("centralMid") if dictionary.get("centralMid") else None
        central_legal_name = dictionary.get("centralLegalName") if dictionary.get("centralLegalName") else None
        central_tax_id = dictionary.get("centralTaxId") if dictionary.get("centralTaxId") else APIHelper.SKIP
        # Return an object of this model
        return cls(central_mid,
                   central_legal_name,
                   central_tax_id)