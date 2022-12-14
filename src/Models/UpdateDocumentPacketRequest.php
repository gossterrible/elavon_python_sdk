<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class UpdateDocumentPacketRequest implements \JsonSerializable
{
    /**
     * @var string
     */
    private $documentPacketId;

    /**
     * @var string|null
     */
    private $profileCode;

    /**
     * @var Signer[]|null
     */
    private $signers;

    /**
     * @var DocumentPacketData|null
     */
    private $documentPacketData;

    /**
     * @param string $documentPacketId
     */
    public function __construct(string $documentPacketId)
    {
        $this->documentPacketId = $documentPacketId;
    }

    /**
     * Returns Document Packet Id.
     * The unique identifier for the document packet
     */
    public function getDocumentPacketId(): string
    {
        return $this->documentPacketId;
    }

    /**
     * Sets Document Packet Id.
     * The unique identifier for the document packet
     *
     * @required
     * @maps documentPacketId
     */
    public function setDocumentPacketId(string $documentPacketId): void
    {
        $this->documentPacketId = $documentPacketId;
    }

    /**
     * Returns Profile Code.
     * The partner's profile code
     */
    public function getProfileCode(): ?string
    {
        return $this->profileCode;
    }

    /**
     * Sets Profile Code.
     * The partner's profile code
     *
     * @maps profileCode
     */
    public function setProfileCode(?string $profileCode): void
    {
        $this->profileCode = $profileCode;
    }

    /**
     * Returns Signers.
     * The document signers
     *
     * @return Signer[]|null
     */
    public function getSigners(): ?array
    {
        return $this->signers;
    }

    /**
     * Sets Signers.
     * The document signers
     *
     * @maps signers
     *
     * @param Signer[]|null $signers
     */
    public function setSigners(?array $signers): void
    {
        $this->signers = $signers;
    }

    /**
     * Returns Document Packet Data.
     */
    public function getDocumentPacketData(): ?DocumentPacketData
    {
        return $this->documentPacketData;
    }

    /**
     * Sets Document Packet Data.
     *
     * @maps documentPacketData
     */
    public function setDocumentPacketData(?DocumentPacketData $documentPacketData): void
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
        $json['documentPacketId']       = $this->documentPacketId;
        if (isset($this->profileCode)) {
            $json['profileCode']        = $this->profileCode;
        }
        if (isset($this->signers)) {
            $json['signers']            = $this->signers;
        }
        if (isset($this->documentPacketData)) {
            $json['documentPacketData'] = $this->documentPacketData;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
