# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.signer_status_response import SignerStatusResponse


class CheckDocumentSigningStatusResponse(object):

    """Implementation of the 'CheckDocumentSigningStatusResponse' model.

    TODO: type model description here.

    Attributes:
        response_id (int): TODO: type description here.
        packet_status (PacketStatusEnum): The document packet's status
        signers (list of SignerStatusResponse): Signers and their status for a
            document status
        error (string): Any error that resulted from the request

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "packet_status": 'packetStatus',
        "signers": 'signers',
        "response_id": 'responseId',
        "error": 'error'
    }

    _optionals = [
        'response_id',
        'error',
    ]

    def __init__(self,
                 packet_status=None,
                 signers=None,
                 response_id=APIHelper.SKIP,
                 error=APIHelper.SKIP):
        """Constructor for the CheckDocumentSigningStatusResponse class"""

        # Initialize members of the class
        if response_id is not APIHelper.SKIP:
            self.response_id = response_id 
        self.packet_status = packet_status 
        self.signers = signers 
        if error is not APIHelper.SKIP:
            self.error = error 

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

        packet_status = dictionary.get("packetStatus") if dictionary.get("packetStatus") else None
        signers = None
        if dictionary.get('signers') is not None:
            signers = [SignerStatusResponse.from_dictionary(x) for x in dictionary.get('signers')]
        response_id = dictionary.get("responseId") if dictionary.get("responseId") else APIHelper.SKIP
        error = dictionary.get("error") if dictionary.get("error") else APIHelper.SKIP
        # Return an object of this model
        return cls(packet_status,
                   signers,
                   response_id,
                   error)
