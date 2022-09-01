
# Upload Documents Request Params

## Structure

`UploadDocumentsRequestParams`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `boardingId` | `string` | Required | MID(EU)/AWB(NA) of application to upload documents for, MID can be used in NA if it has been generated | getBoardingId(): string | setBoardingId(string boardingId): void |
| `clientId` | `string` | Required | Client id of application submission, to be provided to partners, and should match value present on boarding request | getClientId(): string | setClientId(string clientId): void |
| `uniqueId` | `string` | Required | Unique identifier of application submission, alphanumeric. Provided by the client.The uniqueId must be wholly original and never repeated. The client's name followed by a millisecond timestamp would work well. | getUniqueId(): string | setUniqueId(string uniqueId): void |
| `country` | `string` | Required | Country of application submission, ISO 3166-1 alpha-3 standard applies, and should match value present on boarding request | getCountry(): string | setCountry(string country): void |
| `salesRepNumber` | `string` | Required | Identifier of sales representative responsible for submission, should match value present on boarding request | getSalesRepNumber(): string | setSalesRepNumber(string salesRepNumber): void |
| `imageDocumentData` | [`ImageDocumentData`](../../doc/models/image-document-data.md) | Required | - | getImageDocumentData(): ImageDocumentData | setImageDocumentData(ImageDocumentData imageDocumentData): void |

## Example (as JSON)

```json
{
  "boardingId": "2101491576",
  "clientId": "IDNA",
  "uniqueId": "AcmeCorp1572566399123",
  "country": null,
  "salesRepNumber": "12345",
  "imageDocumentData": {
    "docReferenceNumber": null,
    "imageDocuments": {
      "imageId": null,
      "imageTypeCode": "APPLI",
      "dbaName": "Grimm's Bookstore",
      "mimeTypeCode": null,
      "imageContent": null
    }
  }
}
```

