
# Image Document

## Structure

`ImageDocument`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `image_id` | `int` | Required | Unique identifier of document |
| `image_type_code` | `string` | Required | Type of document to upload, default to "APPLI" |
| `dba_name` | `string` | Required | DBA name of application submission document is to be associated with |
| `scan_date` | `datetime` | Optional | Date document was scanned |
| `mime_type_code` | [`MimeTypeCodeEnum`](../../doc/models/mime-type-code-enum.md) | Required | MIME type |
| `image_content` | `List of string` | Required | Base 64 encoded document |
| `additional_document_fields` | [`List of AdditionalDocumentFields`](../../doc/models/additional-document-fields.md) | Optional | Additional lable specifications |
| `name` | `string` | Optional | Document name |
| `category` | [`CategoryEnum`](../../doc/models/category-enum.md) | Optional | Document Category |

## Example (as JSON)

```json
{
  "imageId": null,
  "imageTypeCode": "APPLI",
  "dbaName": "Grimm's Bookstore",
  "mimeTypeCode": null,
  "imageContent": null
}
```

