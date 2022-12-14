<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class Fee implements \JsonSerializable
{
    /**
     * @var string
     */
    private $type;

    /**
     * @var int
     */
    private $quantity;

    /**
     * @var float
     */
    private $amount;

    /**
     * @var string
     */
    private $frequency;

    /**
     * @var string|null
     */
    private $startMonth;

    /**
     * @param string $type
     * @param int $quantity
     * @param float $amount
     * @param string $frequency
     */
    public function __construct(string $type, int $quantity, float $amount, string $frequency)
    {
        $this->type = $type;
        $this->quantity = $quantity;
        $this->amount = $amount;
        $this->frequency = $frequency;
    }

    /**
     * Returns Type.
     * SKU of fee
     */
    public function getType(): string
    {
        return $this->type;
    }

    /**
     * Sets Type.
     * SKU of fee
     *
     * @required
     * @maps type
     */
    public function setType(string $type): void
    {
        $this->type = $type;
    }

    /**
     * Returns Quantity.
     * Quantity of fee
     */
    public function getQuantity(): int
    {
        return $this->quantity;
    }

    /**
     * Sets Quantity.
     * Quantity of fee
     *
     * @required
     * @maps quantity
     */
    public function setQuantity(int $quantity): void
    {
        $this->quantity = $quantity;
    }

    /**
     * Returns Amount.
     * Price of fee
     */
    public function getAmount(): float
    {
        return $this->amount;
    }

    /**
     * Sets Amount.
     * Price of fee
     *
     * @required
     * @maps amount
     */
    public function setAmount(float $amount): void
    {
        $this->amount = $amount;
    }

    /**
     * Returns Frequency.
     * Application of fee
     */
    public function getFrequency(): string
    {
        return $this->frequency;
    }

    /**
     * Sets Frequency.
     * Application of fee
     *
     * @required
     * @maps frequency
     * @factory \SwaggerScarecrowLib\Models\FrequencyEnum::checkValue
     */
    public function setFrequency(string $frequency): void
    {
        $this->frequency = $frequency;
    }

    /**
     * Returns Start Month.
     * [NA] start month
     */
    public function getStartMonth(): ?string
    {
        return $this->startMonth;
    }

    /**
     * Sets Start Month.
     * [NA] start month
     *
     * @maps startMonth
     * @factory \SwaggerScarecrowLib\Models\StartMonthEnum::checkValue
     */
    public function setStartMonth(?string $startMonth): void
    {
        $this->startMonth = $startMonth;
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
        $json['type']           = $this->type;
        $json['quantity']       = $this->quantity;
        $json['amount']         = $this->amount;
        $json['frequency']      = FrequencyEnum::checkValue($this->frequency);
        if (isset($this->startMonth)) {
            $json['startMonth'] = StartMonthEnum::checkValue($this->startMonth);
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
