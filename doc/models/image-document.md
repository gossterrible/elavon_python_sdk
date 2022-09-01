
# Image Document

## Structure

`ImageDocument`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `imageId` | `int` | Required | Unique identifier of document | getImageId(): int | setImageId(int imageId): void |
| `imageTypeCode` | `string` | Required | Type of document to upload, default to "APPLI" | getImageTypeCode(): string | setImageTypeCode(string imageTypeCode): void |
| `dbaName` | `string` | Required | DBA name of application submission document is to be associated with | getDbaName(): string | setDbaName(string dbaName): void |
| `scanDate` | `?\DateTime` | Optional | Date document was scanned | getScanDate(): ?\DateTime | setScanDate(?\DateTime scanDate): void |
| `mimeTypeCode` | [`string (MimeTypeCodeEnum)`](../../doc/models/mime-type-code-enum.md) | Required | MIME type | getMimeTypeCode(): string | setMimeTypeCode(string mimeTypeCode): void |
| `imageContent` | `string[]` | Required | Base 64 encoded document | getImageContent(): array | setImageContent(array imageContent): void |
| `additionalDocumentFields` | [`?(AdditionalDocumentFields[])`](../../doc/models/additional-document-fields.md) | Optional | Additional lable specifications | getAdditionalDocumentFields(): ?array | setAdditionalDocumentFields(?array additionalDocumentFields): void |
| `name` | `?string` | Optional | Document name | getName(): ?string | setName(?string name): void |
| `category` | [`?string (CategoryEnum)`](../../doc/models/category-enum.md) | Optional | Document Category | getCategory(): ?string | setCategory(?string category): void |

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

