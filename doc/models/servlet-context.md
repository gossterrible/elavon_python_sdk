
# Servlet Context

## Structure

`ServletContext`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `majorVersion` | `?int` | Optional | - | getMajorVersion(): ?int | setMajorVersion(?int majorVersion): void |
| `minorVersion` | `?int` | Optional | - | getMinorVersion(): ?int | setMinorVersion(?int minorVersion): void |
| `classLoader` | [`?ClassLoader`](../../doc/models/class-loader.md) | Optional | - | getClassLoader(): ?ClassLoader | setClassLoader(?ClassLoader classLoader): void |
| `servletNames` | `?array` | Optional | - | getServletNames(): ?array | setServletNames(?array servletNames): void |
| `attributeNames` | `?array` | Optional | - | getAttributeNames(): ?array | setAttributeNames(?array attributeNames): void |
| `contextPath` | `?string` | Optional | - | getContextPath(): ?string | setContextPath(?string contextPath): void |
| `sessionTimeout` | `?int` | Optional | - | getSessionTimeout(): ?int | setSessionTimeout(?int sessionTimeout): void |
| `servletContextName` | `?string` | Optional | - | getServletContextName(): ?string | setServletContextName(?string servletContextName): void |
| `serverInfo` | `?string` | Optional | - | getServerInfo(): ?string | setServerInfo(?string serverInfo): void |
| `initParameterNames` | `?array` | Optional | - | getInitParameterNames(): ?array | setInitParameterNames(?array initParameterNames): void |
| `requestCharacterEncoding` | `?string` | Optional | - | getRequestCharacterEncoding(): ?string | setRequestCharacterEncoding(?string requestCharacterEncoding): void |
| `responseCharacterEncoding` | `?string` | Optional | - | getResponseCharacterEncoding(): ?string | setResponseCharacterEncoding(?string responseCharacterEncoding): void |
| `servlets` | `?array` | Optional | - | getServlets(): ?array | setServlets(?array servlets): void |
| `sessionCookieConfig` | [`?SessionCookieConfig`](../../doc/models/session-cookie-config.md) | Optional | - | getSessionCookieConfig(): ?SessionCookieConfig | setSessionCookieConfig(?SessionCookieConfig sessionCookieConfig): void |
| `servletRegistrations` | [`?array<string,ServletRegistration>`](../../doc/models/servlet-registration.md) | Optional | - | getServletRegistrations(): ?array | setServletRegistrations(?array servletRegistrations): void |
| `filterRegistrations` | [`?array<string,FilterRegistration>`](../../doc/models/filter-registration.md) | Optional | - | getFilterRegistrations(): ?array | setFilterRegistrations(?array filterRegistrations): void |
| `defaultSessionTrackingModes` | [`?(string[]) (DefaultSessionTrackingModeEnum)`](../../doc/models/default-session-tracking-mode-enum.md) | Optional | **Constraints**: *Unique Items Required* | getDefaultSessionTrackingModes(): ?array | setDefaultSessionTrackingModes(?array defaultSessionTrackingModes): void |
| `effectiveSessionTrackingModes` | [`?(string[]) (EffectiveSessionTrackingModeEnum)`](../../doc/models/effective-session-tracking-mode-enum.md) | Optional | **Constraints**: *Unique Items Required* | getEffectiveSessionTrackingModes(): ?array | setEffectiveSessionTrackingModes(?array effectiveSessionTrackingModes): void |
| `jspConfigDescriptor` | [`?JspConfigDescriptor`](../../doc/models/jsp-config-descriptor.md) | Optional | - | getJspConfigDescriptor(): ?JspConfigDescriptor | setJspConfigDescriptor(?JspConfigDescriptor jspConfigDescriptor): void |
| `virtualServerName` | `?string` | Optional | - | getVirtualServerName(): ?string | setVirtualServerName(?string virtualServerName): void |
| `effectiveMajorVersion` | `?int` | Optional | - | getEffectiveMajorVersion(): ?int | setEffectiveMajorVersion(?int effectiveMajorVersion): void |
| `effectiveMinorVersion` | `?int` | Optional | - | getEffectiveMinorVersion(): ?int | setEffectiveMinorVersion(?int effectiveMinorVersion): void |

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

