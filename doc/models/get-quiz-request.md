
# Get Quiz Request

## Structure

`GetQuizRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `principal` | [`Person`](../../doc/models/person.md) | Required | - |
| `business_address` | [`Address`](../../doc/models/address.md) | Required | - |
| `language` | `string` | Required | Language of E-KYC requested, ISO 639-2 standard applies, en and fr supported |

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

