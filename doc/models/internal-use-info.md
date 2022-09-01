
# Internal Use Info

## Structure

`InternalUseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field_auto_info` | [`FieldAutoInfo`](../../doc/models/field-auto-info.md) | Optional | - |
| `sales_rep_info` | [`SalesRepInfo`](../../doc/models/sales-rep-info.md) | Optional | - |
| `tin_applied_to_all` | `bool` | Optional | Flag for GBAPI for if this app might have business level mappings.  If null assume business level map mode is true |
| `ip_address` | `string` | Optional | [NA] IP Address of the customer who signed the application |

## Example (as JSON)

```json
{
  "fieldAutoInfo": null,
  "salesRepInfo": null,
  "tinAppliedToAll": null,
  "ipAddress": null
}
```

