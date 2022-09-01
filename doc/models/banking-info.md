
# Banking Info

## Structure

`BankingInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | Account holder name, required in EU<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `bank_name` | `string` | Optional | Name of bank account is associated with |
| `urgent_payment` | `bool` | Optional | [EU] Flag indicating Urgent Payments service |
| `funding_method` | [`FundingMethodEnum`](../../doc/models/funding-method-enum.md) | Required | NETCREDIT or GROSS |
| `account_number` | `string` | Required | Account number |
| `sort_code` | `string` | Required | Account Sort Code in EU, Account ABA Routing Number in NA |
| `iban` | `string` | Optional | [EU] Account IBAN, required in cases where Sort Code + Account Number not Present |
| `swift_code` | `string` | Optional | [EU] SWIFT/BIC code |
| `bank_creditor_id` | `string` | Optional | [EU] Bank Creditor Id |
| `bank_direct` | `bool` | Optional | [EU]  Bank Direct Flag. Boolean true if yes, false if no |
| `country` | `string` | Optional | Country of bank account, should match application's root country, ISO 3166-1 alpha-3 standard applies |
| `tape_id` | `string` | Optional | [NA] Tape Id of account, required in NA |
| `true_daily` | `bool` | Optional | [NA] True Daily Flag. Boolean true if yes, false if no |
| `use_chain_account_number` | `bool` | Optional | Use Chain Account Number Flag, Boolean true if yes, false if no |

## Example (as JSON)

```json
{
  "fundingMethod": null,
  "accountNumber": "20581687",
  "sortCode": "121000248"
}
```

