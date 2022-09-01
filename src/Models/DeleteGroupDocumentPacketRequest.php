<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class DeleteGroupDocumentPacketRequest implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $groupDocumentPacketId;

    /**
     * Returns Group Document Packet Id.
     * The unique identifier for group document packet
     */
    public function getGroupDocumentPacketId(): ?string
    {
        return $this->groupDocumentPacketId;
    }

    /**
     * Sets Group Document Packet Id.
     * The unique identifier for group document packet
     *
     * @maps groupDocumentPacketId
     */
    public function setGroupDocumentPacketId(?string $groupDocumentPacketId): void
    {
        $this->groupDocumentPacketId = $groupDocumentPacketId;
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
        if (isset($this->groupDocumentPacketId)) {
            $json['groupDocumentPacketId'] = $this->groupDocumentPacketId;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}