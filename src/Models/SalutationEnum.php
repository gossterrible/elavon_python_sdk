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

class SalutationEnum
{
    public const MR = 'MR';

    public const MRS = 'MRS';

    public const MS = 'MS';

    public const MISS = 'MISS';

    public const JR = 'JR';

    public const SR = 'SR';

    public const DR = 'DR';

    public const MASTER = 'MASTER';

    public const PROF = 'PROF';

    private const _ALL_VALUES = [
        self::MR,
        self::MRS,
        self::MS,
        self::MISS,
        self::JR,
        self::SR,
        self::DR,
        self::MASTER,
        self::PROF,
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