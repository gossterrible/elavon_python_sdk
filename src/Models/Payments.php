<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class Payments implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $pmsVendorPas;

    /**
     * @var string|null
     */
    private $numberOfProviders;

    /**
     * @var string|null
     */
    private $salesRepPhoneNumber;

    /**
     * @var string|null
     */
    private $integratorNotes;

    /**
     * @var bool|null
     */
    private $hasPaymentPlans;

    /**
     * Returns Pms Vendor Pas.
     */
    public function getPmsVendorPas(): ?string
    {
        return $this->pmsVendorPas;
    }

    /**
     * Sets Pms Vendor Pas.
     *
     * @maps pmsVendorPas
     */
    public function setPmsVendorPas(?string $pmsVendorPas): void
    {
        $this->pmsVendorPas = $pmsVendorPas;
    }

    /**
     * Returns Number of Providers.
     */
    public function getNumberOfProviders(): ?string
    {
        return $this->numberOfProviders;
    }

    /**
     * Sets Number of Providers.
     *
     * @maps numberOfProviders
     */
    public function setNumberOfProviders(?string $numberOfProviders): void
    {
        $this->numberOfProviders = $numberOfProviders;
    }

    /**
     * Returns Sales Rep Phone Number.
     */
    public function getSalesRepPhoneNumber(): ?string
    {
        return $this->salesRepPhoneNumber;
    }

    /**
     * Sets Sales Rep Phone Number.
     *
     * @maps salesRepPhoneNumber
     */
    public function setSalesRepPhoneNumber(?string $salesRepPhoneNumber): void
    {
        $this->salesRepPhoneNumber = $salesRepPhoneNumber;
    }

    /**
     * Returns Integrator Notes.
     */
    public function getIntegratorNotes(): ?string
    {
        return $this->integratorNotes;
    }

    /**
     * Sets Integrator Notes.
     *
     * @maps integratorNotes
     */
    public function setIntegratorNotes(?string $integratorNotes): void
    {
        $this->integratorNotes = $integratorNotes;
    }

    /**
     * Returns Has Payment Plans.
     */
    public function getHasPaymentPlans(): ?bool
    {
        return $this->hasPaymentPlans;
    }

    /**
     * Sets Has Payment Plans.
     *
     * @maps hasPaymentPlans
     */
    public function setHasPaymentPlans(?bool $hasPaymentPlans): void
    {
        $this->hasPaymentPlans = $hasPaymentPlans;
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
        if (isset($this->pmsVendorPas)) {
            $json['pmsVendorPas']        = $this->pmsVendorPas;
        }
        if (isset($this->numberOfProviders)) {
            $json['numberOfProviders']   = $this->numberOfProviders;
        }
        if (isset($this->salesRepPhoneNumber)) {
            $json['salesRepPhoneNumber'] = $this->salesRepPhoneNumber;
        }
        if (isset($this->integratorNotes)) {
            $json['integratorNotes']     = $this->integratorNotes;
        }
        if (isset($this->hasPaymentPlans)) {
            $json['hasPaymentPlans']     = $this->hasPaymentPlans;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}