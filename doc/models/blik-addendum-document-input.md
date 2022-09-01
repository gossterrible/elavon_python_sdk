
# Blik Addendum Document Input

## Structure

`BlikAddendumDocumentInput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `language` | `string` | Required | Language of document to be generated,  ISO 639-1 standard applies |
| `document_id` | `string` | Required | Unique id of document |
| `agreement_id` | `string` | Optional | Merchant id (MID) |
| `document_packet_id` | `string` | Optional | Document packet id |
| `signed` | `bool` | Optional | Boolean flag indicating if document has been signed, true if  YES, false if NO |
| `grouped_application` | `bool` | Optional | Boolean flag indicating if document is of a group of applications, true if  YES, false if NO |
| `wet_signed` | `bool` | Optional | Boolean flag indicating if document is to be wet signed, true if  YES, false if NO |
| `principal` | [`Person`](../../doc/models/person.md) | Required | - |
| `additional_shareholders` | [`List of Person`](../../doc/models/person.md) | Optional | Application's additional shareholders |
| `business_info` | [`BusinessInfo`](../../doc/models/business-info.md) | Required | - |

## Example (as JSON)

```json
{
  "language": "en",
  "documentId": "1",
  "principal": {
    "name": {
      "firstName": "John",
      "lastName": "Doe"
    },
    "positions": null
  },
  "businessInfo": {
    "dbaName": "Grimm's Bookstore",
    "dbaNameExtended": "Grimm's Fairytales and Other Stories Bookstore",
    "businessAddress": {
      "streetName": "Baker Street",
      "city": "Atlanta",
      "country": "USA"
    },
    "legalName": "Barkers Dog Bakery",
    "legalNameExtended": "Baking Better Biscuits for Your Favorite Barkers Dog Bakery LLC",
    "additionalAddresses": null,
    "ownershipType": null,
    "productDescription": "Bakeries",
    "mccCode": "7399E",
    "establishmentYear": "2005",
    "currentOwnershipYears": "3",
    "currentOwnershipMonths": "6",
    "communicationLanguage": "en",
    "posLanguage": "en"
  }
}
```

