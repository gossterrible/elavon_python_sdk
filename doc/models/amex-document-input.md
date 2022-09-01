
# Amex Document Input

## Structure

`AmexDocumentInput`

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
| `cardPricing` | [`CardPricing`](../../doc/models/card-pricing.md) | Required | - | getCardPricing(): CardPricing | setCardPricing(CardPricing cardPricing): void |
| `businessInfo` | [`BusinessInfo`](../../doc/models/business-info.md) | Required | - | getBusinessInfo(): BusinessInfo | setBusinessInfo(BusinessInfo businessInfo): void |
| `monetaryPricingProgram` | `?string` | Optional | Application's monetary pricing program (MPP) | getMonetaryPricingProgram(): ?string | setMonetaryPricingProgram(?string monetaryPricingProgram): void |
| `bankAccounts` | [`array<string,BankingInfo>`](../../doc/models/banking-info.md) | Required | Application's banking information. The valid keys are as follows: BILLING, DEPOSIT, LEASE, CHARGEBACK | getBankAccounts(): array | setBankAccounts(array bankAccounts): void |
| `applicantEmail` | `string` | Required | Email address of applicant | getApplicantEmail(): string | setApplicantEmail(string applicantEmail): void |
| `principal` | [`Person`](../../doc/models/person.md) | Required | - | getPrincipal(): Person | setPrincipal(Person principal): void |
| `additionalShareholders` | [`?(Person[])`](../../doc/models/person.md) | Optional | Application's additional shareholders | getAdditionalShareholders(): ?array | setAdditionalShareholders(?array additionalShareholders): void |

## Example (as JSON)

```json
{
  "language": "en",
  "documentId": "1",
  "cardPricing": null,
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
  "bankAccounts": null,
  "applicantEmail": null,
  "principal": {
    "name": {
      "firstName": "John",
      "lastName": "Doe"
    },
    "positions": null
  }
}
```
