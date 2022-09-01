
# Get Unsigned Documents Packet Request

## Structure

`GetUnsignedDocumentsPacketRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `documentPacketId` | `?string` | Optional | The unique identifier for the document packet | getDocumentPacketId(): ?string | setDocumentPacketId(?string documentPacketId): void |
| `html` | `?bool` | Optional | If true, the document will be returned as HTML, if false the response will be PDF as a binary stream | getHtml(): ?bool | setHtml(?bool html): void |

## Example (as JSON)

```json
{
  "documentPacketId": null,
  "html": null
}
```

