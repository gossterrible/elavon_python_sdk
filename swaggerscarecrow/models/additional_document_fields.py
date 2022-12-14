# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class AdditionalDocumentFields(object):

    """Implementation of the 'AdditionalDocumentFields' model.

    A container used to hold additional documents associated with the
    application

    Attributes:
        label_code (string): TODO: type description here.
        label_value (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "label_code": 'labelCode',
        "label_value": 'labelValue'
    }

    _optionals = [
        'label_code',
        'label_value',
    ]

    def __init__(self,
                 label_code=APIHelper.SKIP,
                 label_value=APIHelper.SKIP):
        """Constructor for the AdditionalDocumentFields class"""

        # Initialize members of the class
        if label_code is not APIHelper.SKIP:
            self.label_code = label_code 
        if label_value is not APIHelper.SKIP:
            self.label_value = label_value 

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

        label_code = dictionary.get("labelCode") if dictionary.get("labelCode") else APIHelper.SKIP
        label_value = dictionary.get("labelValue") if dictionary.get("labelValue") else APIHelper.SKIP
        # Return an object of this model
        return cls(label_code,
                   label_value)
