
# Vat Invoice Statement

## Structure

`VatInvoiceStatement`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `type` | [`string (Type5Enum)`](../../doc/models/type-5-enum.md) | Required | VAT Invoice statement format type | getType(): string | setType(string type): void |
| `media` | [`string (Media3Enum)`](../../doc/models/media-3-enum.md) | Required | VAT Invoice statement media type | getMedia(): string | setMedia(string media): void |
| `addressType` | [`?string (AddressTypeEnum)`](../../doc/models/address-type-enum.md) | Optional | [NA] Billing statement address, required should type and media indicate a mailed form | getAddressType(): ?string | setAddressType(?string addressType): void |

## Example (as JSON)

```json
{
  "type": "FIXED_BANK_COMPLEX_WITH_RECAP",
  "media": "EMAIL",
  "addressType": null
}
```

