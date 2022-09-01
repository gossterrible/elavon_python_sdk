
# List Documents Request

## Structure

`ListDocumentsRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `equipmentInfo` | [`?EquipmentInfo`](../../doc/models/equipment-info.md) | Optional | In NA, it's mandatory to have at least one piece of equipment. For third party vendors<br>managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.<br>Contact your Elavon representative for the VAR code(s).<br><br>          In EU, equipmentInfo is optional and no equipment has to be sent. If you have any equipment <br>          managed by Elavon, contact your Elavon representative for the VAR code(s). | getEquipmentInfo(): ?EquipmentInfo | setEquipmentInfo(?EquipmentInfo equipmentInfo): void |
| `cardPricing` | [`?CardPricing`](../../doc/models/card-pricing.md) | Optional | - | getCardPricing(): ?CardPricing | setCardPricing(?CardPricing cardPricing): void |
| `principal` | [`?Person`](../../doc/models/person.md) | Optional | - | getPrincipal(): ?Person | setPrincipal(?Person principal): void |
| `businessInfo` | [`?BusinessInfo`](../../doc/models/business-info.md) | Optional | - | getBusinessInfo(): ?BusinessInfo | setBusinessInfo(?BusinessInfo businessInfo): void |
| `bankAccounts` | [`?array<string,BankingInfo>`](../../doc/models/banking-info.md) | Optional | - | getBankAccounts(): ?array | setBankAccounts(?array bankAccounts): void |
| `directDebitAuthorizedMap` | `?array<string,bool>` | Optional | - | getDirectDebitAuthorizedMap(): ?array | setDirectDebitAuthorizedMap(?array directDebitAuthorizedMap): void |
| `valueAdds` | `?array<string,bool>` | Optional | - | getValueAdds(): ?array | setValueAdds(?array valueAdds): void |
| `profileCode` | `?string` | Optional | - | getProfileCode(): ?string | setProfileCode(?string profileCode): void |
| `hasGovernmentIncentive` | `?bool` | Optional | - | getHasGovernmentIncentive(): ?bool | setHasGovernmentIncentive(?bool hasGovernmentIncentive): void |
| `hasCustomNotes` | `?bool` | Optional | - | getHasCustomNotes(): ?bool | setHasCustomNotes(?bool hasCustomNotes): void |
| `partnerDocumentKeys` | `?(string[])` | Optional | **Constraints**: *Unique Items Required* | getPartnerDocumentKeys(): ?array | setPartnerDocumentKeys(?array partnerDocumentKeys): void |

## Example (as JSON)

```json
{
  "equipmentInfo": null,
  "cardPricing": null,
  "principal": null,
  "businessInfo": null,
  "bankAccounts": null,
  "directDebitAuthorizedMap": null,
  "valueAdds": null,
  "profileCode": null,
  "hasGovernmentIncentive": null,
  "hasCustomNotes": null,
  "partnerDocumentKeys": null
}
```

