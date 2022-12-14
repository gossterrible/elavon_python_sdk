<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class CanadianCodeOfConductDocumentInput implements \JsonSerializable
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
     * @var ScarecrowApplication
     */
    private $scarecrowApplication;

    /**
     * @var CardVolume
     */
    private $cardVolume;

    /**
     * @var SalesOfficeContact
     */
    private $salesOfficeContact;

    /**
     * @var int|null
     */
    private $subJurisdictionId;

    /**
     * @param string $language
     * @param string $documentId
     * @param ScarecrowApplication $scarecrowApplication
     * @param CardVolume $cardVolume
     * @param SalesOfficeContact $salesOfficeContact
     */
    public function __construct(
        string $language,
        string $documentId,
        ScarecrowApplication $scarecrowApplication,
        CardVolume $cardVolume,
        SalesOfficeContact $salesOfficeContact
    ) {
        $this->language = $language;
        $this->documentId = $documentId;
        $this->scarecrowApplication = $scarecrowApplication;
        $this->cardVolume = $cardVolume;
        $this->salesOfficeContact = $salesOfficeContact;
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
     * Returns Scarecrow Application.
     */
    public function getScarecrowApplication(): ScarecrowApplication
    {
        return $this->scarecrowApplication;
    }

    /**
     * Sets Scarecrow Application.
     *
     * @required
     * @maps scarecrowApplication
     */
    public function setScarecrowApplication(ScarecrowApplication $scarecrowApplication): void
    {
        $this->scarecrowApplication = $scarecrowApplication;
    }

    /**
     * Returns Card Volume.
     */
    public function getCardVolume(): CardVolume
    {
        return $this->cardVolume;
    }

    /**
     * Sets Card Volume.
     *
     * @required
     * @maps cardVolume
     */
    public function setCardVolume(CardVolume $cardVolume): void
    {
        $this->cardVolume = $cardVolume;
    }

    /**
     * Returns Sales Office Contact.
     */
    public function getSalesOfficeContact(): SalesOfficeContact
    {
        return $this->salesOfficeContact;
    }

    /**
     * Sets Sales Office Contact.
     *
     * @required
     * @maps salesOfficeContact
     */
    public function setSalesOfficeContact(SalesOfficeContact $salesOfficeContact): void
    {
        $this->salesOfficeContact = $salesOfficeContact;
    }

    /**
     * Returns Sub Jurisdiction Id.
     */
    public function getSubJurisdictionId(): ?int
    {
        return $this->subJurisdictionId;
    }

    /**
     * Sets Sub Jurisdiction Id.
     *
     * @maps subJurisdictionId
     */
    public function setSubJurisdictionId(?int $subJurisdictionId): void
    {
        $this->subJurisdictionId = $subJurisdictionId;
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
        $json['language']               = $this->language;
        $json['documentId']             = $this->documentId;
        if (isset($this->agreementId)) {
            $json['agreementId']        = $this->agreementId;
        }
        if (isset($this->documentPacketId)) {
            $json['documentPacketId']   = $this->documentPacketId;
        }
        if (isset($this->signed)) {
            $json['signed']             = $this->signed;
        }
        if (isset($this->groupedApplication)) {
            $json['groupedApplication'] = $this->groupedApplication;
        }
        if (isset($this->wetSigned)) {
            $json['wetSigned']          = $this->wetSigned;
        }
        $json['scarecrowApplication']   = $this->scarecrowApplication;
        $json['cardVolume']             = $this->cardVolume;
        $json['salesOfficeContact']     = $this->salesOfficeContact;
        if (isset($this->subJurisdictionId)) {
            $json['subJurisdictionId']  = $this->subJurisdictionId;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
