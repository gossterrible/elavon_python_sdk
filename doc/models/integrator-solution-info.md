
# Integrator Solution Info

## Structure

`IntegratorSolutionInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `healthCareEligibilitySelectionMap` | [`?array<string,HealthCareEligibilityInfo>`](../../doc/models/health-care-eligibility-info.md) | Optional | Map of health care service to related info. The valid keys are as follows: HEALTH_CARE_ELIGIBILITY, HEALTH_CARE_CLAIMS, HEALTH_CARE_REMITTANCEHEALTH_CARE_ELIGIBILITY_AND_ESTIMATOR, HEALTH_CARE_PATIENT_BILLING | getHealthCareEligibilitySelectionMap(): ?array | setHealthCareEligibilitySelectionMap(?array healthCareEligibilitySelectionMap): void |
| `payments` | [`?Payments`](../../doc/models/payments.md) | Optional | - | getPayments(): ?Payments | setPayments(?Payments payments): void |
| `hasEcsOnly` | `?bool` | Optional | - | getHasEcsOnly(): ?bool | setHasEcsOnly(?bool hasEcsOnly): void |
| `sku` | `?string` | Optional | - | getSku(): ?string | setSku(?string sku): void |

## Example (as JSON)

```json
{
  "healthCareEligibilitySelectionMap": null,
  "payments": null,
  "hasEcsOnly": null,
  "sku": null
}
```

