<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class Efs3dSecureInfo implements \JsonSerializable
{
    /**
     * @var float|null
     */
    private $billingPerItemFee;

    /**
     * Returns Billing Per Item Fee.
     * Per item fee applied to service
     */
    public function getBillingPerItemFee(): ?float
    {
        return $this->billingPerItemFee;
    }

    /**
     * Sets Billing Per Item Fee.
     * Per item fee applied to service
     *
     * @maps billingPerItemFee
     */
    public function setBillingPerItemFee(?float $billingPerItemFee): void
    {
        $this->billingPerItemFee = $billingPerItemFee;
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
        if (isset($this->billingPerItemFee)) {
            $json['billingPerItemFee'] = $this->billingPerItemFee;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
