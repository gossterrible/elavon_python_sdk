
# Document Packet Data

## Structure

`DocumentPacketData`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `scarecrowApplication` | [`ScarecrowApplication`](../../doc/models/scarecrow-application.md) | Required | - | getScarecrowApplication(): ScarecrowApplication | setScarecrowApplication(ScarecrowApplication scarecrowApplication): void |
| `language` | `string` | Required | Language of document to be generated,  ISO 639-1 standard applies | getLanguage(): string | setLanguage(string language): void |
| `agreementId` | `?string` | Optional | Merchant Id (MID) | getAgreementId(): ?string | setAgreementId(?string agreementId): void |
| `isGroupedApplication` | `?bool` | Optional | Boolean flag indicating if document is of a group of applications, true if  YES, false if NO | getIsGroupedApplication(): ?bool | setIsGroupedApplication(?bool isGroupedApplication): void |
| `wetSigned` | `?bool` | Optional | Boolean flag indicating if document is to be wet signed, true if  YES, false if NO | getWetSigned(): ?bool | setWetSigned(?bool wetSigned): void |
| `cardVolume` | [`?CardVolume`](../../doc/models/card-volume.md) | Optional | - | getCardVolume(): ?CardVolume | setCardVolume(?CardVolume cardVolume): void |
| `vendorInfo` | [`ProviderInfo`](../../doc/models/provider-info.md) | Required | - | getVendorInfo(): ProviderInfo | setVendorInfo(ProviderInfo vendorInfo): void |
| `actingIntermediaryInfo` | [`?ActingIntermediaryInfo`](../../doc/models/acting-intermediary-info.md) | Optional | - | getActingIntermediaryInfo(): ?ActingIntermediaryInfo | setActingIntermediaryInfo(?ActingIntermediaryInfo actingIntermediaryInfo): void |
| `bankAccountDetailsMap` | [`array<string,BankAccountAdditionalInfo>`](../../doc/models/bank-account-additional-info.md) | Required | Application's additional bank account information. The valid keys are as follows: BILLING, DEPOSIT, LEASE, CHARGEBACK | getBankAccountDetailsMap(): array | setBankAccountDetailsMap(array bankAccountDetailsMap): void |
| `isTaxExemptEquipment` | `?bool` | Optional | Flag indicating if equipment is to be considered tax exempt, true if exempt YES, false if NOT exept | getIsTaxExemptEquipment(): ?bool | setIsTaxExemptEquipment(?bool isTaxExemptEquipment): void |
| `talechEgiftOnly` | `?bool` | Optional | Flag indicating if equipment is to Talech eGift, true if selected YES, false if NOT selected | getTalechEgiftOnly(): ?bool | setTalechEgiftOnly(?bool talechEgiftOnly): void |
| `displayedCurrency` | `string` | Required | Application's currency, ISO 4217 standard applies | getDisplayedCurrency(): string | setDisplayedCurrency(string displayedCurrency): void |
| `additionalDescriptionInfo` | [`?AdditionalDescriptionInfo`](../../doc/models/additional-description-info.md) | Optional | - | getAdditionalDescriptionInfo(): ?AdditionalDescriptionInfo | setAdditionalDescriptionInfo(?AdditionalDescriptionInfo additionalDescriptionInfo): void |
| `additionalValueAddedServiceInfo` | [`?ValueAddedServices`](../../doc/models/value-added-services.md) | Optional | - | getAdditionalValueAddedServiceInfo(): ?ValueAddedServices | setAdditionalValueAddedServiceInfo(?ValueAddedServices additionalValueAddedServiceInfo): void |
| `additionalBusinessInfo` | [`?AdditionalBusinessInfo`](../../doc/models/additional-business-info.md) | Optional | - | getAdditionalBusinessInfo(): ?AdditionalBusinessInfo | setAdditionalBusinessInfo(?AdditionalBusinessInfo additionalBusinessInfo): void |
| `fundingType` | [`?string (FundingTypeEnum)`](../../doc/models/funding-type-enum.md) | Optional | Application's funding type | getFundingType(): ?string | setFundingType(?string fundingType): void |
| `integratorSolutionInfo` | [`?IntegratorSolutionInfo`](../../doc/models/integrator-solution-info.md) | Optional | - | getIntegratorSolutionInfo(): ?IntegratorSolutionInfo | setIntegratorSolutionInfo(?IntegratorSolutionInfo integratorSolutionInfo): void |
| `additionalLeaseInfo` | [`?AdditionalLeaseInfo`](../../doc/models/additional-lease-info.md) | Optional | - | getAdditionalLeaseInfo(): ?AdditionalLeaseInfo | setAdditionalLeaseInfo(?AdditionalLeaseInfo additionalLeaseInfo): void |
| `marketingDataConsentMap` | `?array<string,bool>` | Optional | Application's consent form (POL). The valid keys are the numerical value of the marketing consent option (1, 2, 3, etc) | getMarketingDataConsentMap(): ?array | setMarketingDataConsentMap(?array marketingDataConsentMap): void |
| `additionalSiteSurveyInfo` | [`?AdditionalSiteSurveyInfo`](../../doc/models/additional-site-survey-info.md) | Optional | - | getAdditionalSiteSurveyInfo(): ?AdditionalSiteSurveyInfo | setAdditionalSiteSurveyInfo(?AdditionalSiteSurveyInfo additionalSiteSurveyInfo): void |
| `kycQuizStatusMap` | [`?array<string,string> (KycQuizStatusMapEnum)`](../../doc/models/kyc-quiz-status-map-enum.md) | Optional | Status results of the KCY check. Email to result map. | getKycQuizStatusMap(): ?array | setKycQuizStatusMap(?array kycQuizStatusMap): void |
| `varOtherDetails` | [`?VarOtherDetails`](../../doc/models/var-other-details.md) | Optional | - | getVarOtherDetails(): ?VarOtherDetails | setVarOtherDetails(?VarOtherDetails varOtherDetails): void |
| `additionalCardPricingInfo` | [`?AdditionalCardPricingInfo`](../../doc/models/additional-card-pricing-info.md) | Optional | - | getAdditionalCardPricingInfo(): ?AdditionalCardPricingInfo | setAdditionalCardPricingInfo(?AdditionalCardPricingInfo additionalCardPricingInfo): void |
| `salesOfficeContact` | [`?SalesOfficeContact`](../../doc/models/sales-office-contact.md) | Optional | - | getSalesOfficeContact(): ?SalesOfficeContact | setSalesOfficeContact(?SalesOfficeContact salesOfficeContact): void |
| `salesPersonContact` | [`?SalesPersonContact`](../../doc/models/sales-person-contact.md) | Optional | - | getSalesPersonContact(): ?SalesPersonContact | setSalesPersonContact(?SalesPersonContact salesPersonContact): void |
| `additionalAuthPricingProgramInfo` | [`?AdditionalAuthPricingProgramInfo`](../../doc/models/additional-auth-pricing-program-info.md) | Optional | - | getAdditionalAuthPricingProgramInfo(): ?AdditionalAuthPricingProgramInfo | setAdditionalAuthPricingProgramInfo(?AdditionalAuthPricingProgramInfo additionalAuthPricingProgramInfo): void |
| `applicantEmail` | `?string` | Optional | Email address of applicant | getApplicantEmail(): ?string | setApplicantEmail(?string applicantEmail): void |
| `partnerDocumentData` | `?array<string,string>` | Optional | The data for partner documents | getPartnerDocumentData(): ?array | setPartnerDocumentData(?array partnerDocumentData): void |
| `applicationId` | `?int` | Optional | Application id | getApplicationId(): ?int | setApplicationId(?int applicationId): void |

## Example (as JSON)

```json
{
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
```

