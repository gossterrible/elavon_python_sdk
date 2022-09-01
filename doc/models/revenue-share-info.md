
# Revenue Share Info

## Structure

`RevenueShareInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `secondarySalesPerson` | `string` | Required | Sales person representative code for secondary sales person | getSecondarySalesPerson(): string | setSecondarySalesPerson(string secondarySalesPerson): void |
| `splitPercentage` | `string` | Required | Percentage split allocated for secondary | getSplitPercentage(): string | setSplitPercentage(string splitPercentage): void |

## Example (as JSON)

```json
{
  "secondarySalesPerson": "12345",
  "splitPercentage": "50"
}
```

