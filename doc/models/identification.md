
# Identification

## Structure

`Identification`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `idType` | [`string (IdTypeEnum)`](../../doc/models/id-type-enum.md) | Required | Type of id provieded | getIdType(): string | setIdType(string idType): void |
| `idNumber` | `string` | Required | Id number<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `30` | getIdNumber(): string | setIdNumber(string idNumber): void |
| `expiryDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getExpiryDate(): ?DateComponents | setExpiryDate(?DateComponents expiryDate): void |
| `issueDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getIssueDate(): ?DateComponents | setIssueDate(?DateComponents issueDate): void |
| `issuingCountry` | `?string` | Optional | Id issuing country, ISO 3166-1 alpha-3 standard applies | getIssuingCountry(): ?string | setIssuingCountry(?string issuingCountry): void |
| `issuingState` | [`?string (IssuingStateEnum)`](../../doc/models/issuing-state-enum.md) | Optional | Id issuing state | getIssuingState(): ?string | setIssuingState(?string issuingState): void |
| `idName` | `?string` | Optional | Name of Id | getIdName(): ?string | setIdName(?string idName): void |
| `issuingAgency` | `?string` | Optional | Id issuing agency | getIssuingAgency(): ?string | setIssuingAgency(?string issuingAgency): void |

## Example (as JSON)

```json
{
  "idType": null,
  "idNumber": "123456789"
}
```

