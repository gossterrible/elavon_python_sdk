
# Documentary Info

## Structure

`DocumentaryInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `documentary` | `bool` | Required | Flag indicating if personal documentary info is to be provided, true if Yes, false if NO | getDocumentary(): bool | setDocumentary(bool documentary): void |
| `documentaryVerifier` | [`?string (DocumentaryVerifierEnum)`](../../doc/models/documentary-verifier-enum.md) | Optional | Verifier of documentary information | getDocumentaryVerifier(): ?string | setDocumentaryVerifier(?string documentaryVerifier): void |
| `documentaryIssuer` | `?string` | Optional | Issuer of documentary information | getDocumentaryIssuer(): ?string | setDocumentaryIssuer(?string documentaryIssuer): void |
| `documentaryType` | [`?string (DocumentaryTypeEnum)`](../../doc/models/documentary-type-enum.md) | Optional | Type of documentation provided | getDocumentaryType(): ?string | setDocumentaryType(?string documentaryType): void |
| `idNumber` | `?string` | Optional | Id number of documentation provided | getIdNumber(): ?string | setIdNumber(?string idNumber): void |
| `issueDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getIssueDate(): ?DateComponents | setIssueDate(?DateComponents issueDate): void |
| `expiryDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getExpiryDate(): ?DateComponents | setExpiryDate(?DateComponents expiryDate): void |
| `issuingState` | [`?string (IssuingState1Enum)`](../../doc/models/issuing-state-1-enum.md) | Optional | State of documentation issuance | getIssuingState(): ?string | setIssuingState(?string issuingState): void |
| `foreignIssuingState` | `?string` | Optional | Foreign state of documentation issuance, applicable if State enumeration doesn't contain choice | getForeignIssuingState(): ?string | setForeignIssuingState(?string foreignIssuingState): void |

## Example (as JSON)

```json
{
  "documentary": false,
  "documentaryVerifier": null,
  "documentaryIssuer": null,
  "documentaryType": null,
  "idNumber": null,
  "issueDate": null,
  "expiryDate": null,
  "issuingState": null,
  "foreignIssuingState": null
}
```

