# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class FanfareCardSplits(object):

    """Implementation of the 'FanfareCardSplits' model.

    TODO: type model description here.

    Attributes:
        promotional (string): TODO: type description here.
        loyalty (string): TODO: type description here.
        gift (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "promotional": 'promotional',
        "loyalty": 'loyalty',
        "gift": 'gift'
    }

    _optionals = [
        'promotional',
        'loyalty',
        'gift',
    ]

    def __init__(self,
                 promotional=APIHelper.SKIP,
                 loyalty=APIHelper.SKIP,
                 gift=APIHelper.SKIP):
        """Constructor for the FanfareCardSplits class"""

        # Initialize members of the class
        if promotional is not APIHelper.SKIP:
            self.promotional = promotional 
        if loyalty is not APIHelper.SKIP:
            self.loyalty = loyalty 
        if gift is not APIHelper.SKIP:
            self.gift = gift 

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

        promotional = dictionary.get("promotional") if dictionary.get("promotional") else APIHelper.SKIP
        loyalty = dictionary.get("loyalty") if dictionary.get("loyalty") else APIHelper.SKIP
        gift = dictionary.get("gift") if dictionary.get("gift") else APIHelper.SKIP
        # Return an object of this model
        return cls(promotional,
                   loyalty,
                   gift)
