
# Boarding Status Message

## Structure

`BoardingStatusMessage`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `typeCode` | [`?string (TypeCodeEnum)`](../../doc/models/type-code-enum.md) | Optional | Type of message presented | getTypeCode(): ?string | setTypeCode(?string typeCode): void |
| `code` | `?string` | Optional | Number representing the status message | getCode(): ?string | setCode(?string code): void |
| `description` | `?string` | Optional | Description of message | getDescription(): ?string | setDescription(?string description): void |

## Example (as JSON)

```json
{
  "typeCode": null,
  "code": null,
  "description": null
}
```

