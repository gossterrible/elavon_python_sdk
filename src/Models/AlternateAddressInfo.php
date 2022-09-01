<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

/**
 * Used to hold information about an alternative business address
 */
class AlternateAddressInfo implements \JsonSerializable
{
    /**
     * @var bool
     */
    private $documentNeeded;

    /**
     * @var bool|null
     */
    private $documentVerified;

    /**
     * @var string|null
     */
    private $alternateAddressDocumentType;

    /**
     * @var string|null
     */
    private $documentName;

    /**
     * @param bool $documentNeeded
     */
    public function __construct(bool $documentNeeded)
    {
        $this->documentNeeded = $documentNeeded;
    }

    /**
     * Returns Document Needed.
     * Flag indicating if documentation is needed in Alternate Address Verification
     */
    public function getDocumentNeeded(): bool
    {
        return $this->documentNeeded;
    }

    /**
     * Sets Document Needed.
     * Flag indicating if documentation is needed in Alternate Address Verification
     *
     * @required
     * @maps documentNeeded
     */
    public function setDocumentNeeded(bool $documentNeeded): void
    {
        $this->documentNeeded = $documentNeeded;
    }

    /**
     * Returns Document Verified.
     * Flag indicating if document provided have been verified
     */
    public function getDocumentVerified(): ?bool
    {
        return $this->documentVerified;
    }

    /**
     * Sets Document Verified.
     * Flag indicating if document provided have been verified
     *
     * @maps documentVerified
     */
    public function setDocumentVerified(?bool $documentVerified): void
    {
        $this->documentVerified = $documentVerified;
    }

    /**
     * Returns Alternate Address Document Type.
     * Type of document provided
     */
    public function getAlternateAddressDocumentType(): ?string
    {
        return $this->alternateAddressDocumentType;
    }

    /**
     * Sets Alternate Address Document Type.
     * Type of document provided
     *
     * @maps alternateAddressDocumentType
     * @factory \SwaggerScarecrowLib\Models\AlternateAddressDocumentTypeEnum::checkValue
     */
    public function setAlternateAddressDocumentType(?string $alternateAddressDocumentType): void
    {
        $this->alternateAddressDocumentType = $alternateAddressDocumentType;
    }

    /**
     * Returns Document Name.
     */
    public function getDocumentName(): ?string
    {
        return $this->documentName;
    }

    /**
     * Sets Document Name.
     *
     * @maps documentName
     */
    public function setDocumentName(?string $documentName): void
    {
        $this->documentName = $documentName;
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
        $json['documentNeeded']                   = $this->documentNeeded;
        if (isset($this->documentVerified)) {
            $json['documentVerified']             = $this->documentVerified;
        }
        if (isset($this->alternateAddressDocumentType)) {
            $json['alternateAddressDocumentType'] =
                AlternateAddressDocumentTypeEnum::checkValue(
                    $this->alternateAddressDocumentType
                );
        }
        if (isset($this->documentName)) {
            $json['documentName']                 = $this->documentName;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
