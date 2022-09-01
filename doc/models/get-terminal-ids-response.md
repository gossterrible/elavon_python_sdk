
# Get Terminal Ids Response

## Structure

`GetTerminalIdsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_id` | `int` | Optional | - |
| `error` | `string` | Optional | If processing error occurs, will contain information, else will be empty or null |
| `welcome_url` | `string` | Optional | Welcome to Converge URL, typically provided to costomer via email |
| `virtual_id` | `string` | Optional | Virtual Id, for Converge |
| `terminal_bin` | `string` | Optional | Terminal BIN |
| `terminal_id_data_map` | `dict` | Optional | Map of item code to various Converge data properties |

## Example (as JSON)

```json
{
  "responseId": null,
  "error": null,
  "welcomeUrl": null,
  "virtualId": null,
  "terminalBin": null,
  "terminalIdDataMap": null
}
```

