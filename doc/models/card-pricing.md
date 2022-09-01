
# Card Pricing

## Structure

`CardPricing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_method` | [`PricingMethodEnum`](../../doc/models/pricing-method-enum.md) | Required | Method of card pricing to be applied |
| `pricing_category` | [`PricingCategoryEnum`](../../doc/models/pricing-category-enum.md) | Required | Business card pricing category |
| `amex_accepting_info` | [`AmexAcceptingInfo`](../../doc/models/amex-accepting-info.md) | Optional | - |
| `payment_facilitator_info` | [`PaymentFacilitatorInfo`](../../doc/models/payment-facilitator-info.md) | Optional | - |
| `card_charges` | [`List of CardCharge`](../../doc/models/card-charge.md) | Required | Card charge listing |
| `exception_charges` | [`List of ExceptionCharge`](../../doc/models/exception-charge.md) | Optional | [EU] Card exception charge listing |
| `debit_pricing` | [`DebitPricing`](../../doc/models/debit-pricing.md) | Optional | - |

## Example (as JSON)

```json
{
  "pricingMethod": "ENHANCED_INTERCHANGE_PLUS",
  "pricingCategory": "RETAIL",
  "amexAcceptingInfo": null,
  "paymentFacilitatorInfo": null,
  "cardCharges": [
    {
      "cardType": "DOMESTIC_CREDIT",
      "minimumFee": null,
      "authorizationFee": null,
      "seNumber": null,
      "serviceType": null,
      "cardFunding": null,
      "pricingTiers": null
    },
    {
      "cardType": "DOMESTIC_DEBIT",
      "minimumFee": null,
      "authorizationFee": null,
      "seNumber": null,
      "serviceType": null,
      "cardFunding": null,
      "pricingTiers": null
    }
  ],
  "exceptionCharges": null,
  "debitPricing": null
}
```

