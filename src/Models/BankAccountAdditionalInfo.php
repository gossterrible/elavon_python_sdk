<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class BankAccountAdditionalInfo implements \JsonSerializable
{
    /**
     * @var string|null
     */
    private $bankName;

    /**
     * @var string|null
     */
    private $bankBranch;

    /**
     * @var bool|null
     */
    private $directDebitAuthorized;

    /**
     * Returns Bank Name.
     */
    public function getBankName(): ?string
    {
        return $this->bankName;
    }

    /**
     * Sets Bank Name.
     *
     * @maps bankName
     */
    public function setBankName(?string $bankName): void
    {
        $this->bankName = $bankName;
    }

    /**
     * Returns Bank Branch.
     */
    public function getBankBranch(): ?string
    {
        return $this->bankBranch;
    }

    /**
     * Sets Bank Branch.
     *
     * @maps bankBranch
     */
    public function setBankBranch(?string $bankBranch): void
    {
        $this->bankBranch = $bankBranch;
    }

    /**
     * Returns Direct Debit Authorized.
     */
    public function getDirectDebitAuthorized(): ?bool
    {
        return $this->directDebitAuthorized;
    }

    /**
     * Sets Direct Debit Authorized.
     *
     * @maps directDebitAuthorized
     */
    public function setDirectDebitAuthorized(?bool $directDebitAuthorized): void
    {
        $this->directDebitAuthorized = $directDebitAuthorized;
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
        if (isset($this->bankName)) {
            $json['bankName']              = $this->bankName;
        }
        if (isset($this->bankBranch)) {
            $json['bankBranch']            = $this->bankBranch;
        }
        if (isset($this->directDebitAuthorized)) {
            $json['directDebitAuthorized'] = $this->directDebitAuthorized;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
