
# Vat Info

## Structure

`VatInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `numberOption` | [`?string (NumberOptionEnum)`](../../doc/models/number-option-enum.md) | Optional | Type of VAT id provieded if tax id type is VAT | getNumberOption(): ?string | setNumberOption(?string numberOption): void |
| `number56B` | `?string` | Optional | VAT 56B number | getNumber56B(): ?string | setNumber56B(?string number56B): void |
| `expiryDate56B` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getExpiryDate56B(): ?DateComponents | setExpiryDate56B(?DateComponents expiryDate56B): void |
| `taxNumberType` | [`?string (TaxNumberTypeEnum)`](../../doc/models/tax-number-type-enum.md) | Optional | The Tax Number Type of the Business | getTaxNumberType(): ?string | setTaxNumberType(?string taxNumberType): void |
| `taxNumber` | `?string` | Optional | The Tax Number Type of the Business | getTaxNumber(): ?string | setTaxNumber(?string taxNumber): void |

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

