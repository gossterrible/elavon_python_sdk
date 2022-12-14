# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.models.address import Address
from swaggerscarecrow.models.person import Person


class GetQuizRequest(object):

    """Implementation of the 'GetQuizRequest' model.

    TODO: type model description here.

    Attributes:
        principal (Person): TODO: type description here.
        business_address (Address): TODO: type description here.
        language (string): Language of E-KYC requested, ISO 639-2 standard
            applies, en and fr supported

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "principal": 'principal',
        "business_address": 'businessAddress',
        "language": 'language'
    }

    def __init__(self,
                 principal=None,
                 business_address=None,
                 language=None):
        """Constructor for the GetQuizRequest class"""

        # Initialize members of the class
        self.principal = principal 
        self.business_address = business_address 
        self.language = language 

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

        principal = Person.from_dictionary(dictionary.get('principal')) if dictionary.get('principal') else None
        business_address = Address.from_dictionary(dictionary.get('businessAddress')) if dictionary.get('businessAddress') else None
        language = dictionary.get("language") if dictionary.get("language") else None
        # Return an object of this model
        return cls(principal,
                   business_address,
                   language)
