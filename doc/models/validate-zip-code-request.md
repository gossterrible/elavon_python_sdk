
# Validate Zip Code Request

## Structure

`ValidateZipCodeRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `zipCode` | `string` | Required | Postal code/Zip code to be validated | getZipCode(): string | setZipCode(string zipCode): void |
| `city` | `?string` | Optional | Optional city value related to postal code/zip code | getCity(): ?string | setCity(?string city): void |
| `country` | `string` | Required | Country of postal code/zip code origin, ISO 3166-1 alpha-3 standard applies | getCountry(): string | setCountry(string country): void |

## Example (as JSON)

```json
{
  "zipCode": "20330",
  "country": "USA"
}
```

