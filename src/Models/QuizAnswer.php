<?php

declare(strict_types=1);

/*
 * SwaggerScarecrowLib
 *
 * This file was automatically generated by APIMATIC v3.0 ( https://www.apimatic.io ).
 */

namespace SwaggerScarecrowLib\Models;

use stdClass;

class QuizAnswer implements \JsonSerializable
{
    /**
     * @var int
     */
    private $questionNumber;

    /**
     * @var int
     */
    private $answerNumber;

    /**
     * @param int $questionNumber
     * @param int $answerNumber
     */
    public function __construct(int $questionNumber, int $answerNumber)
    {
        $this->questionNumber = $questionNumber;
        $this->answerNumber = $answerNumber;
    }

    /**
     * Returns Question Number.
     * Quiz question number
     */
    public function getQuestionNumber(): int
    {
        return $this->questionNumber;
    }

    /**
     * Sets Question Number.
     * Quiz question number
     *
     * @required
     * @maps questionNumber
     */
    public function setQuestionNumber(int $questionNumber): void
    {
        $this->questionNumber = $questionNumber;
    }

    /**
     * Returns Answer Number.
     * The correct answer to the given question number
     */
    public function getAnswerNumber(): int
    {
        return $this->answerNumber;
    }

    /**
     * Sets Answer Number.
     * The correct answer to the given question number
     *
     * @required
     * @maps answerNumber
     */
    public function setAnswerNumber(int $answerNumber): void
    {
        $this->answerNumber = $answerNumber;
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
        $json['questionNumber'] = $this->questionNumber;
        $json['answerNumber']   = $this->answerNumber;

        return (!$asArrayWhenEmpty && empty($json)) ? new stdClass() : $json;
    }
}
