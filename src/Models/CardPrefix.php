<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class CardPrefix implements \JsonSerializable
{
    /**
     * @var string
     */
    private $cardType;

    /**
     * @var string
     */
    private $prefix;

    /**
     * @param string $cardType
     * @param string $prefix
     */
    public function __construct(string $cardType, string $prefix)
    {
        $this->cardType = $cardType;
        $this->prefix = $prefix;
    }

    /**
     * Returns Card Type.
     * Type of card
     */
    public function getCardType(): string
    {
        return $this->cardType;
    }

    /**
     * Sets Card Type.
     * Type of card
     *
     * @required
     * @maps cardType
     * @factory \SwaggerScarecrowLib\Models\CardTypeEnum::checkValue
     */
    public function setCardType(string $cardType): void
    {
        $this->cardType = $cardType;
    }

    /**
     * Returns Prefix.
     * Prefix of card
     */
    public function getPrefix(): string
    {
        return $this->prefix;
    }

    /**
     * Sets Prefix.
     * Prefix of card
     *
     * @required
     * @maps prefix
     */
    public function setPrefix(string $prefix): void
    {
        $this->prefix = $prefix;
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
        $json['cardType'] = CardTypeEnum::checkValue($this->cardType);
        $json['prefix']   = $this->prefix;

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
