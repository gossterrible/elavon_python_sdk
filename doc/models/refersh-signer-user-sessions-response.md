
# Refersh Signer User Sessions Response

## Structure

`RefershSignerUserSessionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_id` | `int` | Optional | - |
| `error` | `string` | Optional | Will contain message if unable to process the request |
| `signers` | [`List of SignerResponse`](../../doc/models/signer-response.md) | Required | List of signer and there URL whos session was refreshed |

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

