
# Hemp Grower Info

## Structure

`HempGrowerInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operations_description` | `string` | Required | [NA] Description of type and nature of hemp growers operation<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `200` |
| `is_licensed` | `bool` | Required | [NA] Flag indicating whether the customer is a licensed hemp grower |
| `license_expiration_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `additional_mrb_activity` | `bool` | Required | [NA] Flag indicating whether the customer engages in Marijuana Related Business (MRB) beyond hemp growing |
| `cannabis_revenue_percentage_range` | [`CannabisRevenuePercentageRangeEnum`](../../doc/models/cannabis-revenue-percentage-range-enum.md) | Optional | [NA] Approximate range of percent of business revenue derived from cannabis related sales |

## Example (as JSON)

```json
{
  "operationsDescription": "operationsDescription8",
  "isLicensed": false,
  "licenseExpirationDate": null,
  "additionalMRBActivity": false,
  "cannabisRevenuePercentageRange": null
}
```

