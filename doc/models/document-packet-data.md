
# Document Packet Data

## Structure

`DocumentPacketData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scarecrow_application` | [`ScarecrowApplication`](../../doc/models/scarecrow-application.md) | Required | - |
| `language` | `string` | Required | Language of document to be generated,  ISO 639-1 standard applies |
| `agreement_id` | `string` | Optional | Merchant Id (MID) |
| `is_grouped_application` | `bool` | Optional | Boolean flag indicating if document is of a group of applications, true if  YES, false if NO |
| `wet_signed` | `bool` | Optional | Boolean flag indicating if document is to be wet signed, true if  YES, false if NO |
| `card_volume` | [`CardVolume`](../../doc/models/card-volume.md) | Optional | - |
| `vendor_info` | [`ProviderInfo`](../../doc/models/provider-info.md) | Required | - |
| `acting_intermediary_info` | [`ActingIntermediaryInfo`](../../doc/models/acting-intermediary-info.md) | Optional | - |
| `bank_account_details_map` | [`dict`](../../doc/models/bank-account-additional-info.md) | Required | Application's additional bank account information. The valid keys are as follows: BILLING, DEPOSIT, LEASE, CHARGEBACK |
| `is_tax_exempt_equipment` | `bool` | Optional | Flag indicating if equipment is to be considered tax exempt, true if exempt YES, false if NOT exept |
| `talech_egift_only` | `bool` | Optional | Flag indicating if equipment is to Talech eGift, true if selected YES, false if NOT selected |
| `displayed_currency` | `string` | Required | Application's currency, ISO 4217 standard applies |
| `additional_description_info` | [`AdditionalDescriptionInfo`](../../doc/models/additional-description-info.md) | Optional | - |
| `additional_value_added_service_info` | [`ValueAddedServices`](../../doc/models/value-added-services.md) | Optional | - |
| `additional_business_info` | [`AdditionalBusinessInfo`](../../doc/models/additional-business-info.md) | Optional | - |
| `funding_type` | [`FundingTypeEnum`](../../doc/models/funding-type-enum.md) | Optional | Application's funding type |
| `integrator_solution_info` | [`IntegratorSolutionInfo`](../../doc/models/integrator-solution-info.md) | Optional | - |
| `additional_lease_info` | [`AdditionalLeaseInfo`](../../doc/models/additional-lease-info.md) | Optional | - |
| `marketing_data_consent_map` | `dict` | Optional | Application's consent form (POL). The valid keys are the numerical value of the marketing consent option (1, 2, 3, etc) |
| `additional_site_survey_info` | [`AdditionalSiteSurveyInfo`](../../doc/models/additional-site-survey-info.md) | Optional | - |
| `kyc_quiz_status_map` | [`dict`](../../doc/models/kyc-quiz-status-map-enum.md) | Optional | Status results of the KCY check. Email to result map. |
| `var_other_details` | [`VarOtherDetails`](../../doc/models/var-other-details.md) | Optional | - |
| `additional_card_pricing_info` | [`AdditionalCardPricingInfo`](../../doc/models/additional-card-pricing-info.md) | Optional | - |
| `sales_office_contact` | [`SalesOfficeContact`](../../doc/models/sales-office-contact.md) | Optional | - |
| `sales_person_contact` | [`SalesPersonContact`](../../doc/models/sales-person-contact.md) | Optional | - |
| `additional_auth_pricing_program_info` | [`AdditionalAuthPricingProgramInfo`](../../doc/models/additional-auth-pricing-program-info.md) | Optional | - |
| `applicant_email` | `string` | Optional | Email address of applicant |
| `partner_document_data` | `dict` | Optional | The data for partner documents |
| `application_id` | `int` | Optional | Application id |

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

