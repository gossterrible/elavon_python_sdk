
# Fee

## Structure

`Fee`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `type` | `string` | Required | SKU of fee | getType(): string | setType(string type): void |
| `quantity` | `int` | Required | Quantity of fee | getQuantity(): int | setQuantity(int quantity): void |
| `amount` | `float` | Required | Price of fee | getAmount(): float | setAmount(float amount): void |
| `frequency` | [`string (FrequencyEnum)`](../../doc/models/frequency-enum.md) | Required | Application of fee | getFrequency(): string | setFrequency(string frequency): void |
| `startMonth` | [`?string (StartMonthEnum)`](../../doc/models/start-month-enum.md) | Optional | [NA] start month | getStartMonth(): ?string | setStartMonth(?string startMonth): void |

## Example (as JSON)

```json
{
  "type": "JOI",
  "quantity": 1,
  "amount": 9.99,
  "frequency": null
}
```

