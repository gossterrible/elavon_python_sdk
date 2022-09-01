
# Electronic Statement

## Structure

`ElectronicStatement`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `type` | [`string (Type4Enum)`](../../doc/models/type-4-enum.md) | Required | Electronic statement format type | getType(): string | setType(string type): void |
| `media` | [`string (Media2Enum)`](../../doc/models/media-2-enum.md) | Required | Electronic statement media type | getMedia(): string | setMedia(string media): void |
| `emailAddress` | `?string` | Optional | Email address of statement | getEmailAddress(): ?string | setEmailAddress(?string emailAddress): void |
| `frequency` | [`?string (Frequency3Enum)`](../../doc/models/frequency-3-enum.md) | Optional | Frequency at which statement is provided | getFrequency(): ?string | setFrequency(?string frequency): void |

## Example (as JSON)

```json
{
  "type": "FIXED_BANK_COMPLEX_WITH_RECAP",
  "media": "EMAIL",
  "emailAddress": null,
  "frequency": null
}
```

