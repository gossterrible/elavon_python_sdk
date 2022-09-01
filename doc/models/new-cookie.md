
# New Cookie

## Structure

`NewCookie`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `name` | `?string` | Optional | - | getName(): ?string | setName(?string name): void |
| `value` | `?string` | Optional | - | getValue(): ?string | setValue(?string value): void |
| `version` | `?int` | Optional | - | getVersion(): ?int | setVersion(?int version): void |
| `path` | `?string` | Optional | - | getPath(): ?string | setPath(?string path): void |
| `domain` | `?string` | Optional | - | getDomain(): ?string | setDomain(?string domain): void |
| `comment` | `?string` | Optional | - | getComment(): ?string | setComment(?string comment): void |
| `maxAge` | `?int` | Optional | - | getMaxAge(): ?int | setMaxAge(?int maxAge): void |
| `expiry` | `?\DateTime` | Optional | - | getExpiry(): ?\DateTime | setExpiry(?\DateTime expiry): void |
| `secure` | `?bool` | Optional | - | getSecure(): ?bool | setSecure(?bool secure): void |
| `httpOnly` | `?bool` | Optional | - | getHttpOnly(): ?bool | setHttpOnly(?bool httpOnly): void |

## Example (as JSON)

```json
{
  "name": null,
  "value": null,
  "version": null,
  "path": null,
  "domain": null,
  "comment": null,
  "maxAge": null,
  "expiry": null,
  "secure": null,
  "httpOnly": null
}
```

