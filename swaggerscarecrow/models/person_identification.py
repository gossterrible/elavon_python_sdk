# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class PersonIdentification(object):

    """Implementation of the 'PersonIdentification' model.

    TODO: type model description here.

    Attributes:
        document_description (string): TODO: type description here.
        document_number (string): TODO: type description here.
        document_type (string): TODO: type description here.
        expiry_date (datetime): TODO: type description here.
        issue_date (datetime): TODO: type description here.
        issuing_agency (string): TODO: type description here.
        issuing_country (string): TODO: type description here.
        issuing_province (string): TODO: type description here.
        primary (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "document_description": 'documentDescription',
        "document_number": 'documentNumber',
        "document_type": 'documentType',
        "expiry_date": 'expiryDate',
        "issue_date": 'issueDate',
        "issuing_agency": 'issuingAgency',
        "issuing_country": 'issuingCountry',
        "issuing_province": 'issuingProvince',
        "primary": 'primary'
    }

    _optionals = [
        'document_description',
        'document_number',
        'document_type',
        'expiry_date',
        'issue_date',
        'issuing_agency',
        'issuing_country',
        'issuing_province',
        'primary',
    ]

    def __init__(self,
                 document_description=APIHelper.SKIP,
                 document_number=APIHelper.SKIP,
                 document_type=APIHelper.SKIP,
                 expiry_date=APIHelper.SKIP,
                 issue_date=APIHelper.SKIP,
                 issuing_agency=APIHelper.SKIP,
                 issuing_country=APIHelper.SKIP,
                 issuing_province=APIHelper.SKIP,
                 primary=APIHelper.SKIP):
        """Constructor for the PersonIdentification class"""

        # Initialize members of the class
        if document_description is not APIHelper.SKIP:
            self.document_description = document_description 
        if document_number is not APIHelper.SKIP:
            self.document_number = document_number 
        if document_type is not APIHelper.SKIP:
            self.document_type = document_type 
        if expiry_date is not APIHelper.SKIP:
            self.expiry_date = APIHelper.RFC3339DateTime(expiry_date) if expiry_date else None 
        if issue_date is not APIHelper.SKIP:
            self.issue_date = APIHelper.RFC3339DateTime(issue_date) if issue_date else None 
        if issuing_agency is not APIHelper.SKIP:
            self.issuing_agency = issuing_agency 
        if issuing_country is not APIHelper.SKIP:
            self.issuing_country = issuing_country 
        if issuing_province is not APIHelper.SKIP:
            self.issuing_province = issuing_province 
        if primary is not APIHelper.SKIP:
            self.primary = primary 

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

        document_description = dictionary.get("documentDescription") if dictionary.get("documentDescription") else APIHelper.SKIP
        document_number = dictionary.get("documentNumber") if dictionary.get("documentNumber") else APIHelper.SKIP
        document_type = dictionary.get("documentType") if dictionary.get("documentType") else APIHelper.SKIP
        expiry_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("expiryDate")).datetime if dictionary.get("expiryDate") else APIHelper.SKIP
        issue_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("issueDate")).datetime if dictionary.get("issueDate") else APIHelper.SKIP
        issuing_agency = dictionary.get("issuingAgency") if dictionary.get("issuingAgency") else APIHelper.SKIP
        issuing_country = dictionary.get("issuingCountry") if dictionary.get("issuingCountry") else APIHelper.SKIP
        issuing_province = dictionary.get("issuingProvince") if dictionary.get("issuingProvince") else APIHelper.SKIP
        primary = dictionary.get("primary") if "primary" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(document_description,
                   document_number,
                   document_type,
                   expiry_date,
                   issue_date,
                   issuing_agency,
                   issuing_country,
                   issuing_province,
                   primary)
