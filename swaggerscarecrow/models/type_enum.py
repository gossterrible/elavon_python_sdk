# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class TypeEnum(object):

    """Implementation of the 'Type' enum.

    Type of exception charge

    Attributes:
        BUSINESS_CARDS: TODO: type description here.
        PAPER_VOUCHERS: TODO: type description here.
        NON_EU: TODO: type description here.
        DEBIT_EXCEPTION_VI_MC: TODO: type description here.
        DEBIT_EXCEPTION_UKDM: TODO: type description here.
        CREDIT_EXCEPTION: TODO: type description here.
        CORPORATE: TODO: type description here.
        INT_NATIONAL_CREDIT_EU: TODO: type description here.
        INT_NATIONAL_DEBIT_EU: TODO: type description here.
        DOMESTIC_CREDIT: TODO: type description here.
        DOMESTIC_DEBIT: TODO: type description here.
        INT_NATIONAL_CREDIT: TODO: type description here.
        INT_NATIONAL_DEBIT: TODO: type description here.
        UNION_PAY_RATE: TODO: type description here.
        AMEX_RATE: TODO: type description here.
        JCB_RATE: TODO: type description here.
        DINERS_RATE: TODO: type description here.
        VISA_CREDIT_SECURE_RATE: TODO: type description here.
        VISA_CREDIT_NON_SECURE_RATE: TODO: type description here.
        ALL_NON_EEA_VISA_SECURE_RATE: TODO: type description here.
        ALL_NON_EEA_VISA_NON_SECURE_RATE: TODO: type description here.
        VISA_DEBIT_SECURE_RATE: TODO: type description here.
        VISA_DEBIT_NON_SECURE_RATE: TODO: type description here.
        VISA_BUSINESS_CREDIT_SECURE_RATE: TODO: type description here.
        VISA_BUSINESS_CREDIT_NON_SECURE_RATE: TODO: type description here.
        VISA_BUSINESS_DEBIT_SECURE_RATE: TODO: type description here.
        VISA_BUSINESS_DEBIT_NON_SECURE_RATE: TODO: type description here.
        MASTERCARD_DEBIT_SECURE_RATE: TODO: type description here.
        MASTERCARD_DEBIT_NON_SECURE_RATE: TODO: type description here.
        ALL_NON_EEA_MATERCARD_SECURE_RATE: TODO: type description here.
        ALL_NON_EEA_MATERCARD_NON_SECURE_RATE: TODO: type description here.
        MATERCARD_CREDIT_SECURE_RATE: TODO: type description here.
        MATERCARD_CREDIT_NON_SECURE_RATE: TODO: type description here.
        INTERNATIONAL_MAESTRO_SECURE_RATE: TODO: type description here.
        INTERNATIONAL_MAESTRO_NON_SECURE_RATE: TODO: type description here.
        UK_MAESTRO_SECURE_RATE: TODO: type description here.
        UK_MAESTRO_NON_SECURE_RATE: TODO: type description here.
        VISA_VPAY_SECURE_RATE: TODO: type description here.
        VISA_VPAY_NON_SECURE_RATE: TODO: type description here.
        VISA_PURCHASING_SECURE_RATE: TODO: type description here.
        VISA_CORPORATE_SECURE_RATE: TODO: type description here.
        MASTERCARD_BUSINESS_SECURE_RATE: TODO: type description here.
        MASTERCARD_PURCHASING_SECURE_RATE: TODO: type description here.
        MASTERCARD_FLEET_SECURE_RATE: TODO: type description here.
        MASTERCARD_CORPORATE_SECURE_RATE: TODO: type description here.
        MASTERCARD_PREPAID_COMMERCIAL_SECURE_RATE: TODO: type description
            here.
        VISA_PURCHASING_NON_SECURE_RATE: TODO: type description here.
        VISA_CORPORATE_NON_SECURE_RATE: TODO: type description here.
        MASTERCARD_BUSINESS_NON_SECURE_RATE: TODO: type description here.
        MASTERCARD_PURCHASING_NON_SECURE_RATE: TODO: type description here.
        MASTERCARD_FLEET_NON_SECURE_RATE: TODO: type description here.
        MASTERCARD_CORPORATE_NON_SECURE_RATE: TODO: type description here.
        MASTERCARD_PREPAID_COMMERCIAL_NON_SECURE_RATE: TODO: type description
            here.
        DOMESTIC_VISA_DEBIT_SECURE_RATE: TODO: type description here.
        DOMESTIC_VISA_DEBIT_NON_SECURE_RATE: TODO: type description here.
        DOMESTIC_MASTERCARD_DEBIT_SECURE_RATE: TODO: type description here.
        DOMESTIC_MASTERCARD_DEBIT_NON_SECURE_RATE: TODO: type description
            here.
        VISA_CONSUMER_CREDIT_DOMESTIC: TODO: type description here.
        VISA_CONSUMER_DEBIT_DOMESTIC: TODO: type description here.
        VISA_COMMERCIAL_CREDIT_DOMESTIC: TODO: type description here.
        VISA_COMMERCIAL_DEBIT_DOMESTIC: TODO: type description here.
        VISA_CONSUMER_CREDIT_EU: TODO: type description here.
        VISA_CONSUMER_DEBIT_EU: TODO: type description here.
        VISA_COMMERCIAL_CREDIT_EU: TODO: type description here.
        VISA_COMMERCIAL_DEBIT_EU: TODO: type description here.
        VISA_CONSUMER_CREDIT_INTL: TODO: type description here.
        VISA_CONSUMER_DEBIT_INTL: TODO: type description here.
        VISA_COMMERCIAL_CREDIT_INTL: TODO: type description here.
        VISA_COMMERCIAL_DEBIT_INTL: TODO: type description here.
        MASTERCARD_CONSUMER_CREDIT_DOMESTIC: TODO: type description here.
        MASTERCARD_CONSUMER_DEBIT_DOMESTIC: TODO: type description here.
        MASTERCARD_COMMERCIAL_CREDIT_DOMESTIC: TODO: type description here.
        MASTERCARD_COMMERCIAL_DEBIT_DOMESTIC: TODO: type description here.
        MASTERCARD_CONSUMER_CREDIT_EU: TODO: type description here.
        MASTERCARD_CONSUMER_DEBIT_EU: TODO: type description here.
        MASTERCARD_COMMERCIAL_CREDIT_EU: TODO: type description here.
        MASTERCARD_COMMERCIAL_DEBIT_EU: TODO: type description here.
        MASTERCARD_CONSUMER_CREDIT_INTL: TODO: type description here.
        MASTERCARD_CONSUMER_DEBIT_INTL: TODO: type description here.
        MASTERCARD_COMMERCIAL_CREDIT_INTL: TODO: type description here.
        MASTERCARD_COMMERCIAL_DEBIT_INTL: TODO: type description here.
        ESPMC_B2B: TODO: type description here.
        ESPCOMM: TODO: type description here.
        ESPDOM: TODO: type description here.
        ESPINT: TODO: type description here.
        VISA_B2B_SECURE_RATE: TODO: type description here.
        VISA_B2B_NON_SECURE_RATE: TODO: type description here.
        MASTERCARD_B2B_SECURE_RATE: TODO: type description here.
        MASTERCARD_B2B_NON_SECURE_RATE: TODO: type description here.
        VISA_DEBIT_VPAY_CONSUMER: TODO: type description here.
        MASTERCARD_DEBIT_MAESTRO_CONSUMER: TODO: type description here.
        VISA_CREDIT_CONSUMER: TODO: type description here.
        MASTERCARD_CREDIT_CONSUMER: TODO: type description here.
        VISA_COMMERCIAL: TODO: type description here.
        MASTERCARD_MAESTRO_COMMERCIAL: TODO: type description here.
        NON_EEA_VISA: TODO: type description here.
        NON_EEA_MASTERCARD_MAESTRO: TODO: type description here.
        AMERICAN_EXPRESS: TODO: type description here.
        DCI_DISCOVER_UNION_PAY_JCB: TODO: type description here.
        MASTERCARD_DOMESTIC_DEBIT_CONSUMER: TODO: type description here.
        MASTERCARD_EEA_DEBIT_CONSUMER: TODO: type description here.
        MAESTRO_DOMESTIC_DEBIT_CONSUMER: TODO: type description here.
        MAESTRO_EEA_DEBIT_CONSUMER: TODO: type description here.
        MASTERCARD_MAESTRO_DOMESTIC_CREDIT_CONSUMER: TODO: type description
            here.
        MASTERCARD_MAESTRO_EEA_CREDIT_CONSUMER: TODO: type description here.
        MASTERCARD_MAESTRO_DOM_DEBIT_COMMERCIAL: TODO: type description here.
        MASTERCARD_MAESTRO_EEA_DEBIT_COMMERCIAL: TODO: type description here.
        MASTERCARD_MAESTRO_DOM_CREDIT_COMMERCIAL: TODO: type description
            here.
        MASTERCARD_MAESTRO_EEA_CREDIT_COMMERCIAL: TODO: type description
            here.
        MASTERCARD_DOMESTIC_B2B: TODO: type description here.
        MASTERCARD_EEA_B2B: TODO: type description here.
        MASTERCARD_NON_EEA_B2B: TODO: type description here.
        MASTERCARD_MAESTRO_NON_EEA_DEBIT_CONSUMER: TODO: type description
            here.
        MASTERCARD_MAESTRO_NON_EEA_CREDIT_CONSUMER: TODO: type description
            here.
        MASTERCARD_MAESTRO_NON_EEA_DEBIT_COMMERCIAL: TODO: type description
            here.
        MASTERCARD_MAESTRO_NON_EEA_CREDIT_COMMERCIAL: TODO: type description
            here.
        VISA_V_PAY_DOMESTIC_DEBIT_CONSUMER: TODO: type description here.
        VISA_V_PAY_EEA_DEBIT_CONSUMER: TODO: type description here.
        VISA_DOMESTIC_DEBIT_COMMERCIAL: TODO: type description here.
        VISA_EEA_DEBIT_COMMERCIAL: TODO: type description here.
        VISA_DOMESTIC_CREDIT_CONSUMER: TODO: type description here.
        VISA_EEA_CREDIT_CONSUMER: TODO: type description here.
        VISA_DOMESTIC_CREDIT_COMMERCIAL: TODO: type description here.
        VISA_EEA_CREDIT_COMMERCIAL: TODO: type description here.
        VISA_DOMESTIC_B2B: TODO: type description here.
        VISA_EEA_B2B: TODO: type description here.
        VISA_NON_EEA_B2B: TODO: type description here.
        VISA_NON_EEA_DEBIT_CONSUMER: TODO: type description here.
        VISA_NON_EEA_CREDIT_CONSUMER: TODO: type description here.
        VISA_NON_EEA_DEBIT_COMMERCIAL: TODO: type description here.
        VISA_NON_EEA_CREDIT_COMMERCIAL: TODO: type description here.
        DCI_DISCOVERY_DEBIT_CONSUMER: TODO: type description here.
        DCI_DISCOVERY_CREDIT_CONSUMER: TODO: type description here.
        DCI_DISCOVERY_DEBIT_COMMERCIAL: TODO: type description here.
        DCI_DISCOVERY_CREDIT_COMMERCIAL: TODO: type description here.
        JCB_CREDIT_CONSUMER: TODO: type description here.
        JCB_DEBIT_CONSUMER: TODO: type description here.
        JCB_CREDIT_DEBIT_COMMERCIAL: TODO: type description here.
        UNION_PAY_CREDIT_CONSUMER: TODO: type description here.
        UNION_PAY_DEBIT_CONSUMER: TODO: type description here.
        UNION_PAY_DEBIT_COMMERCIAL: TODO: type description here.
        UNION_PAY_CREDIT_COMMERCIAL: TODO: type description here.
        AMERICAN_EXPRESS_RATE: TODO: type description here.
        SMSC_VISA_CREDIT_SECURE_RATE: TODO: type description here.
        SMSC_MATERCARD_CREDIT_SECURE_RATE: TODO: type description here.
        SMSC_VISA_DEBIT_SECURE_RATE: TODO: type description here.
        SMSC_MASTERCARD_DEBIT_SECURE_RATE: TODO: type description here.
        SMSC_VISA_VPAY_SECURE_RATE: TODO: type description here.
        SMSC_UK_MAESTRO_SECURE_RATE: TODO: type description here.
        SMSC_INTERNATIONAL_MAESTRO_SECURE_RATE: TODO: type description here.
        SMSC_VISA_BUSINESS_CREDIT_SECURE_RATE: TODO: type description here.
        SMSC_VISA_BUSINESS_DEBIT_SECURE_RATE: TODO: type description here.
        SMSC_VISA_PURCHASING_SECURE_RATE: TODO: type description here.
        SMSC_VISA_CORPORATE_SECURE_RATE: TODO: type description here.
        SMSC_MASTERCARD_BUSINESS_SECURE_RATE: TODO: type description here.
        SMSC_MASTERCARD_PURCHASING_SECURE_RATE: TODO: type description here.
        SMSC_MASTERCARD_FLEET_SECURE_RATE: TODO: type description here.
        SMSC_MASTERCARD_CORPORATE_SECURE_RATE: TODO: type description here.
        SMSC_MASTERCARD_PREPAID_COMMERCIAL_SECURE_RATE: TODO: type description
            here.
        SMSC_ALL_NON_EEA_VISA_SECURE_RATE: TODO: type description here.
        SMSC_ALL_NON_EEA_MATERCARD_SECURE_RATE: TODO: type description here.
        SMSC_DCI_DISCOVERY_CREDIT_CONSUMER: TODO: type description here.
        SMSC_DCI_DISCOVERY_DEBIT_CONSUMER: TODO: type description here.
        SMSC_DCI_DISCOVERY_CREDIT_COMMERCIAL: TODO: type description here.
        SMSC_DCI_DISCOVERY_DEBIT_COMMERCIAL: TODO: type description here.
        SMSC_JCB_CREDIT_CONSUMER: TODO: type description here.
        SMSC_JCB_DEBIT_CONSUMER: TODO: type description here.
        SMSC_JCB_CREDIT_DEBIT_COMMERCIAL: TODO: type description here.
        SMSC_UNION_PAY_CREDIT_CONSUMER: TODO: type description here.
        SMSC_UNION_PAY_DEBIT_CONSUMER: TODO: type description here.
        SMSC_UNION_PAY_CREDIT_COMMERCIAL: TODO: type description here.
        SMSC_UNION_PAY_DEBIT_COMMERCIAL: TODO: type description here.
        SMSC_AMEX_RATE: TODO: type description here.
        SMSC_DINERS_RATE: TODO: type description here.
        SMSC_JCB_RATE: TODO: type description here.
        SMSC_UNION_PAY_RATE: TODO: type description here.

    """

    BUSINESS_CARDS = 'BUSINESS_CARDS'

    PAPER_VOUCHERS = 'PAPER_VOUCHERS'

    NON_EU = 'NON_EU'

    DEBIT_EXCEPTION_VI_MC = 'DEBIT_EXCEPTION_VI_MC'

    DEBIT_EXCEPTION_UKDM = 'DEBIT_EXCEPTION_UKDM'

    CREDIT_EXCEPTION = 'CREDIT_EXCEPTION'

    CORPORATE = 'CORPORATE'

    INT_NATIONAL_CREDIT_EU = 'INT_NATIONAL_CREDIT_EU'

    INT_NATIONAL_DEBIT_EU = 'INT_NATIONAL_DEBIT_EU'

    DOMESTIC_CREDIT = 'DOMESTIC_CREDIT'

    DOMESTIC_DEBIT = 'DOMESTIC_DEBIT'

    INT_NATIONAL_CREDIT = 'INT_NATIONAL_CREDIT'

    INT_NATIONAL_DEBIT = 'INT_NATIONAL_DEBIT'

    UNION_PAY_RATE = 'UNION_PAY_RATE'

    AMEX_RATE = 'AMEX_RATE'

    JCB_RATE = 'JCB_RATE'

    DINERS_RATE = 'DINERS_RATE'

    VISA_CREDIT_SECURE_RATE = 'VISA_CREDIT_SECURE_RATE'

    VISA_CREDIT_NON_SECURE_RATE = 'VISA_CREDIT_NON_SECURE_RATE'

    ALL_NON_EEA_VISA_SECURE_RATE = 'ALL_NON_EEA_VISA_SECURE_RATE'

    ALL_NON_EEA_VISA_NON_SECURE_RATE = 'ALL_NON_EEA_VISA_NON_SECURE_RATE'

    VISA_DEBIT_SECURE_RATE = 'VISA_DEBIT_SECURE_RATE'

    VISA_DEBIT_NON_SECURE_RATE = 'VISA_DEBIT_NON_SECURE_RATE'

    VISA_BUSINESS_CREDIT_SECURE_RATE = 'VISA_BUSINESS_CREDIT_SECURE_RATE'

    VISA_BUSINESS_CREDIT_NON_SECURE_RATE = 'VISA_BUSINESS_CREDIT_NON_SECURE_RATE'

    VISA_BUSINESS_DEBIT_SECURE_RATE = 'VISA_BUSINESS_DEBIT_SECURE_RATE'

    VISA_BUSINESS_DEBIT_NON_SECURE_RATE = 'VISA_BUSINESS_DEBIT_NON_SECURE_RATE'

    MASTERCARD_DEBIT_SECURE_RATE = 'MASTERCARD_DEBIT_SECURE_RATE'

    MASTERCARD_DEBIT_NON_SECURE_RATE = 'MASTERCARD_DEBIT_NON_SECURE_RATE'

    ALL_NON_EEA_MATERCARD_SECURE_RATE = 'ALL_NON_EEA_MATERCARD_SECURE_RATE'

    ALL_NON_EEA_MATERCARD_NON_SECURE_RATE = 'ALL_NON_EEA_MATERCARD_NON_SECURE_RATE'

    MATERCARD_CREDIT_SECURE_RATE = 'MATERCARD_CREDIT_SECURE_RATE'

    MATERCARD_CREDIT_NON_SECURE_RATE = 'MATERCARD_CREDIT_NON_SECURE_RATE'

    INTERNATIONAL_MAESTRO_SECURE_RATE = 'INTERNATIONAL_MAESTRO_SECURE_RATE'

    INTERNATIONAL_MAESTRO_NON_SECURE_RATE = 'INTERNATIONAL_MAESTRO_NON_SECURE_RATE'

    UK_MAESTRO_SECURE_RATE = 'UK_MAESTRO_SECURE_RATE'

    UK_MAESTRO_NON_SECURE_RATE = 'UK_MAESTRO_NON_SECURE_RATE'

    VISA_VPAY_SECURE_RATE = 'VISA_VPAY_SECURE_RATE'

    VISA_VPAY_NON_SECURE_RATE = 'VISA_VPAY_NON_SECURE_RATE'

    VISA_PURCHASING_SECURE_RATE = 'VISA_PURCHASING_SECURE_RATE'

    VISA_CORPORATE_SECURE_RATE = 'VISA_CORPORATE_SECURE_RATE'

    MASTERCARD_BUSINESS_SECURE_RATE = 'MASTERCARD_BUSINESS_SECURE_RATE'

    MASTERCARD_PURCHASING_SECURE_RATE = 'MASTERCARD_PURCHASING_SECURE_RATE'

    MASTERCARD_FLEET_SECURE_RATE = 'MASTERCARD_FLEET_SECURE_RATE'

    MASTERCARD_CORPORATE_SECURE_RATE = 'MASTERCARD_CORPORATE_SECURE_RATE'

    MASTERCARD_PREPAID_COMMERCIAL_SECURE_RATE = 'MASTERCARD_PREPAID_COMMERCIAL_SECURE_RATE'

    VISA_PURCHASING_NON_SECURE_RATE = 'VISA_PURCHASING_NON_SECURE_RATE'

    VISA_CORPORATE_NON_SECURE_RATE = 'VISA_CORPORATE_NON_SECURE_RATE'

    MASTERCARD_BUSINESS_NON_SECURE_RATE = 'MASTERCARD_BUSINESS_NON_SECURE_RATE'

    MASTERCARD_PURCHASING_NON_SECURE_RATE = 'MASTERCARD_PURCHASING_NON_SECURE_RATE'

    MASTERCARD_FLEET_NON_SECURE_RATE = 'MASTERCARD_FLEET_NON_SECURE_RATE'

    MASTERCARD_CORPORATE_NON_SECURE_RATE = 'MASTERCARD_CORPORATE_NON_SECURE_RATE'

    MASTERCARD_PREPAID_COMMERCIAL_NON_SECURE_RATE = 'MASTERCARD_PREPAID_COMMERCIAL_NON_SECURE_RATE'

    DOMESTIC_VISA_DEBIT_SECURE_RATE = 'DOMESTIC_VISA_DEBIT_SECURE_RATE'

    DOMESTIC_VISA_DEBIT_NON_SECURE_RATE = 'DOMESTIC_VISA_DEBIT_NON_SECURE_RATE'

    DOMESTIC_MASTERCARD_DEBIT_SECURE_RATE = 'DOMESTIC_MASTERCARD_DEBIT_SECURE_RATE'

    DOMESTIC_MASTERCARD_DEBIT_NON_SECURE_RATE = 'DOMESTIC_MASTERCARD_DEBIT_NON_SECURE_RATE'

    VISA_CONSUMER_CREDIT_DOMESTIC = 'VISA_CONSUMER_CREDIT_DOMESTIC'

    VISA_CONSUMER_DEBIT_DOMESTIC = 'VISA_CONSUMER_DEBIT_DOMESTIC'

    VISA_COMMERCIAL_CREDIT_DOMESTIC = 'VISA_COMMERCIAL_CREDIT_DOMESTIC'

    VISA_COMMERCIAL_DEBIT_DOMESTIC = 'VISA_COMMERCIAL_DEBIT_DOMESTIC'

    VISA_CONSUMER_CREDIT_EU = 'VISA_CONSUMER_CREDIT_EU'

    VISA_CONSUMER_DEBIT_EU = 'VISA_CONSUMER_DEBIT_EU'

    VISA_COMMERCIAL_CREDIT_EU = 'VISA_COMMERCIAL_CREDIT_EU'

    VISA_COMMERCIAL_DEBIT_EU = 'VISA_COMMERCIAL_DEBIT_EU'

    VISA_CONSUMER_CREDIT_INTL = 'VISA_CONSUMER_CREDIT_INTL'

    VISA_CONSUMER_DEBIT_INTL = 'VISA_CONSUMER_DEBIT_INTL'

    VISA_COMMERCIAL_CREDIT_INTL = 'VISA_COMMERCIAL_CREDIT_INTL'

    VISA_COMMERCIAL_DEBIT_INTL = 'VISA_COMMERCIAL_DEBIT_INTL'

    MASTERCARD_CONSUMER_CREDIT_DOMESTIC = 'MASTERCARD_CONSUMER_CREDIT_DOMESTIC'

    MASTERCARD_CONSUMER_DEBIT_DOMESTIC = 'MASTERCARD_CONSUMER_DEBIT_DOMESTIC'

    MASTERCARD_COMMERCIAL_CREDIT_DOMESTIC = 'MASTERCARD_COMMERCIAL_CREDIT_DOMESTIC'

    MASTERCARD_COMMERCIAL_DEBIT_DOMESTIC = 'MASTERCARD_COMMERCIAL_DEBIT_DOMESTIC'

    MASTERCARD_CONSUMER_CREDIT_EU = 'MASTERCARD_CONSUMER_CREDIT_EU'

    MASTERCARD_CONSUMER_DEBIT_EU = 'MASTERCARD_CONSUMER_DEBIT_EU'

    MASTERCARD_COMMERCIAL_CREDIT_EU = 'MASTERCARD_COMMERCIAL_CREDIT_EU'

    MASTERCARD_COMMERCIAL_DEBIT_EU = 'MASTERCARD_COMMERCIAL_DEBIT_EU'

    MASTERCARD_CONSUMER_CREDIT_INTL = 'MASTERCARD_CONSUMER_CREDIT_INTL'

    MASTERCARD_CONSUMER_DEBIT_INTL = 'MASTERCARD_CONSUMER_DEBIT_INTL'

    MASTERCARD_COMMERCIAL_CREDIT_INTL = 'MASTERCARD_COMMERCIAL_CREDIT_INTL'

    MASTERCARD_COMMERCIAL_DEBIT_INTL = 'MASTERCARD_COMMERCIAL_DEBIT_INTL'

    ESPMC_B2B = 'ESPMC_B2B'

    ESPCOMM = 'ESPCOMM'

    ESPDOM = 'ESPDOM'

    ESPINT = 'ESPINT'

    VISA_B2B_SECURE_RATE = 'VISA_B2B_SECURE_RATE'

    VISA_B2B_NON_SECURE_RATE = 'VISA_B2B_NON_SECURE_RATE'

    MASTERCARD_B2B_SECURE_RATE = 'MASTERCARD_B2B_SECURE_RATE'

    MASTERCARD_B2B_NON_SECURE_RATE = 'MASTERCARD_B2B_NON_SECURE_RATE'

    VISA_DEBIT_VPAY_CONSUMER = 'VISA_DEBIT_VPAY_CONSUMER'

    MASTERCARD_DEBIT_MAESTRO_CONSUMER = 'MASTERCARD_DEBIT_MAESTRO_CONSUMER'

    VISA_CREDIT_CONSUMER = 'VISA_CREDIT_CONSUMER'

    MASTERCARD_CREDIT_CONSUMER = 'MASTERCARD_CREDIT_CONSUMER'

    VISA_COMMERCIAL = 'VISA_COMMERCIAL'

    MASTERCARD_MAESTRO_COMMERCIAL = 'MASTERCARD_MAESTRO_COMMERCIAL'

    NON_EEA_VISA = 'NON_EEA_VISA'

    NON_EEA_MASTERCARD_MAESTRO = 'NON_EEA_MASTERCARD_MAESTRO'

    AMERICAN_EXPRESS = 'AMERICAN_EXPRESS'

    DCI_DISCOVER_UNION_PAY_JCB = 'DCI_DISCOVER_UNION_PAY_JCB'

    MASTERCARD_DOMESTIC_DEBIT_CONSUMER = 'MASTERCARD_DOMESTIC_DEBIT_CONSUMER'

    MASTERCARD_EEA_DEBIT_CONSUMER = 'MASTERCARD_EEA_DEBIT_CONSUMER'

    MAESTRO_DOMESTIC_DEBIT_CONSUMER = 'MAESTRO_DOMESTIC_DEBIT_CONSUMER'

    MAESTRO_EEA_DEBIT_CONSUMER = 'MAESTRO_EEA_DEBIT_CONSUMER'

    MASTERCARD_MAESTRO_DOMESTIC_CREDIT_CONSUMER = 'MASTERCARD_MAESTRO_DOMESTIC_CREDIT_CONSUMER'

    MASTERCARD_MAESTRO_EEA_CREDIT_CONSUMER = 'MASTERCARD_MAESTRO_EEA_CREDIT_CONSUMER'

    MASTERCARD_MAESTRO_DOM_DEBIT_COMMERCIAL = 'MASTERCARD_MAESTRO_DOM_DEBIT_COMMERCIAL'

    MASTERCARD_MAESTRO_EEA_DEBIT_COMMERCIAL = 'MASTERCARD_MAESTRO_EEA_DEBIT_COMMERCIAL'

    MASTERCARD_MAESTRO_DOM_CREDIT_COMMERCIAL = 'MASTERCARD_MAESTRO_DOM_CREDIT_COMMERCIAL'

    MASTERCARD_MAESTRO_EEA_CREDIT_COMMERCIAL = 'MASTERCARD_MAESTRO_EEA_CREDIT_COMMERCIAL'

    MASTERCARD_DOMESTIC_B2B = 'MASTERCARD_DOMESTIC_B2B'

    MASTERCARD_EEA_B2B = 'MASTERCARD_EEA_B2B'

    MASTERCARD_NON_EEA_B2B = 'MASTERCARD_NON_EEA_B2B'

    MASTERCARD_MAESTRO_NON_EEA_DEBIT_CONSUMER = 'MASTERCARD_MAESTRO_NON_EEA_DEBIT_CONSUMER'

    MASTERCARD_MAESTRO_NON_EEA_CREDIT_CONSUMER = 'MASTERCARD_MAESTRO_NON_EEA_CREDIT_CONSUMER'

    MASTERCARD_MAESTRO_NON_EEA_DEBIT_COMMERCIAL = 'MASTERCARD_MAESTRO_NON_EEA_DEBIT_COMMERCIAL'

    MASTERCARD_MAESTRO_NON_EEA_CREDIT_COMMERCIAL = 'MASTERCARD_MAESTRO_NON_EEA_CREDIT_COMMERCIAL'

    VISA_V_PAY_DOMESTIC_DEBIT_CONSUMER = 'VISA_V_PAY_DOMESTIC_DEBIT_CONSUMER'

    VISA_V_PAY_EEA_DEBIT_CONSUMER = 'VISA_V_PAY_EEA_DEBIT_CONSUMER'

    VISA_DOMESTIC_DEBIT_COMMERCIAL = 'VISA_DOMESTIC_DEBIT_COMMERCIAL'

    VISA_EEA_DEBIT_COMMERCIAL = 'VISA_EEA_DEBIT_COMMERCIAL'

    VISA_DOMESTIC_CREDIT_CONSUMER = 'VISA_DOMESTIC_CREDIT_CONSUMER'

    VISA_EEA_CREDIT_CONSUMER = 'VISA_EEA_CREDIT_CONSUMER'

    VISA_DOMESTIC_CREDIT_COMMERCIAL = 'VISA_DOMESTIC_CREDIT_COMMERCIAL'

    VISA_EEA_CREDIT_COMMERCIAL = 'VISA_EEA_CREDIT_COMMERCIAL'

    VISA_DOMESTIC_B2B = 'VISA_DOMESTIC_B2B'

    VISA_EEA_B2B = 'VISA_EEA_B2B'

    VISA_NON_EEA_B2B = 'VISA_NON_EEA_B2B'

    VISA_NON_EEA_DEBIT_CONSUMER = 'VISA_NON_EEA_DEBIT_CONSUMER'

    VISA_NON_EEA_CREDIT_CONSUMER = 'VISA_NON_EEA_CREDIT_CONSUMER'

    VISA_NON_EEA_DEBIT_COMMERCIAL = 'VISA_NON_EEA_DEBIT_COMMERCIAL'

    VISA_NON_EEA_CREDIT_COMMERCIAL = 'VISA_NON_EEA_CREDIT_COMMERCIAL'

    DCI_DISCOVERY_DEBIT_CONSUMER = 'DCI_DISCOVERY_DEBIT_CONSUMER'

    DCI_DISCOVERY_CREDIT_CONSUMER = 'DCI_DISCOVERY_CREDIT_CONSUMER'

    DCI_DISCOVERY_DEBIT_COMMERCIAL = 'DCI_DISCOVERY_DEBIT_COMMERCIAL'

    DCI_DISCOVERY_CREDIT_COMMERCIAL = 'DCI_DISCOVERY_CREDIT_COMMERCIAL'

    JCB_CREDIT_CONSUMER = 'JCB_CREDIT_CONSUMER'

    JCB_DEBIT_CONSUMER = 'JCB_DEBIT_CONSUMER'

    JCB_CREDIT_DEBIT_COMMERCIAL = 'JCB_CREDIT_DEBIT_COMMERCIAL'

    UNION_PAY_CREDIT_CONSUMER = 'UNION_PAY_CREDIT_CONSUMER'

    UNION_PAY_DEBIT_CONSUMER = 'UNION_PAY_DEBIT_CONSUMER'

    UNION_PAY_DEBIT_COMMERCIAL = 'UNION_PAY_DEBIT_COMMERCIAL'

    UNION_PAY_CREDIT_COMMERCIAL = 'UNION_PAY_CREDIT_COMMERCIAL'

    AMERICAN_EXPRESS_RATE = 'AMERICAN_EXPRESS_RATE'

    SMSC_VISA_CREDIT_SECURE_RATE = 'SMSC_VISA_CREDIT_SECURE_RATE'

    SMSC_MATERCARD_CREDIT_SECURE_RATE = 'SMSC_MATERCARD_CREDIT_SECURE_RATE'

    SMSC_VISA_DEBIT_SECURE_RATE = 'SMSC_VISA_DEBIT_SECURE_RATE'

    SMSC_MASTERCARD_DEBIT_SECURE_RATE = 'SMSC_MASTERCARD_DEBIT_SECURE_RATE'

    SMSC_VISA_VPAY_SECURE_RATE = 'SMSC_VISA_VPAY_SECURE_RATE'

    SMSC_UK_MAESTRO_SECURE_RATE = 'SMSC_UK_MAESTRO_SECURE_RATE'

    SMSC_INTERNATIONAL_MAESTRO_SECURE_RATE = 'SMSC_INTERNATIONAL_MAESTRO_SECURE_RATE'

    SMSC_VISA_BUSINESS_CREDIT_SECURE_RATE = 'SMSC_VISA_BUSINESS_CREDIT_SECURE_RATE'

    SMSC_VISA_BUSINESS_DEBIT_SECURE_RATE = 'SMSC_VISA_BUSINESS_DEBIT_SECURE_RATE'

    SMSC_VISA_PURCHASING_SECURE_RATE = 'SMSC_VISA_PURCHASING_SECURE_RATE'

    SMSC_VISA_CORPORATE_SECURE_RATE = 'SMSC_VISA_CORPORATE_SECURE_RATE'

    SMSC_MASTERCARD_BUSINESS_SECURE_RATE = 'SMSC_MASTERCARD_BUSINESS_SECURE_RATE'

    SMSC_MASTERCARD_PURCHASING_SECURE_RATE = 'SMSC_MASTERCARD_PURCHASING_SECURE_RATE'

    SMSC_MASTERCARD_FLEET_SECURE_RATE = 'SMSC_MASTERCARD_FLEET_SECURE_RATE'

    SMSC_MASTERCARD_CORPORATE_SECURE_RATE = 'SMSC_MASTERCARD_CORPORATE_SECURE_RATE'

    SMSC_MASTERCARD_PREPAID_COMMERCIAL_SECURE_RATE = 'SMSC_MASTERCARD_PREPAID_COMMERCIAL_SECURE_RATE'

    SMSC_ALL_NON_EEA_VISA_SECURE_RATE = 'SMSC_ALL_NON_EEA_VISA_SECURE_RATE'

    SMSC_ALL_NON_EEA_MATERCARD_SECURE_RATE = 'SMSC_ALL_NON_EEA_MATERCARD_SECURE_RATE'

    SMSC_DCI_DISCOVERY_CREDIT_CONSUMER = 'SMSC_DCI_DISCOVERY_CREDIT_CONSUMER'

    SMSC_DCI_DISCOVERY_DEBIT_CONSUMER = 'SMSC_DCI_DISCOVERY_DEBIT_CONSUMER'

    SMSC_DCI_DISCOVERY_CREDIT_COMMERCIAL = 'SMSC_DCI_DISCOVERY_CREDIT_COMMERCIAL'

    SMSC_DCI_DISCOVERY_DEBIT_COMMERCIAL = 'SMSC_DCI_DISCOVERY_DEBIT_COMMERCIAL'

    SMSC_JCB_CREDIT_CONSUMER = 'SMSC_JCB_CREDIT_CONSUMER'

    SMSC_JCB_DEBIT_CONSUMER = 'SMSC_JCB_DEBIT_CONSUMER'

    SMSC_JCB_CREDIT_DEBIT_COMMERCIAL = 'SMSC_JCB_CREDIT_DEBIT_COMMERCIAL'

    SMSC_UNION_PAY_CREDIT_CONSUMER = 'SMSC_UNION_PAY_CREDIT_CONSUMER'

    SMSC_UNION_PAY_DEBIT_CONSUMER = 'SMSC_UNION_PAY_DEBIT_CONSUMER'

    SMSC_UNION_PAY_CREDIT_COMMERCIAL = 'SMSC_UNION_PAY_CREDIT_COMMERCIAL'

    SMSC_UNION_PAY_DEBIT_COMMERCIAL = 'SMSC_UNION_PAY_DEBIT_COMMERCIAL'

    SMSC_AMEX_RATE = 'SMSC_AMEX_RATE'

    SMSC_DINERS_RATE = 'SMSC_DINERS_RATE'

    SMSC_JCB_RATE = 'SMSC_JCB_RATE'

    SMSC_UNION_PAY_RATE = 'SMSC_UNION_PAY_RATE'
