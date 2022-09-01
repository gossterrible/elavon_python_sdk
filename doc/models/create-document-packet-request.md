
# Create Document Packet Request

## Structure

`CreateDocumentPacketRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `profile_code` | `string` | Required | The partner's profile code |
| `signers` | [`List of Signer`](../../doc/models/signer.md) | Required | The document signers |
| `document_packet_data` | [`DocumentPacketData`](../../doc/models/document-packet-data.md) | Required | - |

## Example (as JSON)

```json
{
  "profileCode": "TEST",
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

