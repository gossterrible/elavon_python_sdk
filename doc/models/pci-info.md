
# PCI Info

## Structure

`PCIInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pci_program_level` | [`PciProgramLevelEnum`](../../doc/models/pci-program-level-enum.md) | Optional | PCI program level |
| `pci_service_type` | [`PciServiceTypeEnum`](../../doc/models/pci-service-type-enum.md) | Optional | PCI service type |
| `pci_contact_first_name` | `string` | Optional | PCI first name |
| `pci_contact_last_name` | `string` | Optional | PCI last name |
| `pci_contact_email_address` | `string` | Optional | PCI email address |
| `pci_contact_phone` | [`PhoneNumber`](../../doc/models/phone-number.md) | Optional | - |
| `pci_groups` | [`List of PciGroupEnum`](../../doc/models/pci-group-enum.md) | Optional | PCI Groups |

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

