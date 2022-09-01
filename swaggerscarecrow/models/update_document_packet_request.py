# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.document_packet_data import DocumentPacketData
from swaggerscarecrow.models.signer import Signer


class UpdateDocumentPacketRequest(object):

    """Implementation of the 'UpdateDocumentPacketRequest' model.

    TODO: type model description here.

    Attributes:
        document_packet_id (string): The unique identifier for the document
            packet
        profile_code (string): The partner's profile code
        signers (list of Signer): The document signers
        document_packet_data (DocumentPacketData): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_packet_id": 'documentPacketId',
        "profile_code": 'profileCode',
        "signers": 'signers',
        "document_packet_data": 'documentPacketData'
    }

    _optionals = [
        'profile_code',
        'signers',
        'document_packet_data',
    ]

    def __init__(self,
                 document_packet_id=None,
                 profile_code=APIHelper.SKIP,
                 signers=APIHelper.SKIP,
                 document_packet_data=APIHelper.SKIP):
        """Constructor for the UpdateDocumentPacketRequest class"""

        # Initialize members of the class
        self.document_packet_id = document_packet_id 
        if profile_code is not APIHelper.SKIP:
            self.profile_code = profile_code 
        if signers is not APIHelper.SKIP:
            self.signers = signers 
        if document_packet_data is not APIHelper.SKIP:
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
        profile_code = dictionary.get("profileCode") if dictionary.get("profileCode") else APIHelper.SKIP
        signers = None
        if dictionary.get('signers') is not None:
            signers = [Signer.from_dictionary(x) for x in dictionary.get('signers')]
        else:
            signers = APIHelper.SKIP
        document_packet_data = DocumentPacketData.from_dictionary(dictionary.get('documentPacketData')) if 'documentPacketData' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(document_packet_id,
                   profile_code,
                   signers,
                   document_packet_data)