
# Sales Person Contact

## Structure

`SalesPersonContact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`Name`](../../doc/models/name.md) | Required | - |
| `phone` | [`PhoneNumber`](../../doc/models/phone-number.md) | Required | - |
| `email_address` | `string` | Required | Contact email address of sales person |

## Example (as JSON)

```json
{
  "name": {
    "firstName": "John",
    "lastName": "Doe"
  },
  "phone": {
    "areaCode": "111",
    "number": "1231234"
  },
  "emailAddress": null
}
```

