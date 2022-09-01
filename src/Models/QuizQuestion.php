<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class QuizQuestion implements \JsonSerializable
{
    /**
     * @var int|null
     */
    private $questionNumber;

    /**
     * @var string|null
     */
    private $questionText;

    /**
     * @var QuizQuestionChoice[]|null
     */
    private $questionChoices;

    /**
     * Returns Question Number.
     * Quiz question number
     */
    public function getQuestionNumber(): ?int
    {
        return $this->questionNumber;
    }

    /**
     * Sets Question Number.
     * Quiz question number
     *
     * @maps questionNumber
     */
    public function setQuestionNumber(?int $questionNumber): void
    {
        $this->questionNumber = $questionNumber;
    }

    /**
     * Returns Question Text.
     * Text of quiz question
     */
    public function getQuestionText(): ?string
    {
        return $this->questionText;
    }

    /**
     * Sets Question Text.
     * Text of quiz question
     *
     * @maps questionText
     */
    public function setQuestionText(?string $questionText): void
    {
        $this->questionText = $questionText;
    }

    /**
     * Returns Question Choices.
     * List of answer choices for question
     *
     * @return QuizQuestionChoice[]|null
     */
    public function getQuestionChoices(): ?array
    {
        return $this->questionChoices;
    }

    /**
     * Sets Question Choices.
     * List of answer choices for question
     *
     * @maps questionChoices
     *
     * @param QuizQuestionChoice[]|null $questionChoices
     */
    public function setQuestionChoices(?array $questionChoices): void
    {
        $this->questionChoices = $questionChoices;
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
        if (isset($this->questionNumber)) {
            $json['questionNumber']  = $this->questionNumber;
        }
        if (isset($this->questionText)) {
            $json['questionText']    = $this->questionText;
        }
        if (isset($this->questionChoices)) {
            $json['questionChoices'] = $this->questionChoices;
        }

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
