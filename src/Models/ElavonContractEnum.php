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
 * [EU] Determine which Merchant Agreement customer will sign
 */
class ElavonContractEnum
{
    public const UK = 'UK';

    public const ROI = 'ROI';

    public const DINERS_UK = 'DINERS_UK';

    public const DINERS_ROI = 'DINERS_ROI';

    public const AMEX_ROI = 'AMEX_ROI';

    public const SAN_UK = 'SAN_UK';

    public const POLISH = 'POLISH';

    public const GERMAN = 'GERMAN';

    public const NORWEGIAN = 'NORWEGIAN';

    public const UK_EURO = 'UK_EURO';

    public const FRENCH = 'FRENCH';

    public const DUTCH = 'DUTCH';

    public const ITALIAN = 'ITALIAN';

    private const _ALL_VALUES = [
        self::UK,
        self::ROI,
        self::DINERS_UK,
        self::DINERS_ROI,
        self::AMEX_ROI,
        self::SAN_UK,
        self::POLISH,
        self::GERMAN,
        self::NORWEGIAN,
        self::UK_EURO,
        self::FRENCH,
        self::DUTCH,
        self::ITALIAN,
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
