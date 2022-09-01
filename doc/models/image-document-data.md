
# Image Document Data

## Structure

`ImageDocumentData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `doc_reference_number` | `string` | Required | Unique identifier of document data, alphanumeric |
| `image_documents` | [`List of ImageDocument`](../../doc/models/image-document.md) | Required | Listing of documents to be uploaded |

## Example (as JSON)

```json
{
  "docReferenceNumber": null,
  "imageDocuments": {
    "imageId": null,
    "imageTypeCode": "APPLI",
    "dbaName": "Grimm's Bookstore",
    "mimeTypeCode": null,
    "imageContent": null
  }
}
```

