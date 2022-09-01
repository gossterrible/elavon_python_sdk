
# Site Survey

## Structure

`SiteSurvey`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `siteSurveyConducted` | `?bool` | Optional | [NA] If site survey was conducted set to true, else false | getSiteSurveyConducted(): ?bool | setSiteSurveyConducted(?bool siteSurveyConducted): void |
| `locationType` | [`?string (LocationTypeEnum)`](../../doc/models/location-type-enum.md) | Optional | [NA] Type of location | getLocationType(): ?string | setLocationType(?string locationType): void |
| `siteAddressSameAsDBA` | `?bool` | Optional | [EU] True if site address is the same as the DBA address | getSiteAddressSameAsDBA(): ?bool | setSiteAddressSameAsDBA(?bool siteAddressSameAsDBA): void |
| `locationEnvironment` | [`?string (LocationEnvironmentEnum)`](../../doc/models/location-environment-enum.md) | Optional | [EU] The type of site location | getLocationEnvironment(): ?string | setLocationEnvironment(?string locationEnvironment): void |
| `vicinityCondition` | [`?string (VicinityConditionEnum)`](../../doc/models/vicinity-condition-enum.md) | Optional | [EU] The condition of the site's vicinity | getVicinityCondition(): ?string | setVicinityCondition(?string vicinityCondition): void |
| `locationSquareMeters` | [`?string (LocationSquareMetersEnum)`](../../doc/models/location-square-meters-enum.md) | Optional | [EU] The size of the site in square meters | getLocationSquareMeters(): ?string | setLocationSquareMeters(?string locationSquareMeters): void |
| `locationAppearance` | [`?string (LocationAppearanceEnum)`](../../doc/models/location-appearance-enum.md) | Optional | [EU] The site's appearance | getLocationAppearance(): ?string | setLocationAppearance(?string locationAppearance): void |
| `businessOperating` | `?bool` | Optional | [EU] True if the business is currently operating at the site | getBusinessOperating(): ?bool | setBusinessOperating(?bool businessOperating): void |
| `inventoryDisplayAdequate` | `?bool` | Optional | [EU] True if the site's displayed inventory is adequate for the type of business | getInventoryDisplayAdequate(): ?bool | setInventoryDisplayAdequate(?bool inventoryDisplayAdequate): void |
| `inventoryConsistentWithBusinessType` | `?bool` | Optional | [EU] True if the site's inventory is consistent for the type of business | getInventoryConsistentWithBusinessType(): ?bool | setInventoryConsistentWithBusinessType(?bool inventoryConsistentWithBusinessType): void |
| `cardDecalsVisible` | `?bool` | Optional | [EU] True if the accepted credit cards decals are displayed at the site | getCardDecalsVisible(): ?bool | setCardDecalsVisible(?bool cardDecalsVisible): void |
| `cardDecalsInstalledAtVisit` | `?bool` | Optional | [EU] True if the accepted credit cards decals were installed during the site survey | getCardDecalsInstalledAtVisit(): ?bool | setCardDecalsInstalledAtVisit(?bool cardDecalsInstalledAtVisit): void |

## Example (as JSON)

```json
{
  "siteSurveyConducted": null,
  "locationType": null,
  "siteAddressSameAsDBA": null,
  "locationEnvironment": null,
  "vicinityCondition": null,
  "locationSquareMeters": null,
  "locationAppearance": null,
  "businessOperating": null,
  "inventoryDisplayAdequate": null,
  "inventoryConsistentWithBusinessType": null,
  "cardDecalsVisible": null,
  "cardDecalsInstalledAtVisit": null
}
```

