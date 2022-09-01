
# Documentary Info

## Structure

`DocumentaryInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documentary` | `bool` | Required | Flag indicating if personal documentary info is to be provided, true if Yes, false if NO |
| `documentary_verifier` | [`DocumentaryVerifierEnum`](../../doc/models/documentary-verifier-enum.md) | Optional | Verifier of documentary information |
| `documentary_issuer` | `string` | Optional | Issuer of documentary information |
| `documentary_type` | [`DocumentaryTypeEnum`](../../doc/models/documentary-type-enum.md) | Optional | Type of documentation provided |
| `id_number` | `string` | Optional | Id number of documentation provided |
| `issue_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `expiry_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `issuing_state` | [`IssuingState1Enum`](../../doc/models/issuing-state-1-enum.md) | Optional | State of documentation issuance |
| `foreign_issuing_state` | `string` | Optional | Foreign state of documentation issuance, applicable if State enumeration doesn't contain choice |

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

