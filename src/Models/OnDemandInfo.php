<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class OnDemandInfo implements \JsonSerializable
{
    /**
     * @var float|null
     */
    private $perTransactionFee;

    /**
     * @var float|null
     */
    private $percentFee;

    /**
     * Returns Per Transaction Fee.
     * Per transaction fee applied to service
     */
    public function getPerTransactionFee(): ?float
    {
        return $this->perTransactionFee;
    }

    /**
     * Sets Per Transaction Fee.
     * Per transaction fee applied to service
     *
     * @maps perTransactionFee
     */
    public function setPerTransactionFee(?float $perTransactionFee): void
    {
        $this->perTransactionFee = $perTransactionFee;
    }

    /**
     * Returns Percent Fee.
     * Fee percentage to be applied to service
     */
    public function getPercentFee(): ?float
    {
        return $this->percentFee;
    }

    /**
     * Sets Percent Fee.
     * Fee percentage to be applied to service
     *
     * @maps percentFee
     */
    public function setPercentFee(?float $percentFee): void
    {
        $this->percentFee = $percentFee;
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
        if (isset($this->perTransactionFee)) {
            $json['perTransactionFee'] = $this->perTransactionFee;
        }
        if (isset($this->percentFee)) {
            $json['percentFee']        = $this->percentFee;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
