# BankingInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**funding_method** | **str** | NETCREDIT or GROSS | 
**account_number** | **str** | Account number | 
**sort_code** | **str** | Account Sort Code in EU, Account ABA Routing Number in NA | 
**account_name** | **str** | Account holder name, required in EU | [optional] 
**bank_name** | **str** | Name of bank account is associated with | [optional] 
**urgent_payment** | **bool** | [EU] Flag indicating Urgent Payments service | [optional] 
**iban** | **str** | [EU] Account IBAN, required in cases where Sort Code + Account Number not Present | [optional] 
**swift_code** | **str** | [EU] SWIFT/BIC code | [optional] 
**bank_creditor_id** | **str** | [EU] Bank Creditor Id | [optional] 
**bank_direct** | **bool** | [EU]  Bank Direct Flag. Boolean true if yes, false if no | [optional] 
**country** | **str** | Country of bank account, should match application&#39;s root country, ISO 3166-1 alpha-3 standard applies | [optional] 
**tape_id** | **str** | [NA] Tape Id of account, required in NA | [optional] 
**true_daily** | **bool** | [NA] True Daily Flag. Boolean true if yes, false if no | [optional] 
**use_chain_account_number** | **bool** | Use Chain Account Number Flag, Boolean true if yes, false if no | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


