
# Distribution Info

## Structure

`DistributionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `method` | [`MethodEnum`](../../doc/models/method-enum.md) | Required | Method of distribution |
| `address_type` | [`AddressType2Enum`](../../doc/models/address-type-2-enum.md) | Optional | Physical address, applicable if distribution method is non-electronic |
| `email_address` | `string` | Optional | Email address, applicable if distribution method is electronic |

## Example (as JSON)

```json
{
  "method": "NONE",
  "addressType": null,
  "emailAddress": null
}
```

