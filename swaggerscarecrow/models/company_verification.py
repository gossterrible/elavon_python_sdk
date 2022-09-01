# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class CompanyVerification(object):

    """Implementation of the 'CompanyVerification' model.

    TODO: type model description here.

    Attributes:
        document_description (string): TODO: type description here.
        document_number (string): TODO: type description here.
        document_type (string): TODO: type description here.
        expiry_date (datetime): TODO: type description here.
        issue_date (datetime): TODO: type description here.
        issuing_agency (string): TODO: type description here.
        issuing_country (string): TODO: type description here.
        issuing_state (string): TODO: type description here.
        met_with (string): TODO: type description here.
        location_type (string): TODO: type description here.
        evidence_of_legal_status (string): TODO: type description here.
        primary (bool): TODO: type description here.
        verification_method_raw (string): TODO: type description here.
        site_visit_date (datetime): TODO: type description here.
        doc_validation_type (string): TODO: type description here.
        non_doc_validation_type (string): TODO: type description here.

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
        "issuing_state": 'issuingState',
        "met_with": 'metWith',
        "location_type": 'locationType',
        "evidence_of_legal_status": 'evidenceOfLegalStatus',
        "primary": 'primary',
        "verification_method_raw": 'verificationMethodRaw',
        "site_visit_date": 'siteVisitDate',
        "doc_validation_type": 'docValidationType',
        "non_doc_validation_type": 'nonDocValidationType'
    }

    _optionals = [
        'document_description',
        'document_number',
        'document_type',
        'expiry_date',
        'issue_date',
        'issuing_agency',
        'issuing_country',
        'issuing_state',
        'met_with',
        'location_type',
        'evidence_of_legal_status',
        'primary',
        'verification_method_raw',
        'site_visit_date',
        'doc_validation_type',
        'non_doc_validation_type',
    ]

    def __init__(self,
                 document_description=APIHelper.SKIP,
                 document_number=APIHelper.SKIP,
                 document_type=APIHelper.SKIP,
                 expiry_date=APIHelper.SKIP,
                 issue_date=APIHelper.SKIP,
                 issuing_agency=APIHelper.SKIP,
                 issuing_country=APIHelper.SKIP,
                 issuing_state=APIHelper.SKIP,
                 met_with=APIHelper.SKIP,
                 location_type=APIHelper.SKIP,
                 evidence_of_legal_status=APIHelper.SKIP,
                 primary=APIHelper.SKIP,
                 verification_method_raw=APIHelper.SKIP,
                 site_visit_date=APIHelper.SKIP,
                 doc_validation_type=APIHelper.SKIP,
                 non_doc_validation_type=APIHelper.SKIP):
        """Constructor for the CompanyVerification class"""

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
        if issuing_state is not APIHelper.SKIP:
            self.issuing_state = issuing_state 
        if met_with is not APIHelper.SKIP:
            self.met_with = met_with 
        if location_type is not APIHelper.SKIP:
            self.location_type = location_type 
        if evidence_of_legal_status is not APIHelper.SKIP:
            self.evidence_of_legal_status = evidence_of_legal_status 
        if primary is not APIHelper.SKIP:
            self.primary = primary 
        if verification_method_raw is not APIHelper.SKIP:
            self.verification_method_raw = verification_method_raw 
        if site_visit_date is not APIHelper.SKIP:
            self.site_visit_date = APIHelper.RFC3339DateTime(site_visit_date) if site_visit_date else None 
        if doc_validation_type is not APIHelper.SKIP:
            self.doc_validation_type = doc_validation_type 
        if non_doc_validation_type is not APIHelper.SKIP:
            self.non_doc_validation_type = non_doc_validation_type 

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
        issuing_state = dictionary.get("issuingState") if dictionary.get("issuingState") else APIHelper.SKIP
        met_with = dictionary.get("metWith") if dictionary.get("metWith") else APIHelper.SKIP
        location_type = dictionary.get("locationType") if dictionary.get("locationType") else APIHelper.SKIP
        evidence_of_legal_status = dictionary.get("evidenceOfLegalStatus") if dictionary.get("evidenceOfLegalStatus") else APIHelper.SKIP
        primary = dictionary.get("primary") if "primary" in dictionary.keys() else APIHelper.SKIP
        verification_method_raw = dictionary.get("verificationMethodRaw") if dictionary.get("verificationMethodRaw") else APIHelper.SKIP
        site_visit_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("siteVisitDate")).datetime if dictionary.get("siteVisitDate") else APIHelper.SKIP
        doc_validation_type = dictionary.get("docValidationType") if dictionary.get("docValidationType") else APIHelper.SKIP
        non_doc_validation_type = dictionary.get("nonDocValidationType") if dictionary.get("nonDocValidationType") else APIHelper.SKIP
        # Return an object of this model
        return cls(document_description,
                   document_number,
                   document_type,
                   expiry_date,
                   issue_date,
                   issuing_agency,
                   issuing_country,
                   issuing_state,
                   met_with,
                   location_type,
                   evidence_of_legal_status,
                   primary,
                   verification_method_raw,
                   site_visit_date,
                   doc_validation_type,
                   non_doc_validation_type)
