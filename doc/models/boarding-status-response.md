
# Boarding Status Response

## Structure

`BoardingStatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `string` | Optional | Error message from service |
| `boarding_status` | [`BoardingStatusEnum`](../../doc/models/boarding-status-enum.md) | Optional | Status of boarded application |
| `application_id` | `string` | Optional | MID (EU) or AWB (NA), MID in NA if boarding status is COMPLETE |
| `messages` | [`List of BoardingStatusMessage`](../../doc/models/boarding-status-message.md) | Optional | [NA] Messages from service |
| `pend_messages` | [`List of BoardingStatusMessage`](../../doc/models/boarding-status-message.md) | Optional | [NA] Pend Messages from service |
| `underwriter_notes` | [`List of BoardingStatusMessage`](../../doc/models/boarding-status-message.md) | Optional | [NA] Notes by downstream underwritter |
| `underwriter_contacts` | `List of string` | Optional | [NA] Contact information for downstream underwritter |

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

