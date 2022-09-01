
# Fanfare

## Structure

`Fanfare`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `setup_fee` | `float` | Optional | - |
| `monthly_fee` | `float` | Optional | - |
| `annual_fee` | `float` | Optional | - |
| `custom_card_upgrade_fee` | `float` | Optional | - |
| `included_cards` | [`FanfareCardSplits`](../../doc/models/fanfare-card-splits.md) | Optional | - |
| `additional_cards_type` | [`AdditionalCardsTypeEnum`](../../doc/models/additional-cards-type-enum.md) | Optional | - |
| `additional_cards` | [`FanfareCardSplits`](../../doc/models/fanfare-card-splits.md) | Optional | - |
| `additional_card_price` | `float` | Optional | - |
| `program_checkup` | `float` | Optional | - |
| `card_style` | `string` | Optional | - |
| `justification_type` | [`JustificationTypeEnum`](../../doc/models/justification-type-enum.md) | Optional | - |
| `card_is_text` | `bool` | Optional | - |
| `card_text` | `string` | Optional | - |
| `text_case_type` | [`TextCaseTypeEnum`](../../doc/models/text-case-type-enum.md) | Optional | - |
| `text_color` | `string` | Optional | - |
| `text_font` | `string` | Optional | - |

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

