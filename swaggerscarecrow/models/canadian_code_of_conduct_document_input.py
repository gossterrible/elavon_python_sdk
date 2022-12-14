# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.card_volume import CardVolume
from swaggerscarecrow.models.sales_office_contact import SalesOfficeContact
from swaggerscarecrow.models.scarecrow_application import ScarecrowApplication


class CanadianCodeOfConductDocumentInput(object):

    """Implementation of the 'CanadianCodeOfConductDocumentInput' model.

    TODO: type model description here.

    Attributes:
        language (string): Language of document to be generated,  ISO 639-1
            standard applies
        document_id (string): Unique id of document
        agreement_id (string): Merchant id (MID)
        document_packet_id (string): Document packet id
        signed (bool): Boolean flag indicating if document has been signed,
            true if  YES, false if NO
        grouped_application (bool): Boolean flag indicating if document is of
            a group of applications, true if  YES, false if NO
        wet_signed (bool): Boolean flag indicating if document is to be wet
            signed, true if  YES, false if NO
        scarecrow_application (ScarecrowApplication): TODO: type description
            here.
        card_volume (CardVolume): TODO: type description here.
        sales_office_contact (SalesOfficeContact): TODO: type description
            here.
        sub_jurisdiction_id (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "language": 'language',
        "document_id": 'documentId',
        "scarecrow_application": 'scarecrowApplication',
        "card_volume": 'cardVolume',
        "sales_office_contact": 'salesOfficeContact',
        "agreement_id": 'agreementId',
        "document_packet_id": 'documentPacketId',
        "signed": 'signed',
        "grouped_application": 'groupedApplication',
        "wet_signed": 'wetSigned',
        "sub_jurisdiction_id": 'subJurisdictionId'
    }

    _optionals = [
        'agreement_id',
        'document_packet_id',
        'signed',
        'grouped_application',
        'wet_signed',
        'sub_jurisdiction_id',
    ]

    def __init__(self,
                 language=None,
                 document_id=None,
                 scarecrow_application=None,
                 card_volume=None,
                 sales_office_contact=None,
                 agreement_id=APIHelper.SKIP,
                 document_packet_id=APIHelper.SKIP,
                 signed=APIHelper.SKIP,
                 grouped_application=APIHelper.SKIP,
                 wet_signed=APIHelper.SKIP,
                 sub_jurisdiction_id=APIHelper.SKIP):
        """Constructor for the CanadianCodeOfConductDocumentInput class"""

        # Initialize members of the class
        self.language = language 
        self.document_id = document_id 
        if agreement_id is not APIHelper.SKIP:
            self.agreement_id = agreement_id 
        if document_packet_id is not APIHelper.SKIP:
            self.document_packet_id = document_packet_id 
        if signed is not APIHelper.SKIP:
            self.signed = signed 
        if grouped_application is not APIHelper.SKIP:
            self.grouped_application = grouped_application 
        if wet_signed is not APIHelper.SKIP:
            self.wet_signed = wet_signed 
        self.scarecrow_application = scarecrow_application 
        self.card_volume = card_volume 
        self.sales_office_contact = sales_office_contact 
        if sub_jurisdiction_id is not APIHelper.SKIP:
            self.sub_jurisdiction_id = sub_jurisdiction_id 

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

        language = dictionary.get("language") if dictionary.get("language") else None
        document_id = dictionary.get("documentId") if dictionary.get("documentId") else None
        scarecrow_application = ScarecrowApplication.from_dictionary(dictionary.get('scarecrowApplication')) if dictionary.get('scarecrowApplication') else None
        card_volume = CardVolume.from_dictionary(dictionary.get('cardVolume')) if dictionary.get('cardVolume') else None
        sales_office_contact = SalesOfficeContact.from_dictionary(dictionary.get('salesOfficeContact')) if dictionary.get('salesOfficeContact') else None
        agreement_id = dictionary.get("agreementId") if dictionary.get("agreementId") else APIHelper.SKIP
        document_packet_id = dictionary.get("documentPacketId") if dictionary.get("documentPacketId") else APIHelper.SKIP
        signed = dictionary.get("signed") if "signed" in dictionary.keys() else APIHelper.SKIP
        grouped_application = dictionary.get("groupedApplication") if "groupedApplication" in dictionary.keys() else APIHelper.SKIP
        wet_signed = dictionary.get("wetSigned") if "wetSigned" in dictionary.keys() else APIHelper.SKIP
        sub_jurisdiction_id = dictionary.get("subJurisdictionId") if dictionary.get("subJurisdictionId") else APIHelper.SKIP
        # Return an object of this model
        return cls(language,
                   document_id,
                   scarecrow_application,
                   card_volume,
                   sales_office_contact,
                   agreement_id,
                   document_packet_id,
                   signed,
                   grouped_application,
                   wet_signed,
                   sub_jurisdiction_id)
