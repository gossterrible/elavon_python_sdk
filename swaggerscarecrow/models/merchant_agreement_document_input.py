# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.acting_intermediary_info import ActingIntermediaryInfo
from swaggerscarecrow.models.additional_auth_pricing_program_info import AdditionalAuthPricingProgramInfo
from swaggerscarecrow.models.additional_business_info import AdditionalBusinessInfo
from swaggerscarecrow.models.additional_card_pricing_info import AdditionalCardPricingInfo
from swaggerscarecrow.models.additional_description_info import AdditionalDescriptionInfo
from swaggerscarecrow.models.additional_lease_info import AdditionalLeaseInfo
from swaggerscarecrow.models.additional_site_survey_info import AdditionalSiteSurveyInfo
from swaggerscarecrow.models.bank_account_additional_info import BankAccountAdditionalInfo
from swaggerscarecrow.models.integrator_solution_info import IntegratorSolutionInfo
from swaggerscarecrow.models.provider_info import ProviderInfo
from swaggerscarecrow.models.sales_office_contact import SalesOfficeContact
from swaggerscarecrow.models.scarecrow_application import ScarecrowApplication
from swaggerscarecrow.models.value_added_services import ValueAddedServices
from swaggerscarecrow.models.var_other_details import VarOtherDetails


class MerchantAgreementDocumentInput(object):

    """Implementation of the 'MerchantAgreementDocumentInput' model.

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
        vendor_info (ProviderInfo): TODO: type description here.
        acting_intermediary_info (ActingIntermediaryInfo): TODO: type
            description here.
        bank_account_details_map (dict): Application's additional bank account
            informationThe valid keys are as follows: BILLING, DEPOSIT, LEASE,
            CHARGEBACK
        is_tax_exempt_equipment (bool): Flag indicating if equipment is to be
            considered tax exempt, true if exempt YES, false if NOT exept
        talech_egift_only (bool): Flag indicating if equipment is to Talech
            eGift, true if selected YES, false if NOT selected
        displayed_currency (string): Application's currency, ISO 4217 standard
            applies
        additional_description_info (AdditionalDescriptionInfo): TODO: type
            description here.
        additional_value_added_service_info (ValueAddedServices): TODO: type
            description here.
        additional_business_info (AdditionalBusinessInfo): TODO: type
            description here.
        funding_type (FundingTypeEnum): Application's funding type
        integrator_solution_info (IntegratorSolutionInfo): TODO: type
            description here.
        additional_lease_info (AdditionalLeaseInfo): TODO: type description
            here.
        marketing_data_consent_map (dict): Application's consent form
            (POL).The valid keys are the numerical value of the marketing
            consent option (1, 2, 3, etc)
        additional_site_survey_info (AdditionalSiteSurveyInfo): TODO: type
            description here.
        kyc_quiz_status_map (dict): Status results of the KCY check
        var_other_details (VarOtherDetails): TODO: type description here.
        additional_card_pricing_info (AdditionalCardPricingInfo): TODO: type
            description here.
        sales_office_contact (SalesOfficeContact): TODO: type description
            here.
        additional_auth_pricing_program_info
            (AdditionalAuthPricingProgramInfo): TODO: type description here.
        applicant_email (string): Applicant's email address
        application_id (int): Application id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "language": 'language',
        "document_id": 'documentId',
        "scarecrow_application": 'scarecrowApplication',
        "vendor_info": 'vendorInfo',
        "bank_account_details_map": 'bankAccountDetailsMap',
        "displayed_currency": 'displayedCurrency',
        "agreement_id": 'agreementId',
        "document_packet_id": 'documentPacketId',
        "signed": 'signed',
        "grouped_application": 'groupedApplication',
        "wet_signed": 'wetSigned',
        "acting_intermediary_info": 'actingIntermediaryInfo',
        "is_tax_exempt_equipment": 'isTaxExemptEquipment',
        "talech_egift_only": 'talechEgiftOnly',
        "additional_description_info": 'additionalDescriptionInfo',
        "additional_value_added_service_info": 'additionalValueAddedServiceInfo',
        "additional_business_info": 'additionalBusinessInfo',
        "funding_type": 'fundingType',
        "integrator_solution_info": 'integratorSolutionInfo',
        "additional_lease_info": 'additionalLeaseInfo',
        "marketing_data_consent_map": 'marketingDataConsentMap',
        "additional_site_survey_info": 'additionalSiteSurveyInfo',
        "kyc_quiz_status_map": 'kycQuizStatusMap',
        "var_other_details": 'varOtherDetails',
        "additional_card_pricing_info": 'additionalCardPricingInfo',
        "sales_office_contact": 'salesOfficeContact',
        "additional_auth_pricing_program_info": 'additionalAuthPricingProgramInfo',
        "applicant_email": 'applicantEmail',
        "application_id": 'applicationId'
    }

    _optionals = [
        'agreement_id',
        'document_packet_id',
        'signed',
        'grouped_application',
        'wet_signed',
        'acting_intermediary_info',
        'is_tax_exempt_equipment',
        'talech_egift_only',
        'additional_description_info',
        'additional_value_added_service_info',
        'additional_business_info',
        'funding_type',
        'integrator_solution_info',
        'additional_lease_info',
        'marketing_data_consent_map',
        'additional_site_survey_info',
        'kyc_quiz_status_map',
        'var_other_details',
        'additional_card_pricing_info',
        'sales_office_contact',
        'additional_auth_pricing_program_info',
        'applicant_email',
        'application_id',
    ]

    def __init__(self,
                 language=None,
                 document_id=None,
                 scarecrow_application=None,
                 vendor_info=None,
                 bank_account_details_map=None,
                 displayed_currency=None,
                 agreement_id=APIHelper.SKIP,
                 document_packet_id=APIHelper.SKIP,
                 signed=APIHelper.SKIP,
                 grouped_application=APIHelper.SKIP,
                 wet_signed=APIHelper.SKIP,
                 acting_intermediary_info=APIHelper.SKIP,
                 is_tax_exempt_equipment=APIHelper.SKIP,
                 talech_egift_only=APIHelper.SKIP,
                 additional_description_info=APIHelper.SKIP,
                 additional_value_added_service_info=APIHelper.SKIP,
                 additional_business_info=APIHelper.SKIP,
                 funding_type=APIHelper.SKIP,
                 integrator_solution_info=APIHelper.SKIP,
                 additional_lease_info=APIHelper.SKIP,
                 marketing_data_consent_map=APIHelper.SKIP,
                 additional_site_survey_info=APIHelper.SKIP,
                 kyc_quiz_status_map=APIHelper.SKIP,
                 var_other_details=APIHelper.SKIP,
                 additional_card_pricing_info=APIHelper.SKIP,
                 sales_office_contact=APIHelper.SKIP,
                 additional_auth_pricing_program_info=APIHelper.SKIP,
                 applicant_email=APIHelper.SKIP,
                 application_id=APIHelper.SKIP):
        """Constructor for the MerchantAgreementDocumentInput class"""

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
        self.vendor_info = vendor_info 
        if acting_intermediary_info is not APIHelper.SKIP:
            self.acting_intermediary_info = acting_intermediary_info 
        self.bank_account_details_map = bank_account_details_map 
        if is_tax_exempt_equipment is not APIHelper.SKIP:
            self.is_tax_exempt_equipment = is_tax_exempt_equipment 
        if talech_egift_only is not APIHelper.SKIP:
            self.talech_egift_only = talech_egift_only 
        self.displayed_currency = displayed_currency 
        if additional_description_info is not APIHelper.SKIP:
            self.additional_description_info = additional_description_info 
        if additional_value_added_service_info is not APIHelper.SKIP:
            self.additional_value_added_service_info = additional_value_added_service_info 
        if additional_business_info is not APIHelper.SKIP:
            self.additional_business_info = additional_business_info 
        if funding_type is not APIHelper.SKIP:
            self.funding_type = funding_type 
        if integrator_solution_info is not APIHelper.SKIP:
            self.integrator_solution_info = integrator_solution_info 
        if additional_lease_info is not APIHelper.SKIP:
            self.additional_lease_info = additional_lease_info 
        if marketing_data_consent_map is not APIHelper.SKIP:
            self.marketing_data_consent_map = marketing_data_consent_map 
        if additional_site_survey_info is not APIHelper.SKIP:
            self.additional_site_survey_info = additional_site_survey_info 
        if kyc_quiz_status_map is not APIHelper.SKIP:
            self.kyc_quiz_status_map = kyc_quiz_status_map 
        if var_other_details is not APIHelper.SKIP:
            self.var_other_details = var_other_details 
        if additional_card_pricing_info is not APIHelper.SKIP:
            self.additional_card_pricing_info = additional_card_pricing_info 
        if sales_office_contact is not APIHelper.SKIP:
            self.sales_office_contact = sales_office_contact 
        if additional_auth_pricing_program_info is not APIHelper.SKIP:
            self.additional_auth_pricing_program_info = additional_auth_pricing_program_info 
        if applicant_email is not APIHelper.SKIP:
            self.applicant_email = applicant_email 
        if application_id is not APIHelper.SKIP:
            self.application_id = application_id 

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
        vendor_info = ProviderInfo.from_dictionary(dictionary.get('vendorInfo')) if dictionary.get('vendorInfo') else None
        bank_account_details_map = BankAccountAdditionalInfo.from_dictionary(dictionary.get('bankAccountDetailsMap')) if dictionary.get('bankAccountDetailsMap') else None
        displayed_currency = dictionary.get("displayedCurrency") if dictionary.get("displayedCurrency") else None
        agreement_id = dictionary.get("agreementId") if dictionary.get("agreementId") else APIHelper.SKIP
        document_packet_id = dictionary.get("documentPacketId") if dictionary.get("documentPacketId") else APIHelper.SKIP
        signed = dictionary.get("signed") if "signed" in dictionary.keys() else APIHelper.SKIP
        grouped_application = dictionary.get("groupedApplication") if "groupedApplication" in dictionary.keys() else APIHelper.SKIP
        wet_signed = dictionary.get("wetSigned") if "wetSigned" in dictionary.keys() else APIHelper.SKIP
        acting_intermediary_info = ActingIntermediaryInfo.from_dictionary(dictionary.get('actingIntermediaryInfo')) if 'actingIntermediaryInfo' in dictionary.keys() else APIHelper.SKIP 
        is_tax_exempt_equipment = dictionary.get("isTaxExemptEquipment") if "isTaxExemptEquipment" in dictionary.keys() else APIHelper.SKIP
        talech_egift_only = dictionary.get("talechEgiftOnly") if "talechEgiftOnly" in dictionary.keys() else APIHelper.SKIP
        additional_description_info = AdditionalDescriptionInfo.from_dictionary(dictionary.get('additionalDescriptionInfo')) if 'additionalDescriptionInfo' in dictionary.keys() else APIHelper.SKIP 
        additional_value_added_service_info = ValueAddedServices.from_dictionary(dictionary.get('additionalValueAddedServiceInfo')) if 'additionalValueAddedServiceInfo' in dictionary.keys() else APIHelper.SKIP 
        additional_business_info = AdditionalBusinessInfo.from_dictionary(dictionary.get('additionalBusinessInfo')) if 'additionalBusinessInfo' in dictionary.keys() else APIHelper.SKIP 
        funding_type = dictionary.get("fundingType") if dictionary.get("fundingType") else APIHelper.SKIP
        integrator_solution_info = IntegratorSolutionInfo.from_dictionary(dictionary.get('integratorSolutionInfo')) if 'integratorSolutionInfo' in dictionary.keys() else APIHelper.SKIP 
        additional_lease_info = AdditionalLeaseInfo.from_dictionary(dictionary.get('additionalLeaseInfo')) if 'additionalLeaseInfo' in dictionary.keys() else APIHelper.SKIP 
        marketing_data_consent_map = dictionary.get("marketingDataConsentMap") if "marketingDataConsentMap" in dictionary.keys() else APIHelper.SKIP
        additional_site_survey_info = AdditionalSiteSurveyInfo.from_dictionary(dictionary.get('additionalSiteSurveyInfo')) if 'additionalSiteSurveyInfo' in dictionary.keys() else APIHelper.SKIP 
        kyc_quiz_status_map = dictionary.get("kycQuizStatusMap") if dictionary.get("kycQuizStatusMap") else APIHelper.SKIP
        var_other_details = VarOtherDetails.from_dictionary(dictionary.get('varOtherDetails')) if 'varOtherDetails' in dictionary.keys() else APIHelper.SKIP 
        additional_card_pricing_info = AdditionalCardPricingInfo.from_dictionary(dictionary.get('additionalCardPricingInfo')) if 'additionalCardPricingInfo' in dictionary.keys() else APIHelper.SKIP 
        sales_office_contact = SalesOfficeContact.from_dictionary(dictionary.get('salesOfficeContact')) if 'salesOfficeContact' in dictionary.keys() else APIHelper.SKIP 
        additional_auth_pricing_program_info = AdditionalAuthPricingProgramInfo.from_dictionary(dictionary.get('additionalAuthPricingProgramInfo')) if 'additionalAuthPricingProgramInfo' in dictionary.keys() else APIHelper.SKIP 
        applicant_email = dictionary.get("applicantEmail") if dictionary.get("applicantEmail") else APIHelper.SKIP
        application_id = dictionary.get("applicationId") if dictionary.get("applicationId") else APIHelper.SKIP
        # Return an object of this model
        return cls(language,
                   document_id,
                   scarecrow_application,
                   vendor_info,
                   bank_account_details_map,
                   displayed_currency,
                   agreement_id,
                   document_packet_id,
                   signed,
                   grouped_application,
                   wet_signed,
                   acting_intermediary_info,
                   is_tax_exempt_equipment,
                   talech_egift_only,
                   additional_description_info,
                   additional_value_added_service_info,
                   additional_business_info,
                   funding_type,
                   integrator_solution_info,
                   additional_lease_info,
                   marketing_data_consent_map,
                   additional_site_survey_info,
                   kyc_quiz_status_map,
                   var_other_details,
                   additional_card_pricing_info,
                   sales_office_contact,
                   additional_auth_pricing_program_info,
                   applicant_email,
                   application_id)