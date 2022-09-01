
# Sales Rep Info

## Structure

`SalesRepInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `salesRepCode` | `string` | Required | Identifier of sales representative responsible for submission | getSalesRepCode(): string | setSalesRepCode(string salesRepCode): void |
| `name` | `?string` | Optional | Name of the sales rep | getName(): ?string | setName(?string name): void |
| `email` | `?string` | Optional | email of the sales rep | getEmail(): ?string | setEmail(?string email): void |
| `submitted` | `?bool` | Optional | Flag if the app has been submitted | getSubmitted(): ?bool | setSubmitted(?bool submitted): void |

## Example (as JSON)

```json
{
  "salesRepCode": "12345"
}
```

