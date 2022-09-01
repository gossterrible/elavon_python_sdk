
# Equipment Info

In NA, it's mandatory to have at least one piece of equipment. For third party vendors
managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.
Contact your Elavon representative for the VAR code(s).

          In EU, equipmentInfo is optional and no equipment has to be sent. If you have any equipment 
          managed by Elavon, contact your Elavon representative for the VAR code(s).

## Structure

`EquipmentInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `equipmentItems` | [`EquipmentItem[]`](../../doc/models/equipment-item.md) | Required | Equipment item listing | getEquipmentItems(): array | setEquipmentItems(array equipmentItems): void |
| `terminalServices` | [`?(TerminalService[])`](../../doc/models/terminal-service.md) | Optional | Terminal services to be applied to equipment items | getTerminalServices(): ?array | setTerminalServices(?array terminalServices): void |
| `trainingType` | [`?string (TrainingTypeEnum)`](../../doc/models/training-type-enum.md) | Optional | [NA] Type of training to be given for equipment | getTrainingType(): ?string | setTrainingType(?string trainingType): void |
| `shippingMethod` | [`?string (ShippingMethodEnum)`](../../doc/models/shipping-method-enum.md) | Optional | Shipping of equipment priority | getShippingMethod(): ?string | setShippingMethod(?string shippingMethod): void |
| `network` | [`?string (NetworkEnum)`](../../doc/models/network-enum.md) | Optional | Network equipment will be connected to | getNetwork(): ?string | setNetwork(?string network): void |
| `fuseboxInfo` | [`FuseboxInfo`](../../doc/models/fusebox-info.md) | Required | - | getFuseboxInfo(): FuseboxInfo | setFuseboxInfo(FuseboxInfo fuseboxInfo): void |
| `anticipatedStartDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getAnticipatedStartDate(): ?DateComponents | setAnticipatedStartDate(?DateComponents anticipatedStartDate): void |

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

