
# Equipment Item

## Structure

`EquipmentItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Required | SKU of product |
| `quantity` | `int` | Required | Number of product being chosen |
| `pricing_items` | [`List of EquipmentPricing`](../../doc/models/equipment-pricing.md) | Required | Product pricinging listing |
| `item_settings` | [`ItemSettings`](../../doc/models/item-settings.md) | Optional | - |
| `exception_items` | [`List of ExceptionItem`](../../doc/models/exception-item.md) | Optional | [EU] Exception pricing to be sent for equipment pricing |
| `service_fee` | `float` | Optional | - |
| `trx_free_month` | `int` | Required | Free transaction per month per terminal |
| `future_effective_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |

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

