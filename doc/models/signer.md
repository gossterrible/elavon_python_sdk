
# Signer

## Structure

`Signer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `signer_id` | `string` | Required | The unique signer identifier |
| `signer` | [`Name`](../../doc/models/name.md) | Required | - |
| `email_address` | `string` | Optional | Email Address of signer |
| `principal` | `bool` | Required | Indicator for signer is principal for business entity |
| `signing_complete_url` | `string` | Optional | The redirect URL for completed signing |
| `signing_decline_url` | `string` | Optional | The redirect URL for declined signing |
| `signing_expired_url` | `string` | Optional | The redirect URL for expired signing |
| `language` | `string` | Optional | The signer's preferred language |
| `opt_in_out_1` | `bool` | Optional | Indicator for opt in/out for checkobox1 |
| `opt_in_out_2` | `bool` | Optional | Indicator for opt in/out for checkobox2 |
| `opt_in_out_3` | `bool` | Optional | Indicator for opt in/out for checkobox3 |

## Example (as JSON)

```json
{
  "signerId": null,
  "signer": {
    "firstName": "John",
    "lastName": "Doe"
  },
  "principal": null
}
```

