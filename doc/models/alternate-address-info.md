
# Alternate Address Info

Used to hold information about an alternative business address

## Structure

`AlternateAddressInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `documentNeeded` | `bool` | Required | Flag indicating if documentation is needed in Alternate Address Verification | getDocumentNeeded(): bool | setDocumentNeeded(bool documentNeeded): void |
| `documentVerified` | `?bool` | Optional | Flag indicating if document provided have been verified | getDocumentVerified(): ?bool | setDocumentVerified(?bool documentVerified): void |
| `alternateAddressDocumentType` | [`?string (AlternateAddressDocumentTypeEnum)`](../../doc/models/alternate-address-document-type-enum.md) | Optional | Type of document provided | getAlternateAddressDocumentType(): ?string | setAlternateAddressDocumentType(?string alternateAddressDocumentType): void |
| `documentName` | `?string` | Optional | - | getDocumentName(): ?string | setDocumentName(?string documentName): void |

## Example (as JSON)

```json
{
  "documentNeeded": false,
  "documentVerified": null,
  "alternateAddressDocumentType": null,
  "documentName": null
}
```

