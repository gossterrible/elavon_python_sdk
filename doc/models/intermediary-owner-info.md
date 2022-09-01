
# Intermediary Owner Info

## Structure

`IntermediaryOwnerInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `intermediary_owners` | [`List of IntermediaryOwner`](../../doc/models/intermediary-owner.md) | Required | Intermediary owners listing |
| `additional_intermediate_owners` | `bool` | Optional | Flag indicating if there are additional intermediary owners beyond the ones noted here, true if YES, false if NO |

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

