# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class DeleteGroupDocumentPacketRequest(object):

    """Implementation of the 'DeleteGroupDocumentPacketRequest' model.

    TODO: type model description here.

    Attributes:
        group_document_packet_id (string): The unique identifier for group
            document packet

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_document_packet_id": 'groupDocumentPacketId'
    }

    _optionals = [
        'group_document_packet_id',
    ]

    def __init__(self,
                 group_document_packet_id=APIHelper.SKIP):
        """Constructor for the DeleteGroupDocumentPacketRequest class"""

        # Initialize members of the class
        if group_document_packet_id is not APIHelper.SKIP:
            self.group_document_packet_id = group_document_packet_id 

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

        group_document_packet_id = dictionary.get("groupDocumentPacketId") if dictionary.get("groupDocumentPacketId") else APIHelper.SKIP
        # Return an object of this model
        return cls(group_document_packet_id)
