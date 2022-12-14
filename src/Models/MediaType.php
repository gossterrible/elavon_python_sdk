<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class MediaType implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $type;

    /**
     * @var string|null
     */
    private $subtype;

    /**
     * @var array<string,string>|null
     */
    private $parameters;

    /**
     * @var bool|null
     */
    private $wildcardType;

    /**
     * @var bool|null
     */
    private $wildcardSubtype;

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
     */
    public function setType(?string $type): void
    {
        $this->type = $type;
    }

    /**
     * Returns Subtype.
     */
    public function getSubtype(): ?string
    {
        return $this->subtype;
    }

    /**
     * Sets Subtype.
     *
     * @maps subtype
     */
    public function setSubtype(?string $subtype): void
    {
        $this->subtype = $subtype;
    }

    /**
     * Returns Parameters.
     *
     * @return array<string,string>|null
     */
    public function getParameters(): ?array
    {
        return $this->parameters;
    }

    /**
     * Sets Parameters.
     *
     * @maps parameters
     *
     * @param array<string,string>|null $parameters
     */
    public function setParameters(?array $parameters): void
    {
        $this->parameters = $parameters;
    }

    /**
     * Returns Wildcard Type.
     */
    public function getWildcardType(): ?bool
    {
        return $this->wildcardType;
    }

    /**
     * Sets Wildcard Type.
     *
     * @maps wildcardType
     */
    public function setWildcardType(?bool $wildcardType): void
    {
        $this->wildcardType = $wildcardType;
    }

    /**
     * Returns Wildcard Subtype.
     */
    public function getWildcardSubtype(): ?bool
    {
        return $this->wildcardSubtype;
    }

    /**
     * Sets Wildcard Subtype.
     *
     * @maps wildcardSubtype
     */
    public function setWildcardSubtype(?bool $wildcardSubtype): void
    {
        $this->wildcardSubtype = $wildcardSubtype;
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
            $json['type']            = $this->type;
        }
        if (isset($this->subtype)) {
            $json['subtype']         = $this->subtype;
        }
        if (isset($this->parameters)) {
            $json['parameters']      = $this->parameters;
        }
        if (isset($this->wildcardType)) {
            $json['wildcardType']    = $this->wildcardType;
        }
        if (isset($this->wildcardSubtype)) {
            $json['wildcardSubtype'] = $this->wildcardSubtype;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
