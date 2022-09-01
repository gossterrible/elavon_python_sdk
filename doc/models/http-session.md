
# Http Session

## Structure

`HttpSession`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `creation_time` | `long\|int` | Optional | - |
| `id` | `string` | Optional | - |
| `new` | `bool` | Optional | - |
| `attribute_names` | `object` | Optional | - |
| `session_context` | [`HttpSessionContext`](../../doc/models/http-session-context.md) | Optional | - |
| `last_accessed_time` | `long\|int` | Optional | - |
| `value_names` | `List of string` | Optional | - |
| `servlet_context` | [`ServletContext`](../../doc/models/servlet-context.md) | Optional | - |
| `max_inactive_interval` | `int` | Optional | - |

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

