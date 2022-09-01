<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class AdditionalDescriptionInfo implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $previousProcessorDescription;

    /**
     * @var string|null
     */
    private $monetaryPricingProgramDescription;

    /**
     * @var string|null
     */
    private $referrerReferenceDescription;

    /**
     * @var string|null
     */
    private $notes;

    /**
     * Returns Previous Processor Description.
     * Additional description of customer's previous payment processor
     */
    public function getPreviousProcessorDescription(): ?string
    {
        return $this->previousProcessorDescription;
    }

    /**
     * Sets Previous Processor Description.
     * Additional description of customer's previous payment processor
     *
     * @maps previousProcessorDescription
     */
    public function setPreviousProcessorDescription(?string $previousProcessorDescription): void
    {
        $this->previousProcessorDescription = $previousProcessorDescription;
    }

    /**
     * Returns Monetary Pricing Program Description.
     * Additional description of application's monetary pricing program (MPP)
     */
    public function getMonetaryPricingProgramDescription(): ?string
    {
        return $this->monetaryPricingProgramDescription;
    }

    /**
     * Sets Monetary Pricing Program Description.
     * Additional description of application's monetary pricing program (MPP)
     *
     * @maps monetaryPricingProgramDescription
     */
    public function setMonetaryPricingProgramDescription(?string $monetaryPricingProgramDescription): void
    {
        $this->monetaryPricingProgramDescription = $monetaryPricingProgramDescription;
    }

    /**
     * Returns Referrer Reference Description.
     * Additional description of referrer reference
     */
    public function getReferrerReferenceDescription(): ?string
    {
        return $this->referrerReferenceDescription;
    }

    /**
     * Sets Referrer Reference Description.
     * Additional description of referrer reference
     *
     * @maps referrerReferenceDescription
     */
    public function setReferrerReferenceDescription(?string $referrerReferenceDescription): void
    {
        $this->referrerReferenceDescription = $referrerReferenceDescription;
    }

    /**
     * Returns Notes.
     * Free text notes for additional information
     */
    public function getNotes(): ?string
    {
        return $this->notes;
    }

    /**
     * Sets Notes.
     * Free text notes for additional information
     *
     * @maps notes
     */
    public function setNotes(?string $notes): void
    {
        $this->notes = $notes;
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
        if (isset($this->previousProcessorDescription)) {
            $json['previousProcessorDescription']      = $this->previousProcessorDescription;
        }
        if (isset($this->monetaryPricingProgramDescription)) {
            $json['monetaryPricingProgramDescription'] = $this->monetaryPricingProgramDescription;
        }
        if (isset($this->referrerReferenceDescription)) {
            $json['referrerReferenceDescription']      = $this->referrerReferenceDescription;
        }
        if (isset($this->notes)) {
            $json['notes']                             = $this->notes;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}