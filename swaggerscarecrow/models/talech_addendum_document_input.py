# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.business_info import BusinessInfo
from swaggerscarecrow.models.equipment_info import EquipmentInfo
from swaggerscarecrow.models.person import Person


class TalechAddendumDocumentInput(object):

    """Implementation of the 'TalechAddendumDocumentInput' model.

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
        principal (Person): TODO: type description here.
        displayed_currency (string): Application's currency, ISO 4217 standard
            applies
        equipment_info (EquipmentInfo): In NA, it's mandatory to have at least
            one piece of equipment. For third party vendors           
            managing their own equipment, at least one Value Added Reseller
            (VAR) code must be sent.            Contact your Elavon
            representative for the VAR code(s).            In EU,
            equipmentInfo is optional and no equipment has to be sent. If you
            have any equipment            managed by Elavon, contact your
            Elavon representative for the VAR code(s).
        business_info (BusinessInfo): TODO: type description here.
        additional_shareholders (list of Person): Application's additional
            shareholders

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "language": 'language',
        "document_id": 'documentId',
        "principal": 'principal',
        "displayed_currency": 'displayedCurrency',
        "equipment_info": 'equipmentInfo',
        "business_info": 'businessInfo',
        "agreement_id": 'agreementId',
        "document_packet_id": 'documentPacketId',
        "signed": 'signed',
        "grouped_application": 'groupedApplication',
        "wet_signed": 'wetSigned',
        "additional_shareholders": 'additionalShareholders'
    }

    _optionals = [
        'agreement_id',
        'document_packet_id',
        'signed',
        'grouped_application',
        'wet_signed',
        'additional_shareholders',
    ]

    def __init__(self,
                 language=None,
                 document_id=None,
                 principal=None,
                 displayed_currency=None,
                 equipment_info=None,
                 business_info=None,
                 agreement_id=APIHelper.SKIP,
                 document_packet_id=APIHelper.SKIP,
                 signed=APIHelper.SKIP,
                 grouped_application=APIHelper.SKIP,
                 wet_signed=APIHelper.SKIP,
                 additional_shareholders=APIHelper.SKIP):
        """Constructor for the TalechAddendumDocumentInput class"""

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
        self.principal = principal 
        self.displayed_currency = displayed_currency 
        self.equipment_info = equipment_info 
        self.business_info = business_info 
        if additional_shareholders is not APIHelper.SKIP:
            self.additional_shareholders = additional_shareholders 

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
        principal = Person.from_dictionary(dictionary.get('principal')) if dictionary.get('principal') else None
        displayed_currency = dictionary.get("displayedCurrency") if dictionary.get("displayedCurrency") else None
        equipment_info = EquipmentInfo.from_dictionary(dictionary.get('equipmentInfo')) if dictionary.get('equipmentInfo') else None
        business_info = BusinessInfo.from_dictionary(dictionary.get('businessInfo')) if dictionary.get('businessInfo') else None
        agreement_id = dictionary.get("agreementId") if dictionary.get("agreementId") else APIHelper.SKIP
        document_packet_id = dictionary.get("documentPacketId") if dictionary.get("documentPacketId") else APIHelper.SKIP
        signed = dictionary.get("signed") if "signed" in dictionary.keys() else APIHelper.SKIP
        grouped_application = dictionary.get("groupedApplication") if "groupedApplication" in dictionary.keys() else APIHelper.SKIP
        wet_signed = dictionary.get("wetSigned") if "wetSigned" in dictionary.keys() else APIHelper.SKIP
        additional_shareholders = None
        if dictionary.get('additionalShareholders') is not None:
            additional_shareholders = [Person.from_dictionary(x) for x in dictionary.get('additionalShareholders')]
        else:
            additional_shareholders = APIHelper.SKIP
        # Return an object of this model
        return cls(language,
                   document_id,
                   principal,
                   displayed_currency,
                   equipment_info,
                   business_info,
                   agreement_id,
                   document_packet_id,
                   signed,
                   grouped_application,
                   wet_signed,
                   additional_shareholders)
