
# Address

## Structure

`Address`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street_name` | `string` | Required | Line one of address, name<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `247` |
| `street_number` | `string` | Optional | Line one of address, number<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `8` |
| `line_two` | `string` | Optional | Line two of address<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `40` |
| `line_three` | `string` | Optional | Line three of address<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `40` |
| `city` | `string` | Required | City of address<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `county` | `string` | Optional | County of address |
| `post_code` | `string` | Optional | Postal/Zip code of address<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `10` |
| `country` | `string` | Required | Country of address, ISO 3166-1 alpha-3 standard applies |
| `state` | [`StateEnum`](../../doc/models/state-enum.md) | Optional | State/Province of address |
| `classification` | [`ClassificationEnum`](../../doc/models/classification-enum.md) | Optional | [NA] Type of address |
| `contact_name` | [`Name`](../../doc/models/name.md) | Optional | - |
| `location_name` | `string` | Optional | [NA] Name of address local name |

## Example (as JSON)

```json
{
  "streetName": "Baker Street",
  "city": "Atlanta",
  "country": "USA"
}
```

