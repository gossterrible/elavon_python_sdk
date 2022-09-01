<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class RefreshSignerUsersSessionsRequest implements \JsonSerializable
{
    /**
     * @var string
     */
    private $documentPacketId;

    /**
     * @var string[]
     */
    private $signerIds;

    /**
     * @param string $documentPacketId
     * @param string[] $signerIds
     */
    public function __construct(string $documentPacketId, array $signerIds)
    {
        $this->documentPacketId = $documentPacketId;
        $this->signerIds = $signerIds;
    }

    /**
     * Returns Document Packet Id.
     * The unique identifier for a document packet
     */
    public function getDocumentPacketId(): string
    {
        return $this->documentPacketId;
    }

    /**
     * Sets Document Packet Id.
     * The unique identifier for a document packet
     *
     * @required
     * @maps documentPacketId
     */
    public function setDocumentPacketId(string $documentPacketId): void
    {
        $this->documentPacketId = $documentPacketId;
    }

    /**
     * Returns Signer Ids.
     * List of users ids whos session needs refreshing
     *
     * @return string[]
     */
    public function getSignerIds(): array
    {
        return $this->signerIds;
    }

    /**
     * Sets Signer Ids.
     * List of users ids whos session needs refreshing
     *
     * @required
     * @maps signerIds
     *
     * @param string[] $signerIds
     */
    public function setSignerIds(array $signerIds): void
    {
        $this->signerIds = $signerIds;
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
        $json['documentPacketId'] = $this->documentPacketId;
        $json['signerIds']        = $this->signerIds;

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
