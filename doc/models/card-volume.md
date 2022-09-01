
# Card Volume

## Structure

`CardVolume`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `visaPercentage` | `string` | Required | Percentage of Visa transactions as a percentage of Annual Revenue | getVisaPercentage(): string | setVisaPercentage(string visaPercentage): void |
| `masterCardPercentage` | `string` | Required | Percentage of MasterCard transactions as a percentage of Annual Revenue | getMasterCardPercentage(): string | setMasterCardPercentage(string masterCardPercentage): void |
| `amexPercentage` | `string` | Required | Percentage of Amex OptBlue transactions as a percentage of Annual Revenue | getAmexPercentage(): string | setAmexPercentage(string amexPercentage): void |
| `amexAverageTransaction` | `string` | Required | Average transaction amount for an Amercian Express OptBlue transaction | getAmexAverageTransaction(): string | setAmexAverageTransaction(string amexAverageTransaction): void |
| `interacAverageTransaction` | `string` | Required | Average transaction amount for an Interac debit transaction | getInteracAverageTransaction(): string | setInteracAverageTransaction(string interacAverageTransaction): void |

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

