
# Quiz Question

## Structure

`QuizQuestion`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `questionNumber` | `?int` | Optional | Quiz question number | getQuestionNumber(): ?int | setQuestionNumber(?int questionNumber): void |
| `questionText` | `?string` | Optional | Text of quiz question | getQuestionText(): ?string | setQuestionText(?string questionText): void |
| `questionChoices` | [`?(QuizQuestionChoice[])`](../../doc/models/quiz-question-choice.md) | Optional | List of answer choices for question | getQuestionChoices(): ?array | setQuestionChoices(?array questionChoices): void |

## Example (as JSON)

```json
{
  "questionNumber": null,
  "questionText": null,
  "questionChoices": null
}
```

