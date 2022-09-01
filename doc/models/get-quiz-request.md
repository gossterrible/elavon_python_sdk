
# Get Quiz Request

## Structure

`GetQuizRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `principal` | [`Person`](../../doc/models/person.md) | Required | - | getPrincipal(): Person | setPrincipal(Person principal): void |
| `businessAddress` | [`Address`](../../doc/models/address.md) | Required | - | getBusinessAddress(): Address | setBusinessAddress(Address businessAddress): void |
| `language` | `string` | Required | Language of E-KYC requested, ISO 639-2 standard applies, en and fr supported | getLanguage(): string | setLanguage(string language): void |

## Example (as JSON)

```json
{
  "principal": {
    "name": {
      "firstName": "John",
      "lastName": "Doe"
    },
    "positions": null
  },
  "businessAddress": {
    "streetName": "Baker Street",
    "city": "Atlanta",
    "country": "USA"
  },
  "language": "en"
}
```

