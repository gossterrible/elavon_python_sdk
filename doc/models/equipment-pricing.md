
# Equipment Pricing

## Structure

`EquipmentPricing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `float` | Required | The cost of the equipment |
| `purchase_type` | [`PurchaseTypeEnum`](../../doc/models/purchase-type-enum.md) | Optional | - |
| `lease_term` | `int` | Optional | - |
| `vendor_code` | `int` | Optional | - |
| `vendor_plan` | `string` | Optional | - |
| `start_month` | [`StartMonth1Enum`](../../doc/models/start-month-1-enum.md) | Optional | - |
| `start_year` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "amount": 200
}
```

