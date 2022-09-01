
# Funding Statement

## Structure

`FundingStatement`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `type` | [`?string (Type3Enum)`](../../doc/models/type-3-enum.md) | Optional | - | getType(): ?string | setType(?string type): void |
| `media` | [`?string (Media1Enum)`](../../doc/models/media-1-enum.md) | Optional | - | getMedia(): ?string | setMedia(?string media): void |
| `emailAddress` | `?string` | Optional | [EU] email address | getEmailAddress(): ?string | setEmailAddress(?string emailAddress): void |
| `frequency` | [`?string (Frequency2Enum)`](../../doc/models/frequency-2-enum.md) | Optional | [EU] DAILY, WEEKLY, MONTHLY | getFrequency(): ?string | setFrequency(?string frequency): void |

## Example (as JSON)

```json
{
  "type": null,
  "media": null,
  "emailAddress": null,
  "frequency": null
}
```

