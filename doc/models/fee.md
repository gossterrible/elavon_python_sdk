
# Fee

## Structure

`Fee`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Required | SKU of fee |
| `quantity` | `int` | Required | Quantity of fee |
| `amount` | `float` | Required | Price of fee |
| `frequency` | [`FrequencyEnum`](../../doc/models/frequency-enum.md) | Required | Application of fee |
| `start_month` | [`StartMonthEnum`](../../doc/models/start-month-enum.md) | Optional | [NA] start month |

## Example (as JSON)

```json
{
  "type": "JOI",
  "quantity": 1,
  "amount": 9.99,
  "frequency": null
}
```

