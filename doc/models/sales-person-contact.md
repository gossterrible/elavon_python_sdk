
# Sales Person Contact

## Structure

`SalesPersonContact`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `name` | [`Name`](../../doc/models/name.md) | Required | - | getName(): Name | setName(Name name): void |
| `phone` | [`PhoneNumber`](../../doc/models/phone-number.md) | Required | - | getPhone(): PhoneNumber | setPhone(PhoneNumber phone): void |
| `emailAddress` | `string` | Required | Contact email address of sales person | getEmailAddress(): string | setEmailAddress(string emailAddress): void |

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

