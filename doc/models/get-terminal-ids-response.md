
# Get Terminal Ids Response

## Structure

`GetTerminalIdsResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `error` | `?string` | Optional | If processing error occurs, will contain information, else will be empty or null | getError(): ?string | setError(?string error): void |
| `welcomeUrl` | `?string` | Optional | Welcome to Converge URL, typically provided to costomer via email | getWelcomeUrl(): ?string | setWelcomeUrl(?string welcomeUrl): void |
| `virtualId` | `?string` | Optional | Virtual Id, for Converge | getVirtualId(): ?string | setVirtualId(?string virtualId): void |
| `terminalBin` | `?string` | Optional | Terminal BIN | getTerminalBin(): ?string | setTerminalBin(?string terminalBin): void |
| `terminalIdDataMap` | `?array` | Optional | Map of item code to various Converge data properties | getTerminalIdDataMap(): ?array | setTerminalIdDataMap(?array terminalIdDataMap): void |

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

