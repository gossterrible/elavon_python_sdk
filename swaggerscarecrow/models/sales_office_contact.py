# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.models.address import Address
from swaggerscarecrow.models.phone_number import PhoneNumber


class SalesOfficeContact(object):

    """Implementation of the 'SalesOfficeContact' model.

    TODO: type model description here.

    Attributes:
        address (Address): TODO: type description here.
        phone (PhoneNumber): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": 'address',
        "phone": 'phone'
    }

    def __init__(self,
                 address=None,
                 phone=None):
        """Constructor for the SalesOfficeContact class"""

        # Initialize members of the class
        self.address = address 
        self.phone = phone 

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

        address = Address.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        phone = PhoneNumber.from_dictionary(dictionary.get('phone')) if dictionary.get('phone') else None
        # Return an object of this model
        return cls(address,
                   phone)
