
# Boarding Response

## Structure

`BoardingResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_id` | `int` | Optional | - |
| `error` | `string` | Optional | Error message from service |
| `boarding_id` | `string` | Optional | AWB (NA) or ApplicationID/MID (EU) |
| `merchant_id` | `string` | Optional | MID (EU) |
| `chain_id` | `string` | Optional | [NA] New chain id, generated if boarding request specified creation of new chain |
| `duplicate_request` | `bool` | Optional | True if boarding request was a duplicate request |
| `process_error_type` | [`ProcessErrorTypeEnum`](../../doc/models/process-error-type-enum.md) | Optional | - |
| `eframe_status` | [`EframeStatusEnum`](../../doc/models/eframe-status-enum.md) | Optional | [EU][Elavon Germany] Eframe boarding Status |
| `eframe_error` | `string` | Optional | Error message from Eframe |

## Example (as JSON)

```json
{
  "responseId": null,
  "error": null,
  "boardingId": null,
  "merchantId": null,
  "chainId": null,
  "duplicateRequest": null,
  "processErrorType": null,
  "eframeStatus": null,
  "eframeError": null
}
```

