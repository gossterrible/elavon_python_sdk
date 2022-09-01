
# Date Components

A container that holds the date (day, month, and year)

## Structure

`DateComponents`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `year` | `?int` | Optional | - | getYear(): ?int | setYear(?int year): void |
| `month` | [`?string (MonthEnum)`](../../doc/models/month-enum.md) | Optional | - | getMonth(): ?string | setMonth(?string month): void |
| `day` | `?int` | Optional | - | getDay(): ?int | setDay(?int day): void |

## Example (as JSON)

```json
{
  "year": null,
  "month": null,
  "day": null
}
```

