
# Terminal Service

A container to hold any terminal services that should be applied to the equipment

## Structure

`TerminalService`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `type` | [`string (Type6Enum)`](../../doc/models/type-6-enum.md) | Required | Type of terminal service to be provided | getType(): string | setType(string type): void |
| `serviceSpecifics` | `?string` | Optional | [NA] Free text for additional specification of terminal service details | getServiceSpecifics(): ?string | setServiceSpecifics(?string serviceSpecifics): void |

## Example (as JSON)

```json
{
  "type": "NO_TIP",
  "serviceSpecifics": null
}
```

