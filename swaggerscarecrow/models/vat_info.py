# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.date_components import DateComponents


class VatInfo(object):

    """Implementation of the 'VatInfo' model.

    TODO: type model description here.

    Attributes:
        number_option (NumberOptionEnum): Type of VAT id provieded if tax id
            type is VAT
        number_56_b (string): VAT 56B number
        expiry_date_56_b (DateComponents): A container that holds the date
            (day, month, and year)
        tax_number_type (TaxNumberTypeEnum): The Tax Number Type of the
            Business
        tax_number (string): The Tax Number Type of the Business

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number_option": 'numberOption',
        "number_56_b": 'number56B',
        "expiry_date_56_b": 'expiryDate56B',
        "tax_number_type": 'taxNumberType',
        "tax_number": 'taxNumber'
    }

    _optionals = [
        'number_option',
        'number_56_b',
        'expiry_date_56_b',
        'tax_number_type',
        'tax_number',
    ]

    def __init__(self,
                 number_option=APIHelper.SKIP,
                 number_56_b=APIHelper.SKIP,
                 expiry_date_56_b=APIHelper.SKIP,
                 tax_number_type=APIHelper.SKIP,
                 tax_number=APIHelper.SKIP):
        """Constructor for the VatInfo class"""

        # Initialize members of the class
        if number_option is not APIHelper.SKIP:
            self.number_option = number_option 
        if number_56_b is not APIHelper.SKIP:
            self.number_56_b = number_56_b 
        if expiry_date_56_b is not APIHelper.SKIP:
            self.expiry_date_56_b = expiry_date_56_b 
        if tax_number_type is not APIHelper.SKIP:
            self.tax_number_type = tax_number_type 
        if tax_number is not APIHelper.SKIP:
            self.tax_number = tax_number 

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

        number_option = dictionary.get("numberOption") if dictionary.get("numberOption") else APIHelper.SKIP
        number_56_b = dictionary.get("number56B") if dictionary.get("number56B") else APIHelper.SKIP
        expiry_date_56_b = DateComponents.from_dictionary(dictionary.get('expiryDate56B')) if 'expiryDate56B' in dictionary.keys() else APIHelper.SKIP 
        tax_number_type = dictionary.get("taxNumberType") if dictionary.get("taxNumberType") else APIHelper.SKIP
        tax_number = dictionary.get("taxNumber") if dictionary.get("taxNumber") else APIHelper.SKIP
        # Return an object of this model
        return cls(number_option,
                   number_56_b,
                   expiry_date_56_b,
                   tax_number_type,
                   tax_number)
