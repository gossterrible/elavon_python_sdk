
# Boarding Status Request Params

A container that holds all the required elements needed to make a boarding status call

## Structure

`BoardingStatusRequestParams`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `boardingId` | `?string` | Optional | MID(EU)/AWB(NA), value is returned from a successful boarding | getBoardingId(): ?string | setBoardingId(?string boardingId): void |
| `correlationId` | `?string` | Optional | [NA] Identifier of alternative correlation Id to be used in the place of boardingId | getCorrelationId(): ?string | setCorrelationId(?string correlationId): void |
| `clientId` | `string` | Required | Client id of application submission, to be provided to partners | getClientId(): string | setClientId(string clientId): void |
| `uniqueId` | `string` | Required | Unique identifier of application submission, alphanumeric. Provided by the client.The uniqueId must be wholly original and never repeated. The client's name followed by a millisecond timestamp would work well. | getUniqueId(): string | setUniqueId(string uniqueId): void |
| `country` | `string` | Required | Country of application submission, ISO 3166-1 alpha-3 standard applies | getCountry(): string | setCountry(string country): void |
| `salesRepCode` | `string` | Required | Identifier of sales representative responsible for submission status is being requested for | getSalesRepCode(): string | setSalesRepCode(string salesRepCode): void |

## Example (as JSON)

```json
{
  "clientId": "IDNA",
  "uniqueId": "AcmeCorp1572566399123",
  "country": "USA",
  "salesRepCode": null
}
```

