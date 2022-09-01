
# Verification Info

## Structure

`VerificationInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documentary` | `bool` | Required | Flag indicating if business or legal documentary/verification info is to be provided, true if Yes, false if NO |
| `issuing_country` | `string` | Optional | Country of documentation issuance, ISO 3166-1 alpha-3 standard applies |
| `issuing_state` | [`IssuingState1Enum`](../../doc/models/issuing-state-1-enum.md) | Optional | State of documentation issuance |
| `site_person_met` | `string` | Optional | If site survey conducted for verification instead of documentation, this is the person on site met with |
| `site_visit_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `id_number` | `string` | Optional | Id number of documentation provided |
| `issue_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `expiry_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `document_type` | [`DocumentTypeEnum`](../../doc/models/document-type-enum.md) | Optional | Type of documentation provided |

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

