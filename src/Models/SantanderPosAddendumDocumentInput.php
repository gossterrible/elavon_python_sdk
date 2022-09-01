<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class SantanderPosAddendumDocumentInput implements \JsonSerializable
{
    /**
     * @var string
     */
    private $language;

    /**
     * @var string
     */
    private $documentId;

    /**
     * @var string|null
     */
    private $agreementId;

    /**
     * @var string|null
     */
    private $documentPacketId;

    /**
     * @var bool|null
     */
    private $signed;

    /**
     * @var bool|null
     */
    private $groupedApplication;

    /**
     * @var bool|null
     */
    private $wetSigned;

    /**
     * @var Person
     */
    private $principal;

    /**
     * @var string
     */
    private $displayedCurrency;

    /**
     * @var EquipmentInfo
     */
    private $equipmentInfo;

    /**
     * @var BusinessInfo
     */
    private $businessInfo;

    /**
     * @var Person[]|null
     */
    private $additionalShareholders;

    /**
     * @param string $language
     * @param string $documentId
     * @param Person $principal
     * @param string $displayedCurrency
     * @param EquipmentInfo $equipmentInfo
     * @param BusinessInfo $businessInfo
     */
    public function __construct(
        string $language,
        string $documentId,
        Person $principal,
        string $displayedCurrency,
        EquipmentInfo $equipmentInfo,
        BusinessInfo $businessInfo
    ) {
        $this->language = $language;
        $this->documentId = $documentId;
        $this->principal = $principal;
        $this->displayedCurrency = $displayedCurrency;
        $this->equipmentInfo = $equipmentInfo;
        $this->businessInfo = $businessInfo;
    }

    /**
     * Returns Language.
     * Language of document to be generated,  ISO 639-1 standard applies
     */
    public function getLanguage(): string
    {
        return $this->language;
    }

    /**
     * Sets Language.
     * Language of document to be generated,  ISO 639-1 standard applies
     *
     * @required
     * @maps language
     */
    public function setLanguage(string $language): void
    {
        $this->language = $language;
    }

    /**
     * Returns Document Id.
     * Unique id of document
     */
    public function getDocumentId(): string
    {
        return $this->documentId;
    }

    /**
     * Sets Document Id.
     * Unique id of document
     *
     * @required
     * @maps documentId
     */
    public function setDocumentId(string $documentId): void
    {
        $this->documentId = $documentId;
    }

    /**
     * Returns Agreement Id.
     * Merchant id (MID)
     */
    public function getAgreementId(): ?string
    {
        return $this->agreementId;
    }

    /**
     * Sets Agreement Id.
     * Merchant id (MID)
     *
     * @maps agreementId
     */
    public function setAgreementId(?string $agreementId): void
    {
        $this->agreementId = $agreementId;
    }

    /**
     * Returns Document Packet Id.
     * Document packet id
     */
    public function getDocumentPacketId(): ?string
    {
        return $this->documentPacketId;
    }

    /**
     * Sets Document Packet Id.
     * Document packet id
     *
     * @maps documentPacketId
     */
    public function setDocumentPacketId(?string $documentPacketId): void
    {
        $this->documentPacketId = $documentPacketId;
    }

    /**
     * Returns Signed.
     * Boolean flag indicating if document has been signed, true if  YES, false if NO
     */
    public function getSigned(): ?bool
    {
        return $this->signed;
    }

    /**
     * Sets Signed.
     * Boolean flag indicating if document has been signed, true if  YES, false if NO
     *
     * @maps signed
     */
    public function setSigned(?bool $signed): void
    {
        $this->signed = $signed;
    }

    /**
     * Returns Grouped Application.
     * Boolean flag indicating if document is of a group of applications, true if  YES, false if NO
     */
    public function getGroupedApplication(): ?bool
    {
        return $this->groupedApplication;
    }

    /**
     * Sets Grouped Application.
     * Boolean flag indicating if document is of a group of applications, true if  YES, false if NO
     *
     * @maps groupedApplication
     */
    public function setGroupedApplication(?bool $groupedApplication): void
    {
        $this->groupedApplication = $groupedApplication;
    }

    /**
     * Returns Wet Signed.
     * Boolean flag indicating if document is to be wet signed, true if  YES, false if NO
     */
    public function getWetSigned(): ?bool
    {
        return $this->wetSigned;
    }

    /**
     * Sets Wet Signed.
     * Boolean flag indicating if document is to be wet signed, true if  YES, false if NO
     *
     * @maps wetSigned
     */
    public function setWetSigned(?bool $wetSigned): void
    {
        $this->wetSigned = $wetSigned;
    }

    /**
     * Returns Principal.
     */
    public function getPrincipal(): Person
    {
        return $this->principal;
    }

    /**
     * Sets Principal.
     *
     * @required
     * @maps principal
     */
    public function setPrincipal(Person $principal): void
    {
        $this->principal = $principal;
    }

    /**
     * Returns Displayed Currency.
     * Application's currency, ISO 4217 standard applies
     */
    public function getDisplayedCurrency(): string
    {
        return $this->displayedCurrency;
    }

    /**
     * Sets Displayed Currency.
     * Application's currency, ISO 4217 standard applies
     *
     * @required
     * @maps displayedCurrency
     */
    public function setDisplayedCurrency(string $displayedCurrency): void
    {
        $this->displayedCurrency = $displayedCurrency;
    }

    /**
     * Returns Equipment Info.
     * In NA, it's mandatory to have at least one piece of equipment. For third party vendors
     * managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.
     * Contact your Elavon representative for the VAR code(s).
     *
     * In EU, equipmentInfo is optional and no equipment has to be sent. If you have any
     * equipment
     * managed by Elavon, contact your Elavon representative for the VAR code(s).
     */
    public function getEquipmentInfo(): EquipmentInfo
    {
        return $this->equipmentInfo;
    }

    /**
     * Sets Equipment Info.
     * In NA, it's mandatory to have at least one piece of equipment. For third party vendors
     * managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.
     * Contact your Elavon representative for the VAR code(s).
     *
     * In EU, equipmentInfo is optional and no equipment has to be sent. If you have any
     * equipment
     * managed by Elavon, contact your Elavon representative for the VAR code(s).
     *
     * @required
     * @maps equipmentInfo
     */
    public function setEquipmentInfo(EquipmentInfo $equipmentInfo): void
    {
        $this->equipmentInfo = $equipmentInfo;
    }

    /**
     * Returns Business Info.
     */
    public function getBusinessInfo(): BusinessInfo
    {
        return $this->businessInfo;
    }

    /**
     * Sets Business Info.
     *
     * @required
     * @maps businessInfo
     */
    public function setBusinessInfo(BusinessInfo $businessInfo): void
    {
        $this->businessInfo = $businessInfo;
    }

    /**
     * Returns Additional Shareholders.
     * Application's additional shareholders
     *
     * @return Person[]|null
     */
    public function getAdditionalShareholders(): ?array
    {
        return $this->additionalShareholders;
    }

    /**
     * Sets Additional Shareholders.
     * Application's additional shareholders
     *
     * @maps additionalShareholders
     *
     * @param Person[]|null $additionalShareholders
     */
    public function setAdditionalShareholders(?array $additionalShareholders): void
    {
        $this->additionalShareholders = $additionalShareholders;
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
        $json['language']                   = $this->language;
        $json['documentId']                 = $this->documentId;
        if (isset($this->agreementId)) {
            $json['agreementId']            = $this->agreementId;
        }
        if (isset($this->documentPacketId)) {
            $json['documentPacketId']       = $this->documentPacketId;
        }
        if (isset($this->signed)) {
            $json['signed']                 = $this->signed;
        }
        if (isset($this->groupedApplication)) {
            $json['groupedApplication']     = $this->groupedApplication;
        }
        if (isset($this->wetSigned)) {
            $json['wetSigned']              = $this->wetSigned;
        }
        $json['principal']                  = $this->principal;
        $json['displayedCurrency']          = $this->displayedCurrency;
        $json['equipmentInfo']              = $this->equipmentInfo;
        $json['businessInfo']               = $this->businessInfo;
        if (isset($this->additionalShareholders)) {
            $json['additionalShareholders'] = $this->additionalShareholders;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
