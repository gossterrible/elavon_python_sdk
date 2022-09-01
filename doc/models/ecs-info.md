
# Ecs Info

## Structure

`EcsInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `processingAcceptanceType` | [`string (ProcessingAcceptanceTypeEnum)`](../../doc/models/processing-acceptance-type-enum.md) | Required | ECS processing acceptance | getProcessingAcceptanceType(): string | setProcessingAcceptanceType(string processingAcceptanceType): void |
| `serviceLevelType` | [`?string (ServiceLevelTypeEnum)`](../../doc/models/service-level-type-enum.md) | Optional | ECS service level | getServiceLevelType(): ?string | setServiceLevelType(?string serviceLevelType): void |
| `annualCheckVolume` | `?float` | Optional | Predicted annual check volume to be given though service | getAnnualCheckVolume(): ?float | setAnnualCheckVolume(?float annualCheckVolume): void |
| `averageCheckAmount` | `?float` | Optional | Predicted average check amount to be given though service | getAverageCheckAmount(): ?float | setAverageCheckAmount(?float averageCheckAmount): void |
| `maxCheckAmount` | `?int` | Optional | Max checks allowed though service | getMaxCheckAmount(): ?int | setMaxCheckAmount(?int maxCheckAmount): void |
| `perTransaction` | `?float` | Optional | Per transaction fee applied to service | getPerTransaction(): ?float | setPerTransaction(?float perTransaction): void |
| `discountRate` | `?float` | Optional | Fee percentage to be applied to service | getDiscountRate(): ?float | setDiscountRate(?float discountRate): void |
| `monthlyMinimum` | `?float` | Optional | Per transaction fee applied to service | getMonthlyMinimum(): ?float | setMonthlyMinimum(?float monthlyMinimum): void |
| `perReturnFee` | `?float` | Optional | Per returns fee applied to service | getPerReturnFee(): ?float | setPerReturnFee(?float perReturnFee): void |
| `nsfServiceProcessingFee` | `?float` | Optional | Processing fee for addtional NSF service | getNsfServiceProcessingFee(): ?float | setNsfServiceProcessingFee(?float nsfServiceProcessingFee): void |
| `nsfServiceFee` | `?float` | Optional | Up front fee for addtional NSF service | getNsfServiceFee(): ?float | setNsfServiceFee(?float nsfServiceFee): void |
| `collection` | `?bool` | Optional | Boolean indicating if ECS collection service is desired, true if YES, false if NO | getCollection(): ?bool | setCollection(?bool collection): void |
| `enquireReporting` | `?bool` | Optional | Boolean indicating if ECS Enquire reporting service is desired, true if YES, false if NO | getEnquireReporting(): ?bool | setEnquireReporting(?bool enquireReporting): void |
| `serviceProviderType` | [`?string (ServiceProviderTypeEnum)`](../../doc/models/service-provider-type-enum.md) | Optional | ECS service provider. If not provided, will board as ENCIRCLE DIRECT | getServiceProviderType(): ?string | setServiceProviderType(?string serviceProviderType): void |

## Example (as JSON)

```json
{
  "processingAcceptanceType": "BOC_POS_IMAGE",
  "serviceLevelType": null,
  "annualCheckVolume": null,
  "averageCheckAmount": null,
  "maxCheckAmount": null,
  "perTransaction": null,
  "discountRate": null,
  "monthlyMinimum": null,
  "perReturnFee": null,
  "nsfServiceProcessingFee": null,
  "nsfServiceFee": null,
  "collection": null,
  "enquireReporting": null,
  "serviceProviderType": null
}
```

