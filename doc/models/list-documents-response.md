
# List Documents Response

## Structure

`ListDocumentsResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `error` | `?string` | Optional | - | getError(): ?string | setError(?string error): void |
| `userDocumentListMap` | [`?array<string,UserDocumentInfo>`](../../doc/models/user-document-info.md) | Optional | - | getUserDocumentListMap(): ?array | setUserDocumentListMap(?array userDocumentListMap): void |

## Example (as JSON)

```json
{
  "responseId": null,
  "error": null,
  "userDocumentListMap": null
}
```

