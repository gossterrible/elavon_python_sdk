
# Amex Accepting Info

## Structure

`AmexAcceptingInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `amexMonthlyCardSales` | `?float` | Optional | - | getAmexMonthlyCardSales(): ?float | setAmexMonthlyCardSales(?float amexMonthlyCardSales): void |
| `isExisting` | `?bool` | Optional | Flag indicating if AMEX account already present for customer | getIsExisting(): ?bool | setIsExisting(?bool isExisting): void |
| `amexMid` | `?string` | Optional | [EU] Field for Girocard + International Schemes and International Schemes Only | getAmexMid(): ?string | setAmexMid(?string amexMid): void |

## Example (as JSON)

```json
{
  "amexMonthlyCardSales": null,
  "isExisting": null,
  "amexMid": null
}
```

