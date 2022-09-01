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
 * ECS service level
 */
class ServiceLevelTypeEnum
{
    public const GUARANTEE_WITH_VERIFY = 'GUARANTEE_WITH_VERIFY';

    public const CONVERSION_WITH_VERIFY = 'CONVERSION_WITH_VERIFY';

    public const CONVERSION_ONLY = 'CONVERSION_ONLY';

    private const _ALL_VALUES = [self::GUARANTEE_WITH_VERIFY, self::CONVERSION_WITH_VERIFY, self::CONVERSION_ONLY];

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
