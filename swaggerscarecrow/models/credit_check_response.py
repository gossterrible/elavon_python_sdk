# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class CreditCheckResponse(object):

    """Implementation of the 'CreditCheckResponse' model.

    TODO: type model description here.

    Attributes:
        decision (Decision1Enum): Determination of credit check request,
            declined decisions don't return a token
        error (string): Error message from service
        credit_check_id (string): Identifier for credit check response
        credit_check_token (string): Value to be appended to the boarding
            request that follows a successful credit check

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "decision": 'decision',
        "error": 'error',
        "credit_check_id": 'creditCheckId',
        "credit_check_token": 'creditCheckToken'
    }

    _optionals = [
        'decision',
        'error',
        'credit_check_id',
        'credit_check_token',
    ]

    def __init__(self,
                 decision=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 credit_check_id=APIHelper.SKIP,
                 credit_check_token=APIHelper.SKIP):
        """Constructor for the CreditCheckResponse class"""

        # Initialize members of the class
        if decision is not APIHelper.SKIP:
            self.decision = decision 
        if error is not APIHelper.SKIP:
            self.error = error 
        if credit_check_id is not APIHelper.SKIP:
            self.credit_check_id = credit_check_id 
        if credit_check_token is not APIHelper.SKIP:
            self.credit_check_token = credit_check_token 

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

        decision = dictionary.get("decision") if dictionary.get("decision") else APIHelper.SKIP
        error = dictionary.get("error") if dictionary.get("error") else APIHelper.SKIP
        credit_check_id = dictionary.get("creditCheckId") if dictionary.get("creditCheckId") else APIHelper.SKIP
        credit_check_token = dictionary.get("creditCheckToken") if dictionary.get("creditCheckToken") else APIHelper.SKIP
        # Return an object of this model
        return cls(decision,
                   error,
                   credit_check_id,
                   credit_check_token)
