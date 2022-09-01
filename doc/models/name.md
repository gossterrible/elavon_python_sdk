
# Name

## Structure

`Name`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `salutation` | [`?string (SalutationEnum)`](../../doc/models/salutation-enum.md) | Optional | - | getSalutation(): ?string | setSalutation(?string salutation): void |
| `firstName` | `string` | Required | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` | getFirstName(): string | setFirstName(string firstName): void |
| `middleName` | `?string` | Optional | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` | getMiddleName(): ?string | setMiddleName(?string middleName): void |
| `lastName` | `string` | Required | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` | getLastName(): string | setLastName(string lastName): void |

## Example (as JSON)

```json
{
  "firstName": "John",
  "lastName": "Doe"
}
```

