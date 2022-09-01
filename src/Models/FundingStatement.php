<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class FundingStatement implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $type;

    /**
     * @var string|null
     */
    private $media;

    /**
     * @var string|null
     */
    private $emailAddress;

    /**
     * @var string|null
     */
    private $frequency;

    /**
     * Returns Type.
     */
    public function getType(): ?string
    {
        return $this->type;
    }

    /**
     * Sets Type.
     *
     * @maps type
     * @factory \SwaggerScarecrowLib\Models\Type3Enum::checkValue
     */
    public function setType(?string $type): void
    {
        $this->type = $type;
    }

    /**
     * Returns Media.
     */
    public function getMedia(): ?string
    {
        return $this->media;
    }

    /**
     * Sets Media.
     *
     * @maps media
     * @factory \SwaggerScarecrowLib\Models\Media1Enum::checkValue
     */
    public function setMedia(?string $media): void
    {
        $this->media = $media;
    }

    /**
     * Returns Email Address.
     * [EU] email address
     */
    public function getEmailAddress(): ?string
    {
        return $this->emailAddress;
    }

    /**
     * Sets Email Address.
     * [EU] email address
     *
     * @maps emailAddress
     */
    public function setEmailAddress(?string $emailAddress): void
    {
        $this->emailAddress = $emailAddress;
    }

    /**
     * Returns Frequency.
     * [EU] DAILY, WEEKLY, MONTHLY
     */
    public function getFrequency(): ?string
    {
        return $this->frequency;
    }

    /**
     * Sets Frequency.
     * [EU] DAILY, WEEKLY, MONTHLY
     *
     * @maps frequency
     * @factory \SwaggerScarecrowLib\Models\Frequency2Enum::checkValue
     */
    public function setFrequency(?string $frequency): void
    {
        $this->frequency = $frequency;
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
        if (isset($this->type)) {
            $json['type']         = Type3Enum::checkValue($this->type);
        }
        if (isset($this->media)) {
            $json['media']        = Media1Enum::checkValue($this->media);
        }
        if (isset($this->emailAddress)) {
            $json['emailAddress'] = $this->emailAddress;
        }
        if (isset($this->frequency)) {
            $json['frequency']    = Frequency2Enum::checkValue($this->frequency);
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
