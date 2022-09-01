
# Fanfare Info

## Structure

`FanfareInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `maxCardValue` | `?string` | Optional | - | getMaxCardValue(): ?string | setMaxCardValue(?string maxCardValue): void |
| `packageType` | [`?string (PackageTypeEnum)`](../../doc/models/package-type-enum.md) | Optional | - | getPackageType(): ?string | setPackageType(?string packageType): void |
| `enrollment` | [`?array<string,EnrollmentInfo>`](../../doc/models/enrollment-info.md) | Optional | - | getEnrollment(): ?array | setEnrollment(?array enrollment): void |
| `loyalty` | [`?array<string,LoyaltyInfo>`](../../doc/models/loyalty-info.md) | Optional | - | getLoyalty(): ?array | setLoyalty(?array loyalty): void |

## Example (as JSON)

```json
{
  "maxCardValue": null,
  "packageType": null,
  "enrollment": null,
  "loyalty": null
}
```

