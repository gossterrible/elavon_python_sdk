# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class CCIHAutoAddressRequest(object):

    """Implementation of the 'CCIHAutoAddressRequest' model.

    TODO: type model description here.

    Attributes:
        address (string): TODO: type description here.
        digest (string): TODO: type description here.
        rel (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": 'address',
        "digest": 'digest',
        "rel": 'rel'
    }

    _optionals = [
        'address',
        'digest',
        'rel',
    ]

    def __init__(self,
                 address=APIHelper.SKIP,
                 digest=APIHelper.SKIP,
                 rel=APIHelper.SKIP):
        """Constructor for the CCIHAutoAddressRequest class"""

        # Initialize members of the class
        if address is not APIHelper.SKIP:
            self.address = address 
        if digest is not APIHelper.SKIP:
            self.digest = digest 
        if rel is not APIHelper.SKIP:
            self.rel = rel 

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

        address = dictionary.get("address") if dictionary.get("address") else APIHelper.SKIP
        digest = dictionary.get("digest") if dictionary.get("digest") else APIHelper.SKIP
        rel = dictionary.get("rel") if dictionary.get("rel") else APIHelper.SKIP
        # Return an object of this model
        return cls(address,
                   digest,
                   rel)
