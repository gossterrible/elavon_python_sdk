
# Exception Item

## Structure

`ExceptionItem`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `type` | `string` | Required | Type of card exception | getType(): string | setType(string type): void |
| `discountRate` | `float` | Required | Card excaption discount rate/fee percentage | getDiscountRate(): float | setDiscountRate(float discountRate): void |
| `discountPerItem` | `float` | Required | Card excaption discount per item/per transaction fee | getDiscountPerItem(): float | setDiscountPerItem(float discountPerItem): void |

## Example (as JSON)

```json
{
  "type": "type0",
  "discountRate": 169.8,
  "discountPerItem": 83.46
}
```

