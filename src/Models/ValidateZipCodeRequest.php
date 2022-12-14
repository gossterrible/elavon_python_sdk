<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class ValidateZipCodeRequest implements \JsonSerializable
{
    /**
     * @var string
     */
    private $zipCode;

    /**
     * @var string|null
     */
    private $city;

    /**
     * @var string
     */
    private $country;

    /**
     * @param string $zipCode
     * @param string $country
     */
    public function __construct(string $zipCode, string $country)
    {
        $this->zipCode = $zipCode;
        $this->country = $country;
    }

    /**
     * Returns Zip Code.
     * Postal code/Zip code to be validated
     */
    public function getZipCode(): string
    {
        return $this->zipCode;
    }

    /**
     * Sets Zip Code.
     * Postal code/Zip code to be validated
     *
     * @required
     * @maps zipCode
     */
    public function setZipCode(string $zipCode): void
    {
        $this->zipCode = $zipCode;
    }

    /**
     * Returns City.
     * Optional city value related to postal code/zip code
     */
    public function getCity(): ?string
    {
        return $this->city;
    }

    /**
     * Sets City.
     * Optional city value related to postal code/zip code
     *
     * @maps city
     */
    public function setCity(?string $city): void
    {
        $this->city = $city;
    }

    /**
     * Returns Country.
     * Country of postal code/zip code origin, ISO 3166-1 alpha-3 standard applies
     */
    public function getCountry(): string
    {
        return $this->country;
    }

    /**
     * Sets Country.
     * Country of postal code/zip code origin, ISO 3166-1 alpha-3 standard applies
     *
     * @required
     * @maps country
     */
    public function setCountry(string $country): void
    {
        $this->country = $country;
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
        $json['zipCode']  = $this->zipCode;
        if (isset($this->city)) {
            $json['city'] = $this->city;
        }
        $json['country']  = $this->country;

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
