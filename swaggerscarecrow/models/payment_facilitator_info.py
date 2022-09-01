# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.card_prefix import CardPrefix


class PaymentFacilitatorInfo(object):

    """Implementation of the 'PaymentFacilitatorInfo' model.

    TODO: type model description here.

    Attributes:
        payment_facilitator_type (PaymentFacilitatorTypeEnum): TODO: type
            description here.
        card_prefixes (list of CardPrefix): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payment_facilitator_type": 'paymentFacilitatorType',
        "card_prefixes": 'cardPrefixes'
    }

    _optionals = [
        'payment_facilitator_type',
        'card_prefixes',
    ]

    def __init__(self,
                 payment_facilitator_type=APIHelper.SKIP,
                 card_prefixes=APIHelper.SKIP):
        """Constructor for the PaymentFacilitatorInfo class"""

        # Initialize members of the class
        if payment_facilitator_type is not APIHelper.SKIP:
            self.payment_facilitator_type = payment_facilitator_type 
        if card_prefixes is not APIHelper.SKIP:
            self.card_prefixes = card_prefixes 

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

        payment_facilitator_type = dictionary.get("paymentFacilitatorType") if dictionary.get("paymentFacilitatorType") else APIHelper.SKIP
        card_prefixes = None
        if dictionary.get('cardPrefixes') is not None:
            card_prefixes = [CardPrefix.from_dictionary(x) for x in dictionary.get('cardPrefixes')]
        else:
            card_prefixes = APIHelper.SKIP
        # Return an object of this model
        return cls(payment_facilitator_type,
                   card_prefixes)
