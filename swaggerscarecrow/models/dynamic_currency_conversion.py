# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class DynamicCurrencyConversion(object):

    """Implementation of the 'DynamicCurrencyConversion' model.

    TODO: type model description here.

    Attributes:
        rebate_percent (float): DCC rebate percentage
        mark_up (MarkUpEnum): DCC markup type. An enum's numerical value
            usually matches their name, but with an exception:
            THREE_POINT_TWO_FIVE = 2.85
        currency_group (CurrencyGroupEnum): [NA] DCC currency group
        registration_fee (float): [NA] DCC registration fee

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rebate_percent": 'rebatePercent',
        "mark_up": 'markUp',
        "currency_group": 'currencyGroup',
        "registration_fee": 'registrationFee'
    }

    _optionals = [
        'currency_group',
        'registration_fee',
    ]

    def __init__(self,
                 rebate_percent=None,
                 mark_up=None,
                 currency_group=APIHelper.SKIP,
                 registration_fee=APIHelper.SKIP):
        """Constructor for the DynamicCurrencyConversion class"""

        # Initialize members of the class
        self.rebate_percent = rebate_percent 
        self.mark_up = mark_up 
        if currency_group is not APIHelper.SKIP:
            self.currency_group = currency_group 
        if registration_fee is not APIHelper.SKIP:
            self.registration_fee = registration_fee 

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

        rebate_percent = dictionary.get("rebatePercent") if dictionary.get("rebatePercent") else None
        mark_up = dictionary.get("markUp") if dictionary.get("markUp") else None
        currency_group = dictionary.get("currencyGroup") if dictionary.get("currencyGroup") else APIHelper.SKIP
        registration_fee = dictionary.get("registrationFee") if dictionary.get("registrationFee") else APIHelper.SKIP
        # Return an object of this model
        return cls(rebate_percent,
                   mark_up,
                   currency_group,
                   registration_fee)
