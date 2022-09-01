
# Card Volume

## Structure

`CardVolume`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `visa_percentage` | `string` | Required | Percentage of Visa transactions as a percentage of Annual Revenue |
| `master_card_percentage` | `string` | Required | Percentage of MasterCard transactions as a percentage of Annual Revenue |
| `amex_percentage` | `string` | Required | Percentage of Amex OptBlue transactions as a percentage of Annual Revenue |
| `amex_average_transaction` | `string` | Required | Average transaction amount for an Amercian Express OptBlue transaction |
| `interac_average_transaction` | `string` | Required | Average transaction amount for an Interac debit transaction |

## Example (as JSON)

```json
{
  "visaPercentage": "15.6",
  "masterCardPercentage": "12.3",
  "amexPercentage": "4.5",
  "amexAverageTransaction": "10.1",
  "interacAverageTransaction": "23.4"
}
```

