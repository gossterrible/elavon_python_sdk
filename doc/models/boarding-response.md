
# Boarding Response

## Structure

`BoardingResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `error` | `?string` | Optional | Error message from service | getError(): ?string | setError(?string error): void |
| `boardingId` | `?string` | Optional | AWB (NA) or ApplicationID/MID (EU) | getBoardingId(): ?string | setBoardingId(?string boardingId): void |
| `merchantId` | `?string` | Optional | MID (EU) | getMerchantId(): ?string | setMerchantId(?string merchantId): void |
| `chainId` | `?string` | Optional | [NA] New chain id, generated if boarding request specified creation of new chain | getChainId(): ?string | setChainId(?string chainId): void |
| `duplicateRequest` | `?bool` | Optional | True if boarding request was a duplicate request | getDuplicateRequest(): ?bool | setDuplicateRequest(?bool duplicateRequest): void |
| `processErrorType` | [`?string (ProcessErrorTypeEnum)`](../../doc/models/process-error-type-enum.md) | Optional | - | getProcessErrorType(): ?string | setProcessErrorType(?string processErrorType): void |
| `eframeStatus` | [`?string (EframeStatusEnum)`](../../doc/models/eframe-status-enum.md) | Optional | [EU][Elavon Germany] Eframe boarding Status | getEframeStatus(): ?string | setEframeStatus(?string eframeStatus): void |
| `eframeError` | `?string` | Optional | Error message from Eframe | getEframeError(): ?string | setEframeError(?string eframeError): void |

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

