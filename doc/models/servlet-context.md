
# Servlet Context

## Structure

`ServletContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `major_version` | `int` | Optional | - |
| `minor_version` | `int` | Optional | - |
| `class_loader` | [`ClassLoader`](../../doc/models/class-loader.md) | Optional | - |
| `servlet_names` | `object` | Optional | - |
| `attribute_names` | `object` | Optional | - |
| `context_path` | `string` | Optional | - |
| `session_timeout` | `int` | Optional | - |
| `servlet_context_name` | `string` | Optional | - |
| `server_info` | `string` | Optional | - |
| `init_parameter_names` | `object` | Optional | - |
| `request_character_encoding` | `string` | Optional | - |
| `response_character_encoding` | `string` | Optional | - |
| `servlets` | `object` | Optional | - |
| `session_cookie_config` | [`SessionCookieConfig`](../../doc/models/session-cookie-config.md) | Optional | - |
| `servlet_registrations` | [`dict`](../../doc/models/servlet-registration.md) | Optional | - |
| `filter_registrations` | [`dict`](../../doc/models/filter-registration.md) | Optional | - |
| `default_session_tracking_modes` | [`List of DefaultSessionTrackingModeEnum`](../../doc/models/default-session-tracking-mode-enum.md) | Optional | **Constraints**: *Unique Items Required* |
| `effective_session_tracking_modes` | [`List of EffectiveSessionTrackingModeEnum`](../../doc/models/effective-session-tracking-mode-enum.md) | Optional | **Constraints**: *Unique Items Required* |
| `jsp_config_descriptor` | [`JspConfigDescriptor`](../../doc/models/jsp-config-descriptor.md) | Optional | - |
| `virtual_server_name` | `string` | Optional | - |
| `effective_major_version` | `int` | Optional | - |
| `effective_minor_version` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "majorVersion": null,
  "minorVersion": null,
  "classLoader": null,
  "servletNames": null,
  "attributeNames": null,
  "contextPath": null,
  "sessionTimeout": null,
  "servletContextName": null,
  "serverInfo": null,
  "initParameterNames": null,
  "requestCharacterEncoding": null,
  "responseCharacterEncoding": null,
  "servlets": null,
  "sessionCookieConfig": null,
  "servletRegistrations": null,
  "filterRegistrations": null,
  "defaultSessionTrackingModes": null,
  "effectiveSessionTrackingModes": null,
  "jspConfigDescriptor": null,
  "virtualServerName": null,
  "effectiveMajorVersion": null,
  "effectiveMinorVersion": null
}
```

