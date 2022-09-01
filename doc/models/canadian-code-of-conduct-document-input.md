
# Canadian Code of Conduct Document Input

## Structure

`CanadianCodeOfConductDocumentInput`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `language` | `string` | Required | Language of document to be generated,  ISO 639-1 standard applies | getLanguage(): string | setLanguage(string language): void |
| `documentId` | `string` | Required | Unique id of document | getDocumentId(): string | setDocumentId(string documentId): void |
| `agreementId` | `?string` | Optional | Merchant id (MID) | getAgreementId(): ?string | setAgreementId(?string agreementId): void |
| `documentPacketId` | `?string` | Optional | Document packet id | getDocumentPacketId(): ?string | setDocumentPacketId(?string documentPacketId): void |
| `signed` | `?bool` | Optional | Boolean flag indicating if document has been signed, true if  YES, false if NO | getSigned(): ?bool | setSigned(?bool signed): void |
| `groupedApplication` | `?bool` | Optional | Boolean flag indicating if document is of a group of applications, true if  YES, false if NO | getGroupedApplication(): ?bool | setGroupedApplication(?bool groupedApplication): void |
| `wetSigned` | `?bool` | Optional | Boolean flag indicating if document is to be wet signed, true if  YES, false if NO | getWetSigned(): ?bool | setWetSigned(?bool wetSigned): void |
| `scarecrowApplication` | [`ScarecrowApplication`](../../doc/models/scarecrow-application.md) | Required | - | getScarecrowApplication(): ScarecrowApplication | setScarecrowApplication(ScarecrowApplication scarecrowApplication): void |
| `cardVolume` | [`CardVolume`](../../doc/models/card-volume.md) | Required | - | getCardVolume(): CardVolume | setCardVolume(CardVolume cardVolume): void |
| `salesOfficeContact` | [`SalesOfficeContact`](../../doc/models/sales-office-contact.md) | Required | - | getSalesOfficeContact(): SalesOfficeContact | setSalesOfficeContact(SalesOfficeContact salesOfficeContact): void |
| `subJurisdictionId` | `?int` | Optional | - | getSubJurisdictionId(): ?int | setSubJurisdictionId(?int subJurisdictionId): void |

## Example (as JSON)

```json
{
  "language": "en",
  "documentId": "1",
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
  "cardVolume": {
    "visaPercentage": "15.6",
    "masterCardPercentage": "12.3",
    "amexPercentage": "4.5",
    "amexAverageTransaction": "10.1",
    "interacAverageTransaction": "23.4"
  },
  "salesOfficeContact": {
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
}
```

