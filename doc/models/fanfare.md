
# Fanfare

## Structure

`Fanfare`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `setupFee` | `?float` | Optional | - | getSetupFee(): ?float | setSetupFee(?float setupFee): void |
| `monthlyFee` | `?float` | Optional | - | getMonthlyFee(): ?float | setMonthlyFee(?float monthlyFee): void |
| `annualFee` | `?float` | Optional | - | getAnnualFee(): ?float | setAnnualFee(?float annualFee): void |
| `customCardUpgradeFee` | `?float` | Optional | - | getCustomCardUpgradeFee(): ?float | setCustomCardUpgradeFee(?float customCardUpgradeFee): void |
| `includedCards` | [`?FanfareCardSplits`](../../doc/models/fanfare-card-splits.md) | Optional | - | getIncludedCards(): ?FanfareCardSplits | setIncludedCards(?FanfareCardSplits includedCards): void |
| `additionalCardsType` | [`?string (AdditionalCardsTypeEnum)`](../../doc/models/additional-cards-type-enum.md) | Optional | - | getAdditionalCardsType(): ?string | setAdditionalCardsType(?string additionalCardsType): void |
| `additionalCards` | [`?FanfareCardSplits`](../../doc/models/fanfare-card-splits.md) | Optional | - | getAdditionalCards(): ?FanfareCardSplits | setAdditionalCards(?FanfareCardSplits additionalCards): void |
| `additionalCardPrice` | `?float` | Optional | - | getAdditionalCardPrice(): ?float | setAdditionalCardPrice(?float additionalCardPrice): void |
| `programCheckup` | `?float` | Optional | - | getProgramCheckup(): ?float | setProgramCheckup(?float programCheckup): void |
| `cardStyle` | `?string` | Optional | - | getCardStyle(): ?string | setCardStyle(?string cardStyle): void |
| `justificationType` | [`?string (JustificationTypeEnum)`](../../doc/models/justification-type-enum.md) | Optional | - | getJustificationType(): ?string | setJustificationType(?string justificationType): void |
| `cardIsText` | `?bool` | Optional | - | getCardIsText(): ?bool | setCardIsText(?bool cardIsText): void |
| `cardText` | `?string` | Optional | - | getCardText(): ?string | setCardText(?string cardText): void |
| `textCaseType` | [`?string (TextCaseTypeEnum)`](../../doc/models/text-case-type-enum.md) | Optional | - | getTextCaseType(): ?string | setTextCaseType(?string textCaseType): void |
| `textColor` | `?string` | Optional | - | getTextColor(): ?string | setTextColor(?string textColor): void |
| `textFont` | `?string` | Optional | - | getTextFont(): ?string | setTextFont(?string textFont): void |

## Example (as JSON)

```json
{
  "setupFee": null,
  "monthlyFee": null,
  "annualFee": null,
  "customCardUpgradeFee": null,
  "includedCards": null,
  "additionalCardsType": null,
  "additionalCards": null,
  "additionalCardPrice": null,
  "programCheckup": null,
  "cardStyle": null,
  "justificationType": null,
  "cardIsText": null,
  "cardText": null,
  "textCaseType": null,
  "textColor": null,
  "textFont": null
}
```

