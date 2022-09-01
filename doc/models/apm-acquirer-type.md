
# Apm Acquirer Type

## Structure

`ApmAcquirerType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type_code` | `string` | Required | Acquirer Type Code of the Alternative Payment Method Type |
| `per_item_amount` | `string` | Required | Default Per Item Amount of the Alternative Payment Method Type |
| `rate_percentage` | `string` | Required | Default Rate Percentage of the Alternative Payment Method Type |
| `pricing_tiers` | [`List of ApmPricingTier`](../../doc/models/apm-pricing-tier.md) | Required | Pricing of the Alternative Payment Method |

## Example (as JSON)

```json
{
  "typeCode": "typeCode4",
  "perItemAmount": "perItemAmount8",
  "ratePercentage": "ratePercentage6",
  "pricingTiers": [
    {
      "combiningCode": "combiningCode2",
      "perItemAmount": "perItemAmount8",
      "ratePercentage": "ratePercentage6",
      "description": "description0"
    },
    {
      "combiningCode": "combiningCode3",
      "perItemAmount": "perItemAmount9",
      "ratePercentage": "ratePercentage7",
      "description": "description9"
    },
    {
      "combiningCode": "combiningCode4",
      "perItemAmount": "perItemAmount0",
      "ratePercentage": "ratePercentage8",
      "description": "description8"
    }
  ]
}
```

