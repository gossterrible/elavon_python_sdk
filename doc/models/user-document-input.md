
# User Document Input

## Structure

`UserDocumentInput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `language` | `string` | Required | Language of document to be generated,  ISO 639-1 standard applies |
| `document_id` | `string` | Required | Unique id of document |
| `agreement_id` | `string` | Optional | Merchant id (MID) |
| `document_packet_id` | `string` | Optional | Document packet id |
| `signed` | `bool` | Optional | Boolean flag indicating if document has been signed, true if  YES, false if NO |
| `grouped_application` | `bool` | Optional | Boolean flag indicating if document is of a group of applications, true if  YES, false if NO |
| `wet_signed` | `bool` | Optional | Boolean flag indicating if document is to be wet signed, true if  YES, false if NO |

## Example (as JSON)

```json
{
  "language": "en",
  "documentId": "1"
}
```

