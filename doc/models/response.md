
# Response

## Structure

`Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `last_modified` | `datetime` | Optional | - |
| `date` | `datetime` | Optional | - |
| `length` | `int` | Optional | - |
| `location` | `string` | Optional | - |
| `language` | [`Locale`](../../doc/models/locale.md) | Optional | - |
| `cookies` | [`dict`](../../doc/models/new-cookie.md) | Optional | - |
| `media_type` | [`MediaType`](../../doc/models/media-type.md) | Optional | - |
| `entity` | `object` | Optional | - |
| `links` | [`List of Link`](../../doc/models/link.md) | Optional | **Constraints**: *Unique Items Required* |
| `status` | `int` | Optional | - |
| `entity_tag` | [`EntityTag`](../../doc/models/entity-tag.md) | Optional | - |
| `string_headers` | `dict` | Optional | - |
| `metadata` | `dict` | Optional | - |
| `status_info` | [`StatusType`](../../doc/models/status-type.md) | Optional | - |
| `allowed_methods` | `List of string` | Optional | **Constraints**: *Unique Items Required* |
| `headers` | `dict` | Optional | - |

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

