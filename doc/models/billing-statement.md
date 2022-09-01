
# Billing Statement

## Structure

`BillingStatement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type2Enum`](../../doc/models/type-2-enum.md) | Required | Billing statement format type |
| `media` | [`MediaEnum`](../../doc/models/media-enum.md) | Required | Billing statement media type |
| `address_type` | [`AddressTypeEnum`](../../doc/models/address-type-enum.md) | Optional | [NA] Billing statement address, required should type and media indicate a mailed form |
| `email_address` | `string` | Optional | [EU] Billing statement email address, required should type and media indicate an emailed form |
| `frequency` | [`Frequency1Enum`](../../doc/models/frequency-1-enum.md) | Optional | [EU] Frequency at which statement is provided |

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

