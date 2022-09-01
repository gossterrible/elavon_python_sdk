<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class SignerStatusResponse implements \JsonSerializable
{
    /**
     * @var string
     */
    private $signerId;

    /**
     * @var string
     */
    private $signerStatus;

    /**
     * @param string $signerId
     * @param string $signerStatus
     */
    public function __construct(string $signerId, string $signerStatus)
    {
        $this->signerId = $signerId;
        $this->signerStatus = $signerStatus;
    }

    /**
     * Returns Signer Id.
     * The unique signer identifier
     */
    public function getSignerId(): string
    {
        return $this->signerId;
    }

    /**
     * Sets Signer Id.
     * The unique signer identifier
     *
     * @required
     * @maps signerId
     */
    public function setSignerId(string $signerId): void
    {
        $this->signerId = $signerId;
    }

    /**
     * Returns Signer Status.
     * The signer's id and state
     */
    public function getSignerStatus(): string
    {
        return $this->signerStatus;
    }

    /**
     * Sets Signer Status.
     * The signer's id and state
     *
     * @required
     * @maps signerStatus
     * @factory \SwaggerScarecrowLib\Models\SignerStatusEnum::checkValue
     */
    public function setSignerStatus(string $signerStatus): void
    {
        $this->signerStatus = $signerStatus;
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
        $json['signerId']     = $this->signerId;
        $json['signerStatus'] = SignerStatusEnum::checkValue($this->signerStatus);

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
