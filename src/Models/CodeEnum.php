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
 * The code related to which unsigned document is desired
 */
class CodeEnum
{
    public const OPERATING_GUIDE = 'OPERATING_GUIDE';

    public const TERMS_OF_SERVICE = 'TERMS_OF_SERVICE';

    public const PAY_NAV_MEDICAL_AND_BUSINESS_AGREEMENT = 'PAY_NAV_MEDICAL_AND_BUSINESS_AGREEMENT';

    public const TALECH_ADDENDUM = 'TALECH_ADDENDUM';

    public const TALECH_ELAVON_TERMS_AND_CONDITION_ADDENDUM = 'TALECH_ELAVON_TERMS_AND_CONDITION_ADDENDUM';

    public const TALECH_TERMS_OF_SERVICE = 'TALECH_TERMS_OF_SERVICE';

    public const AMEX_AGREEMENT = 'AMEX_AGREEMENT';

    public const AMEX_TERMS_OF_SERVICE = 'AMEX_TERMS_OF_SERVICE';

    public const SAFE_T_ADDENDUM = 'SAFE_T_ADDENDUM';

    public const BLIK_ADDENDUM = 'BLIK_ADDENDUM';

    public const EPG_TOC = 'EPG_TOC';

    public const APPLICATION = 'APPLICATION';

    public const MERCHANT_AGREEMENT = 'MERCHANT_AGREEMENT';

    public const SIGNED_APPLICATION = 'SIGNED_APPLICATION';

    public const UNSIGNED_APPLICATION = 'UNSIGNED_APPLICATION';

    public const DEPOSIT_DIRECT_DEBIT = 'DEPOSIT_DIRECT_DEBIT';

    public const DEPOSIT_SIGNED_DIRECT_DEBIT = 'DEPOSIT_SIGNED_DIRECT_DEBIT';

    public const BILLING_DIRECT_DEBIT = 'BILLING_DIRECT_DEBIT';

    public const BILLING_SIGNED_DIRECT_DEBIT = 'BILLING_SIGNED_DIRECT_DEBIT';

    public const CHARGEBACK_DIRECT_DEBIT = 'CHARGEBACK_DIRECT_DEBIT';

    public const CHARGEBACK_SIGNED_DIRECT_DEBIT = 'CHARGEBACK_SIGNED_DIRECT_DEBIT';

    public const APPLICATION_ADDENDUM = 'APPLICATION_ADDENDUM';

    public const TERMINAL_HIRE_AGREEMENT = 'TERMINAL_HIRE_AGREEMENT';

    public const TERMINAL_HIRE_PRE_CONTRACT = 'TERMINAL_HIRE_PRE_CONTRACT';

    public const TERMINAL_HIRE_AGREEMENT_STATUTORY = 'TERMINAL_HIRE_AGREEMENT_STATUTORY';

    public const CUSTOM_NOTES = 'CUSTOM_NOTES';

    public const CALIFORNIA_LEASE = 'CALIFORNIA_LEASE';

    public const LEASE_AGREEMENT = 'LEASE_AGREEMENT';

    public const ELAVON_SECURED_PRO_TOC = 'ELAVON_SECURED_PRO_TOC';

    public const ELAVON_SECURED_ENCRYPT_TOC = 'ELAVON_SECURED_ENCRYPT_TOC';

    public const EPG_ADDENDUM = 'EPG_ADDENDUM';

    public const PROMOTION_ADDENDUM = 'PROMOTION_ADDENDUM';

    public const CANADIAN_CODE_OF_CONDUCT = 'CANADIAN_CODE_OF_CONDUCT';

    public const ELAVON_TOKENIZATION_TOC = 'ELAVON_TOKENIZATION_TOC';

    public const GOVERNMENT_INCENTIVE_ADDENDUM = 'GOVERNMENT_INCENTIVE_ADDENDUM';

    public const AMEX_SITE_LETTER = 'AMEX_SITE_LETTER';

    public const SELF_GUARANTEE = 'SELF_GUARANTEE';

    public const POYNT_ADDENDUM = 'POYNT_ADDENDUM';

    public const CONVERGE_ADDENDUM = 'CONVERGE_ADDENDUM';

    public const SANTANDER_POS_ADDENDUM = 'SANTANDER_POS_ADDENDUM';

    public const CONVERGE_ELAVON_TERMS_AND_CONDITION_ADDENDUM = 'CONVERGE_ELAVON_TERMS_AND_CONDITION_ADDENDUM';

    public const KKT_ADDENDUM = 'KKT_ADDENDUM';

    public const OPAYO_TOS = 'OPAYO_TOS';

    public const PARTNER_DOCUMENTS = 'PARTNER_DOCUMENTS';

    private const _ALL_VALUES = [
        self::OPERATING_GUIDE,
        self::TERMS_OF_SERVICE,
        self::PAY_NAV_MEDICAL_AND_BUSINESS_AGREEMENT,
        self::TALECH_ADDENDUM,
        self::TALECH_ELAVON_TERMS_AND_CONDITION_ADDENDUM,
        self::TALECH_TERMS_OF_SERVICE,
        self::AMEX_AGREEMENT,
        self::AMEX_TERMS_OF_SERVICE,
        self::SAFE_T_ADDENDUM,
        self::BLIK_ADDENDUM,
        self::EPG_TOC,
        self::APPLICATION,
        self::MERCHANT_AGREEMENT,
        self::SIGNED_APPLICATION,
        self::UNSIGNED_APPLICATION,
        self::DEPOSIT_DIRECT_DEBIT,
        self::DEPOSIT_SIGNED_DIRECT_DEBIT,
        self::BILLING_DIRECT_DEBIT,
        self::BILLING_SIGNED_DIRECT_DEBIT,
        self::CHARGEBACK_DIRECT_DEBIT,
        self::CHARGEBACK_SIGNED_DIRECT_DEBIT,
        self::APPLICATION_ADDENDUM,
        self::TERMINAL_HIRE_AGREEMENT,
        self::TERMINAL_HIRE_PRE_CONTRACT,
        self::TERMINAL_HIRE_AGREEMENT_STATUTORY,
        self::CUSTOM_NOTES,
        self::CALIFORNIA_LEASE,
        self::LEASE_AGREEMENT,
        self::ELAVON_SECURED_PRO_TOC,
        self::ELAVON_SECURED_ENCRYPT_TOC,
        self::EPG_ADDENDUM,
        self::PROMOTION_ADDENDUM,
        self::CANADIAN_CODE_OF_CONDUCT,
        self::ELAVON_TOKENIZATION_TOC,
        self::GOVERNMENT_INCENTIVE_ADDENDUM,
        self::AMEX_SITE_LETTER,
        self::SELF_GUARANTEE,
        self::POYNT_ADDENDUM,
        self::CONVERGE_ADDENDUM,
        self::SANTANDER_POS_ADDENDUM,
        self::CONVERGE_ELAVON_TERMS_AND_CONDITION_ADDENDUM,
        self::KKT_ADDENDUM,
        self::OPAYO_TOS,
        self::PARTNER_DOCUMENTS,
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
