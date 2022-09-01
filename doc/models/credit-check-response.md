
# Credit Check Response

## Structure

`CreditCheckResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `decision` | [`Decision1Enum`](../../doc/models/decision-1-enum.md) | Optional | Determination of credit check request, declined decisions don't return a token |
| `error` | `string` | Optional | Error message from service |
| `credit_check_id` | `string` | Optional | Identifier for credit check response |
| `credit_check_token` | `string` | Optional | Value to be appended to the boarding request that follows a successful credit check |

## Example (as JSON)

```json
{
  "decision": null,
  "error": null,
  "creditCheckId": null,
  "creditCheckToken": null
}
```

