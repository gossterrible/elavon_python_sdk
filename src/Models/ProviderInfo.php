<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class ProviderInfo implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $representativeName;

    /**
     * @var string|null
     */
    private $representativeEmail;

    /**
     * @var string|null
     */
    private $representativeSalesCode;

    /**
     * @var PhoneNumber|null
     */
    private $representativeContactNumber;

    /**
     * Returns Representative Name.
     */
    public function getRepresentativeName(): ?string
    {
        return $this->representativeName;
    }

    /**
     * Sets Representative Name.
     *
     * @maps representativeName
     */
    public function setRepresentativeName(?string $representativeName): void
    {
        $this->representativeName = $representativeName;
    }

    /**
     * Returns Representative Email.
     */
    public function getRepresentativeEmail(): ?string
    {
        return $this->representativeEmail;
    }

    /**
     * Sets Representative Email.
     *
     * @maps representativeEmail
     */
    public function setRepresentativeEmail(?string $representativeEmail): void
    {
        $this->representativeEmail = $representativeEmail;
    }

    /**
     * Returns Representative Sales Code.
     */
    public function getRepresentativeSalesCode(): ?string
    {
        return $this->representativeSalesCode;
    }

    /**
     * Sets Representative Sales Code.
     *
     * @maps representativeSalesCode
     */
    public function setRepresentativeSalesCode(?string $representativeSalesCode): void
    {
        $this->representativeSalesCode = $representativeSalesCode;
    }

    /**
     * Returns Representative Contact Number.
     */
    public function getRepresentativeContactNumber(): ?PhoneNumber
    {
        return $this->representativeContactNumber;
    }

    /**
     * Sets Representative Contact Number.
     *
     * @maps representativeContactNumber
     */
    public function setRepresentativeContactNumber(?PhoneNumber $representativeContactNumber): void
    {
        $this->representativeContactNumber = $representativeContactNumber;
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
        if (isset($this->representativeName)) {
            $json['representativeName']          = $this->representativeName;
        }
        if (isset($this->representativeEmail)) {
            $json['representativeEmail']         = $this->representativeEmail;
        }
        if (isset($this->representativeSalesCode)) {
            $json['representativeSalesCode']     = $this->representativeSalesCode;
        }
        if (isset($this->representativeContactNumber)) {
            $json['representativeContactNumber'] = $this->representativeContactNumber;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
