
# Servlet Request

## Structure

`ServletRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
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

