
# Get Document Response

## Structure

`GetDocumentResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `error` | `?string` | Optional | If processing error occurs, will contain information, else will be empty or null | getError(): ?string | setError(?string error): void |
| `document` | `?array` | Optional | The singular document returned | getDocument(): ?array | setDocument(?array document): void |

## Example (as JSON)

```json
{
  "responseId": null,
  "error": null,
  "document": null
}
```

