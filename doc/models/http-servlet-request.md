
# Http Servlet Request

## Structure

`HttpServletRequest`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `method` | `?string` | Optional | - | getMethod(): ?string | setMethod(?string method): void |
| `session` | [`?HttpSession`](../../doc/models/http-session.md) | Optional | - | getSession(): ?HttpSession | setSession(?HttpSession session): void |
| `cookies` | [`?(Cookie[])`](../../doc/models/cookie.md) | Optional | - | getCookies(): ?array | setCookies(?array cookies): void |
| `requestURI` | `?string` | Optional | - | getRequestURI(): ?string | setRequestURI(?string requestURI): void |
| `userPrincipal` | [`?Principal`](../../doc/models/principal.md) | Optional | - | getUserPrincipal(): ?Principal | setUserPrincipal(?Principal userPrincipal): void |
| `contextPath` | `?string` | Optional | - | getContextPath(): ?string | setContextPath(?string contextPath): void |
| `pathInfo` | `?string` | Optional | - | getPathInfo(): ?string | setPathInfo(?string pathInfo): void |
| `queryString` | `?string` | Optional | - | getQueryString(): ?string | setQueryString(?string queryString): void |
| `remoteUser` | `?string` | Optional | - | getRemoteUser(): ?string | setRemoteUser(?string remoteUser): void |
| `servletPath` | `?string` | Optional | - | getServletPath(): ?string | setServletPath(?string servletPath): void |
| `headerNames` | `?array` | Optional | - | getHeaderNames(): ?array | setHeaderNames(?array headerNames): void |
| `requestedSessionId` | `?string` | Optional | - | getRequestedSessionId(): ?string | setRequestedSessionId(?string requestedSessionId): void |
| `httpServletMapping` | [`?HttpServletMapping`](../../doc/models/http-servlet-mapping.md) | Optional | - | getHttpServletMapping(): ?HttpServletMapping | setHttpServletMapping(?HttpServletMapping httpServletMapping): void |
| `trailerFieldsReady` | `?bool` | Optional | - | getTrailerFieldsReady(): ?bool | setTrailerFieldsReady(?bool trailerFieldsReady): void |
| `authType` | `?string` | Optional | - | getAuthType(): ?string | setAuthType(?string authType): void |
| `pathTranslated` | `?string` | Optional | - | getPathTranslated(): ?string | setPathTranslated(?string pathTranslated): void |
| `requestedSessionIdValid` | `?bool` | Optional | - | getRequestedSessionIdValid(): ?bool | setRequestedSessionIdValid(?bool requestedSessionIdValid): void |
| `requestedSessionIdFromCookie` | `?bool` | Optional | - | getRequestedSessionIdFromCookie(): ?bool | setRequestedSessionIdFromCookie(?bool requestedSessionIdFromCookie): void |
| `requestedSessionIdFromURL` | `?bool` | Optional | - | getRequestedSessionIdFromURL(): ?bool | setRequestedSessionIdFromURL(?bool requestedSessionIdFromURL): void |
| `parts` | [`?(Part[])`](../../doc/models/part.md) | Optional | - | getParts(): ?array | setParts(?array parts): void |
| `requestURL` | `?array` | Optional | - | getRequestURL(): ?array | setRequestURL(?array requestURL): void |
| `trailerFields` | `?array<string,string>` | Optional | - | getTrailerFields(): ?array | setTrailerFields(?array trailerFields): void |
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
  "method": null,
  "session": null,
  "cookies": null,
  "requestURI": null,
  "userPrincipal": null,
  "contextPath": null,
  "pathInfo": null,
  "queryString": null,
  "remoteUser": null,
  "servletPath": null,
  "headerNames": null,
  "requestedSessionId": null,
  "httpServletMapping": null,
  "trailerFieldsReady": null,
  "authType": null,
  "pathTranslated": null,
  "requestedSessionIdValid": null,
  "requestedSessionIdFromCookie": null,
  "requestedSessionIdFromURL": null,
  "parts": null,
  "requestURL": null,
  "trailerFields": null,
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

