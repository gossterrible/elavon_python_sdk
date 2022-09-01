
# Update Document Packet Request

## Structure

`UpdateDocumentPacketRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_packet_id` | `string` | Required | The unique identifier for the document packet |
| `profile_code` | `string` | Optional | The partner's profile code |
| `signers` | [`List of Signer`](../../doc/models/signer.md) | Optional | The document signers |
| `document_packet_data` | [`DocumentPacketData`](../../doc/models/document-packet-data.md) | Optional | - |

## Example (as JSON)

```json
{
  "documentPacketId": "documentPacketId6",
  "profileCode": null,
  "signers": null,
  "documentPacketData": null
}
```

