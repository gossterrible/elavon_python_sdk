
# Debit Network Charge

## Structure

`DebitNetworkCharge`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `type` | [`?string (Type1Enum)`](../../doc/models/type-1-enum.md) | Optional | Type of debit network | getType(): ?string | setType(?string type): void |
| `discountRate` | `?float` | Optional | Network discount rate/fee percent | getDiscountRate(): ?float | setDiscountRate(?float discountRate): void |
| `discountPerItem` | `?float` | Optional | Network discount per item amount/per transaction fee | getDiscountPerItem(): ?float | setDiscountPerItem(?float discountPerItem): void |
| `perAuth` | `?float` | Optional | Network per authorization amount | getPerAuth(): ?float | setPerAuth(?float perAuth): void |

## Example (as JSON)

```json
{
  "type": null,
  "discountRate": null,
  "discountPerItem": null,
  "perAuth": null
}
```

