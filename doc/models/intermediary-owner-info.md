
# Intermediary Owner Info

## Structure

`IntermediaryOwnerInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `intermediaryOwners` | [`IntermediaryOwner[]`](../../doc/models/intermediary-owner.md) | Required | Intermediary owners listing | getIntermediaryOwners(): array | setIntermediaryOwners(array intermediaryOwners): void |
| `additionalIntermediateOwners` | `?bool` | Optional | Flag indicating if there are additional intermediary owners beyond the ones noted here, true if YES, false if NO | getAdditionalIntermediateOwners(): ?bool | setAdditionalIntermediateOwners(?bool additionalIntermediateOwners): void |

## Example (as JSON)

```json
{
  "intermediaryOwners": [
    {
      "ownershipPct": null,
      "businessName": null,
      "ownerName": null,
      "phone": null,
      "emailAddress": null,
      "address": null
    },
    {
      "ownershipPct": null,
      "businessName": null,
      "ownerName": null,
      "phone": null,
      "emailAddress": null,
      "address": null
    },
    {
      "ownershipPct": null,
      "businessName": null,
      "ownerName": null,
      "phone": null,
      "emailAddress": null,
      "address": null
    }
  ],
  "additionalIntermediateOwners": null
}
```

