
# Personal Guarantee Document Input

## Structure

`PersonalGuaranteeDocumentInput`

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
| `principal` | [`Person`](../../doc/models/person.md) | Required | - | getPrincipal(): Person | setPrincipal(Person principal): void |
| `equipmentInfo` | [`EquipmentInfo`](../../doc/models/equipment-info.md) | Required | In NA, it's mandatory to have at least one piece of equipment. For third party vendors<br>managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.<br>Contact your Elavon representative for the VAR code(s).<br><br>          In EU, equipmentInfo is optional and no equipment has to be sent. If you have any equipment <br>          managed by Elavon, contact your Elavon representative for the VAR code(s). | getEquipmentInfo(): EquipmentInfo | setEquipmentInfo(EquipmentInfo equipmentInfo): void |
| `additionalShareholders` | [`?(Person[])`](../../doc/models/person.md) | Optional | Application's additional shareholders | getAdditionalShareholders(): ?array | setAdditionalShareholders(?array additionalShareholders): void |
| `businessInfo` | [`BusinessInfo`](../../doc/models/business-info.md) | Required | - | getBusinessInfo(): BusinessInfo | setBusinessInfo(BusinessInfo businessInfo): void |

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
  "equipmentInfo": {
    "equipmentItems": {
      "code": "310T3",
      "quantity": 2,
      "pricingItems": {
        "amount": 200
      },
      "trxFreeMonth": null
    },
    "fuseboxInfo": null
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

