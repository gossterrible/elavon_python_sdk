<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class InternalUseInfo implements \JsonSerializable
{
    /**
     * @var FieldAutoInfo|null
     */
    private $fieldAutoInfo;

    /**
     * @var SalesRepInfo|null
     */
    private $salesRepInfo;

    /**
     * @var bool|null
     */
    private $tinAppliedToAll;

    /**
     * @var string|null
     */
    private $ipAddress;

    /**
     * Returns Field Auto Info.
     */
    public function getFieldAutoInfo(): ?FieldAutoInfo
    {
        return $this->fieldAutoInfo;
    }

    /**
     * Sets Field Auto Info.
     *
     * @maps fieldAutoInfo
     */
    public function setFieldAutoInfo(?FieldAutoInfo $fieldAutoInfo): void
    {
        $this->fieldAutoInfo = $fieldAutoInfo;
    }

    /**
     * Returns Sales Rep Info.
     */
    public function getSalesRepInfo(): ?SalesRepInfo
    {
        return $this->salesRepInfo;
    }

    /**
     * Sets Sales Rep Info.
     *
     * @maps salesRepInfo
     */
    public function setSalesRepInfo(?SalesRepInfo $salesRepInfo): void
    {
        $this->salesRepInfo = $salesRepInfo;
    }

    /**
     * Returns Tin Applied to All.
     * Flag for GBAPI for if this app might have business level mappings.  If null assume business level
     * map mode is true
     */
    public function getTinAppliedToAll(): ?bool
    {
        return $this->tinAppliedToAll;
    }

    /**
     * Sets Tin Applied to All.
     * Flag for GBAPI for if this app might have business level mappings.  If null assume business level
     * map mode is true
     *
     * @maps tinAppliedToAll
     */
    public function setTinAppliedToAll(?bool $tinAppliedToAll): void
    {
        $this->tinAppliedToAll = $tinAppliedToAll;
    }

    /**
     * Returns Ip Address.
     * [NA] IP Address of the customer who signed the application
     */
    public function getIpAddress(): ?string
    {
        return $this->ipAddress;
    }

    /**
     * Sets Ip Address.
     * [NA] IP Address of the customer who signed the application
     *
     * @maps ipAddress
     */
    public function setIpAddress(?string $ipAddress): void
    {
        $this->ipAddress = $ipAddress;
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
        if (isset($this->fieldAutoInfo)) {
            $json['fieldAutoInfo']   = $this->fieldAutoInfo;
        }
        if (isset($this->salesRepInfo)) {
            $json['salesRepInfo']    = $this->salesRepInfo;
        }
        if (isset($this->tinAppliedToAll)) {
            $json['tinAppliedToAll'] = $this->tinAppliedToAll;
        }
        if (isset($this->ipAddress)) {
            $json['ipAddress']       = $this->ipAddress;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}