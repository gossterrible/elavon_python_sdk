
# Debit Pricing

## Structure

`DebitPricing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_method` | [`PricingMethod1Enum`](../../doc/models/pricing-method-1-enum.md) | Required | Debit network pricing method |
| `authorization_method` | [`AuthorizationMethodEnum`](../../doc/models/authorization-method-enum.md) | Required | Debit network authorization method |
| `surcharge_amount` | `float` | Optional | Debit surcharge amount |
| `surcharge_percent` | `string` | Optional | Debit surcharge percentage |
| `debit_network_charges` | [`List of DebitNetworkCharge`](../../doc/models/debit-network-charge.md) | Required | Debit network charges listing |
| `pinless_setup` | `bool` | Optional | Debit pinless setup |

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

