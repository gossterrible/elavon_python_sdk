
# Signer

## Structure

`Signer`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `signerId` | `string` | Required | The unique signer identifier | getSignerId(): string | setSignerId(string signerId): void |
| `signer` | [`Name`](../../doc/models/name.md) | Required | - | getSigner(): Name | setSigner(Name signer): void |
| `emailAddress` | `?string` | Optional | Email Address of signer | getEmailAddress(): ?string | setEmailAddress(?string emailAddress): void |
| `principal` | `bool` | Required | Indicator for signer is principal for business entity | getPrincipal(): bool | setPrincipal(bool principal): void |
| `signingCompleteUrl` | `?string` | Optional | The redirect URL for completed signing | getSigningCompleteUrl(): ?string | setSigningCompleteUrl(?string signingCompleteUrl): void |
| `signingDeclineUrl` | `?string` | Optional | The redirect URL for declined signing | getSigningDeclineUrl(): ?string | setSigningDeclineUrl(?string signingDeclineUrl): void |
| `signingExpiredUrl` | `?string` | Optional | The redirect URL for expired signing | getSigningExpiredUrl(): ?string | setSigningExpiredUrl(?string signingExpiredUrl): void |
| `language` | `?string` | Optional | The signer's preferred language | getLanguage(): ?string | setLanguage(?string language): void |
| `optInOut1` | `?bool` | Optional | Indicator for opt in/out for checkobox1 | getOptInOut1(): ?bool | setOptInOut1(?bool optInOut1): void |
| `optInOut2` | `?bool` | Optional | Indicator for opt in/out for checkobox2 | getOptInOut2(): ?bool | setOptInOut2(?bool optInOut2): void |
| `optInOut3` | `?bool` | Optional | Indicator for opt in/out for checkobox3 | getOptInOut3(): ?bool | setOptInOut3(?bool optInOut3): void |

## Example (as JSON)

```json
{
  "signerId": null,
  "signer": {
    "firstName": "John",
    "lastName": "Doe"
  },
  "principal": null
}
```

