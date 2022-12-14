<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class QuizQuestionChoice implements \JsonSerializable
{
    /**
     * @var int|null
     */
    private $answerNumber;

    /**
     * @var string|null
     */
    private $answerText;

    /**
     * Returns Answer Number.
     * Question answer number
     */
    public function getAnswerNumber(): ?int
    {
        return $this->answerNumber;
    }

    /**
     * Sets Answer Number.
     * Question answer number
     *
     * @maps answerNumber
     */
    public function setAnswerNumber(?int $answerNumber): void
    {
        $this->answerNumber = $answerNumber;
    }

    /**
     * Returns Answer Text.
     * Answer text
     */
    public function getAnswerText(): ?string
    {
        return $this->answerText;
    }

    /**
     * Sets Answer Text.
     * Answer text
     *
     * @maps answerText
     */
    public function setAnswerText(?string $answerText): void
    {
        $this->answerText = $answerText;
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
        if (isset($this->answerNumber)) {
            $json['answerNumber'] = $this->answerNumber;
        }
        if (isset($this->answerText)) {
            $json['answerText']   = $this->answerText;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
