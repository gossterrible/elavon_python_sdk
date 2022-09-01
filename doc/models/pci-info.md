
# PCI Info

## Structure

`PCIInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `pciProgramLevel` | [`?string (PciProgramLevelEnum)`](../../doc/models/pci-program-level-enum.md) | Optional | PCI program level | getPciProgramLevel(): ?string | setPciProgramLevel(?string pciProgramLevel): void |
| `pciServiceType` | [`?string (PciServiceTypeEnum)`](../../doc/models/pci-service-type-enum.md) | Optional | PCI service type | getPciServiceType(): ?string | setPciServiceType(?string pciServiceType): void |
| `pciContactFirstName` | `?string` | Optional | PCI first name | getPciContactFirstName(): ?string | setPciContactFirstName(?string pciContactFirstName): void |
| `pciContactLastName` | `?string` | Optional | PCI last name | getPciContactLastName(): ?string | setPciContactLastName(?string pciContactLastName): void |
| `pciContactEmailAddress` | `?string` | Optional | PCI email address | getPciContactEmailAddress(): ?string | setPciContactEmailAddress(?string pciContactEmailAddress): void |
| `pciContactPhone` | [`?PhoneNumber`](../../doc/models/phone-number.md) | Optional | - | getPciContactPhone(): ?PhoneNumber | setPciContactPhone(?PhoneNumber pciContactPhone): void |
| `pciGroups` | [`?(string[]) (PciGroupEnum)`](../../doc/models/pci-group-enum.md) | Optional | PCI Groups | getPciGroups(): ?array | setPciGroups(?array pciGroups): void |

## Example (as JSON)

```json
{
  "pciProgramLevel": null,
  "pciServiceType": null,
  "pciContactFirstName": null,
  "pciContactLastName": null,
  "pciContactEmailAddress": null,
  "pciContactPhone": null,
  "pciGroups": null
}
```

