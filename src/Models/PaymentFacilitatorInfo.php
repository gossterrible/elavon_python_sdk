<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class PaymentFacilitatorInfo implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $paymentFacilitatorType;

    /**
     * @var CardPrefix[]|null
     */
    private $cardPrefixes;

    /**
     * Returns Payment Facilitator Type.
     */
    public function getPaymentFacilitatorType(): ?string
    {
        return $this->paymentFacilitatorType;
    }

    /**
     * Sets Payment Facilitator Type.
     *
     * @maps paymentFacilitatorType
     * @factory \SwaggerScarecrowLib\Models\PaymentFacilitatorTypeEnum::checkValue
     */
    public function setPaymentFacilitatorType(?string $paymentFacilitatorType): void
    {
        $this->paymentFacilitatorType = $paymentFacilitatorType;
    }

    /**
     * Returns Card Prefixes.
     *
     * @return CardPrefix[]|null
     */
    public function getCardPrefixes(): ?array
    {
        return $this->cardPrefixes;
    }

    /**
     * Sets Card Prefixes.
     *
     * @maps cardPrefixes
     *
     * @param CardPrefix[]|null $cardPrefixes
     */
    public function setCardPrefixes(?array $cardPrefixes): void
    {
        $this->cardPrefixes = $cardPrefixes;
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
        if (isset($this->paymentFacilitatorType)) {
            $json['paymentFacilitatorType'] = PaymentFacilitatorTypeEnum::checkValue($this->paymentFacilitatorType);
        }
        if (isset($this->cardPrefixes)) {
            $json['cardPrefixes']           = $this->cardPrefixes;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
