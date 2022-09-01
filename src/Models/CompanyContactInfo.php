<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class CompanyContactInfo implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $telephone;

    /**
     * @var string[]|null
     */
    private $emailAddresses;

    /**
     * @var string[]|null
     */
    private $webPages;

    /**
     * @var AddressFields|null
     */
    private $address;

    /**
     * @var PhoneFields|null
     */
    private $phoneFields;

    /**
     * Returns Telephone.
     */
    public function getTelephone(): ?string
    {
        return $this->telephone;
    }

    /**
     * Sets Telephone.
     *
     * @maps telephone
     */
    public function setTelephone(?string $telephone): void
    {
        $this->telephone = $telephone;
    }

    /**
     * Returns Email Addresses.
     *
     * @return string[]|null
     */
    public function getEmailAddresses(): ?array
    {
        return $this->emailAddresses;
    }

    /**
     * Sets Email Addresses.
     *
     * @maps emailAddresses
     *
     * @param string[]|null $emailAddresses
     */
    public function setEmailAddresses(?array $emailAddresses): void
    {
        $this->emailAddresses = $emailAddresses;
    }

    /**
     * Returns Web Pages.
     *
     * @return string[]|null
     */
    public function getWebPages(): ?array
    {
        return $this->webPages;
    }

    /**
     * Sets Web Pages.
     *
     * @maps webPages
     *
     * @param string[]|null $webPages
     */
    public function setWebPages(?array $webPages): void
    {
        $this->webPages = $webPages;
    }

    /**
     * Returns Address.
     */
    public function getAddress(): ?AddressFields
    {
        return $this->address;
    }

    /**
     * Sets Address.
     *
     * @maps address
     */
    public function setAddress(?AddressFields $address): void
    {
        $this->address = $address;
    }

    /**
     * Returns Phone Fields.
     */
    public function getPhoneFields(): ?PhoneFields
    {
        return $this->phoneFields;
    }

    /**
     * Sets Phone Fields.
     *
     * @maps phoneFields
     */
    public function setPhoneFields(?PhoneFields $phoneFields): void
    {
        $this->phoneFields = $phoneFields;
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
        if (isset($this->telephone)) {
            $json['telephone']      = $this->telephone;
        }
        if (isset($this->emailAddresses)) {
            $json['emailAddresses'] = $this->emailAddresses;
        }
        if (isset($this->webPages)) {
            $json['webPages']       = $this->webPages;
        }
        if (isset($this->address)) {
            $json['address']        = $this->address;
        }
        if (isset($this->phoneFields)) {
            $json['phoneFields']    = $this->phoneFields;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}