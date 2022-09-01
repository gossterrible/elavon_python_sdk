
# Upload Document Response

## Structure

`UploadDocumentResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `error` | `?string` | Optional | Error message from service | getError(): ?string | setError(?string error): void |
| `docReferenceNumber` | `?string` | Optional | Unique identifier of upload document response | getDocReferenceNumber(): ?string | setDocReferenceNumber(?string docReferenceNumber): void |
| `uploadedDocumentsResponse` | [`?(UploadedDocumentDataResponse[])`](../../doc/models/uploaded-document-data-response.md) | Optional | Listing of individual document upload statuses | getUploadedDocumentsResponse(): ?array | setUploadedDocumentsResponse(?array uploadedDocumentsResponse): void |

## Example (as JSON)

```json
{
  "error": null,
  "docReferenceNumber": null,
  "uploadedDocumentsResponse": null
}
```

