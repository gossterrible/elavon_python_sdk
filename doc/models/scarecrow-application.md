
# Scarecrow Application

## Structure

`ScarecrowApplication`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `string` | Required | Client id of application submission, to be provided to partners |
| `client_group_number` | `string` | Optional | Client group number of application submission, paris with parent entity, to be provided to partners, required in NA |
| `unique_id` | `string` | Required | Unique identifier of application submission, alphanumeric. Provided by the client.The uniqueId must be wholly original and never repeated. The client's name followed by a millisecond timestamp would work well.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `32` |
| `banker_id` | `string` | Optional | [EU] Identifier of banker responsible for submission |
| `banker_partner_id` | `string` | Optional | [EU] Identifier of banker partner responsible for submission |
| `country` | `string` | Required | Country of application submission, ISO 3166-1 alpha-3 standard applies |
| `principal` | [`Person`](../../doc/models/person.md) | Required | - |
| `business_info` | [`BusinessInfo`](../../doc/models/business-info.md) | Required | - |
| `financial_info` | [`FinancialInfo`](../../doc/models/financial-info.md) | Required | - |
| `sales_rep_code` | `string` | Required | Identifier of sales representative responsible for submission |
| `additional_shareholders` | [`List of Person`](../../doc/models/person.md) | Optional | - |
| `contact` | [`Person`](../../doc/models/person.md) | Required | - |
| `bank_accounts` | [`dict`](../../doc/models/banking-info.md) | Required | Bank account container. Valid keys are as follows: BILLING, DEPOSIT, LEASE, CHARGEBACK |
| `card_pricing` | [`CardPricing`](../../doc/models/card-pricing.md) | Required | - |
| `fees` | [`List of Fee`](../../doc/models/fee.md) | Optional | - |
| `monetary_pricing_program` | `string` | Optional | Pricing program also called MPP/NPP, to be provided to partners, required in EU |
| `authenticate_pricing_program` | `string` | Optional | Pricing program also called APP, to be provided to partners, required in EU |
| `parent_entity` | `string` | Required | Entity that is parent to submisssion, forms a pair with client group, to be provided to partners |
| `short_name` | `string` | Optional | [NA] |
| `fraud_check_result` | [`FraudCheckResult`](../../doc/models/fraud-check-result.md) | Optional | - |
| `site_survey` | [`SiteSurvey`](../../doc/models/site-survey.md) | Optional | - |
| `dynamic_currency_conversion` | [`DynamicCurrencyConversion`](../../doc/models/dynamic-currency-conversion.md) | Optional | - |
| `billing_statement` | [`BillingStatement`](../../doc/models/billing-statement.md) | Optional | - |
| `funding_statement` | [`FundingStatement`](../../doc/models/funding-statement.md) | Optional | - |
| `electronic_statement` | [`ElectronicStatement`](../../doc/models/electronic-statement.md) | Optional | - |
| `vat_invoice_statement` | [`VatInvoiceStatement`](../../doc/models/vat-invoice-statement.md) | Optional | - |
| `billing_method` | [`BillingMethodEnum`](../../doc/models/billing-method-enum.md) | Optional | [NA] NETCREDIT or GROSS |
| `referrer_name` | `string` | Optional | Application submission's referrer name, to be provided to partners, required in NA |
| `referrer_reference_number` | `string` | Optional | The reference number associated with the referrer, known by Elavon.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `10` |
| `previous_processor` | `string` | Optional | [NA] Customer's previous payment processor |
| `value_added_info` | [`ValueAddedInfo`](../../doc/models/value-added-info.md) | Optional | - |
| `equipment_info` | [`EquipmentInfo`](../../doc/models/equipment-info.md) | Optional | In NA, it's mandatory to have at least one piece of equipment. For third party vendors<br>managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.<br>Contact your Elavon representative for the VAR code(s).<br><br>          In EU, equipmentInfo is optional and no equipment has to be sent. If you have any equipment <br>          managed by Elavon, contact your Elavon representative for the VAR code(s). |
| `branch_number` | `string` | Optional | Bank branch number associated with application submission |
| `branch_code` | `string` | Optional | Bank branch code associated with application submission |
| `self_boarded_external` | `bool` | Optional | [NA] Flag indicating if application is self boarded externally, suppresses forms of post-boarding contact |
| `employee_number` | `string` | Optional | Number used to identify a specific employee |
| `rep_referral_number` | `string` | Optional | Number used to identify a specific representative |
| `promotional_code` | `string` | Optional | A discount/promotional code |
| `chain_info` | [`ChainInfo`](../../doc/models/chain-info.md) | Optional | - |
| `distributions` | [`dict`](../../doc/models/distribution-info.md) | Optional | Distribution container for chargebacks and retrievals. The valid keys are as follows: CHARGEBACK, RETRIEVAL |
| `additional_location_info` | [`AdditionalLocationInfo`](../../doc/models/additional-location-info.md) | Optional | - |
| `signed_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `signed_type` | [`SignedTypeEnum`](../../doc/models/signed-type-enum.md) | Optional | [NA] How application was signed |
| `intermediary_owner_info` | [`IntermediaryOwnerInfo`](../../doc/models/intermediary-owner-info.md) | Optional | - |
| `revenue_share_info` | [`RevenueShareInfo`](../../doc/models/revenue-share-info.md) | Optional | - |
| `elavon_contract` | [`ElavonContractEnum`](../../doc/models/elavon-contract-enum.md) | Optional | [EU] Determine which Merchant Agreement customer will sign |
| `internal_use_info` | [`InternalUseInfo`](../../doc/models/internal-use-info.md) | Optional | - |
| `eframe_info` | [`EframeInfo`](../../doc/models/eframe-info.md) | Optional | - |
| `partner_info` | [`PartnerInfo`](../../doc/models/partner-info.md) | Optional | - |
| `alternative_payment_methods` | [`List of ApmAcquirer`](../../doc/models/apm-acquirer.md) | Optional | [EU] List of Alternative Payment Method Acquirers container |

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

