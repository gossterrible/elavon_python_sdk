
# Exception Charge

## Structure

`ExceptionCharge`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `type` | [`?string (TypeEnum)`](../../doc/models/type-enum.md) | Optional | Type of exception charge | getType(): ?string | setType(?string type): void |
| `discountRate` | `?float` | Optional | Exception charge discount rate/percentage fee | getDiscountRate(): ?float | setDiscountRate(?float discountRate): void |
| `discountPerItem` | `?float` | Optional | Exception charge discount amount/per transaction fee | getDiscountPerItem(): ?float | setDiscountPerItem(?float discountPerItem): void |

## Example (as JSON)

```json
{
  "type": null,
  "discountRate": null,
  "discountPerItem": null
}
```

