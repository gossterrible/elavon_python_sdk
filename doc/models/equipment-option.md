
# Equipment Option

## Structure

`EquipmentOption`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `integratorCode` | `?string` | Optional | - | getIntegratorCode(): ?string | setIntegratorCode(?string integratorCode): void |
| `ciersNumber` | `?string` | Optional | - | getCiersNumber(): ?string | setCiersNumber(?string ciersNumber): void |
| `serialNumber` | `?string` | Optional | - | getSerialNumber(): ?string | setSerialNumber(?string serialNumber): void |
| `modelNumber` | `?string` | Optional | - | getModelNumber(): ?string | setModelNumber(?string modelNumber): void |
| `ecrType` | [`?string (EcrTypeEnum)`](../../doc/models/ecr-type-enum.md) | Optional | - | getEcrType(): ?string | setEcrType(?string ecrType): void |
| `ecrMode` | [`?string (EcrModeEnum)`](../../doc/models/ecr-mode-enum.md) | Optional | - | getEcrMode(): ?string | setEcrMode(?string ecrMode): void |
| `printViaEcr` | `?bool` | Optional | - | getPrintViaEcr(): ?bool | setPrintViaEcr(?bool printViaEcr): void |
| `ecrIntegrator` | [`?string (EcrIntegratorEnum)`](../../doc/models/ecr-integrator-enum.md) | Optional | - | getEcrIntegrator(): ?string | setEcrIntegrator(?string ecrIntegrator): void |
| `ecrCableType` | [`?string (EcrCableTypeEnum)`](../../doc/models/ecr-cable-type-enum.md) | Optional | - | getEcrCableType(): ?string | setEcrCableType(?string ecrCableType): void |
| `epgIntegrationType` | [`?string (EpgIntegrationTypeEnum)`](../../doc/models/epg-integration-type-enum.md) | Optional | - | getEpgIntegrationType(): ?string | setEpgIntegrationType(?string epgIntegrationType): void |
| `baxNumber` | `?string` | Optional | - | getBaxNumber(): ?string | setBaxNumber(?string baxNumber): void |
| `baxEffectiveDate` | [`?DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) | getBaxEffectiveDate(): ?DateComponents | setBaxEffectiveDate(?DateComponents baxEffectiveDate): void |

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

