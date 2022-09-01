
# Debit Pricing

## Structure

`DebitPricing`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `pricingMethod` | [`string (PricingMethod1Enum)`](../../doc/models/pricing-method-1-enum.md) | Required | Debit network pricing method | getPricingMethod(): string | setPricingMethod(string pricingMethod): void |
| `authorizationMethod` | [`string (AuthorizationMethodEnum)`](../../doc/models/authorization-method-enum.md) | Required | Debit network authorization method | getAuthorizationMethod(): string | setAuthorizationMethod(string authorizationMethod): void |
| `surchargeAmount` | `?float` | Optional | Debit surcharge amount | getSurchargeAmount(): ?float | setSurchargeAmount(?float surchargeAmount): void |
| `surchargePercent` | `?string` | Optional | Debit surcharge percentage | getSurchargePercent(): ?string | setSurchargePercent(?string surchargePercent): void |
| `debitNetworkCharges` | [`DebitNetworkCharge[]`](../../doc/models/debit-network-charge.md) | Required | Debit network charges listing | getDebitNetworkCharges(): array | setDebitNetworkCharges(array debitNetworkCharges): void |
| `pinlessSetup` | `?bool` | Optional | Debit pinless setup | getPinlessSetup(): ?bool | setPinlessSetup(?bool pinlessSetup): void |

## Example (as JSON)

```json
{
  "pricingMethod": "FIXED",
  "authorizationMethod": "NONE",
  "surchargeAmount": null,
  "surchargePercent": null,
  "debitNetworkCharges": [
    {
      "type": null,
      "discountRate": null,
      "discountPerItem": null,
      "perAuth": null
    },
    {
      "type": null,
      "discountRate": null,
      "discountPerItem": null,
      "perAuth": null
    }
  ],
  "pinlessSetup": null
}
```

