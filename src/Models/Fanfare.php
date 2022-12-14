<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class Fanfare implements \JsonSerializable
{
    /**
     * @var float|null
     */
    private $setupFee;

    /**
     * @var float|null
     */
    private $monthlyFee;

    /**
     * @var float|null
     */
    private $annualFee;

    /**
     * @var float|null
     */
    private $customCardUpgradeFee;

    /**
     * @var FanfareCardSplits|null
     */
    private $includedCards;

    /**
     * @var string|null
     */
    private $additionalCardsType;

    /**
     * @var FanfareCardSplits|null
     */
    private $additionalCards;

    /**
     * @var float|null
     */
    private $additionalCardPrice;

    /**
     * @var float|null
     */
    private $programCheckup;

    /**
     * @var string|null
     */
    private $cardStyle;

    /**
     * @var string|null
     */
    private $justificationType;

    /**
     * @var bool|null
     */
    private $cardIsText;

    /**
     * @var string|null
     */
    private $cardText;

    /**
     * @var string|null
     */
    private $textCaseType;

    /**
     * @var string|null
     */
    private $textColor;

    /**
     * @var string|null
     */
    private $textFont;

    /**
     * Returns Setup Fee.
     */
    public function getSetupFee(): ?float
    {
        return $this->setupFee;
    }

    /**
     * Sets Setup Fee.
     *
     * @maps setupFee
     */
    public function setSetupFee(?float $setupFee): void
    {
        $this->setupFee = $setupFee;
    }

    /**
     * Returns Monthly Fee.
     */
    public function getMonthlyFee(): ?float
    {
        return $this->monthlyFee;
    }

    /**
     * Sets Monthly Fee.
     *
     * @maps monthlyFee
     */
    public function setMonthlyFee(?float $monthlyFee): void
    {
        $this->monthlyFee = $monthlyFee;
    }

    /**
     * Returns Annual Fee.
     */
    public function getAnnualFee(): ?float
    {
        return $this->annualFee;
    }

    /**
     * Sets Annual Fee.
     *
     * @maps annualFee
     */
    public function setAnnualFee(?float $annualFee): void
    {
        $this->annualFee = $annualFee;
    }

    /**
     * Returns Custom Card Upgrade Fee.
     */
    public function getCustomCardUpgradeFee(): ?float
    {
        return $this->customCardUpgradeFee;
    }

    /**
     * Sets Custom Card Upgrade Fee.
     *
     * @maps customCardUpgradeFee
     */
    public function setCustomCardUpgradeFee(?float $customCardUpgradeFee): void
    {
        $this->customCardUpgradeFee = $customCardUpgradeFee;
    }

    /**
     * Returns Included Cards.
     */
    public function getIncludedCards(): ?FanfareCardSplits
    {
        return $this->includedCards;
    }

    /**
     * Sets Included Cards.
     *
     * @maps includedCards
     */
    public function setIncludedCards(?FanfareCardSplits $includedCards): void
    {
        $this->includedCards = $includedCards;
    }

    /**
     * Returns Additional Cards Type.
     */
    public function getAdditionalCardsType(): ?string
    {
        return $this->additionalCardsType;
    }

    /**
     * Sets Additional Cards Type.
     *
     * @maps additionalCardsType
     * @factory \SwaggerScarecrowLib\Models\AdditionalCardsTypeEnum::checkValue
     */
    public function setAdditionalCardsType(?string $additionalCardsType): void
    {
        $this->additionalCardsType = $additionalCardsType;
    }

    /**
     * Returns Additional Cards.
     */
    public function getAdditionalCards(): ?FanfareCardSplits
    {
        return $this->additionalCards;
    }

    /**
     * Sets Additional Cards.
     *
     * @maps additionalCards
     */
    public function setAdditionalCards(?FanfareCardSplits $additionalCards): void
    {
        $this->additionalCards = $additionalCards;
    }

    /**
     * Returns Additional Card Price.
     */
    public function getAdditionalCardPrice(): ?float
    {
        return $this->additionalCardPrice;
    }

    /**
     * Sets Additional Card Price.
     *
     * @maps additionalCardPrice
     */
    public function setAdditionalCardPrice(?float $additionalCardPrice): void
    {
        $this->additionalCardPrice = $additionalCardPrice;
    }

    /**
     * Returns Program Checkup.
     */
    public function getProgramCheckup(): ?float
    {
        return $this->programCheckup;
    }

    /**
     * Sets Program Checkup.
     *
     * @maps programCheckup
     */
    public function setProgramCheckup(?float $programCheckup): void
    {
        $this->programCheckup = $programCheckup;
    }

    /**
     * Returns Card Style.
     */
    public function getCardStyle(): ?string
    {
        return $this->cardStyle;
    }

    /**
     * Sets Card Style.
     *
     * @maps cardStyle
     */
    public function setCardStyle(?string $cardStyle): void
    {
        $this->cardStyle = $cardStyle;
    }

    /**
     * Returns Justification Type.
     */
    public function getJustificationType(): ?string
    {
        return $this->justificationType;
    }

    /**
     * Sets Justification Type.
     *
     * @maps justificationType
     * @factory \SwaggerScarecrowLib\Models\JustificationTypeEnum::checkValue
     */
    public function setJustificationType(?string $justificationType): void
    {
        $this->justificationType = $justificationType;
    }

    /**
     * Returns Card Is Text.
     */
    public function getCardIsText(): ?bool
    {
        return $this->cardIsText;
    }

    /**
     * Sets Card Is Text.
     *
     * @maps cardIsText
     */
    public function setCardIsText(?bool $cardIsText): void
    {
        $this->cardIsText = $cardIsText;
    }

    /**
     * Returns Card Text.
     */
    public function getCardText(): ?string
    {
        return $this->cardText;
    }

    /**
     * Sets Card Text.
     *
     * @maps cardText
     */
    public function setCardText(?string $cardText): void
    {
        $this->cardText = $cardText;
    }

    /**
     * Returns Text Case Type.
     */
    public function getTextCaseType(): ?string
    {
        return $this->textCaseType;
    }

    /**
     * Sets Text Case Type.
     *
     * @maps textCaseType
     * @factory \SwaggerScarecrowLib\Models\TextCaseTypeEnum::checkValue
     */
    public function setTextCaseType(?string $textCaseType): void
    {
        $this->textCaseType = $textCaseType;
    }

    /**
     * Returns Text Color.
     */
    public function getTextColor(): ?string
    {
        return $this->textColor;
    }

    /**
     * Sets Text Color.
     *
     * @maps textColor
     */
    public function setTextColor(?string $textColor): void
    {
        $this->textColor = $textColor;
    }

    /**
     * Returns Text Font.
     */
    public function getTextFont(): ?string
    {
        return $this->textFont;
    }

    /**
     * Sets Text Font.
     *
     * @maps textFont
     */
    public function setTextFont(?string $textFont): void
    {
        $this->textFont = $textFont;
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
        if (isset($this->setupFee)) {
            $json['setupFee']             = $this->setupFee;
        }
        if (isset($this->monthlyFee)) {
            $json['monthlyFee']           = $this->monthlyFee;
        }
        if (isset($this->annualFee)) {
            $json['annualFee']            = $this->annualFee;
        }
        if (isset($this->customCardUpgradeFee)) {
            $json['customCardUpgradeFee'] = $this->customCardUpgradeFee;
        }
        if (isset($this->includedCards)) {
            $json['includedCards']        = $this->includedCards;
        }
        if (isset($this->additionalCardsType)) {
            $json['additionalCardsType']  = AdditionalCardsTypeEnum::checkValue($this->additionalCardsType);
        }
        if (isset($this->additionalCards)) {
            $json['additionalCards']      = $this->additionalCards;
        }
        if (isset($this->additionalCardPrice)) {
            $json['additionalCardPrice']  = $this->additionalCardPrice;
        }
        if (isset($this->programCheckup)) {
            $json['programCheckup']       = $this->programCheckup;
        }
        if (isset($this->cardStyle)) {
            $json['cardStyle']            = $this->cardStyle;
        }
        if (isset($this->justificationType)) {
            $json['justificationType']    = JustificationTypeEnum::checkValue($this->justificationType);
        }
        if (isset($this->cardIsText)) {
            $json['cardIsText']           = $this->cardIsText;
        }
        if (isset($this->cardText)) {
            $json['cardText']             = $this->cardText;
        }
        if (isset($this->textCaseType)) {
            $json['textCaseType']         = TextCaseTypeEnum::checkValue($this->textCaseType);
        }
        if (isset($this->textColor)) {
            $json['textColor']            = $this->textColor;
        }
        if (isset($this->textFont)) {
            $json['textFont']             = $this->textFont;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
