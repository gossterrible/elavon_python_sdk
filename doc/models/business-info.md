
# Business Info

## Structure

`BusinessInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `dbaName` | `string` | Required | Doing Business As name for business<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `32` | getDbaName(): string | setDbaName(string dbaName): void |
| `dbaNameExtended` | `string` | Required | Doing Business As name for business, character limit extended<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` | getDbaNameExtended(): string | setDbaNameExtended(string dbaNameExtended): void |
| `businessAddress` | [`Address`](../../doc/models/address.md) | Required | - | getBusinessAddress(): Address | setBusinessAddress(Address businessAddress): void |
| `legalName` | `string` | Required | Certified legal name of business<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` | getLegalName(): string | setLegalName(string legalName): void |
| `legalNameExtended` | `string` | Required | Certified legal name of business, character limit extended<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` | getLegalNameExtended(): string | setLegalNameExtended(string legalNameExtended): void |
| `legalNameMarked` | `?(string[])` | Optional | Certified legal name of business, permits accented characters, required in POL | getLegalNameMarked(): ?array | setLegalNameMarked(?array legalNameMarked): void |
| `additionalAddresses` | [`array<string,Address>`](../../doc/models/address.md) | Required | Container of other addresses, legal required.The valid keys are as follows: BUSINESS, LEGAL, SHIPPING, MAILING, PRINCIPAL, PREVIOUS, STATEMENT | getAdditionalAddresses(): array | setAdditionalAddresses(array additionalAddresses): void |
| `ownershipType` | [`string (OwnershipTypeEnum)`](../../doc/models/ownership-type-enum.md) | Required | Type of business | getOwnershipType(): string | setOwnershipType(string ownershipType): void |
| `registrationNumber` | `?string` | Optional | [EU] Registration number of business, required for LIMITED_LIBABILITY_PARTNERSHIP, LIMITED_COMPANY, or PUBLIC_LIMITED_COMPANY<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `15` | getRegistrationNumber(): ?string | setRegistrationNumber(?string registrationNumber): void |
| `taxID` | `?string` | Optional | Business tax ID. For testing a valid tax ID, use format 78742xxxx where 'xxxx' represents a series of four random, non-repeating, non-sequential numbers<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `15` | getTaxID(): ?string | setTaxID(?string taxID): void |
| `taxIDType` | [`?string (TaxIDTypeEnum)`](../../doc/models/tax-id-type-enum.md) | Optional | [NA] Type of tax id provieded | getTaxIDType(): ?string | setTaxIDType(?string taxIDType): void |
| `vatInfo` | [`?VatInfo`](../../doc/models/vat-info.md) | Optional | - | getVatInfo(): ?VatInfo | setVatInfo(?VatInfo vatInfo): void |
| `taxFormType` | [`?string (TaxFormTypeEnum)`](../../doc/models/tax-form-type-enum.md) | Optional | [NA] Type of tax form provided | getTaxFormType(): ?string | setTaxFormType(?string taxFormType): void |
| `taxClassType` | [`?string (TaxClassTypeEnum)`](../../doc/models/tax-class-type-enum.md) | Optional | [NA] Type of business's tax classification | getTaxClassType(): ?string | setTaxClassType(?string taxClassType): void |
| `customerMembershipNumber` | `?string` | Optional | [NA] Business membership number (ex. COSTCO)<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `12` | getCustomerMembershipNumber(): ?string | setCustomerMembershipNumber(?string customerMembershipNumber): void |
| `productDescription` | `string` | Required | Description of product/service business provides<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` | getProductDescription(): string | setProductDescription(string productDescription): void |
| `mccCode` | `string` | Required | Extended MCC code business qualifies as<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `5` | getMccCode(): string | setMccCode(string mccCode): void |
| `establishmentYear` | `string` | Required | Year business was established | getEstablishmentYear(): string | setEstablishmentYear(string establishmentYear): void |
| `currentOwnershipYears` | `string` | Required | Years business has been in control of current ownership | getCurrentOwnershipYears(): string | setCurrentOwnershipYears(string currentOwnershipYears): void |
| `currentOwnershipMonths` | `string` | Required | Months business has been in control of current ownership | getCurrentOwnershipMonths(): string | setCurrentOwnershipMonths(string currentOwnershipMonths): void |
| `governmentOwnedEntity` | `?bool` | Optional | [EU] Indicate if more than 50% of the business is owned by the government. This field is mandatory for all ownership types. | getGovernmentOwnedEntity(): ?bool | setGovernmentOwnedEntity(?bool governmentOwnedEntity): void |
| `communicationLanguage` | `string` | Required | Language to be used for legal documents and communication between business and customer, ISO 639-1 standard applies | getCommunicationLanguage(): string | setCommunicationLanguage(string communicationLanguage): void |
| `posLanguage` | `string` | Required | Language to be used for equipment displays, ISO 639-1 standard applies | getPosLanguage(): string | setPosLanguage(string posLanguage): void |
| `storeNumber` | `?string` | Optional | [EU] Business store number<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `10` | getStoreNumber(): ?string | setStoreNumber(?string storeNumber): void |
| `associationCodes` | `?(string[])` | Optional | [EU] Elavon promotion/assocation code listing | getAssociationCodes(): ?array | setAssociationCodes(?array associationCodes): void |
| `optOut` | `?bool` | Optional | [EU] Elavon marketing opt out flag, true if opt out YES, false if opt out NO | getOptOut(): ?bool | setOptOut(?bool optOut): void |
| `signDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getSignDate(): ?DateComponents | setSignDate(?DateComponents signDate): void |
| `pciInfo` | [`?PCIInfo`](../../doc/models/pci-info.md) | Optional | - | getPciInfo(): ?PCIInfo | setPciInfo(?PCIInfo pciInfo): void |
| `employerId` | `?string` | Optional | [NA] Employer id | getEmployerId(): ?string | setEmployerId(?string employerId): void |
| `countryOfOrigin` | `?string` | Optional | Country of business origin, ISO 3166-1 alpha-3 standard applies | getCountryOfOrigin(): ?string | setCountryOfOrigin(?string countryOfOrigin): void |
| `exemptionType` | [`?string (ExemptionTypeEnum)`](../../doc/models/exemption-type-enum.md) | Optional | [NA] Exemption type of business (AML) | getExemptionType(): ?string | setExemptionType(?string exemptionType): void |
| `ownerExemptionType` | [`?string (OwnerExemptionTypeEnum)`](../../doc/models/owner-exemption-type-enum.md) | Optional | [NA] Exemption type of owner (AML) | getOwnerExemptionType(): ?string | setOwnerExemptionType(?string ownerExemptionType): void |
| `numberOfPartners` | [`?string (NumberOfPartnersEnum)`](../../doc/models/number-of-partners-enum.md) | Optional | [EU] Number of partners business has, applicable if business is any kind of PARTNERSHIP | getNumberOfPartners(): ?string | setNumberOfPartners(?string numberOfPartners): void |
| `relationshipMgrCode` | `?string` | Optional | [EU] Relationship manager code | getRelationshipMgrCode(): ?string | setRelationshipMgrCode(?string relationshipMgrCode): void |
| `countryOfPrimaryOperation` | `?string` | Optional | Country of business primary operation, ISO 3166-1 alpha-3 standard applies | getCountryOfPrimaryOperation(): ?string | setCountryOfPrimaryOperation(?string countryOfPrimaryOperation): void |
| `bearerShares` | `?bool` | Optional | [NA] Flag indicating if business has bearer shares, true if YES, false if NO | getBearerShares(): ?bool | setBearerShares(?bool bearerShares): void |
| `legalStatus` | [`?string (LegalStatusEnum)`](../../doc/models/legal-status-enum.md) | Optional | [NA] Business entity legal status | getLegalStatus(): ?string | setLegalStatus(?string legalStatus): void |
| `verifications` | [`?array<string,VerificationInfo>`](../../doc/models/verification-info.md) | Optional | [NA] Anti-Money Laundering (AML) oriented documentation info for the business. The valid keys are as follows: BUSINESS, LEGAL, SHIPPING, MAILING, PRINCIPAL, PREVIOUS, STATEMENT | getVerifications(): ?array | setVerifications(?array verifications): void |
| `industryClass` | [`?string (IndustryClassEnum)`](../../doc/models/industry-class-enum.md) | Optional | [NA] Business industry classification | getIndustryClass(): ?string | setIndustryClass(?string industryClass): void |
| `noPlates` | `?bool` | Optional | [NA] Flag indicating if plates are to be delivered to business, true if no delivery, false if yes to delivery (NA) | getNoPlates(): ?bool | setNoPlates(?bool noPlates): void |
| `agentNumber` | `?string` | Optional | [NA] Agent number | getAgentNumber(): ?string | setAgentNumber(?string agentNumber): void |
| `locationMidRange` | [`?string (LocationMidRangeEnum)`](../../doc/models/location-mid-range-enum.md) | Optional | [EU] 10 character MID range for Nordics. | getLocationMidRange(): ?string | setLocationMidRange(?string locationMidRange): void |
| `hempGrowerInfo` | [`?HempGrowerInfo`](../../doc/models/hemp-grower-info.md) | Optional | - | getHempGrowerInfo(): ?HempGrowerInfo | setHempGrowerInfo(?HempGrowerInfo hempGrowerInfo): void |
| `creditDecisionInfo` | [`?CreditDecisionInfo`](../../doc/models/credit-decision-info.md) | Optional | - | getCreditDecisionInfo(): ?CreditDecisionInfo | setCreditDecisionInfo(?CreditDecisionInfo creditDecisionInfo): void |

## Example (as JSON)

```json
{
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
```

