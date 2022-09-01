
# Ebt Info

## Structure

`EbtInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `seNumber` | `string` | Required | EBT Service Establishment number | getSeNumber(): string | setSeNumber(string seNumber): void |
| `authorizationFee` | `?float` | Optional | EBT authorization fee to apply | getAuthorizationFee(): ?float | setAuthorizationFee(?float authorizationFee): void |

## Example (as JSON)

```json
{
  "seNumber": "123456789"
}
```

