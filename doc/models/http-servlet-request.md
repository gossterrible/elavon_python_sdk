
# Http Servlet Request

## Structure

`HttpServletRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `method` | `string` | Optional | - |
| `session` | [`HttpSession`](../../doc/models/http-session.md) | Optional | - |
| `cookies` | [`List of Cookie`](../../doc/models/cookie.md) | Optional | - |
| `request_uri` | `string` | Optional | - |
| `user_principal` | [`Principal`](../../doc/models/principal.md) | Optional | - |
| `context_path` | `string` | Optional | - |
| `path_info` | `string` | Optional | - |
| `query_string` | `string` | Optional | - |
| `remote_user` | `string` | Optional | - |
| `servlet_path` | `string` | Optional | - |
| `header_names` | `object` | Optional | - |
| `requested_session_id` | `string` | Optional | - |
| `http_servlet_mapping` | [`HttpServletMapping`](../../doc/models/http-servlet-mapping.md) | Optional | - |
| `trailer_fields_ready` | `bool` | Optional | - |
| `auth_type` | `string` | Optional | - |
| `path_translated` | `string` | Optional | - |
| `requested_session_id_valid` | `bool` | Optional | - |
| `requested_session_id_from_cookie` | `bool` | Optional | - |
| `requested_session_id_from_url` | `bool` | Optional | - |
| `parts` | [`List of Part`](../../doc/models/part.md) | Optional | - |
| `request_url` | `object` | Optional | - |
| `trailer_fields` | `dict` | Optional | - |
| `content_length` | `int` | Optional | - |
| `locale` | [`Locale`](../../doc/models/locale.md) | Optional | - |
| `protocol` | `string` | Optional | - |
| `scheme` | `string` | Optional | - |
| `input_stream` | [`ServletInputStream`](../../doc/models/servlet-input-stream.md) | Optional | - |
| `local_name` | `string` | Optional | - |
| `parameter_names` | `object` | Optional | - |
| `server_name` | `string` | Optional | - |
| `attribute_names` | `object` | Optional | - |
| `parameter_map` | `dict` | Optional | - |
| `local_addr` | `string` | Optional | - |
| `remote_port` | `int` | Optional | - |
| `secure` | `bool` | Optional | - |
| `local_port` | `int` | Optional | - |
| `remote_addr` | `string` | Optional | - |
| `remote_host` | `string` | Optional | - |
| `reader` | `object` | Optional | - |
| `server_port` | `int` | Optional | - |
| `locales` | `object` | Optional | - |
| `character_encoding` | `string` | Optional | - |
| `servlet_context` | [`ServletContext`](../../doc/models/servlet-context.md) | Optional | - |
| `async_started` | `bool` | Optional | - |
| `async_supported` | `bool` | Optional | - |
| `async_context` | [`AsyncContext`](../../doc/models/async-context.md) | Optional | - |
| `dispatcher_type` | [`DispatcherTypeEnum`](../../doc/models/dispatcher-type-enum.md) | Optional | - |
| `content_length_long` | `long\|int` | Optional | - |
| `content_type` | `string` | Optional | - |

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

