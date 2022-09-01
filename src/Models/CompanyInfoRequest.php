<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class CompanyInfoRequest implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $companyId;

    /**
     * @var string|null
     */
    private $ownershipType;

    /**
     * Returns Company Id.
     */
    public function getCompanyId(): ?string
    {
        return $this->companyId;
    }

    /**
     * Sets Company Id.
     *
     * @maps companyId
     */
    public function setCompanyId(?string $companyId): void
    {
        $this->companyId = $companyId;
    }

    /**
     * Returns Ownership Type.
     */
    public function getOwnershipType(): ?string
    {
        return $this->ownershipType;
    }

    /**
     * Sets Ownership Type.
     *
     * @maps ownershipType
     */
    public function setOwnershipType(?string $ownershipType): void
    {
        $this->ownershipType = $ownershipType;
    }

    /**
     * Encode this object to JSON
     *
     * @param bool $asArrayWhenEmpty Whether to serialize this model as an array whenever no fields
     *        are set. (default: false)
     *
     * @return array|stdClass
     */
    #[\ReturnTypeWillChange] // @phan-suppress-current-line PhanUndeclaredClassAttribute for (php < 8.1)
    public function jsonSerialize(bool $asArrayWhenEmpty = false)
    {
        $json = [];
        if (isset($this->companyId)) {
            $json['companyId']     = $this->companyId;
        }
        if (isset($this->ownershipType)) {
            $json['ownershipType'] = $this->ownershipType;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
