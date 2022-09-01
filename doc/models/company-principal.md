
# Company Principal

## Structure

`CompanyPrincipal`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `name` | `?string` | Optional | - | getName(): ?string | setName(?string name): void |
| `gender` | `?string` | Optional | - | getGender(): ?string | setGender(?string gender): void |
| `dateOfBirth` | `?\DateTime` | Optional | - | getDateOfBirth(): ?\DateTime | setDateOfBirth(?\DateTime dateOfBirth): void |
| `address` | [`?AddressFields`](../../doc/models/address-fields.md) | Optional | - | getAddress(): ?AddressFields | setAddress(?AddressFields address): void |
| `positions` | `?(string[])` | Optional | - | getPositions(): ?array | setPositions(?array positions): void |
| `personNameFields` | [`?PersonNameFields`](../../doc/models/person-name-fields.md) | Optional | - | getPersonNameFields(): ?PersonNameFields | setPersonNameFields(?PersonNameFields personNameFields): void |
| `phoneFields` | [`?PhoneFields`](../../doc/models/phone-fields.md) | Optional | - | getPhoneFields(): ?PhoneFields | setPhoneFields(?PhoneFields phoneFields): void |
| `mobilePhoneFields` | [`?PhoneFields`](../../doc/models/phone-fields.md) | Optional | - | getMobilePhoneFields(): ?PhoneFields | setMobilePhoneFields(?PhoneFields mobilePhoneFields): void |
| `principalIdentifier` | `?string` | Optional | - | getPrincipalIdentifier(): ?string | setPrincipalIdentifier(?string principalIdentifier): void |
| `principalOwnerDetail` | [`?PrincipalOwnerDetail`](../../doc/models/principal-owner-detail.md) | Optional | - | getPrincipalOwnerDetail(): ?PrincipalOwnerDetail | setPrincipalOwnerDetail(?PrincipalOwnerDetail principalOwnerDetail): void |
| `pesel` | `?string` | Optional | - | getPesel(): ?string | setPesel(?string pesel): void |

## Example (as JSON)

```json
{
  "name": null,
  "gender": null,
  "dateOfBirth": null,
  "address": null,
  "positions": null,
  "personNameFields": null,
  "phoneFields": null,
  "mobilePhoneFields": null,
  "principalIdentifier": null,
  "principalOwnerDetail": null,
  "pesel": null
}
```

