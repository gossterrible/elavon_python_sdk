# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class Principal(object):

    """Implementation of the 'Principal' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name'
    }

    _optionals = [
        'name',
    ]

    def __init__(self,
                 name=APIHelper.SKIP):
        """Constructor for the Principal class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 

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

        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        # Return an object of this model
        return cls(name)