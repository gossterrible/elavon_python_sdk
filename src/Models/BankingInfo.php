<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class BankingInfo implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $accountName;

    /**
     * @var string|null
     */
    private $bankName;

    /**
     * @var bool|null
     */
    private $urgentPayment;

    /**
     * @var string
     */
    private $fundingMethod;

    /**
     * @var string
     */
    private $accountNumber;

    /**
     * @var string
     */
    private $sortCode;

    /**
     * @var string|null
     */
    private $iban;

    /**
     * @var string|null
     */
    private $swiftCode;

    /**
     * @var string|null
     */
    private $bankCreditorId;

    /**
     * @var bool|null
     */
    private $bankDirect;

    /**
     * @var string|null
     */
    private $country;

    /**
     * @var string|null
     */
    private $tapeId;

    /**
     * @var bool|null
     */
    private $trueDaily;

    /**
     * @var bool|null
     */
    private $useChainAccountNumber;

    /**
     * @param string $fundingMethod
     * @param string $accountNumber
     * @param string $sortCode
     */
    public function __construct(string $fundingMethod, string $accountNumber, string $sortCode)
    {
        $this->fundingMethod = $fundingMethod;
        $this->accountNumber = $accountNumber;
        $this->sortCode = $sortCode;
    }

    /**
     * Returns Account Name.
     * Account holder name, required in EU
     */
    public function getAccountName(): ?string
    {
        return $this->accountName;
    }

    /**
     * Sets Account Name.
     * Account holder name, required in EU
     *
     * @maps accountName
     */
    public function setAccountName(?string $accountName): void
    {
        $this->accountName = $accountName;
    }

    /**
     * Returns Bank Name.
     * Name of bank account is associated with
     */
    public function getBankName(): ?string
    {
        return $this->bankName;
    }

    /**
     * Sets Bank Name.
     * Name of bank account is associated with
     *
     * @maps bankName
     */
    public function setBankName(?string $bankName): void
    {
        $this->bankName = $bankName;
    }

    /**
     * Returns Urgent Payment.
     * [EU] Flag indicating Urgent Payments service
     */
    public function getUrgentPayment(): ?bool
    {
        return $this->urgentPayment;
    }

    /**
     * Sets Urgent Payment.
     * [EU] Flag indicating Urgent Payments service
     *
     * @maps urgentPayment
     */
    public function setUrgentPayment(?bool $urgentPayment): void
    {
        $this->urgentPayment = $urgentPayment;
    }

    /**
     * Returns Funding Method.
     * NETCREDIT or GROSS
     */
    public function getFundingMethod(): string
    {
        return $this->fundingMethod;
    }

    /**
     * Sets Funding Method.
     * NETCREDIT or GROSS
     *
     * @required
     * @maps fundingMethod
     * @factory \SwaggerScarecrowLib\Models\FundingMethodEnum::checkValue
     */
    public function setFundingMethod(string $fundingMethod): void
    {
        $this->fundingMethod = $fundingMethod;
    }

    /**
     * Returns Account Number.
     * Account number
     */
    public function getAccountNumber(): string
    {
        return $this->accountNumber;
    }

    /**
     * Sets Account Number.
     * Account number
     *
     * @required
     * @maps accountNumber
     */
    public function setAccountNumber(string $accountNumber): void
    {
        $this->accountNumber = $accountNumber;
    }

    /**
     * Returns Sort Code.
     * Account Sort Code in EU, Account ABA Routing Number in NA
     */
    public function getSortCode(): string
    {
        return $this->sortCode;
    }

    /**
     * Sets Sort Code.
     * Account Sort Code in EU, Account ABA Routing Number in NA
     *
     * @required
     * @maps sortCode
     */
    public function setSortCode(string $sortCode): void
    {
        $this->sortCode = $sortCode;
    }

    /**
     * Returns Iban.
     * [EU] Account IBAN, required in cases where Sort Code + Account Number not Present
     */
    public function getIban(): ?string
    {
        return $this->iban;
    }

    /**
     * Sets Iban.
     * [EU] Account IBAN, required in cases where Sort Code + Account Number not Present
     *
     * @maps iban
     */
    public function setIban(?string $iban): void
    {
        $this->iban = $iban;
    }

    /**
     * Returns Swift Code.
     * [EU] SWIFT/BIC code
     */
    public function getSwiftCode(): ?string
    {
        return $this->swiftCode;
    }

    /**
     * Sets Swift Code.
     * [EU] SWIFT/BIC code
     *
     * @maps swiftCode
     */
    public function setSwiftCode(?string $swiftCode): void
    {
        $this->swiftCode = $swiftCode;
    }

    /**
     * Returns Bank Creditor Id.
     * [EU] Bank Creditor Id
     */
    public function getBankCreditorId(): ?string
    {
        return $this->bankCreditorId;
    }

    /**
     * Sets Bank Creditor Id.
     * [EU] Bank Creditor Id
     *
     * @maps bankCreditorId
     */
    public function setBankCreditorId(?string $bankCreditorId): void
    {
        $this->bankCreditorId = $bankCreditorId;
    }

    /**
     * Returns Bank Direct.
     * [EU]  Bank Direct Flag. Boolean true if yes, false if no
     */
    public function getBankDirect(): ?bool
    {
        return $this->bankDirect;
    }

    /**
     * Sets Bank Direct.
     * [EU]  Bank Direct Flag. Boolean true if yes, false if no
     *
     * @maps bankDirect
     */
    public function setBankDirect(?bool $bankDirect): void
    {
        $this->bankDirect = $bankDirect;
    }

    /**
     * Returns Country.
     * Country of bank account, should match application's root country, ISO 3166-1 alpha-3 standard
     * applies
     */
    public function getCountry(): ?string
    {
        return $this->country;
    }

    /**
     * Sets Country.
     * Country of bank account, should match application's root country, ISO 3166-1 alpha-3 standard
     * applies
     *
     * @maps country
     */
    public function setCountry(?string $country): void
    {
        $this->country = $country;
    }

    /**
     * Returns Tape Id.
     * [NA] Tape Id of account, required in NA
     */
    public function getTapeId(): ?string
    {
        return $this->tapeId;
    }

    /**
     * Sets Tape Id.
     * [NA] Tape Id of account, required in NA
     *
     * @maps tapeId
     */
    public function setTapeId(?string $tapeId): void
    {
        $this->tapeId = $tapeId;
    }

    /**
     * Returns True Daily.
     * [NA] True Daily Flag. Boolean true if yes, false if no
     */
    public function getTrueDaily(): ?bool
    {
        return $this->trueDaily;
    }

    /**
     * Sets True Daily.
     * [NA] True Daily Flag. Boolean true if yes, false if no
     *
     * @maps trueDaily
     */
    public function setTrueDaily(?bool $trueDaily): void
    {
        $this->trueDaily = $trueDaily;
    }

    /**
     * Returns Use Chain Account Number.
     * Use Chain Account Number Flag, Boolean true if yes, false if no
     */
    public function getUseChainAccountNumber(): ?bool
    {
        return $this->useChainAccountNumber;
    }

    /**
     * Sets Use Chain Account Number.
     * Use Chain Account Number Flag, Boolean true if yes, false if no
     *
     * @maps useChainAccountNumber
     */
    public function setUseChainAccountNumber(?bool $useChainAccountNumber): void
    {
        $this->useChainAccountNumber = $useChainAccountNumber;
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
        if (isset($this->accountName)) {
            $json['accountName']           = $this->accountName;
        }
        if (isset($this->bankName)) {
            $json['bankName']              = $this->bankName;
        }
        if (isset($this->urgentPayment)) {
            $json['urgentPayment']         = $this->urgentPayment;
        }
        $json['fundingMethod']             = FundingMethodEnum::checkValue($this->fundingMethod);
        $json['accountNumber']             = $this->accountNumber;
        $json['sortCode']                  = $this->sortCode;
        if (isset($this->iban)) {
            $json['iban']                  = $this->iban;
        }
        if (isset($this->swiftCode)) {
            $json['swiftCode']             = $this->swiftCode;
        }
        if (isset($this->bankCreditorId)) {
            $json['bankCreditorId']        = $this->bankCreditorId;
        }
        if (isset($this->bankDirect)) {
            $json['bankDirect']            = $this->bankDirect;
        }
        if (isset($this->country)) {
            $json['country']               = $this->country;
        }
        if (isset($this->tapeId)) {
            $json['tapeId']                = $this->tapeId;
        }
        if (isset($this->trueDaily)) {
            $json['trueDaily']             = $this->trueDaily;
        }
        if (isset($this->useChainAccountNumber)) {
            $json['useChainAccountNumber'] = $this->useChainAccountNumber;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
