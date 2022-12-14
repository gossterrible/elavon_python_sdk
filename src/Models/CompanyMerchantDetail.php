<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;
use SwaggerScarecrowLib\Utils\DateTimeHelper;

class CompanyMerchantDetail implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $amlExemptClass;

    /**
     * @var string|null
     */
    private $fullDBAName;

    /**
     * @var string|null
     */
    private $mccCode;

    /**
     * @var string|null
     */
    private $annualRevenue;

    /**
     * @var string|null
     */
    private $tinFormType;

    /**
     * @var \DateTime|null
     */
    private $taxW8BENSignedDate;

    /**
     * @var string|null
     */
    private $taxClassification;

    /**
     * @var string|null
     */
    private $tinType;

    /**
     * @var string|null
     */
    private $primaryBusinesOps;

    /**
     * @var string|null
     */
    private $countryOfFormation;

    /**
     * @var string|null
     */
    private $boExemptStatus;

    /**
     * @var \DateTime|null
     */
    private $w9CertDate;

    /**
     * Returns Aml Exempt Class.
     */
    public function getAmlExemptClass(): ?string
    {
        return $this->amlExemptClass;
    }

    /**
     * Sets Aml Exempt Class.
     *
     * @maps amlExemptClass
     */
    public function setAmlExemptClass(?string $amlExemptClass): void
    {
        $this->amlExemptClass = $amlExemptClass;
    }

    /**
     * Returns Full DBA Name.
     */
    public function getFullDBAName(): ?string
    {
        return $this->fullDBAName;
    }

    /**
     * Sets Full DBA Name.
     *
     * @maps fullDBAName
     */
    public function setFullDBAName(?string $fullDBAName): void
    {
        $this->fullDBAName = $fullDBAName;
    }

    /**
     * Returns Mcc Code.
     */
    public function getMccCode(): ?string
    {
        return $this->mccCode;
    }

    /**
     * Sets Mcc Code.
     *
     * @maps mccCode
     */
    public function setMccCode(?string $mccCode): void
    {
        $this->mccCode = $mccCode;
    }

    /**
     * Returns Annual Revenue.
     */
    public function getAnnualRevenue(): ?string
    {
        return $this->annualRevenue;
    }

    /**
     * Sets Annual Revenue.
     *
     * @maps annualRevenue
     */
    public function setAnnualRevenue(?string $annualRevenue): void
    {
        $this->annualRevenue = $annualRevenue;
    }

    /**
     * Returns Tin Form Type.
     */
    public function getTinFormType(): ?string
    {
        return $this->tinFormType;
    }

    /**
     * Sets Tin Form Type.
     *
     * @maps tinFormType
     */
    public function setTinFormType(?string $tinFormType): void
    {
        $this->tinFormType = $tinFormType;
    }

    /**
     * Returns Tax W8 BEN Signed Date.
     */
    public function getTaxW8BENSignedDate(): ?\DateTime
    {
        return $this->taxW8BENSignedDate;
    }

    /**
     * Sets Tax W8 BEN Signed Date.
     *
     * @maps taxW8BENSignedDate
     * @factory \SwaggerScarecrowLib\Utils\DateTimeHelper::fromRfc3339DateTime
     */
    public function setTaxW8BENSignedDate(?\DateTime $taxW8BENSignedDate): void
    {
        $this->taxW8BENSignedDate = $taxW8BENSignedDate;
    }

    /**
     * Returns Tax Classification.
     */
    public function getTaxClassification(): ?string
    {
        return $this->taxClassification;
    }

    /**
     * Sets Tax Classification.
     *
     * @maps taxClassification
     */
    public function setTaxClassification(?string $taxClassification): void
    {
        $this->taxClassification = $taxClassification;
    }

    /**
     * Returns Tin Type.
     */
    public function getTinType(): ?string
    {
        return $this->tinType;
    }

    /**
     * Sets Tin Type.
     *
     * @maps tinType
     */
    public function setTinType(?string $tinType): void
    {
        $this->tinType = $tinType;
    }

    /**
     * Returns Primary Busines Ops.
     */
    public function getPrimaryBusinesOps(): ?string
    {
        return $this->primaryBusinesOps;
    }

    /**
     * Sets Primary Busines Ops.
     *
     * @maps primaryBusinesOps
     */
    public function setPrimaryBusinesOps(?string $primaryBusinesOps): void
    {
        $this->primaryBusinesOps = $primaryBusinesOps;
    }

    /**
     * Returns Country of Formation.
     */
    public function getCountryOfFormation(): ?string
    {
        return $this->countryOfFormation;
    }

    /**
     * Sets Country of Formation.
     *
     * @maps countryOfFormation
     */
    public function setCountryOfFormation(?string $countryOfFormation): void
    {
        $this->countryOfFormation = $countryOfFormation;
    }

    /**
     * Returns Bo Exempt Status.
     */
    public function getBoExemptStatus(): ?string
    {
        return $this->boExemptStatus;
    }

    /**
     * Sets Bo Exempt Status.
     *
     * @maps boExemptStatus
     */
    public function setBoExemptStatus(?string $boExemptStatus): void
    {
        $this->boExemptStatus = $boExemptStatus;
    }

    /**
     * Returns W 9 Cert Date.
     */
    public function getW9CertDate(): ?\DateTime
    {
        return $this->w9CertDate;
    }

    /**
     * Sets W 9 Cert Date.
     *
     * @maps w9CertDate
     * @factory \SwaggerScarecrowLib\Utils\DateTimeHelper::fromRfc3339DateTime
     */
    public function setW9CertDate(?\DateTime $w9CertDate): void
    {
        $this->w9CertDate = $w9CertDate;
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
        if (isset($this->amlExemptClass)) {
            $json['amlExemptClass']     = $this->amlExemptClass;
        }
        if (isset($this->fullDBAName)) {
            $json['fullDBAName']        = $this->fullDBAName;
        }
        if (isset($this->mccCode)) {
            $json['mccCode']            = $this->mccCode;
        }
        if (isset($this->annualRevenue)) {
            $json['annualRevenue']      = $this->annualRevenue;
        }
        if (isset($this->tinFormType)) {
            $json['tinFormType']        = $this->tinFormType;
        }
        if (isset($this->taxW8BENSignedDate)) {
            $json['taxW8BENSignedDate'] = DateTimeHelper::toRfc3339DateTime($this->taxW8BENSignedDate);
        }
        if (isset($this->taxClassification)) {
            $json['taxClassification']  = $this->taxClassification;
        }
        if (isset($this->tinType)) {
            $json['tinType']            = $this->tinType;
        }
        if (isset($this->primaryBusinesOps)) {
            $json['primaryBusinesOps']  = $this->primaryBusinesOps;
        }
        if (isset($this->countryOfFormation)) {
            $json['countryOfFormation'] = $this->countryOfFormation;
        }
        if (isset($this->boExemptStatus)) {
            $json['boExemptStatus']     = $this->boExemptStatus;
        }
        if (isset($this->w9CertDate)) {
            $json['w9CertDate']         = DateTimeHelper::toRfc3339DateTime($this->w9CertDate);
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
