# GetQuizResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **int** |  | [optional] 
**quiz_initial_response_type** | **str** | Status of quiz response | [optional] 
**transaction_key** | **str** | Unique identifier of quiz response, to be used in anser request quiz if successful response is given | [optional] 
**quiz_id** | **int** | Unique identifier of quiz, to be used in answer request quiz if successful response is given | [optional] 
**quiz_questions** | [**[QuizQuestion]**](QuizQuestion.md) | Quiz questions, given if request was successful | [optional] 
**error** | **str** | Error message from service | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


