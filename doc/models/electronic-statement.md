
# Electronic Statement

## Structure

`ElectronicStatement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type4Enum`](../../doc/models/type-4-enum.md) | Required | Electronic statement format type |
| `media` | [`Media2Enum`](../../doc/models/media-2-enum.md) | Required | Electronic statement media type |
| `email_address` | `string` | Optional | Email address of statement |
| `frequency` | [`Frequency3Enum`](../../doc/models/frequency-3-enum.md) | Optional | Frequency at which statement is provided |

## Example (as JSON)

```json
{
  "type": "FIXED_BANK_COMPLEX_WITH_RECAP",
  "media": "EMAIL",
  "emailAddress": null,
  "frequency": null
}
```

