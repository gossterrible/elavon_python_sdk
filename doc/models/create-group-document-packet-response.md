
# Create Group Document Packet Response

## Structure

`CreateGroupDocumentPacketResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_id` | `int` | Optional | - |
| `error` | `string` | Optional | If processing error occurs, will contain information, else will be empty or null |
| `group_document_packet_id` | `string` | Optional | The unique identifier for the group document packet |

## Example (as JSON)

```json
{
  "responseId": null,
  "error": null,
  "groupDocumentPacketId": null
}
```

