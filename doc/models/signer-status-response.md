
# Signer Status Response

## Structure

`SignerStatusResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `signerId` | `string` | Required | The unique signer identifier | getSignerId(): string | setSignerId(string signerId): void |
| `signerStatus` | [`string (SignerStatusEnum)`](../../doc/models/signer-status-enum.md) | Required | The signer's id and state | getSignerStatus(): string | setSignerStatus(string signerStatus): void |

## Example (as JSON)

```json
{
  "signerId": "signerId4",
  "signerStatus": "SIGNED"
}
```

