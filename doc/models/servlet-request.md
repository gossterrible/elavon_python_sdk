
# Servlet Request

## Structure

`ServletRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `contentLength` | `?int` | Optional | - | getContentLength(): ?int | setContentLength(?int contentLength): void |
| `locale` | [`?Locale`](../../doc/models/locale.md) | Optional | - | getLocale(): ?Locale | setLocale(?Locale locale): void |
| `protocol` | `?string` | Optional | - | getProtocol(): ?string | setProtocol(?string protocol): void |
| `scheme` | `?string` | Optional | - | getScheme(): ?string | setScheme(?string scheme): void |
| `inputStream` | [`?ServletInputStream`](../../doc/models/servlet-input-stream.md) | Optional | - | getInputStream(): ?ServletInputStream | setInputStream(?ServletInputStream inputStream): void |
| `localName` | `?string` | Optional | - | getLocalName(): ?string | setLocalName(?string localName): void |
| `parameterNames` | `?array` | Optional | - | getParameterNames(): ?array | setParameterNames(?array parameterNames): void |
| `serverName` | `?string` | Optional | - | getServerName(): ?string | setServerName(?string serverName): void |
| `attributeNames` | `?array` | Optional | - | getAttributeNames(): ?array | setAttributeNames(?array attributeNames): void |
| `parameterMap` | `?array` | Optional | - | getParameterMap(): ?array | setParameterMap(?array parameterMap): void |
| `localAddr` | `?string` | Optional | - | getLocalAddr(): ?string | setLocalAddr(?string localAddr): void |
| `remotePort` | `?int` | Optional | - | getRemotePort(): ?int | setRemotePort(?int remotePort): void |
| `secure` | `?bool` | Optional | - | getSecure(): ?bool | setSecure(?bool secure): void |
| `localPort` | `?int` | Optional | - | getLocalPort(): ?int | setLocalPort(?int localPort): void |
| `remoteAddr` | `?string` | Optional | - | getRemoteAddr(): ?string | setRemoteAddr(?string remoteAddr): void |
| `remoteHost` | `?string` | Optional | - | getRemoteHost(): ?string | setRemoteHost(?string remoteHost): void |
| `reader` | `?array` | Optional | - | getReader(): ?array | setReader(?array reader): void |
| `serverPort` | `?int` | Optional | - | getServerPort(): ?int | setServerPort(?int serverPort): void |
| `locales` | `?array` | Optional | - | getLocales(): ?array | setLocales(?array locales): void |
| `characterEncoding` | `?string` | Optional | - | getCharacterEncoding(): ?string | setCharacterEncoding(?string characterEncoding): void |
| `servletContext` | [`?ServletContext`](../../doc/models/servlet-context.md) | Optional | - | getServletContext(): ?ServletContext | setServletContext(?ServletContext servletContext): void |
| `asyncStarted` | `?bool` | Optional | - | getAsyncStarted(): ?bool | setAsyncStarted(?bool asyncStarted): void |
| `asyncSupported` | `?bool` | Optional | - | getAsyncSupported(): ?bool | setAsyncSupported(?bool asyncSupported): void |
| `asyncContext` | [`?AsyncContext`](../../doc/models/async-context.md) | Optional | - | getAsyncContext(): ?AsyncContext | setAsyncContext(?AsyncContext asyncContext): void |
| `dispatcherType` | [`?string (DispatcherTypeEnum)`](../../doc/models/dispatcher-type-enum.md) | Optional | - | getDispatcherType(): ?string | setDispatcherType(?string dispatcherType): void |
| `contentLengthLong` | `?int` | Optional | - | getContentLengthLong(): ?int | setContentLengthLong(?int contentLengthLong): void |
| `contentType` | `?string` | Optional | - | getContentType(): ?string | setContentType(?string contentType): void |

## Example (as JSON)

```json
{
  "contentLength": null,
  "locale": null,
  "protocol": null,
  "scheme": null,
  "inputStream": null,
  "localName": null,
  "parameterNames": null,
  "serverName": null,
  "attributeNames": null,
  "parameterMap": null,
  "localAddr": null,
  "remotePort": null,
  "secure": null,
  "localPort": null,
  "remoteAddr": null,
  "remoteHost": null,
  "reader": null,
  "serverPort": null,
  "locales": null,
  "characterEncoding": null,
  "servletContext": null,
  "asyncStarted": null,
  "asyncSupported": null,
  "asyncContext": null,
  "dispatcherType": null,
  "contentLengthLong": null,
  "contentType": null
}
```

