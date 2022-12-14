<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class Name implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $salutation;

    /**
     * @var string
     */
    private $firstName;

    /**
     * @var string|null
     */
    private $middleName;

    /**
     * @var string
     */
    private $lastName;

    /**
     * @param string $firstName
     * @param string $lastName
     */
    public function __construct(string $firstName, string $lastName)
    {
        $this->firstName = $firstName;
        $this->lastName = $lastName;
    }

    /**
     * Returns Salutation.
     */
    public function getSalutation(): ?string
    {
        return $this->salutation;
    }

    /**
     * Sets Salutation.
     *
     * @maps salutation
     * @factory \SwaggerScarecrowLib\Models\SalutationEnum::checkValue
     */
    public function setSalutation(?string $salutation): void
    {
        $this->salutation = $salutation;
    }

    /**
     * Returns First Name.
     */
    public function getFirstName(): string
    {
        return $this->firstName;
    }

    /**
     * Sets First Name.
     *
     * @required
     * @maps firstName
     */
    public function setFirstName(string $firstName): void
    {
        $this->firstName = $firstName;
    }

    /**
     * Returns Middle Name.
     */
    public function getMiddleName(): ?string
    {
        return $this->middleName;
    }

    /**
     * Sets Middle Name.
     *
     * @maps middleName
     */
    public function setMiddleName(?string $middleName): void
    {
        $this->middleName = $middleName;
    }

    /**
     * Returns Last Name.
     */
    public function getLastName(): string
    {
        return $this->lastName;
    }

    /**
     * Sets Last Name.
     *
     * @required
     * @maps lastName
     */
    public function setLastName(string $lastName): void
    {
        $this->lastName = $lastName;
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
        if (isset($this->salutation)) {
            $json['salutation'] = SalutationEnum::checkValue($this->salutation);
        }
        $json['firstName']      = $this->firstName;
        if (isset($this->middleName)) {
            $json['middleName'] = $this->middleName;
        }
        $json['lastName']       = $this->lastName;

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
