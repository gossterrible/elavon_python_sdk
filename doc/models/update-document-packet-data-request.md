
# Update Document Packet Data Request

## Structure

`UpdateDocumentPacketDataRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `signers` | [`?(Signer[])`](../../doc/models/signer.md) | Optional | The document signers | getSigners(): ?array | setSigners(?array signers): void |
| `documentPacketId` | `string` | Required | The unique id for the document packet | getDocumentPacketId(): string | setDocumentPacketId(string documentPacketId): void |
| `documentPacketData` | [`DocumentPacketData`](../../doc/models/document-packet-data.md) | Required | - | getDocumentPacketData(): DocumentPacketData | setDocumentPacketData(DocumentPacketData documentPacketData): void |

## Example (as JSON)

```json
{
  "documentPacketId": null,
  "documentPacketData": {
    "scarecrowApplication": {
      "clientId": "IDNA",
      "uniqueId": "AcmeCorp1572566399123",
      "country": "USA",
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
      },
      "financialInfo": {
        "avgSaleAmount": "125",
        "monthlyCardSales": "1000",
        "cardPresentAcceptancePercent": "100",
        "internetAcceptancePercent": "0",
        "motoAcceptancePercent": "0"
      },
      "salesRepCode": "12345",
      "contact": {
        "name": {
          "firstName": "John",
          "lastName": "Doe"
        },
        "positions": null
      },
      "bankAccounts": null,
      "cardPricing": null,
      "parentEntity": null
    },
    "language": null,
    "vendorInfo": null,
    "bankAccountDetailsMap": null,
    "displayedCurrency": null
  }
}
```

