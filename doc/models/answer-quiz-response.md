
# Answer Quiz Response

## Structure

`AnswerQuizResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `fraudCheckResult` | [`?FraudCheckResult`](../../doc/models/fraud-check-result.md) | Optional | - | getFraudCheckResult(): ?FraudCheckResult | setFraudCheckResult(?FraudCheckResult fraudCheckResult): void |
| `error` | `?string` | Optional | Error text should issue occur durring answer quiz operation | getError(): ?string | setError(?string error): void |

## Example (as JSON)

```json
{
  "responseId": null,
  "fraudCheckResult": null,
  "error": null
}
```

