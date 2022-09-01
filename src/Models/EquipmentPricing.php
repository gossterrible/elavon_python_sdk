<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class EquipmentPricing implements \JsonSerializable
{
    /**
     * @var float
     */
    private $amount;

    /**
     * @var string|null
     */
    private $purchaseType;

    /**
     * @var int|null
     */
    private $leaseTerm;

    /**
     * @var int|null
     */
    private $vendorCode;

    /**
     * @var string|null
     */
    private $vendorPlan;

    /**
     * @var string|null
     */
    private $startMonth;

    /**
     * @var string|null
     */
    private $startYear;

    /**
     * @param float $amount
     */
    public function __construct(float $amount)
    {
        $this->amount = $amount;
    }

    /**
     * Returns Amount.
     * The cost of the equipment
     */
    public function getAmount(): float
    {
        return $this->amount;
    }

    /**
     * Sets Amount.
     * The cost of the equipment
     *
     * @required
     * @maps amount
     */
    public function setAmount(float $amount): void
    {
        $this->amount = $amount;
    }

    /**
     * Returns Purchase Type.
     */
    public function getPurchaseType(): ?string
    {
        return $this->purchaseType;
    }

    /**
     * Sets Purchase Type.
     *
     * @maps purchaseType
     * @factory \SwaggerScarecrowLib\Models\PurchaseTypeEnum::checkValue
     */
    public function setPurchaseType(?string $purchaseType): void
    {
        $this->purchaseType = $purchaseType;
    }

    /**
     * Returns Lease Term.
     */
    public function getLeaseTerm(): ?int
    {
        return $this->leaseTerm;
    }

    /**
     * Sets Lease Term.
     *
     * @maps leaseTerm
     */
    public function setLeaseTerm(?int $leaseTerm): void
    {
        $this->leaseTerm = $leaseTerm;
    }

    /**
     * Returns Vendor Code.
     */
    public function getVendorCode(): ?int
    {
        return $this->vendorCode;
    }

    /**
     * Sets Vendor Code.
     *
     * @maps vendorCode
     */
    public function setVendorCode(?int $vendorCode): void
    {
        $this->vendorCode = $vendorCode;
    }

    /**
     * Returns Vendor Plan.
     */
    public function getVendorPlan(): ?string
    {
        return $this->vendorPlan;
    }

    /**
     * Sets Vendor Plan.
     *
     * @maps vendorPlan
     */
    public function setVendorPlan(?string $vendorPlan): void
    {
        $this->vendorPlan = $vendorPlan;
    }

    /**
     * Returns Start Month.
     */
    public function getStartMonth(): ?string
    {
        return $this->startMonth;
    }

    /**
     * Sets Start Month.
     *
     * @maps startMonth
     * @factory \SwaggerScarecrowLib\Models\StartMonth1Enum::checkValue
     */
    public function setStartMonth(?string $startMonth): void
    {
        $this->startMonth = $startMonth;
    }

    /**
     * Returns Start Year.
     */
    public function getStartYear(): ?string
    {
        return $this->startYear;
    }

    /**
     * Sets Start Year.
     *
     * @maps startYear
     */
    public function setStartYear(?string $startYear): void
    {
        $this->startYear = $startYear;
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
        $json['amount']           = $this->amount;
        if (isset($this->purchaseType)) {
            $json['purchaseType'] = PurchaseTypeEnum::checkValue($this->purchaseType);
        }
        if (isset($this->leaseTerm)) {
            $json['leaseTerm']    = $this->leaseTerm;
        }
        if (isset($this->vendorCode)) {
            $json['vendorCode']   = $this->vendorCode;
        }
        if (isset($this->vendorPlan)) {
            $json['vendorPlan']   = $this->vendorPlan;
        }
        if (isset($this->startMonth)) {
            $json['startMonth']   = StartMonth1Enum::checkValue($this->startMonth);
        }
        if (isset($this->startYear)) {
            $json['startYear']    = $this->startYear;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
