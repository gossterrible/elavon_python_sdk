
# Answer Quiz Request

## Structure

`AnswerQuizRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The app request ID |
| `mid` | `string` | Optional | The Merchant ID |
| `email` | `string` | Optional | The email address |
| `legal_name` | `string` | Optional | The legal name |
| `vat_id` | `string` | Optional | The VAT ID |
| `cc_email` | `string` | Optional | The CC email address |
| `opt_out` | `bool` | Optional | OptOut |
| `marketing_data_consent_map` | `dict` | Optional | The Marketing Consent |
| `quiz_id` | `int` | Required | Unique identifier of quiz, returned in successful get quiz response |
| `transaction_key` | `string` | Required | Unique identifier of quiz response, returned in get quiz response |
| `quiz_answers` | [`List of QuizAnswer`](../../doc/models/quiz-answer.md) | Required | Answers to quiz |
| `country` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "mid": null,
  "email": null,
  "legalName": null,
  "vatId": null,
  "ccEmail": null,
  "optOut": null,
  "marketingDataConsentMap": null,
  "quizId": 170,
  "transactionKey": "transactionKey2",
  "quizAnswers": [
    {
      "questionNumber": 22,
      "answerNumber": 12
    }
  ],
  "country": null
}
```

