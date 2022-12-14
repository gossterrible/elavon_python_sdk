<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class CompanySummary implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $companyId;

    /**
     * @var string|null
     */
    private $businessName;

    /**
     * @var string|null
     */
    private $country;

    /**
     * @var string|null
     */
    private $countryCode;

    /**
     * @var string|null
     */
    private $companyRegistrationNumber;

    /**
     * @var string|null
     */
    private $status;

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
     * Returns Business Name.
     */
    public function getBusinessName(): ?string
    {
        return $this->businessName;
    }

    /**
     * Sets Business Name.
     *
     * @maps businessName
     */
    public function setBusinessName(?string $businessName): void
    {
        $this->businessName = $businessName;
    }

    /**
     * Returns Country.
     */
    public function getCountry(): ?string
    {
        return $this->country;
    }

    /**
     * Sets Country.
     *
     * @maps country
     */
    public function setCountry(?string $country): void
    {
        $this->country = $country;
    }

    /**
     * Returns Country Code.
     */
    public function getCountryCode(): ?string
    {
        return $this->countryCode;
    }

    /**
     * Sets Country Code.
     *
     * @maps countryCode
     */
    public function setCountryCode(?string $countryCode): void
    {
        $this->countryCode = $countryCode;
    }

    /**
     * Returns Company Registration Number.
     */
    public function getCompanyRegistrationNumber(): ?string
    {
        return $this->companyRegistrationNumber;
    }

    /**
     * Sets Company Registration Number.
     *
     * @maps companyRegistrationNumber
     */
    public function setCompanyRegistrationNumber(?string $companyRegistrationNumber): void
    {
        $this->companyRegistrationNumber = $companyRegistrationNumber;
    }

    /**
     * Returns Status.
     */
    public function getStatus(): ?string
    {
        return $this->status;
    }

    /**
     * Sets Status.
     *
     * @maps status
     */
    public function setStatus(?string $status): void
    {
        $this->status = $status;
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
            $json['companyId']                 = $this->companyId;
        }
        if (isset($this->businessName)) {
            $json['businessName']              = $this->businessName;
        }
        if (isset($this->country)) {
            $json['country']                   = $this->country;
        }
        if (isset($this->countryCode)) {
            $json['countryCode']               = $this->countryCode;
        }
        if (isset($this->companyRegistrationNumber)) {
            $json['companyRegistrationNumber'] = $this->companyRegistrationNumber;
        }
        if (isset($this->status)) {
            $json['status']                    = $this->status;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
