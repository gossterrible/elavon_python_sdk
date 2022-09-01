
# Partner Info

## Structure

`PartnerInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `partner_name` | `string` | Optional | - |
| `associate_id` | `string` | Optional | - |
| `book_of_business` | `string` | Optional | - |
| `correlation_id` | `string` | Optional | - |
| `partner_source` | `string` | Optional | - |
| `merchant_user_id` | `string` | Required | Client End User Id |
| `session_id` | `string` | Required | Fraudnet Id for tracking, required if merchantUserId is provided |

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

