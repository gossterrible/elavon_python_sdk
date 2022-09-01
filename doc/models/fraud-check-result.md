
# Fraud Check Result

## Structure

`FraudCheckResult`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `transactionId` | `?string` | Optional | Unique identifier of quiz response, to be used in answer request for the quiz | getTransactionId(): ?string | setTransactionId(?string transactionId): void |
| `decision` | [`?string (DecisionEnum)`](../../doc/models/decision-enum.md) | Optional | Result reached by quiz process | getDecision(): ?string | setDecision(?string decision): void |

## Example (as JSON)

```json
{
  "transactionId": null,
  "decision": null
}
```

