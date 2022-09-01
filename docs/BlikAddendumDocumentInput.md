# BlikAddendumDocumentInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Language of document to be generated,  ISO 639-1 standard applies | 
**document_id** | **str** | Unique id of document | 
**principal** | [**Person**](Person.md) |  | 
**business_info** | [**BusinessInfo**](BusinessInfo.md) |  | 
**agreement_id** | **str** | Merchant id (MID) | [optional] 
**document_packet_id** | **str** | Document packet id | [optional] 
**signed** | **bool** | Boolean flag indicating if document has been signed, true if  YES, false if NO | [optional] 
**grouped_application** | **bool** | Boolean flag indicating if document is of a group of applications, true if  YES, false if NO | [optional] 
**wet_signed** | **bool** | Boolean flag indicating if document is to be wet signed, true if  YES, false if NO | [optional] 
**additional_shareholders** | [**[Person]**](Person.md) | Application&#39;s additional shareholders | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


