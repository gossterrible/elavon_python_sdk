
# Module

## Structure

`Module`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `layer` | `?array` | Optional | - | getLayer(): ?array | setLayer(?array layer): void |
| `name` | `?string` | Optional | - | getName(): ?string | setName(?string name): void |
| `descriptor` | [`?ModuleDescriptor`](../../doc/models/module-descriptor.md) | Optional | - | getDescriptor(): ?ModuleDescriptor | setDescriptor(?ModuleDescriptor descriptor): void |
| `classLoader` | [`?ClassLoader`](../../doc/models/class-loader.md) | Optional | - | getClassLoader(): ?ClassLoader | setClassLoader(?ClassLoader classLoader): void |
| `annotations` | `?(array[])` | Optional | - | getAnnotations(): ?array | setAnnotations(?array annotations): void |
| `declaredAnnotations` | `?(array[])` | Optional | - | getDeclaredAnnotations(): ?array | setDeclaredAnnotations(?array declaredAnnotations): void |
| `named` | `?bool` | Optional | - | getNamed(): ?bool | setNamed(?bool named): void |
| `packages` | `?(string[])` | Optional | **Constraints**: *Unique Items Required* | getPackages(): ?array | setPackages(?array packages): void |

## Example (as JSON)

```json
{
  "layer": null,
  "name": null,
  "descriptor": null,
  "classLoader": null,
  "annotations": null,
  "declaredAnnotations": null,
  "named": null,
  "packages": null
}
```

