
# Servlet Registration

## Structure

`ServletRegistration`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `mappings` | `?(string[])` | Optional | - | getMappings(): ?array | setMappings(?array mappings): void |
| `runAsRole` | `?string` | Optional | - | getRunAsRole(): ?string | setRunAsRole(?string runAsRole): void |
| `name` | `?string` | Optional | - | getName(): ?string | setName(?string name): void |
| `className` | `?string` | Optional | - | getClassName(): ?string | setClassName(?string className): void |
| `initParameters` | `?array<string,string>` | Optional | - | getInitParameters(): ?array | setInitParameters(?array initParameters): void |

## Example (as JSON)

```json
{
  "mappings": null,
  "runAsRole": null,
  "name": null,
  "className": null,
  "initParameters": null
}
```

