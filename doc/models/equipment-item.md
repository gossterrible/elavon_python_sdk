
# Equipment Item

## Structure

`EquipmentItem`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `code` | `string` | Required | SKU of product | getCode(): string | setCode(string code): void |
| `quantity` | `int` | Required | Number of product being chosen | getQuantity(): int | setQuantity(int quantity): void |
| `pricingItems` | [`EquipmentPricing[]`](../../doc/models/equipment-pricing.md) | Required | Product pricinging listing | getPricingItems(): array | setPricingItems(array pricingItems): void |
| `itemSettings` | [`?ItemSettings`](../../doc/models/item-settings.md) | Optional | - | getItemSettings(): ?ItemSettings | setItemSettings(?ItemSettings itemSettings): void |
| `exceptionItems` | [`?(ExceptionItem[])`](../../doc/models/exception-item.md) | Optional | [EU] Exception pricing to be sent for equipment pricing | getExceptionItems(): ?array | setExceptionItems(?array exceptionItems): void |
| `serviceFee` | `?float` | Optional | - | getServiceFee(): ?float | setServiceFee(?float serviceFee): void |
| `trxFreeMonth` | `int` | Required | Free transaction per month per terminal | getTrxFreeMonth(): int | setTrxFreeMonth(int trxFreeMonth): void |
| `futureEffectiveDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getFutureEffectiveDate(): ?DateComponents | setFutureEffectiveDate(?DateComponents futureEffectiveDate): void |

## Example (as JSON)

```json
{
  "code": "310T3",
  "quantity": 2,
  "pricingItems": {
    "amount": 200
  },
  "trxFreeMonth": null
}
```

