
# Person

## Structure

`Person`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`Name`](../../doc/models/name.md) | Required | - |
| `contact_info` | [`ContactInfo`](../../doc/models/contact-info.md) | Optional | - |
| `dob` | [`DateComponents`](../../doc/models/date-components.md) | Optional | A container that holds the date (day, month, and year) |
| `positions` | `dict` | Required | Boolean map representing positions of person, if position applies true should be value given for position key. The valid keys are as follows: OFFICER, PARTNER, DIRECTOR, OWNER, SECRETARY, OTHER, BENEFICIAL_OWNER, AUTHORIZED_SIGNER, SOLE_PROP |
| `ownership_pct` | `string` | Optional | Ownership percentage of person |
| `ids` | [`List of Identification`](../../doc/models/identification.md) | Optional | Id listing of person |
| `title_type` | [`TitleTypeEnum`](../../doc/models/title-type-enum.md) | Optional | [NA] Title type of person |
| `title` | `string` | Optional | Free text of person's title, should title type not provide correct option (NA OTHER)<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `32` |
| `signing_personal_guarantee` | `bool` | Optional | [NA] Flag indicating if person is signing personal gurantee, true if YES, false if NO |
| `responsible_party` | `bool` | Optional | Flag indicating if person is a responsible party of the business, true if YES, false if NO |
| `related_party` | `bool` | Optional | Flag indicating if person is a related party of the business, true if YES, false if NO |
| `residing_country` | `string` | Optional | Current country of residence of person, ISO 3166-1 alpha-3 standard applies |
| `primary_nationality` | `string` | Optional | Primary citizenship/nationality of person, ISO 3166-1 alpha-3 standard applies |
| `secondary_nationality` | `string` | Optional | Secondary citizenship/nationality of person, ISO 3166-1 alpha-3 standard applies |
| `documentary_info` | [`DocumentaryInfo`](../../doc/models/documentary-info.md) | Optional | - |
| `alternate_address_info` | [`AlternateAddressInfo`](../../doc/models/alternate-address-info.md) | Optional | Used to hold information about an alternative business address |
| `is_new_owner` | `bool` | Optional | [EU] Flag indicating if person is a new owner of the buisness, true if YES, false if NO |
| `directional_ownership_type` | [`DirectionalOwnershipTypeEnum`](../../doc/models/directional-ownership-type-enum.md) | Optional | [EU] Indicator if person has direct or indirect ownership of business |
| `signing_agreement` | `bool` | Optional | Flag indicating if person if signing the agreement, true if YES, false if NO |
| `us_person` | `bool` | Optional | [NA] Flag indicating if person is a US citizen, true if YES, false if NO |

## Example (as JSON)

```json
{
  "name": {
    "firstName": "John",
    "lastName": "Doe"
  },
  "positions": null
}
```

