# EquipmentInfo

In NA, it's mandatory to have at least one piece of equipment. For third party vendors            managing their own equipment, at least one Value Added Reseller (VAR) code must be sent.            Contact your Elavon representative for the VAR code(s).            In EU, equipmentInfo is optional and no equipment has to be sent. If you have any equipment            managed by Elavon, contact your Elavon representative for the VAR code(s).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equipment_items** | [**[EquipmentItem]**](EquipmentItem.md) | Equipment item listing | 
**fusebox_info** | [**FuseboxInfo**](FuseboxInfo.md) |  | 
**terminal_services** | [**[TerminalService]**](TerminalService.md) | Terminal services to be applied to equipment items | [optional] 
**training_type** | **str** | [NA] Type of training to be given for equipment | [optional] 
**shipping_method** | **str** | Shipping of equipment priority | [optional] 
**network** | **str** | Network equipment will be connected to | [optional] 
**anticipated_start_date** | [**DateComponents**](DateComponents.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


