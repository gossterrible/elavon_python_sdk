
# Boarding Status Response

## Structure

`BoardingStatusResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `error` | `?string` | Optional | Error message from service | getError(): ?string | setError(?string error): void |
| `boardingStatus` | [`?string (BoardingStatusEnum)`](../../doc/models/boarding-status-enum.md) | Optional | Status of boarded application | getBoardingStatus(): ?string | setBoardingStatus(?string boardingStatus): void |
| `applicationId` | `?string` | Optional | MID (EU) or AWB (NA), MID in NA if boarding status is COMPLETE | getApplicationId(): ?string | setApplicationId(?string applicationId): void |
| `messages` | [`?(BoardingStatusMessage[])`](../../doc/models/boarding-status-message.md) | Optional | [NA] Messages from service | getMessages(): ?array | setMessages(?array messages): void |
| `pendMessages` | [`?(BoardingStatusMessage[])`](../../doc/models/boarding-status-message.md) | Optional | [NA] Pend Messages from service | getPendMessages(): ?array | setPendMessages(?array pendMessages): void |
| `underwriterNotes` | [`?(BoardingStatusMessage[])`](../../doc/models/boarding-status-message.md) | Optional | [NA] Notes by downstream underwritter | getUnderwriterNotes(): ?array | setUnderwriterNotes(?array underwriterNotes): void |
| `underwriterContacts` | `?(string[])` | Optional | [NA] Contact information for downstream underwritter | getUnderwriterContacts(): ?array | setUnderwriterContacts(?array underwriterContacts): void |

## Example (as JSON)

```json
{
  "error": null,
  "boardingStatus": null,
  "applicationId": null,
  "messages": null,
  "pendMessages": null,
  "underwriterNotes": null,
  "underwriterContacts": null
}
```

