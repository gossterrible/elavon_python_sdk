<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class HealthCareEligibilityInfo implements \JsonSerializable
{
    /**
     * @var float|null
     */
    private $monthlyFee;

    /**
     * @var string[]|null
     */
    private $npiNumbers;

    /**
     * Returns Monthly Fee.
     */
    public function getMonthlyFee(): ?float
    {
        return $this->monthlyFee;
    }

    /**
     * Sets Monthly Fee.
     *
     * @maps monthlyFee
     */
    public function setMonthlyFee(?float $monthlyFee): void
    {
        $this->monthlyFee = $monthlyFee;
    }

    /**
     * Returns Npi Numbers.
     *
     * @return string[]|null
     */
    public function getNpiNumbers(): ?array
    {
        return $this->npiNumbers;
    }

    /**
     * Sets Npi Numbers.
     *
     * @maps npiNumbers
     *
     * @param string[]|null $npiNumbers
     */
    public function setNpiNumbers(?array $npiNumbers): void
    {
        $this->npiNumbers = $npiNumbers;
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
        if (isset($this->monthlyFee)) {
            $json['monthlyFee'] = $this->monthlyFee;
        }
        if (isset($this->npiNumbers)) {
            $json['npiNumbers'] = $this->npiNumbers;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
