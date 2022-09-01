# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApmPricingTier(object):

    """Implementation of the 'ApmPricingTier' model.

    TODO: type model description here.

    Attributes:
        combining_code (string): Combining Code of the Alternative Payment
            Method
        per_item_amount (string): Default Per Item Amount of the Alternative
            Payment Method
        rate_percentage (string): Default Rate Percentage of the Alternative
            Payment Method
        description (string): Long name of the combining code of the
            Alternative Payment Method

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "combining_code": 'combiningCode',
        "per_item_amount": 'perItemAmount',
        "rate_percentage": 'ratePercentage',
        "description": 'description'
    }

    def __init__(self,
                 combining_code=None,
                 per_item_amount=None,
                 rate_percentage=None,
                 description=None):
        """Constructor for the ApmPricingTier class"""

        # Initialize members of the class
        self.combining_code = combining_code 
        self.per_item_amount = per_item_amount 
        self.rate_percentage = rate_percentage 
        self.description = description 

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

        combining_code = dictionary.get("combiningCode") if dictionary.get("combiningCode") else None
        per_item_amount = dictionary.get("perItemAmount") if dictionary.get("perItemAmount") else None
        rate_percentage = dictionary.get("ratePercentage") if dictionary.get("ratePercentage") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        # Return an object of this model
        return cls(combining_code,
                   per_item_amount,
                   rate_percentage,
                   description)