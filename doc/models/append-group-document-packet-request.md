
# Append Group Document Packet Request

## Structure

`AppendGroupDocumentPacketRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `groupDocumentPacketId` | `string` | Required | The unique identifier for the group document packet | getGroupDocumentPacketId(): string | setGroupDocumentPacketId(string groupDocumentPacketId): void |
| `profileCode` | `string` | Required | The partner's profile code | getProfileCode(): string | setProfileCode(string profileCode): void |
| `signers` | [`Signer[]`](../../doc/models/signer.md) | Required | The document signers | getSigners(): array | setSigners(array signers): void |
| `documentPacketData` | [`DocumentPacketData`](../../doc/models/document-packet-data.md) | Required | - | getDocumentPacketData(): DocumentPacketData | setDocumentPacketData(DocumentPacketData documentPacketData): void |

## Example (as JSON)

```json
{
  "groupDocumentPacketId": null,
  "profileCode": null,
  "signers": {
    "signerId": null,
    "signer": {
      "firstName": "John",
      "lastName": "Doe"
    },
    "principal": null
  },
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

