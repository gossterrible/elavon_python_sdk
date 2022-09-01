
# Ocm Info

## Structure

`OcmInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `setupType` | `string` | Required | OCM Service Type | getSetupType(): string | setSetupType(string setupType): void |
| `setupFee` | `?float` | Optional | OCM setup fee to apply | getSetupFee(): ?float | setSetupFee(?float setupFee): void |
| `monthlyFee` | `?float` | Optional | OCM monthly fee to apply | getMonthlyFee(): ?float | setMonthlyFee(?float monthlyFee): void |
| `numberOfUsers` | `?int` | Optional | OCM number of users | getNumberOfUsers(): ?int | setNumberOfUsers(?int numberOfUsers): void |

## Example (as JSON)

```json
{
  "setupType": "Mid, Chain"
}
```

