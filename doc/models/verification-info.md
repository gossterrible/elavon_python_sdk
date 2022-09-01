
# Verification Info

## Structure

`VerificationInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `documentary` | `bool` | Required | Flag indicating if business or legal documentary/verification info is to be provided, true if Yes, false if NO | getDocumentary(): bool | setDocumentary(bool documentary): void |
| `issuingCountry` | `?string` | Optional | Country of documentation issuance, ISO 3166-1 alpha-3 standard applies | getIssuingCountry(): ?string | setIssuingCountry(?string issuingCountry): void |
| `issuingState` | [`?string (IssuingState1Enum)`](../../doc/models/issuing-state-1-enum.md) | Optional | State of documentation issuance | getIssuingState(): ?string | setIssuingState(?string issuingState): void |
| `sitePersonMet` | `?string` | Optional | If site survey conducted for verification instead of documentation, this is the person on site met with | getSitePersonMet(): ?string | setSitePersonMet(?string sitePersonMet): void |
| `siteVisitDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getSiteVisitDate(): ?DateComponents | setSiteVisitDate(?DateComponents siteVisitDate): void |
| `idNumber` | `?string` | Optional | Id number of documentation provided | getIdNumber(): ?string | setIdNumber(?string idNumber): void |
| `issueDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getIssueDate(): ?DateComponents | setIssueDate(?DateComponents issueDate): void |
| `expiryDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getExpiryDate(): ?DateComponents | setExpiryDate(?DateComponents expiryDate): void |
| `documentType` | [`?string (DocumentTypeEnum)`](../../doc/models/document-type-enum.md) | Optional | Type of documentation provided | getDocumentType(): ?string | setDocumentType(?string documentType): void |

## Example (as JSON)

```json
{
  "documentary": false,
  "issuingCountry": null,
  "issuingState": null,
  "sitePersonMet": null,
  "siteVisitDate": null,
  "idNumber": null,
  "issueDate": null,
  "expiryDate": null,
  "documentType": null
}
```

