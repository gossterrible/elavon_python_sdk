
# Response

## Structure

`Response`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `lastModified` | `?\DateTime` | Optional | - | getLastModified(): ?\DateTime | setLastModified(?\DateTime lastModified): void |
| `date` | `?\DateTime` | Optional | - | getDate(): ?\DateTime | setDate(?\DateTime date): void |
| `length` | `?int` | Optional | - | getLength(): ?int | setLength(?int length): void |
| `location` | `?string` | Optional | - | getLocation(): ?string | setLocation(?string location): void |
| `language` | [`?Locale`](../../doc/models/locale.md) | Optional | - | getLanguage(): ?Locale | setLanguage(?Locale language): void |
| `cookies` | [`?array<string,NewCookie>`](../../doc/models/new-cookie.md) | Optional | - | getCookies(): ?array | setCookies(?array cookies): void |
| `mediaType` | [`?MediaType`](../../doc/models/media-type.md) | Optional | - | getMediaType(): ?MediaType | setMediaType(?MediaType mediaType): void |
| `entity` | `?array` | Optional | - | getEntity(): ?array | setEntity(?array entity): void |
| `links` | [`?(Link[])`](../../doc/models/link.md) | Optional | **Constraints**: *Unique Items Required* | getLinks(): ?array | setLinks(?array links): void |
| `status` | `?int` | Optional | - | getStatus(): ?int | setStatus(?int status): void |
| `entityTag` | [`?EntityTag`](../../doc/models/entity-tag.md) | Optional | - | getEntityTag(): ?EntityTag | setEntityTag(?EntityTag entityTag): void |
| `stringHeaders` | `?array` | Optional | - | getStringHeaders(): ?array | setStringHeaders(?array stringHeaders): void |
| `metadata` | `?array` | Optional | - | getMetadata(): ?array | setMetadata(?array metadata): void |
| `statusInfo` | [`?StatusType`](../../doc/models/status-type.md) | Optional | - | getStatusInfo(): ?StatusType | setStatusInfo(?StatusType statusInfo): void |
| `allowedMethods` | `?(string[])` | Optional | **Constraints**: *Unique Items Required* | getAllowedMethods(): ?array | setAllowedMethods(?array allowedMethods): void |
| `headers` | `?array` | Optional | - | getHeaders(): ?array | setHeaders(?array headers): void |

## Example (as JSON)

```json
{
  "lastModified": null,
  "date": null,
  "length": null,
  "location": null,
  "language": null,
  "cookies": null,
  "mediaType": null,
  "entity": null,
  "links": null,
  "status": null,
  "entityTag": null,
  "stringHeaders": null,
  "metadata": null,
  "statusInfo": null,
  "allowedMethods": null,
  "headers": null
}
```

