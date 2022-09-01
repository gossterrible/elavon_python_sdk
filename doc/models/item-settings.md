
# Item Settings

## Structure

`ItemSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `security_level` | [`SecurityLevelEnum`](../../doc/models/security-level-enum.md) | Optional | - |
| `semi_integrated` | `bool` | Optional | - |
| `connection_type` | [`ConnectionTypeEnum`](../../doc/models/connection-type-enum.md) | Required | Connection type of product |
| `close_method` | [`CloseMethodEnum`](../../doc/models/close-method-enum.md) | Optional | - |
| `capture_method` | [`CaptureMethodEnum`](../../doc/models/capture-method-enum.md) | Optional | - |
| `qir_vendor` | `string` | Optional | - |
| `services` | `dict` | Optional | - |
| `options` | [`List of EquipmentOption`](../../doc/models/equipment-option.md) | Optional | - |
| `bundled_thresh_hold` | `int` | Optional | - |
| `service_pricing_code` | [`ServicePricingCodeEnum`](../../doc/models/service-pricing-code-enum.md) | Optional | - |
| `terminal_type` | [`TerminalTypeEnum`](../../doc/models/terminal-type-enum.md) | Optional | - |
| `ingenico_pay_table` | `bool` | Optional | - |
| `deploy_type` | [`DeployTypeEnum`](../../doc/models/deploy-type-enum.md) | Optional | - |

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

