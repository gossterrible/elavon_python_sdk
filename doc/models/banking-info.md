
# Banking Info

## Structure

`BankingInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `accountName` | `?string` | Optional | Account holder name, required in EU<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` | getAccountName(): ?string | setAccountName(?string accountName): void |
| `bankName` | `?string` | Optional | Name of bank account is associated with | getBankName(): ?string | setBankName(?string bankName): void |
| `urgentPayment` | `?bool` | Optional | [EU] Flag indicating Urgent Payments service | getUrgentPayment(): ?bool | setUrgentPayment(?bool urgentPayment): void |
| `fundingMethod` | [`string (FundingMethodEnum)`](../../doc/models/funding-method-enum.md) | Required | NETCREDIT or GROSS | getFundingMethod(): string | setFundingMethod(string fundingMethod): void |
| `accountNumber` | `string` | Required | Account number | getAccountNumber(): string | setAccountNumber(string accountNumber): void |
| `sortCode` | `string` | Required | Account Sort Code in EU, Account ABA Routing Number in NA | getSortCode(): string | setSortCode(string sortCode): void |
| `iban` | `?string` | Optional | [EU] Account IBAN, required in cases where Sort Code + Account Number not Present | getIban(): ?string | setIban(?string iban): void |
| `swiftCode` | `?string` | Optional | [EU] SWIFT/BIC code | getSwiftCode(): ?string | setSwiftCode(?string swiftCode): void |
| `bankCreditorId` | `?string` | Optional | [EU] Bank Creditor Id | getBankCreditorId(): ?string | setBankCreditorId(?string bankCreditorId): void |
| `bankDirect` | `?bool` | Optional | [EU]  Bank Direct Flag. Boolean true if yes, false if no | getBankDirect(): ?bool | setBankDirect(?bool bankDirect): void |
| `country` | `?string` | Optional | Country of bank account, should match application's root country, ISO 3166-1 alpha-3 standard applies | getCountry(): ?string | setCountry(?string country): void |
| `tapeId` | `?string` | Optional | [NA] Tape Id of account, required in NA | getTapeId(): ?string | setTapeId(?string tapeId): void |
| `trueDaily` | `?bool` | Optional | [NA] True Daily Flag. Boolean true if yes, false if no | getTrueDaily(): ?bool | setTrueDaily(?bool trueDaily): void |
| `useChainAccountNumber` | `?bool` | Optional | Use Chain Account Number Flag, Boolean true if yes, false if no | getUseChainAccountNumber(): ?bool | setUseChainAccountNumber(?bool useChainAccountNumber): void |

## Example (as JSON)

```json
{
  "fundingMethod": null,
  "accountNumber": "20581687",
  "sortCode": "121000248"
}
```

