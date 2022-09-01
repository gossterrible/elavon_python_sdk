# EquipmentItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | SKU of product | 
**quantity** | **int** | Number of product being chosen | 
**pricing_items** | [**[EquipmentPricing]**](EquipmentPricing.md) | Product pricinging listing | 
**trx_free_month** | **int** | Free transaction per month per terminal | 
**item_settings** | [**ItemSettings**](ItemSettings.md) |  | [optional] 
**exception_items** | [**[ExceptionItem]**](ExceptionItem.md) | [EU] Exception pricing to be sent for equipment pricing | [optional] 
**service_fee** | **float** |  | [optional] 
**future_effective_date** | [**DateComponents**](DateComponents.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


