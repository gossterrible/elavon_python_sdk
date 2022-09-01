# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.uploaded_document_data_response import UploadedDocumentDataResponse


class UploadDocumentResponse(object):

    """Implementation of the 'UploadDocumentResponse' model.

    TODO: type model description here.

    Attributes:
        error (string): Error message from service
        doc_reference_number (string): Unique identifier of upload document
            response
        uploaded_documents_response (list of UploadedDocumentDataResponse):
            Listing of individual document upload statuses

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error": 'error',
        "doc_reference_number": 'docReferenceNumber',
        "uploaded_documents_response": 'uploadedDocumentsResponse'
    }

    _optionals = [
        'error',
        'doc_reference_number',
        'uploaded_documents_response',
    ]

    def __init__(self,
                 error=APIHelper.SKIP,
                 doc_reference_number=APIHelper.SKIP,
                 uploaded_documents_response=APIHelper.SKIP):
        """Constructor for the UploadDocumentResponse class"""

        # Initialize members of the class
        if error is not APIHelper.SKIP:
            self.error = error 
        if doc_reference_number is not APIHelper.SKIP:
            self.doc_reference_number = doc_reference_number 
        if uploaded_documents_response is not APIHelper.SKIP:
            self.uploaded_documents_response = uploaded_documents_response 

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

        error = dictionary.get("error") if dictionary.get("error") else APIHelper.SKIP
        doc_reference_number = dictionary.get("docReferenceNumber") if dictionary.get("docReferenceNumber") else APIHelper.SKIP
        uploaded_documents_response = None
        if dictionary.get('uploadedDocumentsResponse') is not None:
            uploaded_documents_response = [UploadedDocumentDataResponse.from_dictionary(x) for x in dictionary.get('uploadedDocumentsResponse')]
        else:
            uploaded_documents_response = APIHelper.SKIP
        # Return an object of this model
        return cls(error,
                   doc_reference_number,
                   uploaded_documents_response)
