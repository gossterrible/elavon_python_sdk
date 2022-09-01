# BoardingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **int** |  | [optional] 
**error** | **str** | Error message from service | [optional] 
**boarding_id** | **str** | AWB (NA) or ApplicationID/MID (EU) | [optional] 
**merchant_id** | **str** | MID (EU) | [optional] 
**chain_id** | **str** | [NA] New chain id, generated if boarding request specified creation of new chain | [optional] 
**duplicate_request** | **bool** | True if boarding request was a duplicate request | [optional] 
**process_error_type** | **str** |  | [optional] 
**eframe_status** | **str** | [EU][Elavon Germany] Eframe boarding Status | [optional] 
**eframe_error** | **str** | Error message from Eframe | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


