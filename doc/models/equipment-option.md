
# Equipment Option

## Structure

`EquipmentOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `integrator_code` | `string` | Optional | - |
| `ciers_number` | `string` | Optional | - |
| `serial_number` | `string` | Optional | - |
| `model_number` | `string` | Optional | - |
| `ecr_type` | [`EcrTypeEnum`](../../doc/models/ecr-type-enum.md) | Optional | - |
| `ecr_mode` | [`EcrModeEnum`](../../doc/models/ecr-mode-enum.md) | Optional | - |
| `print_via_ecr` | `bool` | Optional | - |
| `ecr_integrator` | [`EcrIntegratorEnum`](../../doc/models/ecr-integrator-enum.md) | Optional | - |
| `ecr_cable_type` | [`EcrCableTypeEnum`](../../doc/models/ecr-cable-type-enum.md) | Optional | - |
| `epg_integration_type` | [`EpgIntegrationTypeEnum`](../../doc/models/epg-integration-type-enum.md) | Optional | - |
| `bax_number` | `string` | Optional | - |
| `bax_effective_date` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |

## Example (as JSON)

```json
{
  "integratorCode": null,
  "ciersNumber": null,
  "serialNumber": null,
  "modelNumber": null,
  "ecrType": null,
  "ecrMode": null,
  "printViaEcr": null,
  "ecrIntegrator": null,
  "ecrCableType": null,
  "epgIntegrationType": null,
  "baxNumber": null,
  "baxEffectiveDate": null
}
```

