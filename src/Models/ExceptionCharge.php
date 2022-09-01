<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class ExceptionCharge implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $type;

    /**
     * @var float|null
     */
    private $discountRate;

    /**
     * @var float|null
     */
    private $discountPerItem;

    /**
     * Returns Type.
     * Type of exception charge
     */
    public function getType(): ?string
    {
        return $this->type;
    }

    /**
     * Sets Type.
     * Type of exception charge
     *
     * @maps type
     * @factory \SwaggerScarecrowLib\Models\TypeEnum::checkValue
     */
    public function setType(?string $type): void
    {
        $this->type = $type;
    }

    /**
     * Returns Discount Rate.
     * Exception charge discount rate/percentage fee
     */
    public function getDiscountRate(): ?float
    {
        return $this->discountRate;
    }

    /**
     * Sets Discount Rate.
     * Exception charge discount rate/percentage fee
     *
     * @maps discountRate
     */
    public function setDiscountRate(?float $discountRate): void
    {
        $this->discountRate = $discountRate;
    }

    /**
     * Returns Discount Per Item.
     * Exception charge discount amount/per transaction fee
     */
    public function getDiscountPerItem(): ?float
    {
        return $this->discountPerItem;
    }

    /**
     * Sets Discount Per Item.
     * Exception charge discount amount/per transaction fee
     *
     * @maps discountPerItem
     */
    public function setDiscountPerItem(?float $discountPerItem): void
    {
        $this->discountPerItem = $discountPerItem;
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
        if (isset($this->type)) {
            $json['type']            = TypeEnum::checkValue($this->type);
        }
        if (isset($this->discountRate)) {
            $json['discountRate']    = $this->discountRate;
        }
        if (isset($this->discountPerItem)) {
            $json['discountPerItem'] = $this->discountPerItem;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
