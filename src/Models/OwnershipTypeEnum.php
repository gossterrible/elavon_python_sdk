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
 * Type of business
 */
class OwnershipTypeEnum
{
    public const SOLE_TRADER = 'SOLE_TRADER';

    public const PARTNERSHIP = 'PARTNERSHIP';

    public const LIMITED_LIBABILITY_PARTNERSHIP = 'LIMITED_LIBABILITY_PARTNERSHIP';

    public const LIMITED_COMPANY = 'LIMITED_COMPANY';

    public const PUBLIC_LIMITED_COMPANY = 'PUBLIC_LIMITED_COMPANY';

    public const CHARITY = 'CHARITY';

    public const CLUB = 'CLUB';

    public const TRUST = 'TRUST';

    public const OTHER = 'OTHER';

    public const C_CORPORATION_PRIVATE_COMPANY = 'C_CORPORATION_PRIVATE_COMPANY';

    public const C_CORPORATION_PUBLIC_COMPANY = 'C_CORPORATION_PUBLIC_COMPANY';

    public const GOVERNMENT = 'GOVERNMENT';

    public const SUB_S_CORPORATION = 'SUB_S_CORPORATION';

    public const GENERAL_PARTNERSHIP = 'GENERAL_PARTNERSHIP';

    public const SP_AFFILIATES = 'SP_AFFILIATES';

    public const LIMITED_PARTNERSHIP = 'LIMITED_PARTNERSHIP';

    public const PARTNERSHIP_LIMITED_BY_SHARES = 'PARTNERSHIP_LIMITED_BY_SHARES';

    public const JOINT_STOCK_COMPANY = 'JOINT_STOCK_COMPANY';

    public const CO_OPERATIVES = 'CO_OPERATIVES';

    public const ESTATE = 'ESTATE';

    public const LISTED_COMPANY = 'LISTED_COMPANY';

    public const REGISTERED_FOREIGN_ENTERPRISE = 'REGISTERED_FOREIGN_ENTERPRISE';

    public const FOUNDATION = 'FOUNDATION';

    private const _ALL_VALUES = [
        self::SOLE_TRADER,
        self::PARTNERSHIP,
        self::LIMITED_LIBABILITY_PARTNERSHIP,
        self::LIMITED_COMPANY,
        self::PUBLIC_LIMITED_COMPANY,
        self::CHARITY,
        self::CLUB,
        self::TRUST,
        self::OTHER,
        self::C_CORPORATION_PRIVATE_COMPANY,
        self::C_CORPORATION_PUBLIC_COMPANY,
        self::GOVERNMENT,
        self::SUB_S_CORPORATION,
        self::GENERAL_PARTNERSHIP,
        self::SP_AFFILIATES,
        self::LIMITED_PARTNERSHIP,
        self::PARTNERSHIP_LIMITED_BY_SHARES,
        self::JOINT_STOCK_COMPANY,
        self::CO_OPERATIVES,
        self::ESTATE,
        self::LISTED_COMPANY,
        self::REGISTERED_FOREIGN_ENTERPRISE,
        self::FOUNDATION,
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
