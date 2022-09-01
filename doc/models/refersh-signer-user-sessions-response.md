
# Refersh Signer User Sessions Response

## Structure

`RefershSignerUserSessionsResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `error` | `?string` | Optional | Will contain message if unable to process the request | getError(): ?string | setError(?string error): void |
| `signers` | [`SignerResponse[]`](../../doc/models/signer-response.md) | Required | List of signer and there URL whos session was refreshed | getSigners(): array | setSigners(array signers): void |

## Example (as JSON)

```json
{
  "responseId": null,
  "error": null,
  "signers": [
    {
      "signerId": "signerId8",
      "signerUrl": "signerUrl0"
    },
    {
      "signerId": "signerId9",
      "signerUrl": "signerUrl1"
    }
  ]
}
```

