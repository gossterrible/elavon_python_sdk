# ImageDocument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **int** | Unique identifier of document | 
**image_type_code** | **str** | Type of document to upload, default to \&quot;APPLI\&quot; | 
**dba_name** | **str** | DBA name of application submission document is to be associated with | 
**mime_type_code** | **str** | MIME type | 
**image_content** | **[str]** | Base 64 encoded document | 
**scan_date** | **datetime** | Date document was scanned | [optional] 
**additional_document_fields** | [**[AdditionalDocumentFields]**](AdditionalDocumentFields.md) | Additional lable specifications | [optional] 
**name** | **str** | Document name | [optional] 
**category** | **str** | Document Category | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


