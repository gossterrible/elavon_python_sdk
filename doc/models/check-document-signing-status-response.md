
# Check Document Signing Status Response

## Structure

`CheckDocumentSigningStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_id` | `int` | Optional | - |
| `packet_status` | [`PacketStatusEnum`](../../doc/models/packet-status-enum.md) | Required | The document packet's status |
| `signers` | [`List of SignerStatusResponse`](../../doc/models/signer-status-response.md) | Required | Signers and their status for a document status |
| `error` | `string` | Optional | Any error that resulted from the request |

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

