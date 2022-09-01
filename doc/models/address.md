
# Address

## Structure

`Address`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `streetName` | `string` | Required | Line one of address, name<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `247` | getStreetName(): string | setStreetName(string streetName): void |
| `streetNumber` | `?string` | Optional | Line one of address, number<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `8` | getStreetNumber(): ?string | setStreetNumber(?string streetNumber): void |
| `lineTwo` | `?string` | Optional | Line two of address<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `40` | getLineTwo(): ?string | setLineTwo(?string lineTwo): void |
| `lineThree` | `?string` | Optional | Line three of address<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `40` | getLineThree(): ?string | setLineThree(?string lineThree): void |
| `city` | `string` | Required | City of address<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` | getCity(): string | setCity(string city): void |
| `county` | `?string` | Optional | County of address | getCounty(): ?string | setCounty(?string county): void |
| `postCode` | `?string` | Optional | Postal/Zip code of address<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `10` | getPostCode(): ?string | setPostCode(?string postCode): void |
| `country` | `string` | Required | Country of address, ISO 3166-1 alpha-3 standard applies | getCountry(): string | setCountry(string country): void |
| `state` | [`?string (StateEnum)`](../../doc/models/state-enum.md) | Optional | State/Province of address | getState(): ?string | setState(?string state): void |
| `classification` | [`?string (ClassificationEnum)`](../../doc/models/classification-enum.md) | Optional | [NA] Type of address | getClassification(): ?string | setClassification(?string classification): void |
| `contactName` | [`?Name`](../../doc/models/name.md) | Optional | - | getContactName(): ?Name | setContactName(?Name contactName): void |
| `locationName` | `?string` | Optional | [NA] Name of address local name | getLocationName(): ?string | setLocationName(?string locationName): void |

## Example (as JSON)

```json
{
  "streetName": "Baker Street",
  "city": "Atlanta",
  "country": "USA"
}
```

