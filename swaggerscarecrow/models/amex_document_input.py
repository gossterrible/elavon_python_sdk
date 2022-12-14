# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.banking_info import BankingInfo
from swaggerscarecrow.models.business_info import BusinessInfo
from swaggerscarecrow.models.card_pricing import CardPricing
from swaggerscarecrow.models.person import Person


class AmexDocumentInput(object):

    """Implementation of the 'AmexDocumentInput' model.

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
        card_pricing (CardPricing): TODO: type description here.
        business_info (BusinessInfo): TODO: type description here.
        monetary_pricing_program (string): Application's monetary pricing
            program (MPP)
        bank_accounts (dict): Application's banking information. The valid
            keys are as follows: BILLING, DEPOSIT, LEASE, CHARGEBACK
        applicant_email (string): Email address of applicant
        principal (Person): TODO: type description here.
        additional_shareholders (list of Person): Application's additional
            shareholders

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "language": 'language',
        "document_id": 'documentId',
        "card_pricing": 'cardPricing',
        "business_info": 'businessInfo',
        "bank_accounts": 'bankAccounts',
        "applicant_email": 'applicantEmail',
        "principal": 'principal',
        "agreement_id": 'agreementId',
        "document_packet_id": 'documentPacketId',
        "signed": 'signed',
        "grouped_application": 'groupedApplication',
        "wet_signed": 'wetSigned',
        "monetary_pricing_program": 'monetaryPricingProgram',
        "additional_shareholders": 'additionalShareholders'
    }

    _optionals = [
        'agreement_id',
        'document_packet_id',
        'signed',
        'grouped_application',
        'wet_signed',
        'monetary_pricing_program',
        'additional_shareholders',
    ]

    def __init__(self,
                 language=None,
                 document_id=None,
                 card_pricing=None,
                 business_info=None,
                 bank_accounts=None,
                 applicant_email=None,
                 principal=None,
                 agreement_id=APIHelper.SKIP,
                 document_packet_id=APIHelper.SKIP,
                 signed=APIHelper.SKIP,
                 grouped_application=APIHelper.SKIP,
                 wet_signed=APIHelper.SKIP,
                 monetary_pricing_program=APIHelper.SKIP,
                 additional_shareholders=APIHelper.SKIP):
        """Constructor for the AmexDocumentInput class"""

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
        self.card_pricing = card_pricing 
        self.business_info = business_info 
        if monetary_pricing_program is not APIHelper.SKIP:
            self.monetary_pricing_program = monetary_pricing_program 
        self.bank_accounts = bank_accounts 
        self.applicant_email = applicant_email 
        self.principal = principal 
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
        card_pricing = CardPricing.from_dictionary(dictionary.get('cardPricing')) if dictionary.get('cardPricing') else None
        business_info = BusinessInfo.from_dictionary(dictionary.get('businessInfo')) if dictionary.get('businessInfo') else None
        bank_accounts = BankingInfo.from_dictionary(dictionary.get('bankAccounts')) if dictionary.get('bankAccounts') else None
        applicant_email = dictionary.get("applicantEmail") if dictionary.get("applicantEmail") else None
        principal = Person.from_dictionary(dictionary.get('principal')) if dictionary.get('principal') else None
        agreement_id = dictionary.get("agreementId") if dictionary.get("agreementId") else APIHelper.SKIP
        document_packet_id = dictionary.get("documentPacketId") if dictionary.get("documentPacketId") else APIHelper.SKIP
        signed = dictionary.get("signed") if "signed" in dictionary.keys() else APIHelper.SKIP
        grouped_application = dictionary.get("groupedApplication") if "groupedApplication" in dictionary.keys() else APIHelper.SKIP
        wet_signed = dictionary.get("wetSigned") if "wetSigned" in dictionary.keys() else APIHelper.SKIP
        monetary_pricing_program = dictionary.get("monetaryPricingProgram") if dictionary.get("monetaryPricingProgram") else APIHelper.SKIP
        additional_shareholders = None
        if dictionary.get('additionalShareholders') is not None:
            additional_shareholders = [Person.from_dictionary(x) for x in dictionary.get('additionalShareholders')]
        else:
            additional_shareholders = APIHelper.SKIP
        # Return an object of this model
        return cls(language,
                   document_id,
                   card_pricing,
                   business_info,
                   bank_accounts,
                   applicant_email,
                   principal,
                   agreement_id,
                   document_packet_id,
                   signed,
                   grouped_application,
                   wet_signed,
                   monetary_pricing_program,
                   additional_shareholders)
