
# Alternate Address Info

Used to hold information about an alternative business address

## Structure

`AlternateAddressInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_needed` | `bool` | Required | Flag indicating if documentation is needed in Alternate Address Verification |
| `document_verified` | `bool` | Optional | Flag indicating if document provided have been verified |
| `alternate_address_document_type` | [`AlternateAddressDocumentTypeEnum`](../../doc/models/alternate-address-document-type-enum.md) | Optional | Type of document provided |
| `document_name` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "documentNeeded": false,
  "documentVerified": null,
  "alternateAddressDocumentType": null,
  "documentName": null
}
```

