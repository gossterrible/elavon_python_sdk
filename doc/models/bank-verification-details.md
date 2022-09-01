
# Bank Verification Details

## Structure

`BankVerificationDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_name` | `string` | Optional | Name of bank that bank verification call resolved to |
| `bank_branch` | `string` | Optional | Name of bank branh that bank verification call resolved to |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | Status of bank verification response |
| `bank_logo_path` | `string` | Optional | - |
| `bank_country` | `string` | Optional | Country code that bank verification call resolved to, ISO 3166-1 alpha-3 standard applies |
| `sort_code` | `string` | Optional | Sort code/ABA routing number that bank verification call used |
| `account_number` | `string` | Optional | - |
| `has_multiple_branches` | `bool` | Optional | Flag indicating if bank has more than one branch, true if YES, false if NO |
| `realtime_payment_flag` | `bool` | Optional | Flag indicating if the bank can accept true daily/ real time payments |

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

