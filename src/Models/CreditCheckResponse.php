<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class CreditCheckResponse implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $decision;

    /**
     * @var string|null
     */
    private $error;

    /**
     * @var string|null
     */
    private $creditCheckId;

    /**
     * @var string|null
     */
    private $creditCheckToken;

    /**
     * Returns Decision.
     * Determination of credit check request, declined decisions don't return a token
     */
    public function getDecision(): ?string
    {
        return $this->decision;
    }

    /**
     * Sets Decision.
     * Determination of credit check request, declined decisions don't return a token
     *
     * @maps decision
     * @factory \SwaggerScarecrowLib\Models\Decision1Enum::checkValue
     */
    public function setDecision(?string $decision): void
    {
        $this->decision = $decision;
    }

    /**
     * Returns Error.
     * Error message from service
     */
    public function getError(): ?string
    {
        return $this->error;
    }

    /**
     * Sets Error.
     * Error message from service
     *
     * @maps error
     */
    public function setError(?string $error): void
    {
        $this->error = $error;
    }

    /**
     * Returns Credit Check Id.
     * Identifier for credit check response
     */
    public function getCreditCheckId(): ?string
    {
        return $this->creditCheckId;
    }

    /**
     * Sets Credit Check Id.
     * Identifier for credit check response
     *
     * @maps creditCheckId
     */
    public function setCreditCheckId(?string $creditCheckId): void
    {
        $this->creditCheckId = $creditCheckId;
    }

    /**
     * Returns Credit Check Token.
     * Value to be appended to the boarding request that follows a successful credit check
     */
    public function getCreditCheckToken(): ?string
    {
        return $this->creditCheckToken;
    }

    /**
     * Sets Credit Check Token.
     * Value to be appended to the boarding request that follows a successful credit check
     *
     * @maps creditCheckToken
     */
    public function setCreditCheckToken(?string $creditCheckToken): void
    {
        $this->creditCheckToken = $creditCheckToken;
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
        if (isset($this->decision)) {
            $json['decision']         = Decision1Enum::checkValue($this->decision);
        }
        if (isset($this->error)) {
            $json['error']            = $this->error;
        }
        if (isset($this->creditCheckId)) {
            $json['creditCheckId']    = $this->creditCheckId;
        }
        if (isset($this->creditCheckToken)) {
            $json['creditCheckToken'] = $this->creditCheckToken;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}