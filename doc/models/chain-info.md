
# Chain Info

## Structure

`ChainInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `chainNumber` | `string` | Required | Name of new chain to be set up<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `7` | getChainNumber(): string | setChainNumber(string chainNumber): void |
| `chainName` | `string` | Required | Number of new chain to be set up | getChainName(): string | setChainName(string chainName): void |
| `sendStatementToAddress` | [`string (SendStatementToAddressEnum)`](../../doc/models/send-statement-to-address-enum.md) | Required | Address that the new chain's statements will be sent to | getSendStatementToAddress(): string | setSendStatementToAddress(string sendStatementToAddress): void |
| `statementMedia` | [`string (StatementMediaEnum)`](../../doc/models/statement-media-enum.md) | Required | Media type of chain's statements | getStatementMedia(): string | setStatementMedia(string statementMedia): void |
| `address` | [`Address`](../../doc/models/address.md) | Required | - | getAddress(): Address | setAddress(Address address): void |
| `chainLevelBilling` | `bool` | Required | Billing level of new chain | getChainLevelBilling(): bool | setChainLevelBilling(bool chainLevelBilling): void |
| `bankAccounts` | [`array<string,BankingInfo>`](../../doc/models/banking-info.md) | Required | Chain's bank account information. The valid keys are as follows: BILLING, DEPOSIT, LEASE, CHARGEBACK | getBankAccounts(): array | setBankAccounts(array bankAccounts): void |

## Example (as JSON)

```json
{
  "chainNumber": null,
  "chainName": null,
  "sendStatementToAddress": null,
  "statementMedia": null,
  "address": {
    "streetName": "Baker Street",
    "city": "Atlanta",
    "country": "USA"
  },
  "chainLevelBilling": null,
  "bankAccounts": null
}
```

