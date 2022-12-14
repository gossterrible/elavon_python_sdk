<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class GetQuizRequest implements \JsonSerializable
{
    /**
     * @var Person
     */
    private $principal;

    /**
     * @var Address
     */
    private $businessAddress;

    /**
     * @var string
     */
    private $language;

    /**
     * @param Person $principal
     * @param Address $businessAddress
     * @param string $language
     */
    public function __construct(Person $principal, Address $businessAddress, string $language)
    {
        $this->principal = $principal;
        $this->businessAddress = $businessAddress;
        $this->language = $language;
    }

    /**
     * Returns Principal.
     */
    public function getPrincipal(): Person
    {
        return $this->principal;
    }

    /**
     * Sets Principal.
     *
     * @required
     * @maps principal
     */
    public function setPrincipal(Person $principal): void
    {
        $this->principal = $principal;
    }

    /**
     * Returns Business Address.
     */
    public function getBusinessAddress(): Address
    {
        return $this->businessAddress;
    }

    /**
     * Sets Business Address.
     *
     * @required
     * @maps businessAddress
     */
    public function setBusinessAddress(Address $businessAddress): void
    {
        $this->businessAddress = $businessAddress;
    }

    /**
     * Returns Language.
     * Language of E-KYC requested, ISO 639-2 standard applies, en and fr supported
     */
    public function getLanguage(): string
    {
        return $this->language;
    }

    /**
     * Sets Language.
     * Language of E-KYC requested, ISO 639-2 standard applies, en and fr supported
     *
     * @required
     * @maps language
     */
    public function setLanguage(string $language): void
    {
        $this->language = $language;
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
        $json['principal']       = $this->principal;
        $json['businessAddress'] = $this->businessAddress;
        $json['language']        = $this->language;

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
