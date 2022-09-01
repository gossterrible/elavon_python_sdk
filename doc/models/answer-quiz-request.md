
# Answer Quiz Request

## Structure

`AnswerQuizRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `id` | `?string` | Optional | The app request ID | getId(): ?string | setId(?string id): void |
| `mid` | `?string` | Optional | The Merchant ID | getMid(): ?string | setMid(?string mid): void |
| `email` | `?string` | Optional | The email address | getEmail(): ?string | setEmail(?string email): void |
| `legalName` | `?string` | Optional | The legal name | getLegalName(): ?string | setLegalName(?string legalName): void |
| `vatId` | `?string` | Optional | The VAT ID | getVatId(): ?string | setVatId(?string vatId): void |
| `ccEmail` | `?string` | Optional | The CC email address | getCcEmail(): ?string | setCcEmail(?string ccEmail): void |
| `optOut` | `?bool` | Optional | OptOut | getOptOut(): ?bool | setOptOut(?bool optOut): void |
| `marketingDataConsentMap` | `?array<string,bool>` | Optional | The Marketing Consent | getMarketingDataConsentMap(): ?array | setMarketingDataConsentMap(?array marketingDataConsentMap): void |
| `quizId` | `int` | Required | Unique identifier of quiz, returned in successful get quiz response | getQuizId(): int | setQuizId(int quizId): void |
| `transactionKey` | `string` | Required | Unique identifier of quiz response, returned in get quiz response | getTransactionKey(): string | setTransactionKey(string transactionKey): void |
| `quizAnswers` | [`QuizAnswer[]`](../../doc/models/quiz-answer.md) | Required | Answers to quiz | getQuizAnswers(): array | setQuizAnswers(array quizAnswers): void |
| `country` | `?string` | Optional | - | getCountry(): ?string | setCountry(?string country): void |

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

