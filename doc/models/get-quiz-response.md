
# Get Quiz Response

## Structure

`GetQuizResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_id` | `int` | Optional | - |
| `quiz_initial_response_type` | [`QuizInitialResponseTypeEnum`](../../doc/models/quiz-initial-response-type-enum.md) | Optional | Status of quiz response |
| `transaction_key` | `string` | Optional | Unique identifier of quiz response, to be used in anser request quiz if successful response is given |
| `quiz_id` | `int` | Optional | Unique identifier of quiz, to be used in answer request quiz if successful response is given |
| `quiz_questions` | [`List of QuizQuestion`](../../doc/models/quiz-question.md) | Optional | Quiz questions, given if request was successful |
| `error` | `string` | Optional | Error message from service |

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

