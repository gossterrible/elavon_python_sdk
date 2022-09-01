
# Pricing Tier

The pricing tier describes any discount rates or discounts per item that should apply to the card product

## Structure

`PricingTier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `discount_rate` | `float` | Required | Card discount rate/fee percentage |
| `discount_per_item` | `float` | Required | Card discount per item/per transaction fee |

## Example (as JSON)

```json
{
  "discountRate": 2,
  "discountPerItem": 0.2
}
```

