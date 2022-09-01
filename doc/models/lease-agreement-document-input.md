
# Lease Agreement Document Input

## Structure

`LeaseAgreementDocumentInput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `language` | `string` | Required | Language of document to be generated,  ISO 639-1 standard applies |
| `document_id` | `string` | Required | Unique id of document |
| `agreement_id` | `string` | Optional | Merchant id (MID) |
| `document_packet_id` | `string` | Optional | Document packet id |
| `signed` | `bool` | Optional | Boolean flag indicating if document has been signed, true if  YES, false if NO |
| `grouped_application` | `bool` | Optional | Boolean flag indicating if document is of a group of applications, true if  YES, false if NO |
| `wet_signed` | `bool` | Optional | Boolean flag indicating if document is to be wet signed, true if  YES, false if NO |
| `principal` | [`Person`](../../doc/models/person.md) | Required | - |
| `equipment_info` | [`EquipmentInfo`](../../doc/models/equipment-info.md) | Required | In NA, it's mandatory to have at least one piece of equipment. For third party vendors<br>managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.<br>Contact your Elavon representative for the VAR code(s).<br><br>          In EU, equipmentInfo is optional and no equipment has to be sent. If you have any equipment <br>          managed by Elavon, contact your Elavon representative for the VAR code(s). |
| `vendor_info` | [`ProviderInfo`](../../doc/models/provider-info.md) | Required | - |
| `additional_shareholders` | [`List of Person`](../../doc/models/person.md) | Optional | Application's additional shareholders |
| `business_info` | [`BusinessInfo`](../../doc/models/business-info.md) | Required | - |
| `banking_info` | [`BankingInfo`](../../doc/models/banking-info.md) | Required | - |
| `bank_account_additional_info` | [`BankAccountAdditionalInfo`](../../doc/models/bank-account-additional-info.md) | Required | - |
| `additional_lease_info` | [`AdditionalLeaseInfo`](../../doc/models/additional-lease-info.md) | Required | - |

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
  "vendorInfo": null,
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
  "bankingInfo": {
    "fundingMethod": null,
    "accountNumber": "20581687",
    "sortCode": "121000248"
  },
  "bankAccountAdditionalInfo": null,
  "additionalLeaseInfo": null
}
```

