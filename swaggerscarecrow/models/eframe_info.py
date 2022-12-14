# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class EframeInfo(object):

    """Implementation of the 'EframeInfo' model.

    TODO: type model description here.

    Attributes:
        scheme_selection (string): Equipment and Payment Networks Scheme
            Selection
        pos_contract (bool): Flag indicating Terminal Girocard Application
        is_girocard (bool): Flag indicating Girocard Application

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheme_selection": 'schemeSelection',
        "pos_contract": 'posContract',
        "is_girocard": 'isGirocard'
    }

    _optionals = [
        'scheme_selection',
        'pos_contract',
        'is_girocard',
    ]

    def __init__(self,
                 scheme_selection=APIHelper.SKIP,
                 pos_contract=APIHelper.SKIP,
                 is_girocard=APIHelper.SKIP):
        """Constructor for the EframeInfo class"""

        # Initialize members of the class
        if scheme_selection is not APIHelper.SKIP:
            self.scheme_selection = scheme_selection 
        if pos_contract is not APIHelper.SKIP:
            self.pos_contract = pos_contract 
        if is_girocard is not APIHelper.SKIP:
            self.is_girocard = is_girocard 

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

        scheme_selection = dictionary.get("schemeSelection") if dictionary.get("schemeSelection") else APIHelper.SKIP
        pos_contract = dictionary.get("posContract") if "posContract" in dictionary.keys() else APIHelper.SKIP
        is_girocard = dictionary.get("isGirocard") if "isGirocard" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(scheme_selection,
                   pos_contract,
                   is_girocard)
