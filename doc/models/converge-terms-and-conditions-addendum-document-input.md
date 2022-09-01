
# Converge Terms and Conditions Addendum Document Input

## Structure

`ConvergeTermsAndConditionsAddendumDocumentInput`

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
| `equipment_info` | [`EquipmentInfo`](../../doc/models/equipment-info.md) | Required | In NA, it's mandatory to have at least one piece of equipment. For third party vendors<br>managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.<br>Contact your Elavon representative for the VAR code(s).<br><br>          In EU, equipmentInfo is optional and no equipment has to be sent. If you have any equipment <br>          managed by Elavon, contact your Elavon representative for the VAR code(s). |

## Example (as JSON)

```json
{
  "language": "en",
  "documentId": "1",
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
  }
}
```

