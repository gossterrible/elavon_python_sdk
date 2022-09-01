
# Class Loader

## Structure

`ClassLoader`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `parent` | [`?ClassLoader`](../../doc/models/class-loader.md) | Optional | - | getParent(): ?ClassLoader | setParent(?ClassLoader parent): void |
| `name` | `?string` | Optional | - | getName(): ?string | setName(?string name): void |
| `unnamedModule` | [`?Module`](../../doc/models/module.md) | Optional | - | getUnnamedModule(): ?Module | setUnnamedModule(?Module unnamedModule): void |
| `registeredAsParallelCapable` | `?bool` | Optional | - | getRegisteredAsParallelCapable(): ?bool | setRegisteredAsParallelCapable(?bool registeredAsParallelCapable): void |
| `definedPackages` | [`?(Package[])`](../../doc/models/package.md) | Optional | - | getDefinedPackages(): ?array | setDefinedPackages(?array definedPackages): void |

## Example (as JSON)

```json
{
  "parent": null,
  "name": null,
  "unnamedModule": null,
  "registeredAsParallelCapable": null,
  "definedPackages": null
}
```

