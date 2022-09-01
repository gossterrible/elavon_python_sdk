
# Dynamic Currency Conversion

## Structure

`DynamicCurrencyConversion`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rebate_percent` | `float` | Required | DCC rebate percentage |
| `mark_up` | [`MarkUpEnum`](../../doc/models/mark-up-enum.md) | Required | DCC markup type. An enum's numerical value usually matches their name, but with an exception: THREE_POINT_TWO_FIVE = 2.85 |
| `currency_group` | [`CurrencyGroupEnum`](../../doc/models/currency-group-enum.md) | Optional | [NA] DCC currency group |
| `registration_fee` | `float` | Optional | [NA] DCC registration fee |

## Example (as JSON)

```json
{
  "rebatePercent": 0.5,
  "markUp": null
}
```

