
# Exception Item

## Structure

`ExceptionItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Required | Type of card exception |
| `discount_rate` | `float` | Required | Card excaption discount rate/fee percentage |
| `discount_per_item` | `float` | Required | Card excaption discount per item/per transaction fee |

## Example (as JSON)

```json
{
  "type": "type0",
  "discountRate": 169.8,
  "discountPerItem": 83.46
}
```

