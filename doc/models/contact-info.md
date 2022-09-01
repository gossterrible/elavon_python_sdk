
# Contact Info

## Structure

`ContactInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address`](../../doc/models/address.md) | Optional | - |
| `additional_addresses` | [`dict`](../../doc/models/address.md) | Optional | Contact's additional addresses. The valid keys are as follows: PREVIOUS |
| `phone` | [`PhoneNumber`](../../doc/models/phone-number.md) | Optional | - |
| `mobile` | [`PhoneNumber`](../../doc/models/phone-number.md) | Optional | - |
| `fax` | [`PhoneNumber`](../../doc/models/phone-number.md) | Optional | - |
| `email_address` | `string` | Optional | Contact's email address |

## Example (as JSON)

```json
{
  "address": null,
  "additionalAddresses": null,
  "phone": null,
  "mobile": null,
  "fax": null,
  "emailAddress": null
}
```

