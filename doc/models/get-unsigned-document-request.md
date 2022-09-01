
# Get Unsigned Document Request

## Structure

`GetUnsignedDocumentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_packet_id` | `string` | Optional | The unique identifier for the document packet |
| `html` | `bool` | Optional | If true, the document will be returned as HTML, if false the response will be PDF as a binary stream |
| `code` | [`CodeEnum`](../../doc/models/code-enum.md) | Optional | The code related to which unsigned document is desired |
| `cardinal_number` | `int` | Optional | For PARTNER_DOCUMENTS. The cardinal related to which partner document is desired |

## Example (as JSON)

```json
{
  "documentPacketId": null,
  "html": null,
  "code": null,
  "cardinalNumber": null
}
```

