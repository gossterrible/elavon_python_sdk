# BoardingStatusRequestParams

A container that holds all the required elements needed to make a boarding status call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client id of application submission, to be provided to partners | 
**unique_id** | **str** | Unique identifier of application submission, alphanumeric. Provided by the client.The uniqueId must be wholly original and never repeated. The client&#39;s name followed by a millisecond timestamp would work well. | 
**country** | **str** | Country of application submission, ISO 3166-1 alpha-3 standard applies | 
**sales_rep_code** | **str** | Identifier of sales representative responsible for submission status is being requested for | 
**boarding_id** | **str** | MID(EU)/AWB(NA), value is returned from a successful boarding | [optional] 
**correlation_id** | **str** | [NA] Identifier of alternative correlation Id to be used in the place of boardingId | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


