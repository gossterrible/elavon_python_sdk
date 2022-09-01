
# Get Documents Response

## Structure

`GetDocumentsResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `error` | `?string` | Optional | If processing error occurs, will contain information, else will be empty or null | getError(): ?string | setError(?string error): void |
| `documents` | `?array` | Optional | A map of documents where the key is a UserDocumentCode and the value the document | getDocuments(): ?array | setDocuments(?array documents): void |

## Example (as JSON)

```json
{
  "responseId": null,
  "error": null,
  "documents": null
}
```

