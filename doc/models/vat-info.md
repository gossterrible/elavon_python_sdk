
# Vat Info

## Structure

`VatInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number_option` | [`NumberOptionEnum`](../../doc/models/number-option-enum.md) | Optional | Type of VAT id provieded if tax id type is VAT |
| `number_56_b` | `string` | Optional | VAT 56B number |
| `expiry_date_56_b` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `tax_number_type` | [`TaxNumberTypeEnum`](../../doc/models/tax-number-type-enum.md) | Optional | The Tax Number Type of the Business |
| `tax_number` | `string` | Optional | The Tax Number Type of the Business |

## Example (as JSON)

```json
{
  "numberOption": null,
  "number56B": null,
  "expiryDate56B": null,
  "taxNumberType": null,
  "taxNumber": null
}
```

