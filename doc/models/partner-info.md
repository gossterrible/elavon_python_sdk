
# Partner Info

## Structure

`PartnerInfo`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `partnerName` | `?string` | Optional | - | getPartnerName(): ?string | setPartnerName(?string partnerName): void |
| `associateId` | `?string` | Optional | - | getAssociateId(): ?string | setAssociateId(?string associateId): void |
| `bookOfBusiness` | `?string` | Optional | - | getBookOfBusiness(): ?string | setBookOfBusiness(?string bookOfBusiness): void |
| `correlationId` | `?string` | Optional | - | getCorrelationId(): ?string | setCorrelationId(?string correlationId): void |
| `partnerSource` | `?string` | Optional | - | getPartnerSource(): ?string | setPartnerSource(?string partnerSource): void |
| `merchantUserId` | `string` | Required | Client End User Id | getMerchantUserId(): string | setMerchantUserId(string merchantUserId): void |
| `sessionId` | `string` | Required | Fraudnet Id for tracking, required if merchantUserId is provided | getSessionId(): string | setSessionId(string sessionId): void |

## Example (as JSON)

```json
{
  "partnerName": null,
  "associateId": null,
  "bookOfBusiness": null,
  "correlationId": null,
  "partnerSource": null,
  "merchantUserId": "merchantUserId0",
  "sessionId": "sessionId8"
}
```

