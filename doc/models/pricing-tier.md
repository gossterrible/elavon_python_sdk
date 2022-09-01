
# Pricing Tier

The pricing tier describes any discount rates or discounts per item that should apply to the card product

## Structure

`PricingTier`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `discountRate` | `float` | Required | Card discount rate/fee percentage | getDiscountRate(): float | setDiscountRate(float discountRate): void |
| `discountPerItem` | `float` | Required | Card discount per item/per transaction fee | getDiscountPerItem(): float | setDiscountPerItem(float discountPerItem): void |

## Example (as JSON)

```json
{
  "discountRate": 2,
  "discountPerItem": 0.2
}
```

