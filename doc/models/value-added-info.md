
# Value Added Info

## Structure

`ValueAddedInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `valueAdds` | `?array<string,bool>` | Optional | Boolean map to indicate presence of various value added services, true if present, false/null if absent.The valid keys are as follows: FANFARE, ELECTRONIC_CHECKING_SERVICE, CREDIT_CARD_SURCHARGING, CASH_BACK, MERCHANT_CONNECT_PREMIUM, CONTACTLESS, CONVERGE_BILLING_AND_INVOICE, CONVERGE_HOSPITALITY, E_TOKENIZATION, SECURED_ENCRYPT, HEALTH_CARE_ELIGIBILITY, HEALTH_CARE_CLAIMS, HEALTH_CARE_REMITTANCE, HEALTH_CARE_ELIGIBILITY_AND_ESTIMATOR, HEALTH_CARE_PATIENT_BILLING, FRAUD_SERVICES_3D_SECURE, STRAIGHT_SEND, ON_DEMAND | getValueAdds(): ?array | setValueAdds(?array valueAdds): void |
| `ebtInfo` | [`?EbtInfo`](../../doc/models/ebt-info.md) | Optional | - | getEbtInfo(): ?EbtInfo | setEbtInfo(?EbtInfo ebtInfo): void |
| `ecsInfo` | [`?EcsInfo`](../../doc/models/ecs-info.md) | Optional | - | getEcsInfo(): ?EcsInfo | setEcsInfo(?EcsInfo ecsInfo): void |
| `acsInfo` | [`?AcsInfo`](../../doc/models/acs-info.md) | Optional | - | getAcsInfo(): ?AcsInfo | setAcsInfo(?AcsInfo acsInfo): void |
| `fanfareInfo` | [`?FanfareInfo`](../../doc/models/fanfare-info.md) | Optional | - | getFanfareInfo(): ?FanfareInfo | setFanfareInfo(?FanfareInfo fanfareInfo): void |
| `gsmPrepaidType` | [`?string (GsmPrepaidTypeEnum)`](../../doc/models/gsm-prepaid-type-enum.md) | Optional | [EU] Additional GSM SIM prepaid information | getGsmPrepaidType(): ?string | setGsmPrepaidType(?string gsmPrepaidType): void |
| `surchargeManagedBy` | `?string` | Optional | [NA] Surcharge Managed By | getSurchargeManagedBy(): ?string | setSurchargeManagedBy(?string surchargeManagedBy): void |
| `creditSurchargeAmt` | `?string` | Optional | [NA] Credit Surcharge Amount | getCreditSurchargeAmt(): ?string | setCreditSurchargeAmt(?string creditSurchargeAmt): void |
| `efs3dSecureInfo` | [`?Efs3dSecureInfo`](../../doc/models/efs-3-d-secure-info.md) | Optional | - | getEfs3dSecureInfo(): ?Efs3dSecureInfo | setEfs3dSecureInfo(?Efs3dSecureInfo efs3dSecureInfo): void |
| `straightSendInfo` | [`?StraightSendInfo`](../../doc/models/straight-send-info.md) | Optional | - | getStraightSendInfo(): ?StraightSendInfo | setStraightSendInfo(?StraightSendInfo straightSendInfo): void |
| `onDemandInfo` | [`?OnDemandInfo`](../../doc/models/on-demand-info.md) | Optional | - | getOnDemandInfo(): ?OnDemandInfo | setOnDemandInfo(?OnDemandInfo onDemandInfo): void |
| `ocmInfo` | [`?OcmInfo`](../../doc/models/ocm-info.md) | Optional | - | getOcmInfo(): ?OcmInfo | setOcmInfo(?OcmInfo ocmInfo): void |

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

