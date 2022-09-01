
# Card Charge

## Structure

`CardCharge`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_type` | [`CardTypeEnum`](../../doc/models/card-type-enum.md) | Required | Type of card |
| `minimum_fee` | `float` | Optional | [EU] Minimum charge fee to be applied to card |
| `authorization_fee` | `float` | Optional | [NA] Auth fee to be applied to card |
| `se_number` | `string` | Optional | [NA] Service Establishment number of card<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `15` |
| `service_type` | [`ServiceTypeEnum`](../../doc/models/service-type-enum.md) | Optional | [EU] Service level of card |
| `card_funding` | [`CardFundingEnum`](../../doc/models/card-funding-enum.md) | Optional | [NA] Who is providing the funding for the card |
| `pricing_tiers` | [`dict`](../../doc/models/pricing-tier.md) | Optional | - |

## Example (as JSON)

```json
{
  "cardType": "SOLO",
  "minimumFee": null,
  "authorizationFee": null,
  "seNumber": null,
  "serviceType": null,
  "cardFunding": null,
  "pricingTiers": null
}
```

