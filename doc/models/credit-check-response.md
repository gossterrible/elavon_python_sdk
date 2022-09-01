
# Credit Check Response

## Structure

`CreditCheckResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `decision` | [`?string (Decision1Enum)`](../../doc/models/decision-1-enum.md) | Optional | Determination of credit check request, declined decisions don't return a token | getDecision(): ?string | setDecision(?string decision): void |
| `error` | `?string` | Optional | Error message from service | getError(): ?string | setError(?string error): void |
| `creditCheckId` | `?string` | Optional | Identifier for credit check response | getCreditCheckId(): ?string | setCreditCheckId(?string creditCheckId): void |
| `creditCheckToken` | `?string` | Optional | Value to be appended to the boarding request that follows a successful credit check | getCreditCheckToken(): ?string | setCreditCheckToken(?string creditCheckToken): void |

## Example (as JSON)

```json
{
  "decision": null,
  "error": null,
  "creditCheckId": null,
  "creditCheckToken": null
}
```

