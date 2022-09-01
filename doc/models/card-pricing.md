
# Card Pricing

## Structure

`CardPricing`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `pricingMethod` | [`string (PricingMethodEnum)`](../../doc/models/pricing-method-enum.md) | Required | Method of card pricing to be applied | getPricingMethod(): string | setPricingMethod(string pricingMethod): void |
| `pricingCategory` | [`string (PricingCategoryEnum)`](../../doc/models/pricing-category-enum.md) | Required | Business card pricing category | getPricingCategory(): string | setPricingCategory(string pricingCategory): void |
| `amexAcceptingInfo` | [`?AmexAcceptingInfo`](../../doc/models/amex-accepting-info.md) | Optional | - | getAmexAcceptingInfo(): ?AmexAcceptingInfo | setAmexAcceptingInfo(?AmexAcceptingInfo amexAcceptingInfo): void |
| `paymentFacilitatorInfo` | [`?PaymentFacilitatorInfo`](../../doc/models/payment-facilitator-info.md) | Optional | - | getPaymentFacilitatorInfo(): ?PaymentFacilitatorInfo | setPaymentFacilitatorInfo(?PaymentFacilitatorInfo paymentFacilitatorInfo): void |
| `cardCharges` | [`CardCharge[]`](../../doc/models/card-charge.md) | Required | Card charge listing | getCardCharges(): array | setCardCharges(array cardCharges): void |
| `exceptionCharges` | [`?(ExceptionCharge[])`](../../doc/models/exception-charge.md) | Optional | [EU] Card exception charge listing | getExceptionCharges(): ?array | setExceptionCharges(?array exceptionCharges): void |
| `debitPricing` | [`?DebitPricing`](../../doc/models/debit-pricing.md) | Optional | - | getDebitPricing(): ?DebitPricing | setDebitPricing(?DebitPricing debitPricing): void |

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

