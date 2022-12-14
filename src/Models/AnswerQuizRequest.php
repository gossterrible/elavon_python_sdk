<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class AnswerQuizRequest implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $id;

    /**
     * @var string|null
     */
    private $mid;

    /**
     * @var string|null
     */
    private $email;

    /**
     * @var string|null
     */
    private $legalName;

    /**
     * @var string|null
     */
    private $vatId;

    /**
     * @var string|null
     */
    private $ccEmail;

    /**
     * @var bool|null
     */
    private $optOut;

    /**
     * @var array<string,bool>|null
     */
    private $marketingDataConsentMap;

    /**
     * @var int
     */
    private $quizId;

    /**
     * @var string
     */
    private $transactionKey;

    /**
     * @var QuizAnswer[]
     */
    private $quizAnswers;

    /**
     * @var string|null
     */
    private $country;

    /**
     * @param int $quizId
     * @param string $transactionKey
     * @param QuizAnswer[] $quizAnswers
     */
    public function __construct(int $quizId, string $transactionKey, array $quizAnswers)
    {
        $this->quizId = $quizId;
        $this->transactionKey = $transactionKey;
        $this->quizAnswers = $quizAnswers;
    }

    /**
     * Returns Id.
     * The app request ID
     */
    public function getId(): ?string
    {
        return $this->id;
    }

    /**
     * Sets Id.
     * The app request ID
     *
     * @maps id
     */
    public function setId(?string $id): void
    {
        $this->id = $id;
    }

    /**
     * Returns Mid.
     * The Merchant ID
     */
    public function getMid(): ?string
    {
        return $this->mid;
    }

    /**
     * Sets Mid.
     * The Merchant ID
     *
     * @maps mid
     */
    public function setMid(?string $mid): void
    {
        $this->mid = $mid;
    }

    /**
     * Returns Email.
     * The email address
     */
    public function getEmail(): ?string
    {
        return $this->email;
    }

    /**
     * Sets Email.
     * The email address
     *
     * @maps email
     */
    public function setEmail(?string $email): void
    {
        $this->email = $email;
    }

    /**
     * Returns Legal Name.
     * The legal name
     */
    public function getLegalName(): ?string
    {
        return $this->legalName;
    }

    /**
     * Sets Legal Name.
     * The legal name
     *
     * @maps legalName
     */
    public function setLegalName(?string $legalName): void
    {
        $this->legalName = $legalName;
    }

    /**
     * Returns Vat Id.
     * The VAT ID
     */
    public function getVatId(): ?string
    {
        return $this->vatId;
    }

    /**
     * Sets Vat Id.
     * The VAT ID
     *
     * @maps vatId
     */
    public function setVatId(?string $vatId): void
    {
        $this->vatId = $vatId;
    }

    /**
     * Returns Cc Email.
     * The CC email address
     */
    public function getCcEmail(): ?string
    {
        return $this->ccEmail;
    }

    /**
     * Sets Cc Email.
     * The CC email address
     *
     * @maps ccEmail
     */
    public function setCcEmail(?string $ccEmail): void
    {
        $this->ccEmail = $ccEmail;
    }

    /**
     * Returns Opt Out.
     * OptOut
     */
    public function getOptOut(): ?bool
    {
        return $this->optOut;
    }

    /**
     * Sets Opt Out.
     * OptOut
     *
     * @maps optOut
     */
    public function setOptOut(?bool $optOut): void
    {
        $this->optOut = $optOut;
    }

    /**
     * Returns Marketing Data Consent Map.
     * The Marketing Consent
     *
     * @return array<string,bool>|null
     */
    public function getMarketingDataConsentMap(): ?array
    {
        return $this->marketingDataConsentMap;
    }

    /**
     * Sets Marketing Data Consent Map.
     * The Marketing Consent
     *
     * @maps marketingDataConsentMap
     *
     * @param array<string,bool>|null $marketingDataConsentMap
     */
    public function setMarketingDataConsentMap(?array $marketingDataConsentMap): void
    {
        $this->marketingDataConsentMap = $marketingDataConsentMap;
    }

    /**
     * Returns Quiz Id.
     * Unique identifier of quiz, returned in successful get quiz response
     */
    public function getQuizId(): int
    {
        return $this->quizId;
    }

    /**
     * Sets Quiz Id.
     * Unique identifier of quiz, returned in successful get quiz response
     *
     * @required
     * @maps quizId
     */
    public function setQuizId(int $quizId): void
    {
        $this->quizId = $quizId;
    }

    /**
     * Returns Transaction Key.
     * Unique identifier of quiz response, returned in get quiz response
     */
    public function getTransactionKey(): string
    {
        return $this->transactionKey;
    }

    /**
     * Sets Transaction Key.
     * Unique identifier of quiz response, returned in get quiz response
     *
     * @required
     * @maps transactionKey
     */
    public function setTransactionKey(string $transactionKey): void
    {
        $this->transactionKey = $transactionKey;
    }

    /**
     * Returns Quiz Answers.
     * Answers to quiz
     *
     * @return QuizAnswer[]
     */
    public function getQuizAnswers(): array
    {
        return $this->quizAnswers;
    }

    /**
     * Sets Quiz Answers.
     * Answers to quiz
     *
     * @required
     * @maps quizAnswers
     *
     * @param QuizAnswer[] $quizAnswers
     */
    public function setQuizAnswers(array $quizAnswers): void
    {
        $this->quizAnswers = $quizAnswers;
    }

    /**
     * Returns Country.
     */
    public function getCountry(): ?string
    {
        return $this->country;
    }

    /**
     * Sets Country.
     *
     * @maps country
     */
    public function setCountry(?string $country): void
    {
        $this->country = $country;
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
        if (isset($this->id)) {
            $json['id']                      = $this->id;
        }
        if (isset($this->mid)) {
            $json['mid']                     = $this->mid;
        }
        if (isset($this->email)) {
            $json['email']                   = $this->email;
        }
        if (isset($this->legalName)) {
            $json['legalName']               = $this->legalName;
        }
        if (isset($this->vatId)) {
            $json['vatId']                   = $this->vatId;
        }
        if (isset($this->ccEmail)) {
            $json['ccEmail']                 = $this->ccEmail;
        }
        if (isset($this->optOut)) {
            $json['optOut']                  = $this->optOut;
        }
        if (isset($this->marketingDataConsentMap)) {
            $json['marketingDataConsentMap'] = $this->marketingDataConsentMap;
        }
        $json['quizId']                      = $this->quizId;
        $json['transactionKey']              = $this->transactionKey;
        $json['quizAnswers']                 = $this->quizAnswers;
        if (isset($this->country)) {
            $json['country']                 = $this->country;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
