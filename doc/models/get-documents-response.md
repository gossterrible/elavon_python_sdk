
# Get Documents Response

## Structure

`GetDocumentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_id` | `int` | Optional | - |
| `error` | `string` | Optional | If processing error occurs, will contain information, else will be empty or null |
| `documents` | `dict` | Optional | A map of documents where the key is a UserDocumentCode and the value the document |

## Example (as JSON)

```json
{
  "responseId": null,
  "error": null,
  "documents": null
}
```

