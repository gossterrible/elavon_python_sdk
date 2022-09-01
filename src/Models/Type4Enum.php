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
 * Electronic statement format type
 */
class Type4Enum
{
    public const SURCHARGE_TIERED = 'SURCHARGE_TIERED';

    public const SANS_SUMMARY_NO_RECAP = 'SANS_SUMMARY_NO_RECAP';

    public const TIERED_SUMMARY_NO_RECAP = 'TIERED_SUMMARY_NO_RECAP';

    public const SUMMARY_ONLY = 'SUMMARY_ONLY';

    public const SUMMARY_ACCUMULATION_BASIC = 'SUMMARY_ACCUMULATION_BASIC';

    public const FIXED_BANK_COMPLEX_WITH_RECAP = 'FIXED_BANK_COMPLEX_WITH_RECAP';

    public const ASSOCIATION_INTERCHANGE_WITH_RECAP = 'ASSOCIATION_INTERCHANGE_WITH_RECAP';

    public const BATCH = 'BATCH';

    public const TRANSACTION_DETAIL = 'TRANSACTION_DETAIL';

    public const XML = 'XML';

    public const CSV = 'CSV';

    public const INVOICE = 'INVOICE';

    public const SUMMARY_BASIC_BASIC = 'SUMMARY_BASIC_BASIC';

    public const DETAIL_COMPLEX_COMPLEX = 'DETAIL_COMPLEX_COMPLEX';

    public const DETAIL_INTERCHANGE_PLUS_COMPLEX = 'DETAIL_INTERCHANGE_PLUS_COMPLEX';

    public const DETAIL_INTERCHANGE_PLUS_BASIC = 'DETAIL_INTERCHANGE_PLUS_BASIC';

    public const SUMMARY_QUALIFIED_BASIC = 'SUMMARY_QUALIFIED_BASIC';

    public const SUMMARY_INTERCHANGE_PLUS_BASIC = 'SUMMARY_INTERCHANGE_PLUS_BASIC';

    public const SUMMARY_ENHANCED_DEBIT_INT = 'SUMMARY_ENHANCED_DEBIT_INT';

    public const SUMMARY_ENHANCED_DEBIT_BASIC = 'SUMMARY_ENHANCED_DEBIT_BASIC';

    public const S2_SUMMARY_DETAIL = 'S2_SUMMARY_DETAIL';

    private const _ALL_VALUES = [
        self::SURCHARGE_TIERED,
        self::SANS_SUMMARY_NO_RECAP,
        self::TIERED_SUMMARY_NO_RECAP,
        self::SUMMARY_ONLY,
        self::SUMMARY_ACCUMULATION_BASIC,
        self::FIXED_BANK_COMPLEX_WITH_RECAP,
        self::ASSOCIATION_INTERCHANGE_WITH_RECAP,
        self::BATCH,
        self::TRANSACTION_DETAIL,
        self::XML,
        self::CSV,
        self::INVOICE,
        self::SUMMARY_BASIC_BASIC,
        self::DETAIL_COMPLEX_COMPLEX,
        self::DETAIL_INTERCHANGE_PLUS_COMPLEX,
        self::DETAIL_INTERCHANGE_PLUS_BASIC,
        self::SUMMARY_QUALIFIED_BASIC,
        self::SUMMARY_INTERCHANGE_PLUS_BASIC,
        self::SUMMARY_ENHANCED_DEBIT_INT,
        self::SUMMARY_ENHANCED_DEBIT_BASIC,
        self::S2_SUMMARY_DETAIL,
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