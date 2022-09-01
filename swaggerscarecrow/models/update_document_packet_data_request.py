# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.document_packet_data import DocumentPacketData
from swaggerscarecrow.models.signer import Signer


class UpdateDocumentPacketDataRequest(object):

    """Implementation of the 'UpdateDocumentPacketDataRequest' model.

    TODO: type model description here.

    Attributes:
        signers (list of Signer): The document signers
        document_packet_id (string): The unique id for the document packet
        document_packet_data (DocumentPacketData): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_packet_id": 'documentPacketId',
        "document_packet_data": 'documentPacketData',
        "signers": 'signers'
    }

    _optionals = [
        'signers',
    ]

    def __init__(self,
                 document_packet_id=None,
                 document_packet_data=None,
                 signers=APIHelper.SKIP):
        """Constructor for the UpdateDocumentPacketDataRequest class"""

        # Initialize members of the class
        if signers is not APIHelper.SKIP:
            self.signers = signers 
        self.document_packet_id = document_packet_id 
        self.document_packet_data = document_packet_data 

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

        document_packet_id = dictionary.get("documentPacketId") if dictionary.get("documentPacketId") else None
        document_packet_data = DocumentPacketData.from_dictionary(dictionary.get('documentPacketData')) if dictionary.get('documentPacketData') else None
        signers = None
        if dictionary.get('signers') is not None:
            signers = [Signer.from_dictionary(x) for x in dictionary.get('signers')]
        else:
            signers = APIHelper.SKIP
        # Return an object of this model
        return cls(document_packet_id,
                   document_packet_data,
                   signers)