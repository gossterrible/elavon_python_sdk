
# Get Unsigned Documents Packet Request

## Structure

`GetUnsignedDocumentsPacketRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_packet_id` | `string` | Optional | The unique identifier for the document packet |
| `html` | `bool` | Optional | If true, the document will be returned as HTML, if false the response will be PDF as a binary stream |

## Example (as JSON)

```json
{
  "documentPacketId": null,
  "html": null
}
```

