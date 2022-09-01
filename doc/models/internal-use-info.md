
# Internal Use Info

## Structure

`InternalUseInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `fieldAutoInfo` | [`?FieldAutoInfo`](../../doc/models/field-auto-info.md) | Optional | - | getFieldAutoInfo(): ?FieldAutoInfo | setFieldAutoInfo(?FieldAutoInfo fieldAutoInfo): void |
| `salesRepInfo` | [`?SalesRepInfo`](../../doc/models/sales-rep-info.md) | Optional | - | getSalesRepInfo(): ?SalesRepInfo | setSalesRepInfo(?SalesRepInfo salesRepInfo): void |
| `tinAppliedToAll` | `?bool` | Optional | Flag for GBAPI for if this app might have business level mappings.  If null assume business level map mode is true | getTinAppliedToAll(): ?bool | setTinAppliedToAll(?bool tinAppliedToAll): void |
| `ipAddress` | `?string` | Optional | [NA] IP Address of the customer who signed the application | getIpAddress(): ?string | setIpAddress(?string ipAddress): void |

## Example (as JSON)

```json
{
  "fieldAutoInfo": null,
  "salesRepInfo": null,
  "tinAppliedToAll": null,
  "ipAddress": null
}
```

