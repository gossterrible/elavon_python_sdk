
# Identification

## Structure

`Identification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id_type` | [`IdTypeEnum`](../../doc/models/id-type-enum.md) | Required | Type of id provieded |
| `id_number` | `string` | Required | Id number<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `30` |
| `expiry_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `issue_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `issuing_country` | `string` | Optional | Id issuing country, ISO 3166-1 alpha-3 standard applies |
| `issuing_state` | [`IssuingStateEnum`](../../doc/models/issuing-state-enum.md) | Optional | Id issuing state |
| `id_name` | `string` | Optional | Name of Id |
| `issuing_agency` | `string` | Optional | Id issuing agency |

## Example (as JSON)

```json
{
  "idType": null,
  "idNumber": "123456789"
}
```

