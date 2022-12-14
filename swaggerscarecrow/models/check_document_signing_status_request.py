# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class CheckDocumentSigningStatusRequest(object):

    """Implementation of the 'CheckDocumentSigningStatusRequest' model.

    TODO: type model description here.

    Attributes:
        document_packet_id (string): The unique identifier for the document
            packet

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_packet_id": 'documentPacketId'
    }

    _optionals = [
        'document_packet_id',
    ]

    def __init__(self,
                 document_packet_id=APIHelper.SKIP):
        """Constructor for the CheckDocumentSigningStatusRequest class"""

        # Initialize members of the class
        if document_packet_id is not APIHelper.SKIP:
            self.document_packet_id = document_packet_id 

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

        document_packet_id = dictionary.get("documentPacketId") if dictionary.get("documentPacketId") else APIHelper.SKIP
        # Return an object of this model
        return cls(document_packet_id)
