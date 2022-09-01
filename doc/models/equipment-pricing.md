
# Equipment Pricing

## Structure

`EquipmentPricing`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `amount` | `float` | Required | The cost of the equipment | getAmount(): float | setAmount(float amount): void |
| `purchaseType` | [`?string (PurchaseTypeEnum)`](../../doc/models/purchase-type-enum.md) | Optional | - | getPurchaseType(): ?string | setPurchaseType(?string purchaseType): void |
| `leaseTerm` | `?int` | Optional | - | getLeaseTerm(): ?int | setLeaseTerm(?int leaseTerm): void |
| `vendorCode` | `?int` | Optional | - | getVendorCode(): ?int | setVendorCode(?int vendorCode): void |
| `vendorPlan` | `?string` | Optional | - | getVendorPlan(): ?string | setVendorPlan(?string vendorPlan): void |
| `startMonth` | [`?string (StartMonth1Enum)`](../../doc/models/start-month-1-enum.md) | Optional | - | getStartMonth(): ?string | setStartMonth(?string startMonth): void |
| `startYear` | `?string` | Optional | - | getStartYear(): ?string | setStartYear(?string startYear): void |

## Example (as JSON)

```json
{
  "amount": 200
}
```

