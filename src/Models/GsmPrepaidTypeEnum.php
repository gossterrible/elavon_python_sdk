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
 * [EU] Additional GSM SIM prepaid information
 */
class GsmPrepaidTypeEnum
{
    public const EURONET_NO_PAYS = 'EURONET_NO_PAYS';

    public const BP_EURONET = 'BP_EURONET';

    public const EURONET = 'EURONET';

    public const LEW_LEASE = 'LEW_LEASE';

    public const LEW = 'LEW';

    private const _ALL_VALUES = [self::EURONET_NO_PAYS, self::BP_EURONET, self::EURONET, self::LEW_LEASE, self::LEW];

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
