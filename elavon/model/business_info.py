"""
    Swagger Scarecrow

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from elavon.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from elavon.exceptions import ApiAttributeError


def lazy_import():
    from elavon.model.address import Address
    from elavon.model.credit_decision_info import CreditDecisionInfo
    from elavon.model.date_components import DateComponents
    from elavon.model.hemp_grower_info import HempGrowerInfo
    from elavon.model.pci_info import PCIInfo
    from elavon.model.vat_info import VatInfo
    from elavon.model.verification_info import VerificationInfo
    globals()['Address'] = Address
    globals()['CreditDecisionInfo'] = CreditDecisionInfo
    globals()['DateComponents'] = DateComponents
    globals()['HempGrowerInfo'] = HempGrowerInfo
    globals()['PCIInfo'] = PCIInfo
    globals()['VatInfo'] = VatInfo
    globals()['VerificationInfo'] = VerificationInfo


class BusinessInfo(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('ownership_type',): {
            'SOLE_TRADER': "SOLE_TRADER",
            'PARTNERSHIP': "PARTNERSHIP",
            'LIMITED_LIBABILITY_PARTNERSHIP': "LIMITED_LIBABILITY_PARTNERSHIP",
            'LIMITED_COMPANY': "LIMITED_COMPANY",
            'PUBLIC_LIMITED_COMPANY': "PUBLIC_LIMITED_COMPANY",
            'CHARITY': "CHARITY",
            'CLUB': "CLUB",
            'TRUST': "TRUST",
            'OTHER': "OTHER",
            'C_CORPORATION_PRIVATE_COMPANY': "C_CORPORATION_PRIVATE_COMPANY",
            'C_CORPORATION_PUBLIC_COMPANY': "C_CORPORATION_PUBLIC_COMPANY",
            'GOVERNMENT': "GOVERNMENT",
            'SUB_S_CORPORATION': "SUB_S_CORPORATION",
            'GENERAL_PARTNERSHIP': "GENERAL_PARTNERSHIP",
            'SP_AFFILIATES': "SP_AFFILIATES",
            'LIMITED_PARTNERSHIP': "LIMITED_PARTNERSHIP",
            'PARTNERSHIP_LIMITED_BY_SHARES': "PARTNERSHIP_LIMITED_BY_SHARES",
            'JOINT_STOCK_COMPANY': "JOINT_STOCK_COMPANY",
            'CO_OPERATIVES': "CO_OPERATIVES",
            'ESTATE': "ESTATE",
            'LISTED_COMPANY': "LISTED_COMPANY",
            'REGISTERED_FOREIGN_ENTERPRISE': "REGISTERED_FOREIGN_ENTERPRISE",
            'FOUNDATION': "FOUNDATION",
        },
        ('tax_id_type',): {
            'FEDERAL_TAX_ID': "FEDERAL_TAX_ID",
            'SOCIAL_INSURANCE_NUMBER': "SOCIAL_INSURANCE_NUMBER",
            'BUSINESS_REGISTRATION_NUMBER': "BUSINESS_REGISTRATION_NUMBER",
            'SOCIAL_SECURITY_NUMBER': "SOCIAL_SECURITY_NUMBER",
            'TAX_ID_NUMBER': "TAX_ID_NUMBER",
        },
        ('tax_form_type',): {
            'W9': "W9",
            'W8BEN': "W8BEN",
            'W8IMY': "W8IMY",
        },
        ('tax_class_type',): {
            'CORPORATION': "CORPORATION",
            'DISREGARDED_ENTITY': "DISREGARDED_ENTITY",
            'PARTNERSHIP': "PARTNERSHIP",
        },
        ('exemption_type',): {
            'ADDITIONAL_LOCATION': "ADDITIONAL_LOCATION",
            'CUSTOMER_REFUSAL': "CUSTOMER_REFUSAL",
            'FINANCIAL_INSTITUTION': "FINANCIAL_INSTITUTION",
            'US_LOCAL_GOVERNMENT': "US_LOCAL_GOVERNMENT",
            'NON_PROFIT': "NON_PROFIT",
            'PUBLICLY_TRADED': "PUBLICLY_TRADED",
            'STATE_REGULATED_BANK': "STATE_REGULATED_BANK",
            'US_STATE_DEPARTMENT': "US_STATE_DEPARTMENT",
            'US_FEDERAL_GOVERNMENT': "US_FEDERAL_GOVERNMENT",
            'SUBSIDIARY_OF_PUBLICLY_TRADED': "SUBSIDIARY_OF_PUBLICLY_TRADED",
            'CAN_PROVINCIAL_FEDERAL': "CAN_PROVINCIAL_FEDERAL",
            'INCORPORATED_MUNICIPAL_BODY': "INCORPORATED_MUNICIPAL_BODY",
            'INCORPORATED_REGIONAL_ENTITY': "INCORPORATED_REGIONAL_ENTITY",
            'PUBLIC_HOSPITAL_AUTHORITY': "PUBLIC_HOSPITAL_AUTHORITY",
            'SUBMERCHANT': "SUBMERCHANT",
            'CN_LEGAL_ENTITY': "CN_LEGAL_ENTITY",
            'AFFILIATE_FINANCIAL_ENTITY': "AFFILIATE_FINANCIAL_ENTITY",
            'HOSPITAL_AUTHORITY': "HOSPITAL_AUTHORITY",
        },
        ('owner_exemption_type',): {
            'BANK_ADVISED_POOLED': "BANK_ADVISED_POOLED",
            'BANK_HOLDING_COMPANY_ACT': "BANK_HOLDING_COMPANY_ACT",
            'BANK_ADVISED_POOLED_RP': "BANK_ADVISED_POOLED_RP",
            'CFR': "CFR",
            'COMMODITY_EXCHANGE_ACT': "COMMODITY_EXCHANGE_ACT",
            'SECURITIES_EXCHANGE_ACT_CLEARING': "SECURITIES_EXCHANGE_ACT_CLEARING",
            'SECURITIES_EXCHANGE_ACT_REGISTERED': "SECURITIES_EXCHANGE_ACT_REGISTERED",
            'FINANCIAL_MARKET_UTILITY': "FINANCIAL_MARKET_UTILITY",
            'FOREIGN_BANK': "FOREIGN_BANK",
            'FOREIGN_GOVERNMENT': "FOREIGN_GOVERNMENT",
            'INVESTMENT_COMPANY_ACT_ADVISOR': "INVESTMENT_COMPANY_ACT_ADVISOR",
            'INVESTMENT_COMPANY_ACT_COMPANY': "INVESTMENT_COMPANY_ACT_COMPANY",
            'SECURITIES_EXCHANGE_ACT_ISSUER': "SECURITIES_EXCHANGE_ACT_ISSUER",
            'NON_PROFIT': "NON_PROFIT",
            'NONE': "NONE",
            'PUBLIC_ACCOUNTING_FIRM': "PUBLIC_ACCOUNTING_FIRM",
            'SUBSIDIARY_OF_PUBLIC_TRADE': "SUBSIDIARY_OF_PUBLIC_TRADE",
            'STATE_REGULATED_INSURANCE': "STATE_REGULATED_INSURANCE",
        },
        ('number_of_partners',): {
            'ONE': "ONE",
            'TWO': "TWO",
            'THREE': "THREE",
            'FOUR': "FOUR",
            'FIVE': "FIVE",
            'SIX_TO_TEN': "SIX_TO_TEN",
            'ELEVEN_TO_TWENTY': "ELEVEN_TO_TWENTY",
            'TWENTY_ONE_TO_FIFTY': "TWENTY_ONE_TO_FIFTY",
            'MORE_THAN_FIFTY': "MORE_THAN_FIFTY",
        },
        ('legal_status',): {
            'CERTIFIED_INCORPORATION_ARTICLES': "CERTIFIED_INCORPORATION_ARTICLES",
            'DEED_OF_TRUST': "DEED_OF_TRUST",
            'GOVERNMENT_BUSINESS_LICENSE': "GOVERNMENT_BUSINESS_LICENSE",
            'SIGNED_OPERATING_AGREEMENT': "SIGNED_OPERATING_AGREEMENT",
            'SIGNED_TESTAMENTARY_LETTER': "SIGNED_TESTAMENTARY_LETTER",
            'SIGNED_EXECUTORSHIP_LETTER': "SIGNED_EXECUTORSHIP_LETTER",
            'SIGNED_ASSOCIATION_ARTICLES': "SIGNED_ASSOCIATION_ARTICLES",
            'SIGNED_PARTNERSHIP_AGREEMENT': "SIGNED_PARTNERSHIP_AGREEMENT",
            'SIGNED_LIMITED_PARTNERSHIP_AGREEMENT': "SIGNED_LIMITED_PARTNERSHIP_AGREEMENT",
            'SIGNED_LIMITED_LIABILITY_AGREEMENT': "SIGNED_LIMITED_LIABILITY_AGREEMENT",
            'FORM_990': "FORM_990",
            'FOREIGN_GOV_CERT_GOOD_STANDING': "FOREIGN_GOV_CERT_GOOD_STANDING",
            'FOREIGN_ENTITY_ANNUAL_REPORT': "FOREIGN_ENTITY_ANNUAL_REPORT",
            'FOREIGN_ENTITY_CERT_ORG_DOCUMENT': "FOREIGN_ENTITY_CERT_ORG_DOCUMENT",
            'FOREIGN_GOV_BUSINESS_LICENSE': "FOREIGN_GOV_BUSINESS_LICENSE",
            'FEDERAL_CERTIFICATE_OF_AMALGAMATION': "FEDERAL_CERTIFICATE_OF_AMALGAMATION",
            'CERTIFICATE_OF_STATUS': "CERTIFICATE_OF_STATUS",
            'GOVERNMENT': "GOVERNMENT",
            'BUSINESS_NAME_REPORT': "BUSINESS_NAME_REPORT",
            'CORPORATE_PROFILE_REPORT_BY_GOVERNMENT_SITES': "CORPORATE_PROFILE_REPORT_BY_GOVERNMENT_SITES",
            'SIGNED_INDEPENDENT_CORPORATE_ANNUAL_AUDIT': "SIGNED_INDEPENDENT_CORPORATE_ANNUAL_AUDIT",
            'INCORPORATION_DOCUMENTS_FILED_WITH_GOVERNMENT': "INCORPORATION_DOCUMENTS_FILED_WITH_GOVERNMENT",
            'LETTER_OF_NOTICE_OF_ASSESSMENT_FROM_GOVERNMENT': "LETTER_OF_NOTICE_OF_ASSESSMENT_FROM_GOVERNMENT",
            'NAME_CHANGE_DOCUMENTS_FILED_WITH_GOVERNMENT': "NAME_CHANGE_DOCUMENTS_FILED_WITH_GOVERNMENT",
            'PARTNERSHIP_AGREEMENTS': "PARTNERSHIP_AGREEMENTS",
            'ANNUAL_SECURITIES_FILING': "ANNUAL_SECURITIES_FILING",
            'ARTICLES_OF_AMENDMENT': "ARTICLES_OF_AMENDMENT",
            'ARTICLES_OF_INCORPORATION': "ARTICLES_OF_INCORPORATION",
            'BUSINESS_REGISTRATION': "BUSINESS_REGISTRATION",
            'BYLAWS': "BYLAWS",
            'CERTIFICATE_OF_INCORPORATION': "CERTIFICATE_OF_INCORPORATION",
            'LETTERS_PATENT': "LETTERS_PATENT",
            'NOTICE_OF_CHANGE': "NOTICE_OF_CHANGE",
            'SECRETARY_OF_STATE_WEBSITE': "SECRETARY_OF_STATE_WEBSITE",
            'CRA_CORPORATION_REMITTANCE_VOUCHER': "CRA_CORPORATION_REMITTANCE_VOUCHER",
            'CRA_HST_REMITTANCE_STUB': "CRA_HST_REMITTANCE_STUB",
            'CRA_SUMMARY_OF_ACCOUNTS': "CRA_SUMMARY_OF_ACCOUNTS",
            'CRA_TAX_CREDIT_RECEIPT': "CRA_TAX_CREDIT_RECEIPT",
            'ARTICLES_OF_ORGANIZATION': "ARTICLES_OF_ORGANIZATION",
        },
        ('industry_class',): {
            'LODGING': "LODGING",
            'MOTO': "MOTO",
            'RESTAURANT': "RESTAURANT",
            'RETAIL': "RETAIL",
            'INTERNET': "INTERNET",
        },
        ('location_mid_range',): {
            'NORDIC': "NORDIC",
            'STANDARD': "STANDARD",
        },
    }

    validations = {
        ('dba_name',): {
            'max_length': 32,
            'min_length': 0,
        },
        ('dba_name_extended',): {
            'max_length': 255,
            'min_length': 0,
        },
        ('legal_name',): {
            'max_length': 50,
            'min_length': 0,
        },
        ('legal_name_extended',): {
            'max_length': 255,
            'min_length': 0,
        },
        ('product_description',): {
            'max_length': 255,
            'min_length': 0,
        },
        ('mcc_code',): {
            'max_length': 5,
            'min_length': 0,
        },
        ('registration_number',): {
            'max_length': 15,
            'min_length': 0,
        },
        ('tax_id',): {
            'max_length': 15,
            'min_length': 0,
        },
        ('customer_membership_number',): {
            'max_length': 12,
            'min_length': 0,
        },
        ('store_number',): {
            'max_length': 10,
            'min_length': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'dba_name': (str,),  # noqa: E501
            'dba_name_extended': (str,),  # noqa: E501
            'business_address': (Address,),  # noqa: E501
            'legal_name': (str,),  # noqa: E501
            'legal_name_extended': (str,),  # noqa: E501
            'additional_addresses': ({str: (Address,)},),  # noqa: E501
            'ownership_type': (str,),  # noqa: E501
            'product_description': (str,),  # noqa: E501
            'mcc_code': (str,),  # noqa: E501
            'establishment_year': (str,),  # noqa: E501
            'current_ownership_years': (str,),  # noqa: E501
            'current_ownership_months': (str,),  # noqa: E501
            'communication_language': (str,),  # noqa: E501
            'pos_language': (str,),  # noqa: E501
            'legal_name_marked': ([str],),  # noqa: E501
            'registration_number': (str,),  # noqa: E501
            'tax_id': (str,),  # noqa: E501
            'tax_id_type': (str,),  # noqa: E501
            'vat_info': (VatInfo,),  # noqa: E501
            'tax_form_type': (str,),  # noqa: E501
            'tax_class_type': (str,),  # noqa: E501
            'customer_membership_number': (str,),  # noqa: E501
            'government_owned_entity': (bool,),  # noqa: E501
            'store_number': (str,),  # noqa: E501
            'association_codes': ([str],),  # noqa: E501
            'opt_out': (bool,),  # noqa: E501
            'sign_date': (DateComponents,),  # noqa: E501
            'pci_info': (PCIInfo,),  # noqa: E501
            'employer_id': (str,),  # noqa: E501
            'country_of_origin': (str,),  # noqa: E501
            'exemption_type': (str,),  # noqa: E501
            'owner_exemption_type': (str,),  # noqa: E501
            'number_of_partners': (str,),  # noqa: E501
            'relationship_mgr_code': (str,),  # noqa: E501
            'country_of_primary_operation': (str,),  # noqa: E501
            'bearer_shares': (bool,),  # noqa: E501
            'legal_status': (str,),  # noqa: E501
            'verifications': ({str: (VerificationInfo,)},),  # noqa: E501
            'industry_class': (str,),  # noqa: E501
            'no_plates': (bool,),  # noqa: E501
            'agent_number': (str,),  # noqa: E501
            'location_mid_range': (str,),  # noqa: E501
            'hemp_grower_info': (HempGrowerInfo,),  # noqa: E501
            'credit_decision_info': (CreditDecisionInfo,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'dba_name': 'dbaName',  # noqa: E501
        'dba_name_extended': 'dbaNameExtended',  # noqa: E501
        'business_address': 'businessAddress',  # noqa: E501
        'legal_name': 'legalName',  # noqa: E501
        'legal_name_extended': 'legalNameExtended',  # noqa: E501
        'additional_addresses': 'additionalAddresses',  # noqa: E501
        'ownership_type': 'ownershipType',  # noqa: E501
        'product_description': 'productDescription',  # noqa: E501
        'mcc_code': 'mccCode',  # noqa: E501
        'establishment_year': 'establishmentYear',  # noqa: E501
        'current_ownership_years': 'currentOwnershipYears',  # noqa: E501
        'current_ownership_months': 'currentOwnershipMonths',  # noqa: E501
        'communication_language': 'communicationLanguage',  # noqa: E501
        'pos_language': 'posLanguage',  # noqa: E501
        'legal_name_marked': 'legalNameMarked',  # noqa: E501
        'registration_number': 'registrationNumber',  # noqa: E501
        'tax_id': 'taxID',  # noqa: E501
        'tax_id_type': 'taxIDType',  # noqa: E501
        'vat_info': 'vatInfo',  # noqa: E501
        'tax_form_type': 'taxFormType',  # noqa: E501
        'tax_class_type': 'taxClassType',  # noqa: E501
        'customer_membership_number': 'customerMembershipNumber',  # noqa: E501
        'government_owned_entity': 'governmentOwnedEntity',  # noqa: E501
        'store_number': 'storeNumber',  # noqa: E501
        'association_codes': 'associationCodes',  # noqa: E501
        'opt_out': 'optOut',  # noqa: E501
        'sign_date': 'signDate',  # noqa: E501
        'pci_info': 'pciInfo',  # noqa: E501
        'employer_id': 'employerId',  # noqa: E501
        'country_of_origin': 'countryOfOrigin',  # noqa: E501
        'exemption_type': 'exemptionType',  # noqa: E501
        'owner_exemption_type': 'ownerExemptionType',  # noqa: E501
        'number_of_partners': 'numberOfPartners',  # noqa: E501
        'relationship_mgr_code': 'relationshipMgrCode',  # noqa: E501
        'country_of_primary_operation': 'countryOfPrimaryOperation',  # noqa: E501
        'bearer_shares': 'bearerShares',  # noqa: E501
        'legal_status': 'legalStatus',  # noqa: E501
        'verifications': 'verifications',  # noqa: E501
        'industry_class': 'industryClass',  # noqa: E501
        'no_plates': 'noPlates',  # noqa: E501
        'agent_number': 'agentNumber',  # noqa: E501
        'location_mid_range': 'locationMidRange',  # noqa: E501
        'hemp_grower_info': 'hempGrowerInfo',  # noqa: E501
        'credit_decision_info': 'creditDecisionInfo',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, dba_name, dba_name_extended, business_address, legal_name, legal_name_extended, additional_addresses, ownership_type, product_description, mcc_code, establishment_year, current_ownership_years, current_ownership_months, communication_language, pos_language, *args, **kwargs):  # noqa: E501
        """BusinessInfo - a model defined in OpenAPI

        Args:
            dba_name (str): Doing Business As name for business
            dba_name_extended (str): Doing Business As name for business, character limit extended
            business_address (Address):
            legal_name (str): Certified legal name of business
            legal_name_extended (str): Certified legal name of business, character limit extended
            additional_addresses ({str: (Address,)}): Container of other addresses, legal required.The valid keys are as follows: BUSINESS, LEGAL, SHIPPING, MAILING, PRINCIPAL, PREVIOUS, STATEMENT
            ownership_type (str): Type of business
            product_description (str): Description of product/service business provides
            mcc_code (str): Extended MCC code business qualifies as
            establishment_year (str): Year business was established
            current_ownership_years (str): Years business has been in control of current ownership
            current_ownership_months (str): Months business has been in control of current ownership
            communication_language (str): Language to be used for legal documents and communication between business and customer, ISO 639-1 standard applies
            pos_language (str): Language to be used for equipment displays, ISO 639-1 standard applies

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            legal_name_marked ([str]): Certified legal name of business, permits accented characters, required in POL. [optional]  # noqa: E501
            registration_number (str): [EU] Registration number of business, required for LIMITED_LIBABILITY_PARTNERSHIP, LIMITED_COMPANY, or PUBLIC_LIMITED_COMPANY. [optional]  # noqa: E501
            tax_id (str): Business tax ID. For testing a valid tax ID, use format 78742xxxx where 'xxxx' represents a series of four random, non-repeating, non-sequential numbers. [optional]  # noqa: E501
            tax_id_type (str): [NA] Type of tax id provieded. [optional]  # noqa: E501
            vat_info (VatInfo): [optional]  # noqa: E501
            tax_form_type (str): [NA] Type of tax form provided. [optional]  # noqa: E501
            tax_class_type (str): [NA] Type of business's tax classification. [optional]  # noqa: E501
            customer_membership_number (str): [NA] Business membership number (ex. COSTCO). [optional]  # noqa: E501
            government_owned_entity (bool): [EU] Indicate if more than 50% of the business is owned by the government. This field is mandatory for all ownership types.. [optional]  # noqa: E501
            store_number (str): [EU] Business store number. [optional]  # noqa: E501
            association_codes ([str]): [EU] Elavon promotion/assocation code listing. [optional]  # noqa: E501
            opt_out (bool): [EU] Elavon marketing opt out flag, true if opt out YES, false if opt out NO. [optional]  # noqa: E501
            sign_date (DateComponents): [optional]  # noqa: E501
            pci_info (PCIInfo): [optional]  # noqa: E501
            employer_id (str): [NA] Employer id. [optional]  # noqa: E501
            country_of_origin (str): Country of business origin, ISO 3166-1 alpha-3 standard applies. [optional]  # noqa: E501
            exemption_type (str): [NA] Exemption type of business (AML). [optional]  # noqa: E501
            owner_exemption_type (str): [NA] Exemption type of owner (AML). [optional]  # noqa: E501
            number_of_partners (str): [EU] Number of partners business has, applicable if business is any kind of PARTNERSHIP. [optional]  # noqa: E501
            relationship_mgr_code (str): [EU] Relationship manager code. [optional]  # noqa: E501
            country_of_primary_operation (str): Country of business primary operation, ISO 3166-1 alpha-3 standard applies. [optional]  # noqa: E501
            bearer_shares (bool): [NA] Flag indicating if business has bearer shares, true if YES, false if NO. [optional]  # noqa: E501
            legal_status (str): [NA] Business entity legal status. [optional]  # noqa: E501
            verifications ({str: (VerificationInfo,)}): [NA] Anti-Money Laundering (AML) oriented documentation info for the business. The valid keys are as follows: BUSINESS, LEGAL, SHIPPING, MAILING, PRINCIPAL, PREVIOUS, STATEMENT. [optional]  # noqa: E501
            industry_class (str): [NA] Business industry classification. [optional]  # noqa: E501
            no_plates (bool): [NA] Flag indicating if plates are to be delivered to business, true if no delivery, false if yes to delivery (NA). [optional]  # noqa: E501
            agent_number (str): [NA] Agent number. [optional]  # noqa: E501
            location_mid_range (str): [EU] 10 character MID range for Nordics.. [optional]  # noqa: E501
            hemp_grower_info (HempGrowerInfo): [optional]  # noqa: E501
            credit_decision_info (CreditDecisionInfo): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.dba_name = dba_name
        self.dba_name_extended = dba_name_extended
        self.business_address = business_address
        self.legal_name = legal_name
        self.legal_name_extended = legal_name_extended
        self.additional_addresses = additional_addresses
        self.ownership_type = ownership_type
        self.product_description = product_description
        self.mcc_code = mcc_code
        self.establishment_year = establishment_year
        self.current_ownership_years = current_ownership_years
        self.current_ownership_months = current_ownership_months
        self.communication_language = communication_language
        self.pos_language = pos_language
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, dba_name, dba_name_extended, business_address, legal_name, legal_name_extended, additional_addresses, ownership_type, product_description, mcc_code, establishment_year, current_ownership_years, current_ownership_months, communication_language, pos_language, *args, **kwargs):  # noqa: E501
        """BusinessInfo - a model defined in OpenAPI

        Args:
            dba_name (str): Doing Business As name for business
            dba_name_extended (str): Doing Business As name for business, character limit extended
            business_address (Address):
            legal_name (str): Certified legal name of business
            legal_name_extended (str): Certified legal name of business, character limit extended
            additional_addresses ({str: (Address,)}): Container of other addresses, legal required.The valid keys are as follows: BUSINESS, LEGAL, SHIPPING, MAILING, PRINCIPAL, PREVIOUS, STATEMENT
            ownership_type (str): Type of business
            product_description (str): Description of product/service business provides
            mcc_code (str): Extended MCC code business qualifies as
            establishment_year (str): Year business was established
            current_ownership_years (str): Years business has been in control of current ownership
            current_ownership_months (str): Months business has been in control of current ownership
            communication_language (str): Language to be used for legal documents and communication between business and customer, ISO 639-1 standard applies
            pos_language (str): Language to be used for equipment displays, ISO 639-1 standard applies

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            legal_name_marked ([str]): Certified legal name of business, permits accented characters, required in POL. [optional]  # noqa: E501
            registration_number (str): [EU] Registration number of business, required for LIMITED_LIBABILITY_PARTNERSHIP, LIMITED_COMPANY, or PUBLIC_LIMITED_COMPANY. [optional]  # noqa: E501
            tax_id (str): Business tax ID. For testing a valid tax ID, use format 78742xxxx where 'xxxx' represents a series of four random, non-repeating, non-sequential numbers. [optional]  # noqa: E501
            tax_id_type (str): [NA] Type of tax id provieded. [optional]  # noqa: E501
            vat_info (VatInfo): [optional]  # noqa: E501
            tax_form_type (str): [NA] Type of tax form provided. [optional]  # noqa: E501
            tax_class_type (str): [NA] Type of business's tax classification. [optional]  # noqa: E501
            customer_membership_number (str): [NA] Business membership number (ex. COSTCO). [optional]  # noqa: E501
            government_owned_entity (bool): [EU] Indicate if more than 50% of the business is owned by the government. This field is mandatory for all ownership types.. [optional]  # noqa: E501
            store_number (str): [EU] Business store number. [optional]  # noqa: E501
            association_codes ([str]): [EU] Elavon promotion/assocation code listing. [optional]  # noqa: E501
            opt_out (bool): [EU] Elavon marketing opt out flag, true if opt out YES, false if opt out NO. [optional]  # noqa: E501
            sign_date (DateComponents): [optional]  # noqa: E501
            pci_info (PCIInfo): [optional]  # noqa: E501
            employer_id (str): [NA] Employer id. [optional]  # noqa: E501
            country_of_origin (str): Country of business origin, ISO 3166-1 alpha-3 standard applies. [optional]  # noqa: E501
            exemption_type (str): [NA] Exemption type of business (AML). [optional]  # noqa: E501
            owner_exemption_type (str): [NA] Exemption type of owner (AML). [optional]  # noqa: E501
            number_of_partners (str): [EU] Number of partners business has, applicable if business is any kind of PARTNERSHIP. [optional]  # noqa: E501
            relationship_mgr_code (str): [EU] Relationship manager code. [optional]  # noqa: E501
            country_of_primary_operation (str): Country of business primary operation, ISO 3166-1 alpha-3 standard applies. [optional]  # noqa: E501
            bearer_shares (bool): [NA] Flag indicating if business has bearer shares, true if YES, false if NO. [optional]  # noqa: E501
            legal_status (str): [NA] Business entity legal status. [optional]  # noqa: E501
            verifications ({str: (VerificationInfo,)}): [NA] Anti-Money Laundering (AML) oriented documentation info for the business. The valid keys are as follows: BUSINESS, LEGAL, SHIPPING, MAILING, PRINCIPAL, PREVIOUS, STATEMENT. [optional]  # noqa: E501
            industry_class (str): [NA] Business industry classification. [optional]  # noqa: E501
            no_plates (bool): [NA] Flag indicating if plates are to be delivered to business, true if no delivery, false if yes to delivery (NA). [optional]  # noqa: E501
            agent_number (str): [NA] Agent number. [optional]  # noqa: E501
            location_mid_range (str): [EU] 10 character MID range for Nordics.. [optional]  # noqa: E501
            hemp_grower_info (HempGrowerInfo): [optional]  # noqa: E501
            credit_decision_info (CreditDecisionInfo): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.dba_name = dba_name
        self.dba_name_extended = dba_name_extended
        self.business_address = business_address
        self.legal_name = legal_name
        self.legal_name_extended = legal_name_extended
        self.additional_addresses = additional_addresses
        self.ownership_type = ownership_type
        self.product_description = product_description
        self.mcc_code = mcc_code
        self.establishment_year = establishment_year
        self.current_ownership_years = current_ownership_years
        self.current_ownership_months = current_ownership_months
        self.communication_language = communication_language
        self.pos_language = pos_language
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
