
# Additional Location Info

## Structure

`AdditionalLocationInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `central_mid` | `string` | Required | Merchant Id of existing business |
| `central_legal_name` | `string` | Required | Legal Name of existing business<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `central_tax_id` | `string` | Optional | Tax Id of existing busines, required in cases where Central Legal Name not present |

## Example (as JSON)

```json
{
  "centralMid": "8024999222",
  "centralLegalName": "Elavon"
}
```

