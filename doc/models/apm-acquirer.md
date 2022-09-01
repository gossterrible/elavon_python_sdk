
# Apm Acquirer

## Structure

`ApmAcquirer`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `acquirerCode` | `string` | Required | Acquirer Code of the Alternative Payment Method | getAcquirerCode(): string | setAcquirerCode(string acquirerCode): void |
| `acquirerTypes` | [`ApmAcquirerType[]`](../../doc/models/apm-acquirer-type.md) | Required | Acquirer Type of the Alternative Payment Method | getAcquirerTypes(): array | setAcquirerTypes(array acquirerTypes): void |

## Example (as JSON)

```json
{
  "acquirerCode": "acquirerCode8",
  "acquirerTypes": [
    {
      "typeCode": "typeCode7",
      "perItemAmount": "perItemAmount1",
      "ratePercentage": "ratePercentage9",
      "pricingTiers": [
        {
          "combiningCode": "combiningCode5",
          "perItemAmount": "perItemAmount1",
          "ratePercentage": "ratePercentage9",
          "description": "description7"
        }
      ]
    },
    {
      "typeCode": "typeCode8",
      "perItemAmount": "perItemAmount2",
      "ratePercentage": "ratePercentage0",
      "pricingTiers": [
        {
          "combiningCode": "combiningCode6",
          "perItemAmount": "perItemAmount2",
          "ratePercentage": "ratePercentage0",
          "description": "description6"
        },
        {
          "combiningCode": "combiningCode7",
          "perItemAmount": "perItemAmount3",
          "ratePercentage": "ratePercentage1",
          "description": "description5"
        }
      ]
    },
    {
      "typeCode": "typeCode9",
      "perItemAmount": "perItemAmount3",
      "ratePercentage": "ratePercentage1",
      "pricingTiers": [
        {
          "combiningCode": "combiningCode7",
          "perItemAmount": "perItemAmount3",
          "ratePercentage": "ratePercentage1",
          "description": "description5"
        },
        {
          "combiningCode": "combiningCode8",
          "perItemAmount": "perItemAmount4",
          "ratePercentage": "ratePercentage2",
          "description": "description4"
        },
        {
          "combiningCode": "combiningCode9",
          "perItemAmount": "perItemAmount5",
          "ratePercentage": "ratePercentage3",
          "description": "description3"
        }
      ]
    }
  ]
}
```

