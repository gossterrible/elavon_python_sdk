
# Value Added Info

## Structure

`ValueAddedInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value_adds` | `dict` | Optional | Boolean map to indicate presence of various value added services, true if present, false/null if absent.The valid keys are as follows: FANFARE, ELECTRONIC_CHECKING_SERVICE, CREDIT_CARD_SURCHARGING, CASH_BACK, MERCHANT_CONNECT_PREMIUM, CONTACTLESS, CONVERGE_BILLING_AND_INVOICE, CONVERGE_HOSPITALITY, E_TOKENIZATION, SECURED_ENCRYPT, HEALTH_CARE_ELIGIBILITY, HEALTH_CARE_CLAIMS, HEALTH_CARE_REMITTANCE, HEALTH_CARE_ELIGIBILITY_AND_ESTIMATOR, HEALTH_CARE_PATIENT_BILLING, FRAUD_SERVICES_3D_SECURE, STRAIGHT_SEND, ON_DEMAND |
| `ebt_info` | [`EbtInfo`](../../doc/models/ebt-info.md) | Optional | - |
| `ecs_info` | [`EcsInfo`](../../doc/models/ecs-info.md) | Optional | - |
| `acs_info` | [`AcsInfo`](../../doc/models/acs-info.md) | Optional | - |
| `fanfare_info` | [`FanfareInfo`](../../doc/models/fanfare-info.md) | Optional | - |
| `gsm_prepaid_type` | [`GsmPrepaidTypeEnum`](../../doc/models/gsm-prepaid-type-enum.md) | Optional | [EU] Additional GSM SIM prepaid information |
| `surcharge_managed_by` | `string` | Optional | [NA] Surcharge Managed By |
| `credit_surcharge_amt` | `string` | Optional | [NA] Credit Surcharge Amount |
| `efs_3_d_secure_info` | [`Efs3dSecureInfo`](../../doc/models/efs-3-d-secure-info.md) | Optional | - |
| `straight_send_info` | [`StraightSendInfo`](../../doc/models/straight-send-info.md) | Optional | - |
| `on_demand_info` | [`OnDemandInfo`](../../doc/models/on-demand-info.md) | Optional | - |
| `ocm_info` | [`OcmInfo`](../../doc/models/ocm-info.md) | Optional | - |

## Example (as JSON)

```json
{
  "valueAdds": null,
  "ebtInfo": null,
  "ecsInfo": null,
  "acsInfo": null,
  "fanfareInfo": null,
  "gsmPrepaidType": null,
  "surchargeManagedBy": null,
  "creditSurchargeAmt": null,
  "efs3dSecureInfo": null,
  "straightSendInfo": null,
  "onDemandInfo": null,
  "ocmInfo": null
}
```

