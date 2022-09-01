<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class UpdateDocumentPacketDataResponse implements \JsonSerializable
{
    /**
     * @var int|null
     */
    private $responseId;

    /**
     * @var string|null
     */
    private $error;

    /**
     * @var string|null
     */
    private $documentPacketId;

    /**
     * @var SignerResponse[]|null
     */
    private $signerResponses;

    /**
     * Returns Response Id.
     */
    public function getResponseId(): ?int
    {
        return $this->responseId;
    }

    /**
     * Sets Response Id.
     *
     * @maps responseId
     */
    public function setResponseId(?int $responseId): void
    {
        $this->responseId = $responseId;
    }

    /**
     * Returns Error.
     * If processing error occurs, will contain information, else will be empty or null
     */
    public function getError(): ?string
    {
        return $this->error;
    }

    /**
     * Sets Error.
     * If processing error occurs, will contain information, else will be empty or null
     *
     * @maps error
     */
    public function setError(?string $error): void
    {
        $this->error = $error;
    }

    /**
     * Returns Document Packet Id.
     * The unique identifier for the document packet
     */
    public function getDocumentPacketId(): ?string
    {
        return $this->documentPacketId;
    }

    /**
     * Sets Document Packet Id.
     * The unique identifier for the document packet
     *
     * @maps documentPacketId
     */
    public function setDocumentPacketId(?string $documentPacketId): void
    {
        $this->documentPacketId = $documentPacketId;
    }

    /**
     * Returns Signer Responses.
     * The signer containing signer information
     *
     * @return SignerResponse[]|null
     */
    public function getSignerResponses(): ?array
    {
        return $this->signerResponses;
    }

    /**
     * Sets Signer Responses.
     * The signer containing signer information
     *
     * @maps signerResponses
     *
     * @param SignerResponse[]|null $signerResponses
     */
    public function setSignerResponses(?array $signerResponses): void
    {
        $this->signerResponses = $signerResponses;
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
        if (isset($this->responseId)) {
            $json['responseId']       = $this->responseId;
        }
        if (isset($this->error)) {
            $json['error']            = $this->error;
        }
        if (isset($this->documentPacketId)) {
            $json['documentPacketId'] = $this->documentPacketId;
        }
        if (isset($this->signerResponses)) {
            $json['signerResponses']  = $this->signerResponses;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}