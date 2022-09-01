
# Item Settings

## Structure

`ItemSettings`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `securityLevel` | [`?string (SecurityLevelEnum)`](../../doc/models/security-level-enum.md) | Optional | - | getSecurityLevel(): ?string | setSecurityLevel(?string securityLevel): void |
| `semiIntegrated` | `?bool` | Optional | - | getSemiIntegrated(): ?bool | setSemiIntegrated(?bool semiIntegrated): void |
| `connectionType` | [`string (ConnectionTypeEnum)`](../../doc/models/connection-type-enum.md) | Required | Connection type of product | getConnectionType(): string | setConnectionType(string connectionType): void |
| `closeMethod` | [`?string (CloseMethodEnum)`](../../doc/models/close-method-enum.md) | Optional | - | getCloseMethod(): ?string | setCloseMethod(?string closeMethod): void |
| `captureMethod` | [`?string (CaptureMethodEnum)`](../../doc/models/capture-method-enum.md) | Optional | - | getCaptureMethod(): ?string | setCaptureMethod(?string captureMethod): void |
| `qirVendor` | `?string` | Optional | - | getQirVendor(): ?string | setQirVendor(?string qirVendor): void |
| `services` | `?array<string,bool>` | Optional | - | getServices(): ?array | setServices(?array services): void |
| `options` | [`?(EquipmentOption[])`](../../doc/models/equipment-option.md) | Optional | - | getOptions(): ?array | setOptions(?array options): void |
| `bundledThreshHold` | `?int` | Optional | - | getBundledThreshHold(): ?int | setBundledThreshHold(?int bundledThreshHold): void |
| `servicePricingCode` | [`?string (ServicePricingCodeEnum)`](../../doc/models/service-pricing-code-enum.md) | Optional | - | getServicePricingCode(): ?string | setServicePricingCode(?string servicePricingCode): void |
| `terminalType` | [`?string (TerminalTypeEnum)`](../../doc/models/terminal-type-enum.md) | Optional | - | getTerminalType(): ?string | setTerminalType(?string terminalType): void |
| `ingenicoPayTable` | `?bool` | Optional | - | getIngenicoPayTable(): ?bool | setIngenicoPayTable(?bool ingenicoPayTable): void |
| `deployType` | [`?string (DeployTypeEnum)`](../../doc/models/deploy-type-enum.md) | Optional | - | getDeployType(): ?string | setDeployType(?string deployType): void |

## Example (as JSON)

```json
{
  "securityLevel": null,
  "semiIntegrated": null,
  "connectionType": "WIRELESS",
  "closeMethod": null,
  "captureMethod": null,
  "qirVendor": null,
  "services": null,
  "options": null,
  "bundledThreshHold": null,
  "servicePricingCode": null,
  "terminalType": null,
  "ingenicoPayTable": null,
  "deployType": null
}
```

