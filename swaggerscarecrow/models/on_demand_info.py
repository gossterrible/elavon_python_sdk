# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class OnDemandInfo(object):

    """Implementation of the 'OnDemandInfo' model.

    TODO: type model description here.

    Attributes:
        per_transaction_fee (float): Per transaction fee applied to service
        percent_fee (float): Fee percentage to be applied to service

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "per_transaction_fee": 'perTransactionFee',
        "percent_fee": 'percentFee'
    }

    _optionals = [
        'per_transaction_fee',
        'percent_fee',
    ]

    def __init__(self,
                 per_transaction_fee=APIHelper.SKIP,
                 percent_fee=APIHelper.SKIP):
        """Constructor for the OnDemandInfo class"""

        # Initialize members of the class
        if per_transaction_fee is not APIHelper.SKIP:
            self.per_transaction_fee = per_transaction_fee 
        if percent_fee is not APIHelper.SKIP:
            self.percent_fee = percent_fee 

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

        per_transaction_fee = dictionary.get("perTransactionFee") if dictionary.get("perTransactionFee") else APIHelper.SKIP
        percent_fee = dictionary.get("percentFee") if dictionary.get("percentFee") else APIHelper.SKIP
        # Return an object of this model
        return cls(per_transaction_fee,
                   percent_fee)
