
# Ecs Info

## Structure

`EcsInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `processing_acceptance_type` | [`ProcessingAcceptanceTypeEnum`](../../doc/models/processing-acceptance-type-enum.md) | Required | ECS processing acceptance |
| `service_level_type` | [`ServiceLevelTypeEnum`](../../doc/models/service-level-type-enum.md) | Optional | ECS service level |
| `annual_check_volume` | `float` | Optional | Predicted annual check volume to be given though service |
| `average_check_amount` | `float` | Optional | Predicted average check amount to be given though service |
| `max_check_amount` | `int` | Optional | Max checks allowed though service |
| `per_transaction` | `float` | Optional | Per transaction fee applied to service |
| `discount_rate` | `float` | Optional | Fee percentage to be applied to service |
| `monthly_minimum` | `float` | Optional | Per transaction fee applied to service |
| `per_return_fee` | `float` | Optional | Per returns fee applied to service |
| `nsf_service_processing_fee` | `float` | Optional | Processing fee for addtional NSF service |
| `nsf_service_fee` | `float` | Optional | Up front fee for addtional NSF service |
| `collection` | `bool` | Optional | Boolean indicating if ECS collection service is desired, true if YES, false if NO |
| `enquire_reporting` | `bool` | Optional | Boolean indicating if ECS Enquire reporting service is desired, true if YES, false if NO |
| `service_provider_type` | [`ServiceProviderTypeEnum`](../../doc/models/service-provider-type-enum.md) | Optional | ECS service provider. If not provided, will board as ENCIRCLE DIRECT |

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

