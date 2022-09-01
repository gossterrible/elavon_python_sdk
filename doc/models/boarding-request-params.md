
# Boarding Request Params

## Structure

`BoardingRequestParams`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credit_check_token` | `string` | Optional | [EU] Token provided by credit check response |
| `group_info` | [`GroupInfo`](../../doc/models/group-info.md) | Optional | - |
| `scarecrow_application` | [`ScarecrowApplication`](../../doc/models/scarecrow-application.md) | Required | - |
| `profile_code` | `string` | Optional | The partner's profile code |
| `document_packet_id` | `string` | Optional | The unique identifier for the document packet. For use with createdocumentpacket |

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
  }
}
```

