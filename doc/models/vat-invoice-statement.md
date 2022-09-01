
# Vat Invoice Statement

## Structure

`VatInvoiceStatement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type5Enum`](../../doc/models/type-5-enum.md) | Required | VAT Invoice statement format type |
| `media` | [`Media3Enum`](../../doc/models/media-3-enum.md) | Required | VAT Invoice statement media type |
| `address_type` | [`AddressTypeEnum`](../../doc/models/address-type-enum.md) | Optional | [NA] Billing statement address, required should type and media indicate a mailed form |

## Example (as JSON)

```json
{
  "type": "FIXED_BANK_COMPLEX_WITH_RECAP",
  "media": "EMAIL",
  "addressType": null
}
```

