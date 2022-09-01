
# Create Document Packet Response

## Structure

`CreateDocumentPacketResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `error` | `?string` | Optional | If processing error occurs, will contain information, else will be empty or null | getError(): ?string | setError(?string error): void |
| `documentPacketId` | `?string` | Optional | The unique identifier for the document packet | getDocumentPacketId(): ?string | setDocumentPacketId(?string documentPacketId): void |
| `signerResponses` | [`?(SignerResponse[])`](../../doc/models/signer-response.md) | Optional | The signer containing signer information | getSignerResponses(): ?array | setSignerResponses(?array signerResponses): void |

## Example (as JSON)

```json
{
  "responseId": null,
  "error": null,
  "documentPacketId": null,
  "signerResponses": null
}
```

