
# Equipment Info

In NA, it's mandatory to have at least one piece of equipment. For third party vendors
managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.
Contact your Elavon representative for the VAR code(s).

          In EU, equipmentInfo is optional and no equipment has to be sent. If you have any equipment 
          managed by Elavon, contact your Elavon representative for the VAR code(s).

## Structure

`EquipmentInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `equipment_items` | [`List of EquipmentItem`](../../doc/models/equipment-item.md) | Required | Equipment item listing |
| `terminal_services` | [`List of TerminalService`](../../doc/models/terminal-service.md) | Optional | Terminal services to be applied to equipment items |
| `training_type` | [`TrainingTypeEnum`](../../doc/models/training-type-enum.md) | Optional | [NA] Type of training to be given for equipment |
| `shipping_method` | [`ShippingMethodEnum`](../../doc/models/shipping-method-enum.md) | Optional | Shipping of equipment priority |
| `network` | [`NetworkEnum`](../../doc/models/network-enum.md) | Optional | Network equipment will be connected to |
| `fusebox_info` | [`FuseboxInfo`](../../doc/models/fusebox-info.md) | Required | - |
| `anticipated_start_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |

## Example (as JSON)

```json
{
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
```

