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
 * Connection type of product
 */
class ConnectionTypeEnum
{
    public const STANDARD_IP = 'STANDARD_IP';

    public const STANDARD_DIAL = 'STANDARD_DIAL';

    public const WIRELESS = 'WIRELESS';

    public const GENERAL_RADIO = 'GENERAL_RADIO';

    public const PUBLIC_TELENET = 'PUBLIC_TELENET';

    public const PUBLIC_TELENET_IP = 'PUBLIC_TELENET_IP';

    public const BLUETOOTH_IP = 'BLUETOOTH_IP';

    public const BLUETOOTH = 'BLUETOOTH';

    public const WIFI = 'WIFI';

    public const UNKNOWN = 'UNKNOWN';

    public const BLUETOOTH_PUBLIC_TELENET = 'BLUETOOTH_PUBLIC_TELENET';

    public const PWPW = 'PWPW';

    private const _ALL_VALUES = [
        self::STANDARD_IP,
        self::STANDARD_DIAL,
        self::WIRELESS,
        self::GENERAL_RADIO,
        self::PUBLIC_TELENET,
        self::PUBLIC_TELENET_IP,
        self::BLUETOOTH_IP,
        self::BLUETOOTH,
        self::WIFI,
        self::UNKNOWN,
        self::BLUETOOTH_PUBLIC_TELENET,
        self::PWPW,
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
