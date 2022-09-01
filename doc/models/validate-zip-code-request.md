
# Validate Zip Code Request

## Structure

`ValidateZipCodeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `zip_code` | `string` | Required | Postal code/Zip code to be validated |
| `city` | `string` | Optional | Optional city value related to postal code/zip code |
| `country` | `string` | Required | Country of postal code/zip code origin, ISO 3166-1 alpha-3 standard applies |

## Example (as JSON)

```json
{
  "zipCode": "20330",
  "country": "USA"
}
```

