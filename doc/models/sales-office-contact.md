
# Sales Office Contact

## Structure

`SalesOfficeContact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address`](../../doc/models/address.md) | Required | - |
| `phone` | [`PhoneNumber`](../../doc/models/phone-number.md) | Required | - |

## Example (as JSON)

```json
{
  "address": {
    "streetName": "Baker Street",
    "city": "Atlanta",
    "country": "USA"
  },
  "phone": {
    "areaCode": "111",
    "number": "1231234"
  }
}
```

