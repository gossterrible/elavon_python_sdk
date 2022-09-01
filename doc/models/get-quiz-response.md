
# Get Quiz Response

## Structure

`GetQuizResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `quizInitialResponseType` | [`?string (QuizInitialResponseTypeEnum)`](../../doc/models/quiz-initial-response-type-enum.md) | Optional | Status of quiz response | getQuizInitialResponseType(): ?string | setQuizInitialResponseType(?string quizInitialResponseType): void |
| `transactionKey` | `?string` | Optional | Unique identifier of quiz response, to be used in anser request quiz if successful response is given | getTransactionKey(): ?string | setTransactionKey(?string transactionKey): void |
| `quizId` | `?int` | Optional | Unique identifier of quiz, to be used in answer request quiz if successful response is given | getQuizId(): ?int | setQuizId(?int quizId): void |
| `quizQuestions` | [`?(QuizQuestion[])`](../../doc/models/quiz-question.md) | Optional | Quiz questions, given if request was successful | getQuizQuestions(): ?array | setQuizQuestions(?array quizQuestions): void |
| `error` | `?string` | Optional | Error message from service | getError(): ?string | setError(?string error): void |

## Example (as JSON)

```json
{
  "responseId": null,
  "quizInitialResponseType": null,
  "transactionKey": null,
  "quizId": null,
  "quizQuestions": null,
  "error": null
}
```

