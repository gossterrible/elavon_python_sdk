
# Bank Verification Details

## Structure

`BankVerificationDetails`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `bankName` | `?string` | Optional | Name of bank that bank verification call resolved to | getBankName(): ?string | setBankName(?string bankName): void |
| `bankBranch` | `?string` | Optional | Name of bank branh that bank verification call resolved to | getBankBranch(): ?string | setBankBranch(?string bankBranch): void |
| `status` | [`?string (StatusEnum)`](../../doc/models/status-enum.md) | Optional | Status of bank verification response | getStatus(): ?string | setStatus(?string status): void |
| `bankLogoPath` | `?string` | Optional | - | getBankLogoPath(): ?string | setBankLogoPath(?string bankLogoPath): void |
| `bankCountry` | `?string` | Optional | Country code that bank verification call resolved to, ISO 3166-1 alpha-3 standard applies | getBankCountry(): ?string | setBankCountry(?string bankCountry): void |
| `sortCode` | `?string` | Optional | Sort code/ABA routing number that bank verification call used | getSortCode(): ?string | setSortCode(?string sortCode): void |
| `accountNumber` | `?string` | Optional | - | getAccountNumber(): ?string | setAccountNumber(?string accountNumber): void |
| `hasMultipleBranches` | `?bool` | Optional | Flag indicating if bank has more than one branch, true if YES, false if NO | getHasMultipleBranches(): ?bool | setHasMultipleBranches(?bool hasMultipleBranches): void |
| `realtimePaymentFlag` | `?bool` | Optional | Flag indicating if the bank can accept true daily/ real time payments | getRealtimePaymentFlag(): ?bool | setRealtimePaymentFlag(?bool realtimePaymentFlag): void |

## Example (as JSON)

```json
{
  "bankName": null,
  "bankBranch": null,
  "status": null,
  "bankLogoPath": null,
  "bankCountry": null,
  "sortCode": null,
  "accountNumber": null,
  "hasMultipleBranches": null,
  "realtimePaymentFlag": null
}
```

