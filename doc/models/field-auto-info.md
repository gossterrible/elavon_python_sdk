
# Field Auto Info

## Structure

`FieldAutoInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `requested` | `?bool` | Optional | If field automation was requested | getRequested(): ?bool | setRequested(?bool requested): void |
| `applied` | `?bool` | Optional | If field auomation was applied successfully | getApplied(): ?bool | setApplied(?bool applied): void |
| `monitored` | `?bool` | Optional | Indicator if field automated fields should be monitored for changes | getMonitored(): ?bool | setMonitored(?bool monitored): void |
| `valuesModified` | `?bool` | Optional | Indicator if field automated fields were modified | getValuesModified(): ?bool | setValuesModified(?bool valuesModified): void |
| `fieldAutoReferenceId` | `?string` | Optional | ccih field automation reference id or company id | getFieldAutoReferenceId(): ?string | setFieldAutoReferenceId(?string fieldAutoReferenceId): void |

## Example (as JSON)

```json
{
  "requested": null,
  "applied": null,
  "monitored": null,
  "valuesModified": null,
  "fieldAutoReferenceId": null
}
```

