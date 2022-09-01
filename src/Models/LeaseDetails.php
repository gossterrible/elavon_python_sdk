<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class LeaseDetails implements \JsonSerializable
{
    /**
     * @var float|null
     */
    private $alternatePrice;

    /**
     * @var string|null
     */
    private $pricingPlan;

    /**
     * Returns Alternate Price.
     */
    public function getAlternatePrice(): ?float
    {
        return $this->alternatePrice;
    }

    /**
     * Sets Alternate Price.
     *
     * @maps alternatePrice
     */
    public function setAlternatePrice(?float $alternatePrice): void
    {
        $this->alternatePrice = $alternatePrice;
    }

    /**
     * Returns Pricing Plan.
     */
    public function getPricingPlan(): ?string
    {
        return $this->pricingPlan;
    }

    /**
     * Sets Pricing Plan.
     *
     * @maps pricingPlan
     */
    public function setPricingPlan(?string $pricingPlan): void
    {
        $this->pricingPlan = $pricingPlan;
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
        if (isset($this->alternatePrice)) {
            $json['alternatePrice'] = $this->alternatePrice;
        }
        if (isset($this->pricingPlan)) {
            $json['pricingPlan']    = $this->pricingPlan;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
