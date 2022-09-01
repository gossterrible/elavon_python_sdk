
# Integrator Solution Info

## Structure

`IntegratorSolutionInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `health_care_eligibility_selection_map` | [`dict`](../../doc/models/health-care-eligibility-info.md) | Optional | Map of health care service to related info. The valid keys are as follows: HEALTH_CARE_ELIGIBILITY, HEALTH_CARE_CLAIMS, HEALTH_CARE_REMITTANCEHEALTH_CARE_ELIGIBILITY_AND_ESTIMATOR, HEALTH_CARE_PATIENT_BILLING |
| `payments` | [`Payments`](../../doc/models/payments.md) | Optional | - |
| `has_ecs_only` | `bool` | Optional | - |
| `sku` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "healthCareEligibilitySelectionMap": null,
  "payments": null,
  "hasEcsOnly": null,
  "sku": null
}
```

