<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class GroupInfo implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $groupId;

    /**
     * @var int|null
     */
    private $sequenceNumber;

    /**
     * @var int|null
     */
    private $totalNumber;

    /**
     * Returns Group Id.
     */
    public function getGroupId(): ?string
    {
        return $this->groupId;
    }

    /**
     * Sets Group Id.
     *
     * @maps groupId
     */
    public function setGroupId(?string $groupId): void
    {
        $this->groupId = $groupId;
    }

    /**
     * Returns Sequence Number.
     */
    public function getSequenceNumber(): ?int
    {
        return $this->sequenceNumber;
    }

    /**
     * Sets Sequence Number.
     *
     * @maps sequenceNumber
     */
    public function setSequenceNumber(?int $sequenceNumber): void
    {
        $this->sequenceNumber = $sequenceNumber;
    }

    /**
     * Returns Total Number.
     */
    public function getTotalNumber(): ?int
    {
        return $this->totalNumber;
    }

    /**
     * Sets Total Number.
     *
     * @maps totalNumber
     */
    public function setTotalNumber(?int $totalNumber): void
    {
        $this->totalNumber = $totalNumber;
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
        if (isset($this->groupId)) {
            $json['groupId']        = $this->groupId;
        }
        if (isset($this->sequenceNumber)) {
            $json['sequenceNumber'] = $this->sequenceNumber;
        }
        if (isset($this->totalNumber)) {
            $json['totalNumber']    = $this->totalNumber;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
