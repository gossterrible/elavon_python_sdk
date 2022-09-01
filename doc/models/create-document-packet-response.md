
# Create Document Packet Response

## Structure

`CreateDocumentPacketResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_id` | `int` | Optional | - |
| `error` | `string` | Optional | If processing error occurs, will contain information, else will be empty or null |
| `document_packet_id` | `string` | Optional | The unique identifier for the document packet |
| `signer_responses` | [`List of SignerResponse`](../../doc/models/signer-response.md) | Optional | The signer containing signer information |

## Example (as JSON)

```json
{
  "responseId": null,
  "error": null,
  "documentPacketId": null,
  "signerResponses": null
}
```

