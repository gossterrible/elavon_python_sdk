
# Person

## Structure

`Person`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `name` | [`Name`](../../doc/models/name.md) | Required | - | getName(): Name | setName(Name name): void |
| `contactInfo` | [`?ContactInfo`](../../doc/models/contact-info.md) | Optional | - | getContactInfo(): ?ContactInfo | setContactInfo(?ContactInfo contactInfo): void |
| `dob` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getDob(): ?DateComponents | setDob(?DateComponents dob): void |
| `positions` | `array<string,bool>` | Required | Boolean map representing positions of person, if position applies true should be value given for position key. The valid keys are as follows: OFFICER, PARTNER, DIRECTOR, OWNER, SECRETARY, OTHER, BENEFICIAL_OWNER, AUTHORIZED_SIGNER, SOLE_PROP | getPositions(): array | setPositions(array positions): void |
| `ownershipPct` | `?string` | Optional | Ownership percentage of person | getOwnershipPct(): ?string | setOwnershipPct(?string ownershipPct): void |
| `ids` | [`?(Identification[])`](../../doc/models/identification.md) | Optional | Id listing of person | getIds(): ?array | setIds(?array ids): void |
| `titleType` | [`?string (TitleTypeEnum)`](../../doc/models/title-type-enum.md) | Optional | [NA] Title type of person | getTitleType(): ?string | setTitleType(?string titleType): void |
| `title` | `?string` | Optional | Free text of person's title, should title type not provide correct option (NA OTHER)<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `32` | getTitle(): ?string | setTitle(?string title): void |
| `signingPersonalGuarantee` | `?bool` | Optional | [NA] Flag indicating if person is signing personal gurantee, true if YES, false if NO | getSigningPersonalGuarantee(): ?bool | setSigningPersonalGuarantee(?bool signingPersonalGuarantee): void |
| `responsibleParty` | `?bool` | Optional | Flag indicating if person is a responsible party of the business, true if YES, false if NO | getResponsibleParty(): ?bool | setResponsibleParty(?bool responsibleParty): void |
| `relatedParty` | `?bool` | Optional | Flag indicating if person is a related party of the business, true if YES, false if NO | getRelatedParty(): ?bool | setRelatedParty(?bool relatedParty): void |
| `residingCountry` | `?string` | Optional | Current country of residence of person, ISO 3166-1 alpha-3 standard applies | getResidingCountry(): ?string | setResidingCountry(?string residingCountry): void |
| `primaryNationality` | `?string` | Optional | Primary citizenship/nationality of person, ISO 3166-1 alpha-3 standard applies | getPrimaryNationality(): ?string | setPrimaryNationality(?string primaryNationality): void |
| `secondaryNationality` | `?string` | Optional | Secondary citizenship/nationality of person, ISO 3166-1 alpha-3 standard applies | getSecondaryNationality(): ?string | setSecondaryNationality(?string secondaryNationality): void |
| `documentaryInfo` | [`?DocumentaryInfo`](../../doc/models/documentary-info.md) | Optional | - | getDocumentaryInfo(): ?DocumentaryInfo | setDocumentaryInfo(?DocumentaryInfo documentaryInfo): void |
| `alternateAddressInfo` | [`?AlternateAddressInfo`](../../doc/models/alternate-address-info.md) | Optional | Used to hold information about an alternative business address | getAlternateAddressInfo(): ?AlternateAddressInfo | setAlternateAddressInfo(?AlternateAddressInfo alternateAddressInfo): void |
| `isNewOwner` | `?bool` | Optional | [EU] Flag indicating if person is a new owner of the buisness, true if YES, false if NO | getIsNewOwner(): ?bool | setIsNewOwner(?bool isNewOwner): void |
| `directionalOwnershipType` | [`?string (DirectionalOwnershipTypeEnum)`](../../doc/models/directional-ownership-type-enum.md) | Optional | [EU] Indicator if person has direct or indirect ownership of business | getDirectionalOwnershipType(): ?string | setDirectionalOwnershipType(?string directionalOwnershipType): void |
| `signingAgreement` | `?bool` | Optional | Flag indicating if person if signing the agreement, true if YES, false if NO | getSigningAgreement(): ?bool | setSigningAgreement(?bool signingAgreement): void |
| `usPerson` | `?bool` | Optional | [NA] Flag indicating if person is a US citizen, true if YES, false if NO | getUsPerson(): ?bool | setUsPerson(?bool usPerson): void |

## Example (as JSON)

```json
{
  "name": {
    "firstName": "John",
    "lastName": "Doe"
  },
  "positions": null
}
```

