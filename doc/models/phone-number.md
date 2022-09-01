
# Phone Number

## Structure

`PhoneNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `intl_code` | `string` | Optional | Standard International calling code |
| `area_code` | `string` | Required | Area code of phone number |
| `number` | `string` | Required | The main phone number, not including the area code or International calling code |
| `extension` | `string` | Optional | Phone extension number |

## Example (as JSON)

```json
{
  "areaCode": "111",
  "number": "1231234"
}
```

