
# Upload Document Response

## Structure

`UploadDocumentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `string` | Optional | Error message from service |
| `doc_reference_number` | `string` | Optional | Unique identifier of upload document response |
| `uploaded_documents_response` | [`List of UploadedDocumentDataResponse`](../../doc/models/uploaded-document-data-response.md) | Optional | Listing of individual document upload statuses |

## Example (as JSON)

```json
{
  "error": null,
  "docReferenceNumber": null,
  "uploadedDocumentsResponse": null
}
```

