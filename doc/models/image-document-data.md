
# Image Document Data

## Structure

`ImageDocumentData`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `docReferenceNumber` | `string` | Required | Unique identifier of document data, alphanumeric | getDocReferenceNumber(): string | setDocReferenceNumber(string docReferenceNumber): void |
| `imageDocuments` | [`ImageDocument[]`](../../doc/models/image-document.md) | Required | Listing of documents to be uploaded | getImageDocuments(): array | setImageDocuments(array imageDocuments): void |

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

