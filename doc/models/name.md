
# Name

## Structure

`Name`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `salutation` | [`SalutationEnum`](../../doc/models/salutation-enum.md) | Optional | - |
| `first_name` | `string` | Required | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `middle_name` | `string` | Optional | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |
| `last_name` | `string` | Required | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `255` |

## Example (as JSON)

```json
{
  "firstName": "John",
  "lastName": "Doe"
}
```

