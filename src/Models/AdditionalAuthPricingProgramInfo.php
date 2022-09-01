<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class AdditionalAuthPricingProgramInfo implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $description;

    /**
     * @var float|null
     */
    private $fee;

    /**
     * @var float|null
     */
    private $authAmount;

    /**
     * Returns Description.
     * Description of the pricing program
     */
    public function getDescription(): ?string
    {
        return $this->description;
    }

    /**
     * Sets Description.
     * Description of the pricing program
     *
     * @maps description
     */
    public function setDescription(?string $description): void
    {
        $this->description = $description;
    }

    /**
     * Returns Fee.
     * The program fee
     */
    public function getFee(): ?float
    {
        return $this->fee;
    }

    /**
     * Sets Fee.
     * The program fee
     *
     * @maps fee
     */
    public function setFee(?float $fee): void
    {
        $this->fee = $fee;
    }

    /**
     * Returns Auth Amount.
     * The program amount
     */
    public function getAuthAmount(): ?float
    {
        return $this->authAmount;
    }

    /**
     * Sets Auth Amount.
     * The program amount
     *
     * @maps authAmount
     */
    public function setAuthAmount(?float $authAmount): void
    {
        $this->authAmount = $authAmount;
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
        if (isset($this->description)) {
            $json['description'] = $this->description;
        }
        if (isset($this->fee)) {
            $json['fee']         = $this->fee;
        }
        if (isset($this->authAmount)) {
            $json['authAmount']  = $this->authAmount;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}