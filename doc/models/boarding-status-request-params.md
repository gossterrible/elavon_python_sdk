
# Boarding Status Request Params

A container that holds all the required elements needed to make a boarding status call

## Structure

`BoardingStatusRequestParams`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `boarding_id` | `string` | Optional | MID(EU)/AWB(NA), value is returned from a successful boarding |
| `correlation_id` | `string` | Optional | [NA] Identifier of alternative correlation Id to be used in the place of boardingId |
| `client_id` | `string` | Required | Client id of application submission, to be provided to partners |
| `unique_id` | `string` | Required | Unique identifier of application submission, alphanumeric. Provided by the client.The uniqueId must be wholly original and never repeated. The client's name followed by a millisecond timestamp would work well. |
| `country` | `string` | Required | Country of application submission, ISO 3166-1 alpha-3 standard applies |
| `sales_rep_code` | `string` | Required | Identifier of sales representative responsible for submission status is being requested for |

## Example (as JSON)

```json
{
  "clientId": "IDNA",
  "uniqueId": "AcmeCorp1572566399123",
  "country": "USA",
  "salesRepCode": null
}
```

