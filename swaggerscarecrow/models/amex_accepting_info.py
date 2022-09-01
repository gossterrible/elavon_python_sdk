# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class AmexAcceptingInfo(object):

    """Implementation of the 'AmexAcceptingInfo' model.

    TODO: type model description here.

    Attributes:
        amex_monthly_card_sales (float): TODO: type description here.
        is_existing (bool): Flag indicating if AMEX account already present
            for customer
        amex_mid (string): [EU] Field for Girocard + International Schemes and
            International Schemes Only

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amex_monthly_card_sales": 'amexMonthlyCardSales',
        "is_existing": 'isExisting',
        "amex_mid": 'amexMid'
    }

    _optionals = [
        'amex_monthly_card_sales',
        'is_existing',
        'amex_mid',
    ]

    def __init__(self,
                 amex_monthly_card_sales=APIHelper.SKIP,
                 is_existing=APIHelper.SKIP,
                 amex_mid=APIHelper.SKIP):
        """Constructor for the AmexAcceptingInfo class"""

        # Initialize members of the class
        if amex_monthly_card_sales is not APIHelper.SKIP:
            self.amex_monthly_card_sales = amex_monthly_card_sales 
        if is_existing is not APIHelper.SKIP:
            self.is_existing = is_existing 
        if amex_mid is not APIHelper.SKIP:
            self.amex_mid = amex_mid 

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

        amex_monthly_card_sales = dictionary.get("amexMonthlyCardSales") if dictionary.get("amexMonthlyCardSales") else APIHelper.SKIP
        is_existing = dictionary.get("isExisting") if "isExisting" in dictionary.keys() else APIHelper.SKIP
        amex_mid = dictionary.get("amexMid") if dictionary.get("amexMid") else APIHelper.SKIP
        # Return an object of this model
        return cls(amex_monthly_card_sales,
                   is_existing,
                   amex_mid)
