
# Billing Statement

## Structure

`BillingStatement`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `type` | [`string (Type2Enum)`](../../doc/models/type-2-enum.md) | Required | Billing statement format type | getType(): string | setType(string type): void |
| `media` | [`string (MediaEnum)`](../../doc/models/media-enum.md) | Required | Billing statement media type | getMedia(): string | setMedia(string media): void |
| `addressType` | [`?string (AddressTypeEnum)`](../../doc/models/address-type-enum.md) | Optional | [NA] Billing statement address, required should type and media indicate a mailed form | getAddressType(): ?string | setAddressType(?string addressType): void |
| `emailAddress` | `?string` | Optional | [EU] Billing statement email address, required should type and media indicate an emailed form | getEmailAddress(): ?string | setEmailAddress(?string emailAddress): void |
| `frequency` | [`?string (Frequency1Enum)`](../../doc/models/frequency-1-enum.md) | Optional | [EU] Frequency at which statement is provided | getFrequency(): ?string | setFrequency(?string frequency): void |

## Example (as JSON)

```json
{
  "type": "FIXED_BANK_COMPLEX_WITH_RECAP",
  "media": "EMAIL",
  "addressType": null,
  "emailAddress": null,
  "frequency": null
}
```

