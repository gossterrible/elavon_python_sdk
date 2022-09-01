
# Signer Status Response

## Structure

`SignerStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `signer_id` | `string` | Required | The unique signer identifier |
| `signer_status` | [`SignerStatusEnum`](../../doc/models/signer-status-enum.md) | Required | The signer's id and state |

## Example (as JSON)

```json
{
  "signerId": "signerId4",
  "signerStatus": "SIGNED"
}
```

