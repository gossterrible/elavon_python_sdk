# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CardVolume(object):

    """Implementation of the 'CardVolume' model.

    TODO: type model description here.

    Attributes:
        visa_percentage (string): Percentage of Visa transactions as a
            percentage of Annual Revenue
        master_card_percentage (string): Percentage of MasterCard transactions
            as a percentage of Annual Revenue
        amex_percentage (string): Percentage of Amex OptBlue transactions as a
            percentage of Annual Revenue
        amex_average_transaction (string): Average transaction amount for an
            Amercian Express OptBlue transaction
        interac_average_transaction (string): Average transaction amount for
            an Interac debit transaction

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "visa_percentage": 'visaPercentage',
        "master_card_percentage": 'masterCardPercentage',
        "amex_percentage": 'amexPercentage',
        "amex_average_transaction": 'amexAverageTransaction',
        "interac_average_transaction": 'interacAverageTransaction'
    }

    def __init__(self,
                 visa_percentage=None,
                 master_card_percentage=None,
                 amex_percentage=None,
                 amex_average_transaction=None,
                 interac_average_transaction=None):
        """Constructor for the CardVolume class"""

        # Initialize members of the class
        self.visa_percentage = visa_percentage 
        self.master_card_percentage = master_card_percentage 
        self.amex_percentage = amex_percentage 
        self.amex_average_transaction = amex_average_transaction 
        self.interac_average_transaction = interac_average_transaction 

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

        visa_percentage = dictionary.get("visaPercentage") if dictionary.get("visaPercentage") else None
        master_card_percentage = dictionary.get("masterCardPercentage") if dictionary.get("masterCardPercentage") else None
        amex_percentage = dictionary.get("amexPercentage") if dictionary.get("amexPercentage") else None
        amex_average_transaction = dictionary.get("amexAverageTransaction") if dictionary.get("amexAverageTransaction") else None
        interac_average_transaction = dictionary.get("interacAverageTransaction") if dictionary.get("interacAverageTransaction") else None
        # Return an object of this model
        return cls(visa_percentage,
                   master_card_percentage,
                   amex_percentage,
                   amex_average_transaction,
                   interac_average_transaction)
