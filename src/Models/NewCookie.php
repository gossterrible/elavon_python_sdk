<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;
use SwaggerScarecrowLib\Utils\DateTimeHelper;

class NewCookie implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $name;

    /**
     * @var string|null
     */
    private $value;

    /**
     * @var int|null
     */
    private $version;

    /**
     * @var string|null
     */
    private $path;

    /**
     * @var string|null
     */
    private $domain;

    /**
     * @var string|null
     */
    private $comment;

    /**
     * @var int|null
     */
    private $maxAge;

    /**
     * @var \DateTime|null
     */
    private $expiry;

    /**
     * @var bool|null
     */
    private $secure;

    /**
     * @var bool|null
     */
    private $httpOnly;

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
     * Returns Value.
     */
    public function getValue(): ?string
    {
        return $this->value;
    }

    /**
     * Sets Value.
     *
     * @maps value
     */
    public function setValue(?string $value): void
    {
        $this->value = $value;
    }

    /**
     * Returns Version.
     */
    public function getVersion(): ?int
    {
        return $this->version;
    }

    /**
     * Sets Version.
     *
     * @maps version
     */
    public function setVersion(?int $version): void
    {
        $this->version = $version;
    }

    /**
     * Returns Path.
     */
    public function getPath(): ?string
    {
        return $this->path;
    }

    /**
     * Sets Path.
     *
     * @maps path
     */
    public function setPath(?string $path): void
    {
        $this->path = $path;
    }

    /**
     * Returns Domain.
     */
    public function getDomain(): ?string
    {
        return $this->domain;
    }

    /**
     * Sets Domain.
     *
     * @maps domain
     */
    public function setDomain(?string $domain): void
    {
        $this->domain = $domain;
    }

    /**
     * Returns Comment.
     */
    public function getComment(): ?string
    {
        return $this->comment;
    }

    /**
     * Sets Comment.
     *
     * @maps comment
     */
    public function setComment(?string $comment): void
    {
        $this->comment = $comment;
    }

    /**
     * Returns Max Age.
     */
    public function getMaxAge(): ?int
    {
        return $this->maxAge;
    }

    /**
     * Sets Max Age.
     *
     * @maps maxAge
     */
    public function setMaxAge(?int $maxAge): void
    {
        $this->maxAge = $maxAge;
    }

    /**
     * Returns Expiry.
     */
    public function getExpiry(): ?\DateTime
    {
        return $this->expiry;
    }

    /**
     * Sets Expiry.
     *
     * @maps expiry
     * @factory \SwaggerScarecrowLib\Utils\DateTimeHelper::fromRfc3339DateTime
     */
    public function setExpiry(?\DateTime $expiry): void
    {
        $this->expiry = $expiry;
    }

    /**
     * Returns Secure.
     */
    public function getSecure(): ?bool
    {
        return $this->secure;
    }

    /**
     * Sets Secure.
     *
     * @maps secure
     */
    public function setSecure(?bool $secure): void
    {
        $this->secure = $secure;
    }

    /**
     * Returns Http Only.
     */
    public function getHttpOnly(): ?bool
    {
        return $this->httpOnly;
    }

    /**
     * Sets Http Only.
     *
     * @maps httpOnly
     */
    public function setHttpOnly(?bool $httpOnly): void
    {
        $this->httpOnly = $httpOnly;
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
        if (isset($this->name)) {
            $json['name']     = $this->name;
        }
        if (isset($this->value)) {
            $json['value']    = $this->value;
        }
        if (isset($this->version)) {
            $json['version']  = $this->version;
        }
        if (isset($this->path)) {
            $json['path']     = $this->path;
        }
        if (isset($this->domain)) {
            $json['domain']   = $this->domain;
        }
        if (isset($this->comment)) {
            $json['comment']  = $this->comment;
        }
        if (isset($this->maxAge)) {
            $json['maxAge']   = $this->maxAge;
        }
        if (isset($this->expiry)) {
            $json['expiry']   = DateTimeHelper::toRfc3339DateTime($this->expiry);
        }
        if (isset($this->secure)) {
            $json['secure']   = $this->secure;
        }
        if (isset($this->httpOnly)) {
            $json['httpOnly'] = $this->httpOnly;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}