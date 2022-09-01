# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class Fee(object):

    """Implementation of the 'Fee' model.

    TODO: type model description here.

    Attributes:
        mtype (string): SKU of fee
        quantity (int): Quantity of fee
        amount (float): Price of fee
        frequency (FrequencyEnum): Application of fee
        start_month (StartMonthEnum): [NA] start month

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "quantity": 'quantity',
        "amount": 'amount',
        "frequency": 'frequency',
        "start_month": 'startMonth'
    }

    _optionals = [
        'start_month',
    ]

    def __init__(self,
                 mtype=None,
                 quantity=None,
                 amount=None,
                 frequency=None,
                 start_month=APIHelper.SKIP):
        """Constructor for the Fee class"""

        # Initialize members of the class
        self.mtype = mtype 
        self.quantity = quantity 
        self.amount = amount 
        self.frequency = frequency 
        if start_month is not APIHelper.SKIP:
            self.start_month = start_month 

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

        mtype = dictionary.get("type") if dictionary.get("type") else None
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else None
        amount = dictionary.get("amount") if dictionary.get("amount") else None
        frequency = dictionary.get("frequency") if dictionary.get("frequency") else None
        start_month = dictionary.get("startMonth") if dictionary.get("startMonth") else APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   quantity,
                   amount,
                   frequency,
                   start_month)