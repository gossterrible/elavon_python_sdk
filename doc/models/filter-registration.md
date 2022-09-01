
# Filter Registration

## Structure

`FilterRegistration`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `servletNameMappings` | `?(string[])` | Optional | - | getServletNameMappings(): ?array | setServletNameMappings(?array servletNameMappings): void |
| `urlPatternMappings` | `?(string[])` | Optional | - | getUrlPatternMappings(): ?array | setUrlPatternMappings(?array urlPatternMappings): void |
| `name` | `?string` | Optional | - | getName(): ?string | setName(?string name): void |
| `className` | `?string` | Optional | - | getClassName(): ?string | setClassName(?string className): void |
| `initParameters` | `?array<string,string>` | Optional | - | getInitParameters(): ?array | setInitParameters(?array initParameters): void |

## Example (as JSON)

```json
{
  "servletNameMappings": null,
  "urlPatternMappings": null,
  "name": null,
  "className": null,
  "initParameters": null
}
```

