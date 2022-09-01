# UploadDocumentsRequestParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boarding_id** | **str** | MID(EU)/AWB(NA) of application to upload documents for, MID can be used in NA if it has been generated | 
**client_id** | **str** | Client id of application submission, to be provided to partners, and should match value present on boarding request | 
**unique_id** | **str** | Unique identifier of application submission, alphanumeric. Provided by the client.The uniqueId must be wholly original and never repeated. The client&#39;s name followed by a millisecond timestamp would work well. | 
**country** | **str** | Country of application submission, ISO 3166-1 alpha-3 standard applies, and should match value present on boarding request | 
**sales_rep_number** | **str** | Identifier of sales representative responsible for submission, should match value present on boarding request | 
**image_document_data** | [**ImageDocumentData**](ImageDocumentData.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


