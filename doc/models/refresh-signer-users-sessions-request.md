
# Refresh Signer Users Sessions Request

## Structure

`RefreshSignerUsersSessionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `document_packet_id` | `string` | Required | The unique identifier for a document packet |
| `signer_ids` | `List of string` | Required | List of users ids whos session needs refreshing |

## Example (as JSON)

```json
{
  "documentPacketId": "42f441d0-0c23-468d-8319-f1e2af17dc15",
  "signerIds": null
}
```

