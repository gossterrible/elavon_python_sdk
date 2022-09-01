
# Refresh Signer Users Sessions Request

## Structure

`RefreshSignerUsersSessionsRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `documentPacketId` | `string` | Required | The unique identifier for a document packet | getDocumentPacketId(): string | setDocumentPacketId(string documentPacketId): void |
| `signerIds` | `string[]` | Required | List of users ids whos session needs refreshing | getSignerIds(): array | setSignerIds(array signerIds): void |

## Example (as JSON)

```json
{
  "documentPacketId": "42f441d0-0c23-468d-8319-f1e2af17dc15",
  "signerIds": null
}
```

