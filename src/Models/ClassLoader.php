<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class ClassLoader implements \JsonSerializable
{
    /**
     * @var ClassLoader|null
     */
    private $parent;

    /**
     * @var string|null
     */
    private $name;

    /**
     * @var Module|null
     */
    private $unnamedModule;

    /**
     * @var bool|null
     */
    private $registeredAsParallelCapable;

    /**
     * @var Package[]|null
     */
    private $definedPackages;

    /**
     * Returns Parent.
     */
    public function getParent(): ?ClassLoader
    {
        return $this->parent;
    }

    /**
     * Sets Parent.
     *
     * @maps parent
     */
    public function setParent(?ClassLoader $parent): void
    {
        $this->parent = $parent;
    }

    /**
     * Returns Name.
     */
    public function getName(): ?string
    {
        return $this->name;
    }

    /**
     * Sets Name.
     *
     * @maps name
     */
    public function setName(?string $name): void
    {
        $this->name = $name;
    }

    /**
     * Returns Unnamed Module.
     */
    public function getUnnamedModule(): ?Module
    {
        return $this->unnamedModule;
    }

    /**
     * Sets Unnamed Module.
     *
     * @maps unnamedModule
     */
    public function setUnnamedModule(?Module $unnamedModule): void
    {
        $this->unnamedModule = $unnamedModule;
    }

    /**
     * Returns Registered as Parallel Capable.
     */
    public function getRegisteredAsParallelCapable(): ?bool
    {
        return $this->registeredAsParallelCapable;
    }

    /**
     * Sets Registered as Parallel Capable.
     *
     * @maps registeredAsParallelCapable
     */
    public function setRegisteredAsParallelCapable(?bool $registeredAsParallelCapable): void
    {
        $this->registeredAsParallelCapable = $registeredAsParallelCapable;
    }

    /**
     * Returns Defined Packages.
     *
     * @return Package[]|null
     */
    public function getDefinedPackages(): ?array
    {
        return $this->definedPackages;
    }

    /**
     * Sets Defined Packages.
     *
     * @maps definedPackages
     *
     * @param Package[]|null $definedPackages
     */
    public function setDefinedPackages(?array $definedPackages): void
    {
        $this->definedPackages = $definedPackages;
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
        if (isset($this->parent)) {
            $json['parent']                      = $this->parent;
        }
        if (isset($this->name)) {
            $json['name']                        = $this->name;
        }
        if (isset($this->unnamedModule)) {
            $json['unnamedModule']               = $this->unnamedModule;
        }
        if (isset($this->registeredAsParallelCapable)) {
            $json['registeredAsParallelCapable'] = $this->registeredAsParallelCapable;
        }
        if (isset($this->definedPackages)) {
            $json['definedPackages']             = $this->definedPackages;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
