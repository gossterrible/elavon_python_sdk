
# Site Survey

## Structure

`SiteSurvey`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_survey_conducted` | `bool` | Optional | [NA] If site survey was conducted set to true, else false |
| `location_type` | [`LocationTypeEnum`](../../doc/models/location-type-enum.md) | Optional | [NA] Type of location |
| `site_address_same_as_dba` | `bool` | Optional | [EU] True if site address is the same as the DBA address |
| `location_environment` | [`LocationEnvironmentEnum`](../../doc/models/location-environment-enum.md) | Optional | [EU] The type of site location |
| `vicinity_condition` | [`VicinityConditionEnum`](../../doc/models/vicinity-condition-enum.md) | Optional | [EU] The condition of the site's vicinity |
| `location_square_meters` | [`LocationSquareMetersEnum`](../../doc/models/location-square-meters-enum.md) | Optional | [EU] The size of the site in square meters |
| `location_appearance` | [`LocationAppearanceEnum`](../../doc/models/location-appearance-enum.md) | Optional | [EU] The site's appearance |
| `business_operating` | `bool` | Optional | [EU] True if the business is currently operating at the site |
| `inventory_display_adequate` | `bool` | Optional | [EU] True if the site's displayed inventory is adequate for the type of business |
| `inventory_consistent_with_business_type` | `bool` | Optional | [EU] True if the site's inventory is consistent for the type of business |
| `card_decals_visible` | `bool` | Optional | [EU] True if the accepted credit cards decals are displayed at the site |
| `card_decals_installed_at_visit` | `bool` | Optional | [EU] True if the accepted credit cards decals were installed during the site survey |

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

