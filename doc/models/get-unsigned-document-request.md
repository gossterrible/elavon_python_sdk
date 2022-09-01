
# Get Unsigned Document Request

## Structure

`GetUnsignedDocumentRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `documentPacketId` | `?string` | Optional | The unique identifier for the document packet | getDocumentPacketId(): ?string | setDocumentPacketId(?string documentPacketId): void |
| `html` | `?bool` | Optional | If true, the document will be returned as HTML, if false the response will be PDF as a binary stream | getHtml(): ?bool | setHtml(?bool html): void |
| `code` | [`?string (CodeEnum)`](../../doc/models/code-enum.md) | Optional | The code related to which unsigned document is desired | getCode(): ?string | setCode(?string code): void |
| `cardinalNumber` | `?int` | Optional | For PARTNER_DOCUMENTS. The cardinal related to which partner document is desired | getCardinalNumber(): ?int | setCardinalNumber(?int cardinalNumber): void |

## Example (as JSON)

```json
{
  "documentPacketId": null,
  "html": null,
  "code": null,
  "cardinalNumber": null
}
```

