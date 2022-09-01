
# Verify Bank Account Response

## Structure

`VerifyBankAccountResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `details` | [`?BankVerificationDetails`](../../doc/models/bank-verification-details.md) | Optional | - | getDetails(): ?BankVerificationDetails | setDetails(?BankVerificationDetails details): void |
| `error` | `?string` | Optional | Error message from service | getError(): ?string | setError(?string error): void |

## Example (as JSON)

```json
{
  "responseId": null,
  "details": null,
  "error": null
}
```

