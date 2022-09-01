<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class DebitPricing implements \JsonSerializable
{
    /**
     * @var string
     */
    private $pricingMethod;

    /**
     * @var string
     */
    private $authorizationMethod;

    /**
     * @var float|null
     */
    private $surchargeAmount;

    /**
     * @var string|null
     */
    private $surchargePercent;

    /**
     * @var DebitNetworkCharge[]
     */
    private $debitNetworkCharges;

    /**
     * @var bool|null
     */
    private $pinlessSetup;

    /**
     * @param string $pricingMethod
     * @param string $authorizationMethod
     * @param DebitNetworkCharge[] $debitNetworkCharges
     */
    public function __construct(string $pricingMethod, string $authorizationMethod, array $debitNetworkCharges)
    {
        $this->pricingMethod = $pricingMethod;
        $this->authorizationMethod = $authorizationMethod;
        $this->debitNetworkCharges = $debitNetworkCharges;
    }

    /**
     * Returns Pricing Method.
     * Debit network pricing method
     */
    public function getPricingMethod(): string
    {
        return $this->pricingMethod;
    }

    /**
     * Sets Pricing Method.
     * Debit network pricing method
     *
     * @required
     * @maps pricingMethod
     * @factory \SwaggerScarecrowLib\Models\PricingMethod1Enum::checkValue
     */
    public function setPricingMethod(string $pricingMethod): void
    {
        $this->pricingMethod = $pricingMethod;
    }

    /**
     * Returns Authorization Method.
     * Debit network authorization method
     */
    public function getAuthorizationMethod(): string
    {
        return $this->authorizationMethod;
    }

    /**
     * Sets Authorization Method.
     * Debit network authorization method
     *
     * @required
     * @maps authorizationMethod
     * @factory \SwaggerScarecrowLib\Models\AuthorizationMethodEnum::checkValue
     */
    public function setAuthorizationMethod(string $authorizationMethod): void
    {
        $this->authorizationMethod = $authorizationMethod;
    }

    /**
     * Returns Surcharge Amount.
     * Debit surcharge amount
     */
    public function getSurchargeAmount(): ?float
    {
        return $this->surchargeAmount;
    }

    /**
     * Sets Surcharge Amount.
     * Debit surcharge amount
     *
     * @maps surchargeAmount
     */
    public function setSurchargeAmount(?float $surchargeAmount): void
    {
        $this->surchargeAmount = $surchargeAmount;
    }

    /**
     * Returns Surcharge Percent.
     * Debit surcharge percentage
     */
    public function getSurchargePercent(): ?string
    {
        return $this->surchargePercent;
    }

    /**
     * Sets Surcharge Percent.
     * Debit surcharge percentage
     *
     * @maps surchargePercent
     */
    public function setSurchargePercent(?string $surchargePercent): void
    {
        $this->surchargePercent = $surchargePercent;
    }

    /**
     * Returns Debit Network Charges.
     * Debit network charges listing
     *
     * @return DebitNetworkCharge[]
     */
    public function getDebitNetworkCharges(): array
    {
        return $this->debitNetworkCharges;
    }

    /**
     * Sets Debit Network Charges.
     * Debit network charges listing
     *
     * @required
     * @maps debitNetworkCharges
     *
     * @param DebitNetworkCharge[] $debitNetworkCharges
     */
    public function setDebitNetworkCharges(array $debitNetworkCharges): void
    {
        $this->debitNetworkCharges = $debitNetworkCharges;
    }

    /**
     * Returns Pinless Setup.
     * Debit pinless setup
     */
    public function getPinlessSetup(): ?bool
    {
        return $this->pinlessSetup;
    }

    /**
     * Sets Pinless Setup.
     * Debit pinless setup
     *
     * @maps pinlessSetup
     */
    public function setPinlessSetup(?bool $pinlessSetup): void
    {
        $this->pinlessSetup = $pinlessSetup;
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
        $json['pricingMethod']        = PricingMethod1Enum::checkValue($this->pricingMethod);
        $json['authorizationMethod']  = AuthorizationMethodEnum::checkValue($this->authorizationMethod);
        if (isset($this->surchargeAmount)) {
            $json['surchargeAmount']  = $this->surchargeAmount;
        }
        if (isset($this->surchargePercent)) {
            $json['surchargePercent'] = $this->surchargePercent;
        }
        $json['debitNetworkCharges']  = $this->debitNetworkCharges;
        if (isset($this->pinlessSetup)) {
            $json['pinlessSetup']     = $this->pinlessSetup;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}