
# Hemp Grower Info

## Structure

`HempGrowerInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `operationsDescription` | `string` | Required | [NA] Description of type and nature of hemp growers operation<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `200` | getOperationsDescription(): string | setOperationsDescription(string operationsDescription): void |
| `isLicensed` | `bool` | Required | [NA] Flag indicating whether the customer is a licensed hemp grower | getIsLicensed(): bool | setIsLicensed(bool isLicensed): void |
| `licenseExpirationDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getLicenseExpirationDate(): ?DateComponents | setLicenseExpirationDate(?DateComponents licenseExpirationDate): void |
| `additionalMRBActivity` | `bool` | Required | [NA] Flag indicating whether the customer engages in Marijuana Related Business (MRB) beyond hemp growing | getAdditionalMRBActivity(): bool | setAdditionalMRBActivity(bool additionalMRBActivity): void |
| `cannabisRevenuePercentageRange` | [`?string (CannabisRevenuePercentageRangeEnum)`](../../doc/models/cannabis-revenue-percentage-range-enum.md) | Optional | [NA] Approximate range of percent of business revenue derived from cannabis related sales | getCannabisRevenuePercentageRange(): ?string | setCannabisRevenuePercentageRange(?string cannabisRevenuePercentageRange): void |

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

