<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use Exception;
use stdClass;
use SwaggerScarecrowLib\ApiHelper;

/**
 * Type of documentation provided
 */
class DocumentTypeEnum
{
    public const CERTIFIED_INCORPORATION_ARTICLES = 'CERTIFIED_INCORPORATION_ARTICLES';

    public const DEED_OF_TRUST = 'DEED_OF_TRUST';

    public const GOVERNMENT_BUSINESS_LICENSE = 'GOVERNMENT_BUSINESS_LICENSE';

    public const SIGNED_OPERATING_AGREEMENT = 'SIGNED_OPERATING_AGREEMENT';

    public const SIGNED_TESTAMENTARY_LETTER = 'SIGNED_TESTAMENTARY_LETTER';

    public const SIGNED_EXECUTORSHIP_LETTER = 'SIGNED_EXECUTORSHIP_LETTER';

    public const SIGNED_ASSOCIATION_ARTICLES = 'SIGNED_ASSOCIATION_ARTICLES';

    public const SIGNED_PARTNERSHIP_AGREEMENT = 'SIGNED_PARTNERSHIP_AGREEMENT';

    public const SIGNED_LIMITED_PARTNERSHIP_AGREEMENT = 'SIGNED_LIMITED_PARTNERSHIP_AGREEMENT';

    public const SIGNED_LIMITED_LIABILITY_AGREEMENT = 'SIGNED_LIMITED_LIABILITY_AGREEMENT';

    public const FORM_990 = 'FORM_990';

    public const FOREIGN_GOV_CERT_GOOD_STANDING = 'FOREIGN_GOV_CERT_GOOD_STANDING';

    public const FOREIGN_ENTITY_ANNUAL_REPORT = 'FOREIGN_ENTITY_ANNUAL_REPORT';

    public const FOREIGN_ENTITY_CERT_ORG_DOCUMENT = 'FOREIGN_ENTITY_CERT_ORG_DOCUMENT';

    public const FOREIGN_GOV_BUSINESS_LICENSE = 'FOREIGN_GOV_BUSINESS_LICENSE';

    public const FEDERAL_CERTIFICATE_OF_AMALGAMATION = 'FEDERAL_CERTIFICATE_OF_AMALGAMATION';

    public const CERTIFICATE_OF_STATUS = 'CERTIFICATE_OF_STATUS';

    public const GOVERNMENT = 'GOVERNMENT';

    public const BUSINESS_NAME_REPORT = 'BUSINESS_NAME_REPORT';

    public const CORPORATE_PROFILE_REPORT_BY_GOVERNMENT_SITES = 'CORPORATE_PROFILE_REPORT_BY_GOVERNMENT_SITES';

    public const SIGNED_INDEPENDENT_CORPORATE_ANNUAL_AUDIT = 'SIGNED_INDEPENDENT_CORPORATE_ANNUAL_AUDIT';

    public const INCORPORATION_DOCUMENTS_FILED_WITH_GOVERNMENT = 'INCORPORATION_DOCUMENTS_FILED_WITH_GOVERNMENT';

    public const LETTER_OF_NOTICE_OF_ASSESSMENT_FROM_GOVERNMENT = 'LETTER_OF_NOTICE_OF_ASSESSMENT_FROM_GOVERNMENT';

    public const NAME_CHANGE_DOCUMENTS_FILED_WITH_GOVERNMENT = 'NAME_CHANGE_DOCUMENTS_FILED_WITH_GOVERNMENT';

    public const PARTNERSHIP_AGREEMENTS = 'PARTNERSHIP_AGREEMENTS';

    public const ANNUAL_SECURITIES_FILING = 'ANNUAL_SECURITIES_FILING';

    public const ARTICLES_OF_AMENDMENT = 'ARTICLES_OF_AMENDMENT';

    public const ARTICLES_OF_INCORPORATION = 'ARTICLES_OF_INCORPORATION';

    public const BUSINESS_REGISTRATION = 'BUSINESS_REGISTRATION';

    public const BYLAWS = 'BYLAWS';

    public const CERTIFICATE_OF_INCORPORATION = 'CERTIFICATE_OF_INCORPORATION';

    public const LETTERS_PATENT = 'LETTERS_PATENT';

    public const NOTICE_OF_CHANGE = 'NOTICE_OF_CHANGE';

    public const SECRETARY_OF_STATE_WEBSITE = 'SECRETARY_OF_STATE_WEBSITE';

    public const CRA_CORPORATION_REMITTANCE_VOUCHER = 'CRA_CORPORATION_REMITTANCE_VOUCHER';

    public const CRA_HST_REMITTANCE_STUB = 'CRA_HST_REMITTANCE_STUB';

    public const CRA_SUMMARY_OF_ACCOUNTS = 'CRA_SUMMARY_OF_ACCOUNTS';

    public const CRA_TAX_CREDIT_RECEIPT = 'CRA_TAX_CREDIT_RECEIPT';

    public const ARTICLES_OF_ORGANIZATION = 'ARTICLES_OF_ORGANIZATION';

    private const _ALL_VALUES = [
        self::CERTIFIED_INCORPORATION_ARTICLES,
        self::DEED_OF_TRUST,
        self::GOVERNMENT_BUSINESS_LICENSE,
        self::SIGNED_OPERATING_AGREEMENT,
        self::SIGNED_TESTAMENTARY_LETTER,
        self::SIGNED_EXECUTORSHIP_LETTER,
        self::SIGNED_ASSOCIATION_ARTICLES,
        self::SIGNED_PARTNERSHIP_AGREEMENT,
        self::SIGNED_LIMITED_PARTNERSHIP_AGREEMENT,
        self::SIGNED_LIMITED_LIABILITY_AGREEMENT,
        self::FORM_990,
        self::FOREIGN_GOV_CERT_GOOD_STANDING,
        self::FOREIGN_ENTITY_ANNUAL_REPORT,
        self::FOREIGN_ENTITY_CERT_ORG_DOCUMENT,
        self::FOREIGN_GOV_BUSINESS_LICENSE,
        self::FEDERAL_CERTIFICATE_OF_AMALGAMATION,
        self::CERTIFICATE_OF_STATUS,
        self::GOVERNMENT,
        self::BUSINESS_NAME_REPORT,
        self::CORPORATE_PROFILE_REPORT_BY_GOVERNMENT_SITES,
        self::SIGNED_INDEPENDENT_CORPORATE_ANNUAL_AUDIT,
        self::INCORPORATION_DOCUMENTS_FILED_WITH_GOVERNMENT,
        self::LETTER_OF_NOTICE_OF_ASSESSMENT_FROM_GOVERNMENT,
        self::NAME_CHANGE_DOCUMENTS_FILED_WITH_GOVERNMENT,
        self::PARTNERSHIP_AGREEMENTS,
        self::ANNUAL_SECURITIES_FILING,
        self::ARTICLES_OF_AMENDMENT,
        self::ARTICLES_OF_INCORPORATION,
        self::BUSINESS_REGISTRATION,
        self::BYLAWS,
        self::CERTIFICATE_OF_INCORPORATION,
        self::LETTERS_PATENT,
        self::NOTICE_OF_CHANGE,
        self::SECRETARY_OF_STATE_WEBSITE,
        self::CRA_CORPORATION_REMITTANCE_VOUCHER,
        self::CRA_HST_REMITTANCE_STUB,
        self::CRA_SUMMARY_OF_ACCOUNTS,
        self::CRA_TAX_CREDIT_RECEIPT,
        self::ARTICLES_OF_ORGANIZATION,
    ];

    /**
     * Ensures that all the given values are present in this Enum.
     *
     * @param array|stdClass|null|string $value Value or a list/map of values to be checked
     *
     * @return array|null|string Input value(s), if all are a part of this Enum
     *
     * @throws Exception Throws exception if any given value is not in this Enum
     */
    public static function checkValue($value)
    {
        $value = json_decode(json_encode($value), true); // converts stdClass into array
        ApiHelper::checkValueInEnum($value, self::class, self::_ALL_VALUES);
        return $value;
    }
}