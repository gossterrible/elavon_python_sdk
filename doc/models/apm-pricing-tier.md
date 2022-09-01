
# Apm Pricing Tier

## Structure

`ApmPricingTier`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `combiningCode` | `string` | Required | Combining Code of the Alternative Payment Method | getCombiningCode(): string | setCombiningCode(string combiningCode): void |
| `perItemAmount` | `string` | Required | Default Per Item Amount of the Alternative Payment Method | getPerItemAmount(): string | setPerItemAmount(string perItemAmount): void |
| `ratePercentage` | `string` | Required | Default Rate Percentage of the Alternative Payment Method | getRatePercentage(): string | setRatePercentage(string ratePercentage): void |
| `description` | `string` | Required | Long name of the combining code of the Alternative Payment Method | getDescription(): string | setDescription(string description): void |

## Example (as JSON)

```json
{
  "combiningCode": "combiningCode8",
  "perItemAmount": "perItemAmount8",
  "ratePercentage": "ratePercentage6",
  "description": "description0"
}
```

