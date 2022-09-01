
# Dynamic Currency Conversion

## Structure

`DynamicCurrencyConversion`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `rebatePercent` | `float` | Required | DCC rebate percentage | getRebatePercent(): float | setRebatePercent(float rebatePercent): void |
| `markUp` | [`string (MarkUpEnum)`](../../doc/models/mark-up-enum.md) | Required | DCC markup type. An enum's numerical value usually matches their name, but with an exception: THREE_POINT_TWO_FIVE = 2.85 | getMarkUp(): string | setMarkUp(string markUp): void |
| `currencyGroup` | [`?string (CurrencyGroupEnum)`](../../doc/models/currency-group-enum.md) | Optional | [NA] DCC currency group | getCurrencyGroup(): ?string | setCurrencyGroup(?string currencyGroup): void |
| `registrationFee` | `?float` | Optional | [NA] DCC registration fee | getRegistrationFee(): ?float | setRegistrationFee(?float registrationFee): void |

## Example (as JSON)

```json
{
  "rebatePercent": 0.5,
  "markUp": null
}
```

