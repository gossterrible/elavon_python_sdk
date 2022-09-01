
# Phone Number

## Structure

`PhoneNumber`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `intlCode` | `?string` | Optional | Standard International calling code | getIntlCode(): ?string | setIntlCode(?string intlCode): void |
| `areaCode` | `string` | Required | Area code of phone number | getAreaCode(): string | setAreaCode(string areaCode): void |
| `number` | `string` | Required | The main phone number, not including the area code or International calling code | getNumber(): string | setNumber(string number): void |
| `extension` | `?string` | Optional | Phone extension number | getExtension(): ?string | setExtension(?string extension): void |

## Example (as JSON)

```json
{
  "areaCode": "111",
  "number": "1231234"
}
```

