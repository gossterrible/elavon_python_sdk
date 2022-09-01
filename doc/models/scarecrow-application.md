
# Scarecrow Application

## Structure

`ScarecrowApplication`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `clientId` | `string` | Required | Client id of application submission, to be provided to partners | getClientId(): string | setClientId(string clientId): void |
| `clientGroupNumber` | `?string` | Optional | Client group number of application submission, paris with parent entity, to be provided to partners, required in NA | getClientGroupNumber(): ?string | setClientGroupNumber(?string clientGroupNumber): void |
| `uniqueId` | `string` | Required | Unique identifier of application submission, alphanumeric. Provided by the client.The uniqueId must be wholly original and never repeated. The client's name followed by a millisecond timestamp would work well.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `32` | getUniqueId(): string | setUniqueId(string uniqueId): void |
| `bankerId` | `?string` | Optional | [EU] Identifier of banker responsible for submission | getBankerId(): ?string | setBankerId(?string bankerId): void |
| `bankerPartnerId` | `?string` | Optional | [EU] Identifier of banker partner responsible for submission | getBankerPartnerId(): ?string | setBankerPartnerId(?string bankerPartnerId): void |
| `country` | `string` | Required | Country of application submission, ISO 3166-1 alpha-3 standard applies | getCountry(): string | setCountry(string country): void |
| `principal` | [`Person`](../../doc/models/person.md) | Required | - | getPrincipal(): Person | setPrincipal(Person principal): void |
| `businessInfo` | [`BusinessInfo`](../../doc/models/business-info.md) | Required | - | getBusinessInfo(): BusinessInfo | setBusinessInfo(BusinessInfo businessInfo): void |
| `financialInfo` | [`FinancialInfo`](../../doc/models/financial-info.md) | Required | - | getFinancialInfo(): FinancialInfo | setFinancialInfo(FinancialInfo financialInfo): void |
| `salesRepCode` | `string` | Required | Identifier of sales representative responsible for submission | getSalesRepCode(): string | setSalesRepCode(string salesRepCode): void |
| `additionalShareholders` | [`?(Person[])`](../../doc/models/person.md) | Optional | - | getAdditionalShareholders(): ?array | setAdditionalShareholders(?array additionalShareholders): void |
| `contact` | [`Person`](../../doc/models/person.md) | Required | - | getContact(): Person | setContact(Person contact): void |
| `bankAccounts` | [`array<string,BankingInfo>`](../../doc/models/banking-info.md) | Required | Bank account container. Valid keys are as follows: BILLING, DEPOSIT, LEASE, CHARGEBACK | getBankAccounts(): array | setBankAccounts(array bankAccounts): void |
| `cardPricing` | [`CardPricing`](../../doc/models/card-pricing.md) | Required | - | getCardPricing(): CardPricing | setCardPricing(CardPricing cardPricing): void |
| `fees` | [`?(Fee[])`](../../doc/models/fee.md) | Optional | - | getFees(): ?array | setFees(?array fees): void |
| `monetaryPricingProgram` | `?string` | Optional | Pricing program also called MPP/NPP, to be provided to partners, required in EU | getMonetaryPricingProgram(): ?string | setMonetaryPricingProgram(?string monetaryPricingProgram): void |
| `authenticatePricingProgram` | `?string` | Optional | Pricing program also called APP, to be provided to partners, required in EU | getAuthenticatePricingProgram(): ?string | setAuthenticatePricingProgram(?string authenticatePricingProgram): void |
| `parentEntity` | `string` | Required | Entity that is parent to submisssion, forms a pair with client group, to be provided to partners | getParentEntity(): string | setParentEntity(string parentEntity): void |
| `shortName` | `?string` | Optional | [NA] | getShortName(): ?string | setShortName(?string shortName): void |
| `fraudCheckResult` | [`?FraudCheckResult`](../../doc/models/fraud-check-result.md) | Optional | - | getFraudCheckResult(): ?FraudCheckResult | setFraudCheckResult(?FraudCheckResult fraudCheckResult): void |
| `siteSurvey` | [`?SiteSurvey`](../../doc/models/site-survey.md) | Optional | - | getSiteSurvey(): ?SiteSurvey | setSiteSurvey(?SiteSurvey siteSurvey): void |
| `dynamicCurrencyConversion` | [`?DynamicCurrencyConversion`](../../doc/models/dynamic-currency-conversion.md) | Optional | - | getDynamicCurrencyConversion(): ?DynamicCurrencyConversion | setDynamicCurrencyConversion(?DynamicCurrencyConversion dynamicCurrencyConversion): void |
| `billingStatement` | [`?BillingStatement`](../../doc/models/billing-statement.md) | Optional | - | getBillingStatement(): ?BillingStatement | setBillingStatement(?BillingStatement billingStatement): void |
| `fundingStatement` | [`?FundingStatement`](../../doc/models/funding-statement.md) | Optional | - | getFundingStatement(): ?FundingStatement | setFundingStatement(?FundingStatement fundingStatement): void |
| `electronicStatement` | [`?ElectronicStatement`](../../doc/models/electronic-statement.md) | Optional | - | getElectronicStatement(): ?ElectronicStatement | setElectronicStatement(?ElectronicStatement electronicStatement): void |
| `vatInvoiceStatement` | [`?VatInvoiceStatement`](../../doc/models/vat-invoice-statement.md) | Optional | - | getVatInvoiceStatement(): ?VatInvoiceStatement | setVatInvoiceStatement(?VatInvoiceStatement vatInvoiceStatement): void |
| `billingMethod` | [`?string (BillingMethodEnum)`](../../doc/models/billing-method-enum.md) | Optional | [NA] NETCREDIT or GROSS | getBillingMethod(): ?string | setBillingMethod(?string billingMethod): void |
| `referrerName` | `?string` | Optional | Application submission's referrer name, to be provided to partners, required in NA | getReferrerName(): ?string | setReferrerName(?string referrerName): void |
| `referrerReferenceNumber` | `?string` | Optional | The reference number associated with the referrer, known by Elavon.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `10` | getReferrerReferenceNumber(): ?string | setReferrerReferenceNumber(?string referrerReferenceNumber): void |
| `previousProcessor` | `?string` | Optional | [NA] Customer's previous payment processor | getPreviousProcessor(): ?string | setPreviousProcessor(?string previousProcessor): void |
| `valueAddedInfo` | [`?ValueAddedInfo`](../../doc/models/value-added-info.md) | Optional | - | getValueAddedInfo(): ?ValueAddedInfo | setValueAddedInfo(?ValueAddedInfo valueAddedInfo): void |
| `equipmentInfo` | [`?EquipmentInfo`](../../doc/models/equipment-info.md) | Optional | In NA, it's mandatory to have at least one piece of equipment. For third party vendors<br>managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.<br>Contact your Elavon representative for the VAR code(s).<br><br>          In EU, equipmentInfo is optional and no equipment has to be sent. If you have any equipment <br>          managed by Elavon, contact your Elavon representative for the VAR code(s). | getEquipmentInfo(): ?EquipmentInfo | setEquipmentInfo(?EquipmentInfo equipmentInfo): void |
| `branchNumber` | `?string` | Optional | Bank branch number associated with application submission | getBranchNumber(): ?string | setBranchNumber(?string branchNumber): void |
| `branchCode` | `?string` | Optional | Bank branch code associated with application submission | getBranchCode(): ?string | setBranchCode(?string branchCode): void |
| `selfBoardedExternal` | `?bool` | Optional | [NA] Flag indicating if application is self boarded externally, suppresses forms of post-boarding contact | getSelfBoardedExternal(): ?bool | setSelfBoardedExternal(?bool selfBoardedExternal): void |
| `employeeNumber` | `?string` | Optional | Number used to identify a specific employee | getEmployeeNumber(): ?string | setEmployeeNumber(?string employeeNumber): void |
| `repReferralNumber` | `?string` | Optional | Number used to identify a specific representative | getRepReferralNumber(): ?string | setRepReferralNumber(?string repReferralNumber): void |
| `promotionalCode` | `?string` | Optional | A discount/promotional code | getPromotionalCode(): ?string | setPromotionalCode(?string promotionalCode): void |
| `chainInfo` | [`?ChainInfo`](../../doc/models/chain-info.md) | Optional | - | getChainInfo(): ?ChainInfo | setChainInfo(?ChainInfo chainInfo): void |
| `distributions` | [`?array<string,DistributionInfo>`](../../doc/models/distribution-info.md) | Optional | Distribution container for chargebacks and retrievals. The valid keys are as follows: CHARGEBACK, RETRIEVAL | getDistributions(): ?array | setDistributions(?array distributions): void |
| `additionalLocationInfo` | [`?AdditionalLocationInfo`](../../doc/models/additional-location-info.md) | Optional | - | getAdditionalLocationInfo(): ?AdditionalLocationInfo | setAdditionalLocationInfo(?AdditionalLocationInfo additionalLocationInfo): void |
| `signedDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getSignedDate(): ?DateComponents | setSignedDate(?DateComponents signedDate): void |
| `signedType` | [`?string (SignedTypeEnum)`](../../doc/models/signed-type-enum.md) | Optional | [NA] How application was signed | getSignedType(): ?string | setSignedType(?string signedType): void |
| `intermediaryOwnerInfo` | [`?IntermediaryOwnerInfo`](../../doc/models/intermediary-owner-info.md) | Optional | - | getIntermediaryOwnerInfo(): ?IntermediaryOwnerInfo | setIntermediaryOwnerInfo(?IntermediaryOwnerInfo intermediaryOwnerInfo): void |
| `revenueShareInfo` | [`?RevenueShareInfo`](../../doc/models/revenue-share-info.md) | Optional | - | getRevenueShareInfo(): ?RevenueShareInfo | setRevenueShareInfo(?RevenueShareInfo revenueShareInfo): void |
| `elavonContract` | [`?string (ElavonContractEnum)`](../../doc/models/elavon-contract-enum.md) | Optional | [EU] Determine which Merchant Agreement customer will sign | getElavonContract(): ?string | setElavonContract(?string elavonContract): void |
| `internalUseInfo` | [`?InternalUseInfo`](../../doc/models/internal-use-info.md) | Optional | - | getInternalUseInfo(): ?InternalUseInfo | setInternalUseInfo(?InternalUseInfo internalUseInfo): void |
| `eframeInfo` | [`?EframeInfo`](../../doc/models/eframe-info.md) | Optional | - | getEframeInfo(): ?EframeInfo | setEframeInfo(?EframeInfo eframeInfo): void |
| `partnerInfo` | [`?PartnerInfo`](../../doc/models/partner-info.md) | Optional | - | getPartnerInfo(): ?PartnerInfo | setPartnerInfo(?PartnerInfo partnerInfo): void |
| `alternativePaymentMethods` | [`?(ApmAcquirer[])`](../../doc/models/apm-acquirer.md) | Optional | [EU] List of Alternative Payment Method Acquirers container | getAlternativePaymentMethods(): ?array | setAlternativePaymentMethods(?array alternativePaymentMethods): void |

## Example (as JSON)

```json
{
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
}
```

