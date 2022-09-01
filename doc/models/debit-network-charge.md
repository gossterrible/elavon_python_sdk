
# Debit Network Charge

## Structure

`DebitNetworkCharge`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type1Enum`](../../doc/models/type-1-enum.md) | Optional | Type of debit network |
| `discount_rate` | `float` | Optional | Network discount rate/fee percent |
| `discount_per_item` | `float` | Optional | Network discount per item amount/per transaction fee |
| `per_auth` | `float` | Optional | Network per authorization amount |

## Example (as JSON)

```json
{
  "type": null,
  "discountRate": null,
  "discountPerItem": null,
  "perAuth": null
}
```

