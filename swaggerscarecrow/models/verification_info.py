# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.date_components import DateComponents


class VerificationInfo(object):

    """Implementation of the 'VerificationInfo' model.

    TODO: type model description here.

    Attributes:
        documentary (bool): Flag indicating if business or legal
            documentary/verification info is to be provided, true if Yes,
            false if NO
        issuing_country (string): Country of documentation issuance, ISO
            3166-1 alpha-3 standard applies
        issuing_state (IssuingState1Enum): State of documentation issuance
        site_person_met (string): If site survey conducted for verification
            instead of documentation, this is the person on site met with
        site_visit_date (DateComponents): A container that holds the date
            (day, month, and year)
        id_number (string): Id number of documentation provided
        issue_date (DateComponents): A container that holds the date (day,
            month, and year)
        expiry_date (DateComponents): A container that holds the date (day,
            month, and year)
        document_type (DocumentTypeEnum): Type of documentation provided

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "documentary": 'documentary',
        "issuing_country": 'issuingCountry',
        "issuing_state": 'issuingState',
        "site_person_met": 'sitePersonMet',
        "site_visit_date": 'siteVisitDate',
        "id_number": 'idNumber',
        "issue_date": 'issueDate',
        "expiry_date": 'expiryDate',
        "document_type": 'documentType'
    }

    _optionals = [
        'issuing_country',
        'issuing_state',
        'site_person_met',
        'site_visit_date',
        'id_number',
        'issue_date',
        'expiry_date',
        'document_type',
    ]

    def __init__(self,
                 documentary=None,
                 issuing_country=APIHelper.SKIP,
                 issuing_state=APIHelper.SKIP,
                 site_person_met=APIHelper.SKIP,
                 site_visit_date=APIHelper.SKIP,
                 id_number=APIHelper.SKIP,
                 issue_date=APIHelper.SKIP,
                 expiry_date=APIHelper.SKIP,
                 document_type=APIHelper.SKIP):
        """Constructor for the VerificationInfo class"""

        # Initialize members of the class
        self.documentary = documentary 
        if issuing_country is not APIHelper.SKIP:
            self.issuing_country = issuing_country 
        if issuing_state is not APIHelper.SKIP:
            self.issuing_state = issuing_state 
        if site_person_met is not APIHelper.SKIP:
            self.site_person_met = site_person_met 
        if site_visit_date is not APIHelper.SKIP:
            self.site_visit_date = site_visit_date 
        if id_number is not APIHelper.SKIP:
            self.id_number = id_number 
        if issue_date is not APIHelper.SKIP:
            self.issue_date = issue_date 
        if expiry_date is not APIHelper.SKIP:
            self.expiry_date = expiry_date 
        if document_type is not APIHelper.SKIP:
            self.document_type = document_type 

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

        documentary = dictionary.get("documentary") if "documentary" in dictionary.keys() else None
        issuing_country = dictionary.get("issuingCountry") if dictionary.get("issuingCountry") else APIHelper.SKIP
        issuing_state = dictionary.get("issuingState") if dictionary.get("issuingState") else APIHelper.SKIP
        site_person_met = dictionary.get("sitePersonMet") if dictionary.get("sitePersonMet") else APIHelper.SKIP
        site_visit_date = DateComponents.from_dictionary(dictionary.get('siteVisitDate')) if 'siteVisitDate' in dictionary.keys() else APIHelper.SKIP 
        id_number = dictionary.get("idNumber") if dictionary.get("idNumber") else APIHelper.SKIP
        issue_date = DateComponents.from_dictionary(dictionary.get('issueDate')) if 'issueDate' in dictionary.keys() else APIHelper.SKIP 
        expiry_date = DateComponents.from_dictionary(dictionary.get('expiryDate')) if 'expiryDate' in dictionary.keys() else APIHelper.SKIP 
        document_type = dictionary.get("documentType") if dictionary.get("documentType") else APIHelper.SKIP
        # Return an object of this model
        return cls(documentary,
                   issuing_country,
                   issuing_state,
                   site_person_met,
                   site_visit_date,
                   id_number,
                   issue_date,
                   expiry_date,
                   document_type)