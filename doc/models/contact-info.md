
# Contact Info

## Structure

`ContactInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `address` | [`?Address`](../../doc/models/address.md) | Optional | - | getAddress(): ?Address | setAddress(?Address address): void |
| `additionalAddresses` | [`?array<string,Address>`](../../doc/models/address.md) | Optional | Contact's additional addresses. The valid keys are as follows: PREVIOUS | getAdditionalAddresses(): ?array | setAdditionalAddresses(?array additionalAddresses): void |
| `phone` | [`?PhoneNumber`](../../doc/models/phone-number.md) | Optional | - | getPhone(): ?PhoneNumber | setPhone(?PhoneNumber phone): void |
| `mobile` | [`?PhoneNumber`](../../doc/models/phone-number.md) | Optional | - | getMobile(): ?PhoneNumber | setMobile(?PhoneNumber mobile): void |
| `fax` | [`?PhoneNumber`](../../doc/models/phone-number.md) | Optional | - | getFax(): ?PhoneNumber | setFax(?PhoneNumber fax): void |
| `emailAddress` | `?string` | Optional | Contact's email address | getEmailAddress(): ?string | setEmailAddress(?string emailAddress): void |

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

