# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class FraudCheckResult(object):

    """Implementation of the 'FraudCheckResult' model.

    TODO: type model description here.

    Attributes:
        transaction_id (string): Unique identifier of quiz response, to be
            used in answer request for the quiz
        decision (DecisionEnum): Result reached by quiz process

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_id": 'transactionId',
        "decision": 'decision'
    }

    _optionals = [
        'transaction_id',
        'decision',
    ]

    def __init__(self,
                 transaction_id=APIHelper.SKIP,
                 decision=APIHelper.SKIP):
        """Constructor for the FraudCheckResult class"""

        # Initialize members of the class
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if decision is not APIHelper.SKIP:
            self.decision = decision 

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

        transaction_id = dictionary.get("transactionId") if dictionary.get("transactionId") else APIHelper.SKIP
        decision = dictionary.get("decision") if dictionary.get("decision") else APIHelper.SKIP
        # Return an object of this model
        return cls(transaction_id,
                   decision)
