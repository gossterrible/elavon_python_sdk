
# Chain Info

## Structure

`ChainInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chain_number` | `string` | Required | Name of new chain to be set up<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `7` |
| `chain_name` | `string` | Required | Number of new chain to be set up |
| `send_statement_to_address` | [`SendStatementToAddressEnum`](../../doc/models/send-statement-to-address-enum.md) | Required | Address that the new chain's statements will be sent to |
| `statement_media` | [`StatementMediaEnum`](../../doc/models/statement-media-enum.md) | Required | Media type of chain's statements |
| `address` | [`Address`](../../doc/models/address.md) | Required | - |
| `chain_level_billing` | `bool` | Required | Billing level of new chain |
| `bank_accounts` | [`dict`](../../doc/models/banking-info.md) | Required | Chain's bank account information. The valid keys are as follows: BILLING, DEPOSIT, LEASE, CHARGEBACK |

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

