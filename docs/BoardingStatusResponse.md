# BoardingStatusResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message from service | [optional] 
**boarding_status** | **str** | Status of boarded application | [optional] 
**application_id** | **str** | MID (EU) or AWB (NA), MID in NA if boarding status is COMPLETE | [optional] 
**messages** | [**[BoardingStatusMessage]**](BoardingStatusMessage.md) | [NA] Messages from service | [optional] 
**pend_messages** | [**[BoardingStatusMessage]**](BoardingStatusMessage.md) | [NA] Pend Messages from service | [optional] 
**underwriter_notes** | [**[BoardingStatusMessage]**](BoardingStatusMessage.md) | [NA] Notes by downstream underwritter | [optional] 
**underwriter_contacts** | **[str]** | [NA] Contact information for downstream underwritter | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


