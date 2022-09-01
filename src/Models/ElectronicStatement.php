<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class ElectronicStatement implements \JsonSerializable
{
    /**
     * @var string
     */
    private $type;

    /**
     * @var string
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
     * @param string $type
     * @param string $media
     */
    public function __construct(string $type, string $media)
    {
        $this->type = $type;
        $this->media = $media;
    }

    /**
     * Returns Type.
     * Electronic statement format type
     */
    public function getType(): string
    {
        return $this->type;
    }

    /**
     * Sets Type.
     * Electronic statement format type
     *
     * @required
     * @maps type
     * @factory \SwaggerScarecrowLib\Models\Type4Enum::checkValue
     */
    public function setType(string $type): void
    {
        $this->type = $type;
    }

    /**
     * Returns Media.
     * Electronic statement media type
     */
    public function getMedia(): string
    {
        return $this->media;
    }

    /**
     * Sets Media.
     * Electronic statement media type
     *
     * @required
     * @maps media
     * @factory \SwaggerScarecrowLib\Models\Media2Enum::checkValue
     */
    public function setMedia(string $media): void
    {
        $this->media = $media;
    }

    /**
     * Returns Email Address.
     * Email address of statement
     */
    public function getEmailAddress(): ?string
    {
        return $this->emailAddress;
    }

    /**
     * Sets Email Address.
     * Email address of statement
     *
     * @maps emailAddress
     */
    public function setEmailAddress(?string $emailAddress): void
    {
        $this->emailAddress = $emailAddress;
    }

    /**
     * Returns Frequency.
     * Frequency at which statement is provided
     */
    public function getFrequency(): ?string
    {
        return $this->frequency;
    }

    /**
     * Sets Frequency.
     * Frequency at which statement is provided
     *
     * @maps frequency
     * @factory \SwaggerScarecrowLib\Models\Frequency3Enum::checkValue
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
        $json['type']             = Type4Enum::checkValue($this->type);
        $json['media']            = Media2Enum::checkValue($this->media);
        if (isset($this->emailAddress)) {
            $json['emailAddress'] = $this->emailAddress;
        }
        if (isset($this->frequency)) {
            $json['frequency']    = Frequency3Enum::checkValue($this->frequency);
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}