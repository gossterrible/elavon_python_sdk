
# Card Charge

## Structure

`CardCharge`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `cardType` | [`string (CardTypeEnum)`](../../doc/models/card-type-enum.md) | Required | Type of card | getCardType(): string | setCardType(string cardType): void |
| `minimumFee` | `?float` | Optional | [EU] Minimum charge fee to be applied to card | getMinimumFee(): ?float | setMinimumFee(?float minimumFee): void |
| `authorizationFee` | `?float` | Optional | [NA] Auth fee to be applied to card | getAuthorizationFee(): ?float | setAuthorizationFee(?float authorizationFee): void |
| `seNumber` | `?string` | Optional | [NA] Service Establishment number of card<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `15` | getSeNumber(): ?string | setSeNumber(?string seNumber): void |
| `serviceType` | [`?string (ServiceTypeEnum)`](../../doc/models/service-type-enum.md) | Optional | [EU] Service level of card | getServiceType(): ?string | setServiceType(?string serviceType): void |
| `cardFunding` | [`?string (CardFundingEnum)`](../../doc/models/card-funding-enum.md) | Optional | [NA] Who is providing the funding for the card | getCardFunding(): ?string | setCardFunding(?string cardFunding): void |
| `pricingTiers` | [`?array<string,PricingTier>`](../../doc/models/pricing-tier.md) | Optional | - | getPricingTiers(): ?array | setPricingTiers(?array pricingTiers): void |

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

