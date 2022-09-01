# AnswerQuizRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiz_id** | **int** | Unique identifier of quiz, returned in successful get quiz response | 
**transaction_key** | **str** | Unique identifier of quiz response, returned in get quiz response | 
**quiz_answers** | [**[QuizAnswer]**](QuizAnswer.md) | Answers to quiz | 
**id** | **str** | The app request ID | [optional] 
**mid** | **str** | The Merchant ID | [optional] 
**email** | **str** | The email address | [optional] 
**legal_name** | **str** | The legal name | [optional] 
**vat_id** | **str** | The VAT ID | [optional] 
**cc_email** | **str** | The CC email address | [optional] 
**opt_out** | **bool** | OptOut | [optional] 
**marketing_data_consent_map** | **{str: (bool,)}** | The Marketing Consent | [optional] 
**country** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


