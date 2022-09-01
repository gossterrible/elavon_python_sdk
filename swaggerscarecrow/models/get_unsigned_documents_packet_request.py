# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class GetUnsignedDocumentsPacketRequest(object):

    """Implementation of the 'GetUnsignedDocumentsPacketRequest' model.

    TODO: type model description here.

    Attributes:
        document_packet_id (string): The unique identifier for the document
            packet
        html (bool): If true, the document will be returned as HTML, if false
            the response will be PDF as a binary stream

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_packet_id": 'documentPacketId',
        "html": 'html'
    }

    _optionals = [
        'document_packet_id',
        'html',
    ]

    def __init__(self,
                 document_packet_id=APIHelper.SKIP,
                 html=APIHelper.SKIP):
        """Constructor for the GetUnsignedDocumentsPacketRequest class"""

        # Initialize members of the class
        if document_packet_id is not APIHelper.SKIP:
            self.document_packet_id = document_packet_id 
        if html is not APIHelper.SKIP:
            self.html = html 

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
        html = dictionary.get("html") if "html" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(document_packet_id,
                   html)
