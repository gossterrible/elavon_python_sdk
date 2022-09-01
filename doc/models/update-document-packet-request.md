
# Update Document Packet Request

## Structure

`UpdateDocumentPacketRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `documentPacketId` | `string` | Required | The unique identifier for the document packet | getDocumentPacketId(): string | setDocumentPacketId(string documentPacketId): void |
| `profileCode` | `?string` | Optional | The partner's profile code | getProfileCode(): ?string | setProfileCode(?string profileCode): void |
| `signers` | [`?(Signer[])`](../../doc/models/signer.md) | Optional | The document signers | getSigners(): ?array | setSigners(?array signers): void |
| `documentPacketData` | [`?DocumentPacketData`](../../doc/models/document-packet-data.md) | Optional | - | getDocumentPacketData(): ?DocumentPacketData | setDocumentPacketData(?DocumentPacketData documentPacketData): void |

## Example (as JSON)

```json
{
  "documentPacketId": "documentPacketId6",
  "profileCode": null,
  "signers": null,
  "documentPacketData": null
}
```

