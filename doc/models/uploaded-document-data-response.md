
# Uploaded Document Data Response

## Structure

`UploadedDocumentDataResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `documentId` | `?string` | Optional | Identifier of document passed in prior upload document request | getDocumentId(): ?string | setDocumentId(?string documentId): void |
| `documentStatus` | `?string` | Optional | Status of uploaded document | getDocumentStatus(): ?string | setDocumentStatus(?string documentStatus): void |
| `messages` | [`?BoardingStatusMessage`](../../doc/models/boarding-status-message.md) | Optional | - | getMessages(): ?BoardingStatusMessage | setMessages(?BoardingStatusMessage messages): void |

## Example (as JSON)

```json
{
  "documentId": null,
  "documentStatus": null,
  "messages": null
}
```

