<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class LoyaltyInfo implements \JsonSerializable
{
    /**
     * @var int|null
     */
    private $visits;

    /**
     * @var float|null
     */
    private $amountSpent;

    /**
     * @var float|null
     */
    private $discountRate;

    /**
     * @var float|null
     */
    private $discountAmount;

    /**
     * Returns Visits.
     */
    public function getVisits(): ?int
    {
        return $this->visits;
    }

    /**
     * Sets Visits.
     *
     * @maps visits
     */
    public function setVisits(?int $visits): void
    {
        $this->visits = $visits;
    }

    /**
     * Returns Amount Spent.
     */
    public function getAmountSpent(): ?float
    {
        return $this->amountSpent;
    }

    /**
     * Sets Amount Spent.
     *
     * @maps amountSpent
     */
    public function setAmountSpent(?float $amountSpent): void
    {
        $this->amountSpent = $amountSpent;
    }

    /**
     * Returns Discount Rate.
     */
    public function getDiscountRate(): ?float
    {
        return $this->discountRate;
    }

    /**
     * Sets Discount Rate.
     *
     * @maps discountRate
     */
    public function setDiscountRate(?float $discountRate): void
    {
        $this->discountRate = $discountRate;
    }

    /**
     * Returns Discount Amount.
     */
    public function getDiscountAmount(): ?float
    {
        return $this->discountAmount;
    }

    /**
     * Sets Discount Amount.
     *
     * @maps discountAmount
     */
    public function setDiscountAmount(?float $discountAmount): void
    {
        $this->discountAmount = $discountAmount;
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
        if (isset($this->visits)) {
            $json['visits']         = $this->visits;
        }
        if (isset($this->amountSpent)) {
            $json['amountSpent']    = $this->amountSpent;
        }
        if (isset($this->discountRate)) {
            $json['discountRate']   = $this->discountRate;
        }
        if (isset($this->discountAmount)) {
            $json['discountAmount'] = $this->discountAmount;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}