<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class AppendGroupDocumentPacketRequest implements \JsonSerializable
{
    /**
     * @var string
     */
    private $groupDocumentPacketId;

    /**
     * @var string
     */
    private $profileCode;

    /**
     * @var Signer[]
     */
    private $signers;

    /**
     * @var DocumentPacketData
     */
    private $documentPacketData;

    /**
     * @param string $groupDocumentPacketId
     * @param string $profileCode
     * @param Signer[] $signers
     * @param DocumentPacketData $documentPacketData
     */
    public function __construct(
        string $groupDocumentPacketId,
        string $profileCode,
        array $signers,
        DocumentPacketData $documentPacketData
    ) {
        $this->groupDocumentPacketId = $groupDocumentPacketId;
        $this->profileCode = $profileCode;
        $this->signers = $signers;
        $this->documentPacketData = $documentPacketData;
    }

    /**
     * Returns Group Document Packet Id.
     * The unique identifier for the group document packet
     */
    public function getGroupDocumentPacketId(): string
    {
        return $this->groupDocumentPacketId;
    }

    /**
     * Sets Group Document Packet Id.
     * The unique identifier for the group document packet
     *
     * @required
     * @maps groupDocumentPacketId
     */
    public function setGroupDocumentPacketId(string $groupDocumentPacketId): void
    {
        $this->groupDocumentPacketId = $groupDocumentPacketId;
    }

    /**
     * Returns Profile Code.
     * The partner's profile code
     */
    public function getProfileCode(): string
    {
        return $this->profileCode;
    }

    /**
     * Sets Profile Code.
     * The partner's profile code
     *
     * @required
     * @maps profileCode
     */
    public function setProfileCode(string $profileCode): void
    {
        $this->profileCode = $profileCode;
    }

    /**
     * Returns Signers.
     * The document signers
     *
     * @return Signer[]
     */
    public function getSigners(): array
    {
        return $this->signers;
    }

    /**
     * Sets Signers.
     * The document signers
     *
     * @required
     * @maps signers
     *
     * @param Signer[] $signers
     */
    public function setSigners(array $signers): void
    {
        $this->signers = $signers;
    }

    /**
     * Returns Document Packet Data.
     */
    public function getDocumentPacketData(): DocumentPacketData
    {
        return $this->documentPacketData;
    }

    /**
     * Sets Document Packet Data.
     *
     * @required
     * @maps documentPacketData
     */
    public function setDocumentPacketData(DocumentPacketData $documentPacketData): void
    {
        $this->documentPacketData = $documentPacketData;
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
        $json['groupDocumentPacketId'] = $this->groupDocumentPacketId;
        $json['profileCode']           = $this->profileCode;
        $json['signers']               = $this->signers;
        $json['documentPacketData']    = $this->documentPacketData;

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
