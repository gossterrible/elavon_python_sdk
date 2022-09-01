
# Check Document Signing Status Response

## Structure

`CheckDocumentSigningStatusResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `packetStatus` | [`string (PacketStatusEnum)`](../../doc/models/packet-status-enum.md) | Required | The document packet's status | getPacketStatus(): string | setPacketStatus(string packetStatus): void |
| `signers` | [`SignerStatusResponse[]`](../../doc/models/signer-status-response.md) | Required | Signers and their status for a document status | getSigners(): array | setSigners(array signers): void |
| `error` | `?string` | Optional | Any error that resulted from the request | getError(): ?string | setError(?string error): void |

## Example (as JSON)

```json
{
  "responseId": null,
  "packetStatus": "ACTIVE",
  "signers": [
    {
      "signerId": "signerId8",
      "signerStatus": "DRAFT"
    },
    {
      "signerId": "signerId9",
      "signerStatus": "EXPIRED"
    }
  ],
  "error": null
}
```

