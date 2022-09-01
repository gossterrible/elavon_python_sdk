
# Company Query Response

## Structure

`CompanyQueryResponse`

## Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `responseId` | `?int` | Optional | - | getResponseId(): ?int | setResponseId(?int responseId): void |
| `searchResults` | [`?(CompanyLightweight[])`](../../doc/models/company-lightweight.md) | Optional | - | getSearchResults(): ?array | setSearchResults(?array searchResults): void |
| `error` | `?string` | Optional | - | getError(): ?string | setError(?string error): void |
| `timings` | [`?Timings`](../../doc/models/timings.md) | Optional | - | getTimings(): ?Timings | setTimings(?Timings timings): void |

## Example (as JSON)

```json
{
  "responseId": null,
  "searchResults": null,
  "error": null,
  "timings": null
}
```

