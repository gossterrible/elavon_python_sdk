
# Additional Card Pricing Info

## Structure

`AdditionalCardPricingInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `minimumCardFee` | `?float` | Optional | Minimum charge fee to be applied to card | getMinimumCardFee(): ?float | setMinimumCardFee(?float minimumCardFee): void |
| `clearAndSimpleType` | `?string` | Optional | The type of the clear and simple plan | getClearAndSimpleType(): ?string | setClearAndSimpleType(?string clearAndSimpleType): void |
| `c4PricingType` | `?string` | Optional | The type of the C4 pricing plan | getC4PricingType(): ?string | setC4PricingType(?string c4PricingType): void |
| `highRiskCostAdditionalLoading` | `?string` | Optional | Risk loading percentage as it relates to Simplified MSC | getHighRiskCostAdditionalLoading(): ?string | setHighRiskCostAdditionalLoading(?string highRiskCostAdditionalLoading): void |

## Example (as JSON)

```json
{
  "minimumCardFee": null,
  "clearAndSimpleType": null,
  "c4PricingType": null,
  "highRiskCostAdditionalLoading": null
}
```

