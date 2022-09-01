
# Company Contact Info

## Structure

`CompanyContactInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `telephone` | `?string` | Optional | - | getTelephone(): ?string | setTelephone(?string telephone): void |
| `emailAddresses` | `?(string[])` | Optional | - | getEmailAddresses(): ?array | setEmailAddresses(?array emailAddresses): void |
| `webPages` | `?(string[])` | Optional | - | getWebPages(): ?array | setWebPages(?array webPages): void |
| `address` | [`?AddressFields`](../../doc/models/address-fields.md) | Optional | - | getAddress(): ?AddressFields | setAddress(?AddressFields address): void |
| `phoneFields` | [`?PhoneFields`](../../doc/models/phone-fields.md) | Optional | - | getPhoneFields(): ?PhoneFields | setPhoneFields(?PhoneFields phoneFields): void |

## Example (as JSON)

```json
{
  "telephone": null,
  "emailAddresses": null,
  "webPages": null,
  "address": null,
  "phoneFields": null
}
```

