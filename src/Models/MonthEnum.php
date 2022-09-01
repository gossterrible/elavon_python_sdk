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

class MonthEnum
{
    public const JAN = 'JAN';

    public const FEB = 'FEB';

    public const MAR = 'MAR';

    public const APR = 'APR';

    public const MAY = 'MAY';

    public const JUN = 'JUN';

    public const JUL = 'JUL';

    public const AUG = 'AUG';

    public const SEP = 'SEP';

    public const OCT = 'OCT';

    public const NOV = 'NOV';

    public const DEC = 'DEC';

    private const _ALL_VALUES = [
        self::JAN,
        self::FEB,
        self::MAR,
        self::APR,
        self::MAY,
        self::JUN,
        self::JUL,
        self::AUG,
        self::SEP,
        self::OCT,
        self::NOV,
        self::DEC,
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
