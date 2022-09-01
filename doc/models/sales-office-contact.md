
# Sales Office Contact

## Structure

`SalesOfficeContact`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `address` | [`Address`](../../doc/models/address.md) | Required | - | getAddress(): Address | setAddress(Address address): void |
| `phone` | [`PhoneNumber`](../../doc/models/phone-number.md) | Required | - | getPhone(): PhoneNumber | setPhone(PhoneNumber phone): void |

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

