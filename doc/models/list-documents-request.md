
# List Documents Request

## Structure

`ListDocumentsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `equipment_info` | [`EquipmentInfo`](../../doc/models/equipment-info.md) | Optional | In NA, it's mandatory to have at least one piece of equipment. For third party vendors<br>managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.<br>Contact your Elavon representative for the VAR code(s).<br><br>          In EU, equipmentInfo is optional and no equipment has to be sent. If you have any equipment <br>          managed by Elavon, contact your Elavon representative for the VAR code(s). |
| `card_pricing` | [`CardPricing`](../../doc/models/card-pricing.md) | Optional | - |
| `principal` | [`Person`](../../doc/models/person.md) | Optional | - |
| `business_info` | [`BusinessInfo`](../../doc/models/business-info.md) | Optional | - |
| `bank_accounts` | [`dict`](../../doc/models/banking-info.md) | Optional | - |
| `direct_debit_authorized_map` | `dict` | Optional | - |
| `value_adds` | `dict` | Optional | - |
| `profile_code` | `string` | Optional | - |
| `has_government_incentive` | `bool` | Optional | - |
| `has_custom_notes` | `bool` | Optional | - |
| `partner_document_keys` | `List of string` | Optional | **Constraints**: *Unique Items Required* |

## Example (as JSON)

```json
{
  "equipmentInfo": null,
  "cardPricing": null,
  "principal": null,
  "businessInfo": null,
  "bankAccounts": null,
  "directDebitAuthorizedMap": null,
  "valueAdds": null,
  "profileCode": null,
  "hasGovernmentIncentive": null,
  "hasCustomNotes": null,
  "partnerDocumentKeys": null
}
```

