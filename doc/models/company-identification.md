
# Company Identification

## Structure

`CompanyIdentification`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `businessName` | `?string` | Optional | - | getBusinessName(): ?string | setBusinessName(?string businessName): void |
| `registeredCompanyName` | `?string` | Optional | - | getRegisteredCompanyName(): ?string | setRegisteredCompanyName(?string registeredCompanyName): void |
| `country` | `?string` | Optional | - | getCountry(): ?string | setCountry(?string country): void |
| `countryCode` | `?string` | Optional | - | getCountryCode(): ?string | setCountryCode(?string countryCode): void |
| `companyRegistrationNumber` | `?string` | Optional | - | getCompanyRegistrationNumber(): ?string | setCompanyRegistrationNumber(?string companyRegistrationNumber): void |
| `vatRegistrationNumber` | `?string` | Optional | - | getVatRegistrationNumber(): ?string | setVatRegistrationNumber(?string vatRegistrationNumber): void |
| `dateOfCompanyRegistration` | `?\DateTime` | Optional | - | getDateOfCompanyRegistration(): ?\DateTime | setDateOfCompanyRegistration(?\DateTime dateOfCompanyRegistration): void |
| `dateOfStartingOperation` | `?\DateTime` | Optional | - | getDateOfStartingOperation(): ?\DateTime | setDateOfStartingOperation(?\DateTime dateOfStartingOperation): void |
| `contactAddress` | [`?AddressFields`](../../doc/models/address-fields.md) | Optional | - | getContactAddress(): ?AddressFields | setContactAddress(?AddressFields contactAddress): void |
| `ownerType` | `?string` | Optional | - | getOwnerType(): ?string | setOwnerType(?string ownerType): void |
| `taxIdType` | `?string` | Optional | - | getTaxIdType(): ?string | setTaxIdType(?string taxIdType): void |
| `taxIdNumber` | `?string` | Optional | - | getTaxIdNumber(): ?string | setTaxIdNumber(?string taxIdNumber): void |
| `fedTaxId` | `?string` | Optional | - | getFedTaxId(): ?string | setFedTaxId(?string fedTaxId): void |
| `certificationDate` | `?\DateTime` | Optional | - | getCertificationDate(): ?\DateTime | setCertificationDate(?\DateTime certificationDate): void |
| `customerCentricFlag` | `?bool` | Optional | - | getCustomerCentricFlag(): ?bool | setCustomerCentricFlag(?bool customerCentricFlag): void |
| `mid` | `?string` | Optional | - | getMid(): ?string | setMid(?string mid): void |

## Example (as JSON)

```json
{
  "businessName": null,
  "registeredCompanyName": null,
  "country": null,
  "countryCode": null,
  "companyRegistrationNumber": null,
  "vatRegistrationNumber": null,
  "dateOfCompanyRegistration": null,
  "dateOfStartingOperation": null,
  "contactAddress": null,
  "ownerType": null,
  "taxIdType": null,
  "taxIdNumber": null,
  "fedTaxId": null,
  "certificationDate": null,
  "customerCentricFlag": null,
  "mid": null
}
```

