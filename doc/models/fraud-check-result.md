
# Fraud Check Result

## Structure

`FraudCheckResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `string` | Optional | Unique identifier of quiz response, to be used in answer request for the quiz |
| `decision` | [`DecisionEnum`](../../doc/models/decision-enum.md) | Optional | Result reached by quiz process |

## Example (as JSON)

```json
{
  "transactionId": null,
  "decision": null
}
```

