<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class LeaseAgreementDocumentInput implements \JsonSerializable
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
     * @var EquipmentInfo
     */
    private $equipmentInfo;

    /**
     * @var ProviderInfo
     */
    private $vendorInfo;

    /**
     * @var Person[]|null
     */
    private $additionalShareholders;

    /**
     * @var BusinessInfo
     */
    private $businessInfo;

    /**
     * @var BankingInfo
     */
    private $bankingInfo;

    /**
     * @var BankAccountAdditionalInfo
     */
    private $bankAccountAdditionalInfo;

    /**
     * @var AdditionalLeaseInfo
     */
    private $additionalLeaseInfo;

    /**
     * @param string $language
     * @param string $documentId
     * @param Person $principal
     * @param EquipmentInfo $equipmentInfo
     * @param ProviderInfo $vendorInfo
     * @param BusinessInfo $businessInfo
     * @param BankingInfo $bankingInfo
     * @param BankAccountAdditionalInfo $bankAccountAdditionalInfo
     * @param AdditionalLeaseInfo $additionalLeaseInfo
     */
    public function __construct(
        string $language,
        string $documentId,
        Person $principal,
        EquipmentInfo $equipmentInfo,
        ProviderInfo $vendorInfo,
        BusinessInfo $businessInfo,
        BankingInfo $bankingInfo,
        BankAccountAdditionalInfo $bankAccountAdditionalInfo,
        AdditionalLeaseInfo $additionalLeaseInfo
    ) {
        $this->language = $language;
        $this->documentId = $documentId;
        $this->principal = $principal;
        $this->equipmentInfo = $equipmentInfo;
        $this->vendorInfo = $vendorInfo;
        $this->businessInfo = $businessInfo;
        $this->bankingInfo = $bankingInfo;
        $this->bankAccountAdditionalInfo = $bankAccountAdditionalInfo;
        $this->additionalLeaseInfo = $additionalLeaseInfo;
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
     * Returns Vendor Info.
     */
    public function getVendorInfo(): ProviderInfo
    {
        return $this->vendorInfo;
    }

    /**
     * Sets Vendor Info.
     *
     * @required
     * @maps vendorInfo
     */
    public function setVendorInfo(ProviderInfo $vendorInfo): void
    {
        $this->vendorInfo = $vendorInfo;
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
     * Returns Banking Info.
     */
    public function getBankingInfo(): BankingInfo
    {
        return $this->bankingInfo;
    }

    /**
     * Sets Banking Info.
     *
     * @required
     * @maps bankingInfo
     */
    public function setBankingInfo(BankingInfo $bankingInfo): void
    {
        $this->bankingInfo = $bankingInfo;
    }

    /**
     * Returns Bank Account Additional Info.
     */
    public function getBankAccountAdditionalInfo(): BankAccountAdditionalInfo
    {
        return $this->bankAccountAdditionalInfo;
    }

    /**
     * Sets Bank Account Additional Info.
     *
     * @required
     * @maps bankAccountAdditionalInfo
     */
    public function setBankAccountAdditionalInfo(BankAccountAdditionalInfo $bankAccountAdditionalInfo): void
    {
        $this->bankAccountAdditionalInfo = $bankAccountAdditionalInfo;
    }

    /**
     * Returns Additional Lease Info.
     */
    public function getAdditionalLeaseInfo(): AdditionalLeaseInfo
    {
        return $this->additionalLeaseInfo;
    }

    /**
     * Sets Additional Lease Info.
     *
     * @required
     * @maps additionalLeaseInfo
     */
    public function setAdditionalLeaseInfo(AdditionalLeaseInfo $additionalLeaseInfo): void
    {
        $this->additionalLeaseInfo = $additionalLeaseInfo;
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
        $json['equipmentInfo']              = $this->equipmentInfo;
        $json['vendorInfo']                 = $this->vendorInfo;
        if (isset($this->additionalShareholders)) {
            $json['additionalShareholders'] = $this->additionalShareholders;
        }
        $json['businessInfo']               = $this->businessInfo;
        $json['bankingInfo']                = $this->bankingInfo;
        $json['bankAccountAdditionalInfo']  = $this->bankAccountAdditionalInfo;
        $json['additionalLeaseInfo']        = $this->additionalLeaseInfo;

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}