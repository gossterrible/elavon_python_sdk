
# Servlet Response

## Structure

`ServletResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `locale` | [`?Locale`](../../doc/models/locale.md) | Optional | - | getLocale(): ?Locale | setLocale(?Locale locale): void |
| `bufferSize` | `?int` | Optional | - | getBufferSize(): ?int | setBufferSize(?int bufferSize): void |
| `writer` | `?array` | Optional | - | getWriter(): ?array | setWriter(?array writer): void |
| `characterEncoding` | `?string` | Optional | - | getCharacterEncoding(): ?string | setCharacterEncoding(?string characterEncoding): void |
| `committed` | `?bool` | Optional | - | getCommitted(): ?bool | setCommitted(?bool committed): void |
| `contentType` | `?string` | Optional | - | getContentType(): ?string | setContentType(?string contentType): void |
| `outputStream` | [`?ServletOutputStream`](../../doc/models/servlet-output-stream.md) | Optional | - | getOutputStream(): ?ServletOutputStream | setOutputStream(?ServletOutputStream outputStream): void |

## Example (as JSON)

```json
{
  "locale": null,
  "bufferSize": null,
  "writer": null,
  "characterEncoding": null,
  "committed": null,
  "contentType": null,
  "outputStream": null
}
```

