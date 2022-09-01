
# Business Info

## Structure

`BusinessInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dba_name` | `string` | Required | Doing Business As name for business<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `32` |
| `dba_name_extended` | `string` | Required | Doing Business As name for business, character limit extended<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `business_address` | [`Address`](../../doc/models/address.md) | Required | - |
| `legal_name` | `string` | Required | Certified legal name of business<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `legal_name_extended` | `string` | Required | Certified legal name of business, character limit extended<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `legal_name_marked` | `List of string` | Optional | Certified legal name of business, permits accented characters, required in POL |
| `additional_addresses` | [`dict`](../../doc/models/address.md) | Required | Container of other addresses, legal required.The valid keys are as follows: BUSINESS, LEGAL, SHIPPING, MAILING, PRINCIPAL, PREVIOUS, STATEMENT |
| `ownership_type` | [`OwnershipTypeEnum`](../../doc/models/ownership-type-enum.md) | Required | Type of business |
| `registration_number` | `string` | Optional | [EU] Registration number of business, required for LIMITED_LIBABILITY_PARTNERSHIP, LIMITED_COMPANY, or PUBLIC_LIMITED_COMPANY<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `15` |
| `tax_id` | `string` | Optional | Business tax ID. For testing a valid tax ID, use format 78742xxxx where 'xxxx' represents a series of four random, non-repeating, non-sequential numbers<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `15` |
| `tax_id_type` | [`TaxIDTypeEnum`](../../doc/models/tax-id-type-enum.md) | Optional | [NA] Type of tax id provieded |
| `vat_info` | [`VatInfo`](../../doc/models/vat-info.md) | Optional | - |
| `tax_form_type` | [`TaxFormTypeEnum`](../../doc/models/tax-form-type-enum.md) | Optional | [NA] Type of tax form provided |
| `tax_class_type` | [`TaxClassTypeEnum`](../../doc/models/tax-class-type-enum.md) | Optional | [NA] Type of business's tax classification |
| `customer_membership_number` | `string` | Optional | [NA] Business membership number (ex. COSTCO)<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `12` |
| `product_description` | `string` | Required | Description of product/service business provides<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `mcc_code` | `string` | Required | Extended MCC code business qualifies as<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `5` |
| `establishment_year` | `string` | Required | Year business was established |
| `current_ownership_years` | `string` | Required | Years business has been in control of current ownership |
| `current_ownership_months` | `string` | Required | Months business has been in control of current ownership |
| `government_owned_entity` | `bool` | Optional | [EU] Indicate if more than 50% of the business is owned by the government. This field is mandatory for all ownership types. |
| `communication_language` | `string` | Required | Language to be used for legal documents and communication between business and customer, ISO 639-1 standard applies |
| `pos_language` | `string` | Required | Language to be used for equipment displays, ISO 639-1 standard applies |
| `store_number` | `string` | Optional | [EU] Business store number<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `10` |
| `association_codes` | `List of string` | Optional | [EU] Elavon promotion/assocation code listing |
| `opt_out` | `bool` | Optional | [EU] Elavon marketing opt out flag, true if opt out YES, false if opt out NO |
| `sign_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `pci_info` | [`PCIInfo`](../../doc/models/pci-info.md) | Optional | - |
| `employer_id` | `string` | Optional | [NA] Employer id |
| `country_of_origin` | `string` | Optional | Country of business origin, ISO 3166-1 alpha-3 standard applies |
| `exemption_type` | [`ExemptionTypeEnum`](../../doc/models/exemption-type-enum.md) | Optional | [NA] Exemption type of business (AML) |
| `owner_exemption_type` | [`OwnerExemptionTypeEnum`](../../doc/models/owner-exemption-type-enum.md) | Optional | [NA] Exemption type of owner (AML) |
| `number_of_partners` | [`NumberOfPartnersEnum`](../../doc/models/number-of-partners-enum.md) | Optional | [EU] Number of partners business has, applicable if business is any kind of PARTNERSHIP |
| `relationship_mgr_code` | `string` | Optional | [EU] Relationship manager code |
| `country_of_primary_operation` | `string` | Optional | Country of business primary operation, ISO 3166-1 alpha-3 standard applies |
| `bearer_shares` | `bool` | Optional | [NA] Flag indicating if business has bearer shares, true if YES, false if NO |
| `legal_status` | [`LegalStatusEnum`](../../doc/models/legal-status-enum.md) | Optional | [NA] Business entity legal status |
| `verifications` | [`dict`](../../doc/models/verification-info.md) | Optional | [NA] Anti-Money Laundering (AML) oriented documentation info for the business. The valid keys are as follows: BUSINESS, LEGAL, SHIPPING, MAILING, PRINCIPAL, PREVIOUS, STATEMENT |
| `industry_class` | [`IndustryClassEnum`](../../doc/models/industry-class-enum.md) | Optional | [NA] Business industry classification |
| `no_plates` | `bool` | Optional | [NA] Flag indicating if plates are to be delivered to business, true if no delivery, false if yes to delivery (NA) |
| `agent_number` | `string` | Optional | [NA] Agent number |
| `location_mid_range` | [`LocationMidRangeEnum`](../../doc/models/location-mid-range-enum.md) | Optional | [EU] 10 character MID range for Nordics. |
| `hemp_grower_info` | [`HempGrowerInfo`](../../doc/models/hemp-grower-info.md) | Optional | - |
| `credit_decision_info` | [`CreditDecisionInfo`](../../doc/models/credit-decision-info.md) | Optional | - |

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

