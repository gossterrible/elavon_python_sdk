<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class CompanyShareHolder implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $name;

    /**
     * @var string|null
     */
    private $percentSharesHeld;

    /**
     * @var string|null
     */
    private $shareHolderType;

    /**
     * @var AddressFields|null
     */
    private $address;

    /**
     * @var PersonNameFields|null
     */
    private $personNameFields;

    /**
     * @var PhoneFields|null
     */
    private $phoneFields;

    /**
     * @var string|null
     */
    private $shareHolderIdentifier;

    /**
     * @var string|null
     */
    private $pesel;

    /**
     * @var PrincipalOwnerDetail|null
     */
    private $principalOwnerDetail;

    /**
     * Returns Name.
     */
    public function getName(): ?string
    {
        return $this->name;
    }

    /**
     * Sets Name.
     *
     * @maps name
     */
    public function setName(?string $name): void
    {
        $this->name = $name;
    }

    /**
     * Returns Percent Shares Held.
     */
    public function getPercentSharesHeld(): ?string
    {
        return $this->percentSharesHeld;
    }

    /**
     * Sets Percent Shares Held.
     *
     * @maps percentSharesHeld
     */
    public function setPercentSharesHeld(?string $percentSharesHeld): void
    {
        $this->percentSharesHeld = $percentSharesHeld;
    }

    /**
     * Returns Share Holder Type.
     */
    public function getShareHolderType(): ?string
    {
        return $this->shareHolderType;
    }

    /**
     * Sets Share Holder Type.
     *
     * @maps shareHolderType
     */
    public function setShareHolderType(?string $shareHolderType): void
    {
        $this->shareHolderType = $shareHolderType;
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
     * Returns Person Name Fields.
     */
    public function getPersonNameFields(): ?PersonNameFields
    {
        return $this->personNameFields;
    }

    /**
     * Sets Person Name Fields.
     *
     * @maps personNameFields
     */
    public function setPersonNameFields(?PersonNameFields $personNameFields): void
    {
        $this->personNameFields = $personNameFields;
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
     * Returns Share Holder Identifier.
     */
    public function getShareHolderIdentifier(): ?string
    {
        return $this->shareHolderIdentifier;
    }

    /**
     * Sets Share Holder Identifier.
     *
     * @maps shareHolderIdentifier
     */
    public function setShareHolderIdentifier(?string $shareHolderIdentifier): void
    {
        $this->shareHolderIdentifier = $shareHolderIdentifier;
    }

    /**
     * Returns Pesel.
     */
    public function getPesel(): ?string
    {
        return $this->pesel;
    }

    /**
     * Sets Pesel.
     *
     * @maps pesel
     */
    public function setPesel(?string $pesel): void
    {
        $this->pesel = $pesel;
    }

    /**
     * Returns Principal Owner Detail.
     */
    public function getPrincipalOwnerDetail(): ?PrincipalOwnerDetail
    {
        return $this->principalOwnerDetail;
    }

    /**
     * Sets Principal Owner Detail.
     *
     * @maps principalOwnerDetail
     */
    public function setPrincipalOwnerDetail(?PrincipalOwnerDetail $principalOwnerDetail): void
    {
        $this->principalOwnerDetail = $principalOwnerDetail;
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
        if (isset($this->name)) {
            $json['name']                  = $this->name;
        }
        if (isset($this->percentSharesHeld)) {
            $json['percentSharesHeld']     = $this->percentSharesHeld;
        }
        if (isset($this->shareHolderType)) {
            $json['shareHolderType']       = $this->shareHolderType;
        }
        if (isset($this->address)) {
            $json['address']               = $this->address;
        }
        if (isset($this->personNameFields)) {
            $json['personNameFields']      = $this->personNameFields;
        }
        if (isset($this->phoneFields)) {
            $json['phoneFields']           = $this->phoneFields;
        }
        if (isset($this->shareHolderIdentifier)) {
            $json['shareHolderIdentifier'] = $this->shareHolderIdentifier;
        }
        if (isset($this->pesel)) {
            $json['pesel']                 = $this->pesel;
        }
        if (isset($this->principalOwnerDetail)) {
            $json['principalOwnerDetail']  = $this->principalOwnerDetail;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
