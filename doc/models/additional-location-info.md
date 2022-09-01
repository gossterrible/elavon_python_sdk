
# Additional Location Info

## Structure

`AdditionalLocationInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `centralMid` | `string` | Required | Merchant Id of existing business | getCentralMid(): string | setCentralMid(string centralMid): void |
| `centralLegalName` | `string` | Required | Legal Name of existing business<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` | getCentralLegalName(): string | setCentralLegalName(string centralLegalName): void |
| `centralTaxId` | `?string` | Optional | Tax Id of existing busines, required in cases where Central Legal Name not present | getCentralTaxId(): ?string | setCentralTaxId(?string centralTaxId): void |

## Example (as JSON)

```json
{
  "centralMid": "8024999222",
  "centralLegalName": "Elavon"
}
```

