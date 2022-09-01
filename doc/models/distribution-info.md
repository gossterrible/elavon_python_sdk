
# Distribution Info

## Structure

`DistributionInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `method` | [`string (MethodEnum)`](../../doc/models/method-enum.md) | Required | Method of distribution | getMethod(): string | setMethod(string method): void |
| `addressType` | [`?string (AddressType2Enum)`](../../doc/models/address-type-2-enum.md) | Optional | Physical address, applicable if distribution method is non-electronic | getAddressType(): ?string | setAddressType(?string addressType): void |
| `emailAddress` | `?string` | Optional | Email address, applicable if distribution method is electronic | getEmailAddress(): ?string | setEmailAddress(?string emailAddress): void |

## Example (as JSON)

```json
{
  "method": "NONE",
  "addressType": null,
  "emailAddress": null
}
```

