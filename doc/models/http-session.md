
# Http Session

## Structure

`HttpSession`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `creationTime` | `?int` | Optional | - | getCreationTime(): ?int | setCreationTime(?int creationTime): void |
| `id` | `?string` | Optional | - | getId(): ?string | setId(?string id): void |
| `mNew` | `?bool` | Optional | - | getMNew(): ?bool | setMNew(?bool mNew): void |
| `attributeNames` | `?array` | Optional | - | getAttributeNames(): ?array | setAttributeNames(?array attributeNames): void |
| `sessionContext` | [`?HttpSessionContext`](../../doc/models/http-session-context.md) | Optional | - | getSessionContext(): ?HttpSessionContext | setSessionContext(?HttpSessionContext sessionContext): void |
| `lastAccessedTime` | `?int` | Optional | - | getLastAccessedTime(): ?int | setLastAccessedTime(?int lastAccessedTime): void |
| `valueNames` | `?(string[])` | Optional | - | getValueNames(): ?array | setValueNames(?array valueNames): void |
| `servletContext` | [`?ServletContext`](../../doc/models/servlet-context.md) | Optional | - | getServletContext(): ?ServletContext | setServletContext(?ServletContext servletContext): void |
| `maxInactiveInterval` | `?int` | Optional | - | getMaxInactiveInterval(): ?int | setMaxInactiveInterval(?int maxInactiveInterval): void |

## Example (as JSON)

```json
{
  "creationTime": null,
  "id": null,
  "new": null,
  "attributeNames": null,
  "sessionContext": null,
  "lastAccessedTime": null,
  "valueNames": null,
  "servletContext": null,
  "maxInactiveInterval": null
}
```

