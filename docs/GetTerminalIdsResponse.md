# GetTerminalIdsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **int** |  | [optional] 
**error** | **str** | If processing error occurs, will contain information, else will be empty or null | [optional] 
**welcome_url** | **str** | Welcome to Converge URL, typically provided to costomer via email | [optional] 
**virtual_id** | **str** | Virtual Id, for Converge | [optional] 
**terminal_bin** | **str** | Terminal BIN | [optional] 
**terminal_id_data_map** | **{str: ([TerminalIdData],)}** | Map of item code to various Converge data properties | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


