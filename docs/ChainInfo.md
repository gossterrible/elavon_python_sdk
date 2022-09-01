# ChainInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_number** | **str** | Name of new chain to be set up | 
**chain_name** | **str** | Number of new chain to be set up | 
**send_statement_to_address** | **str** | Address that the new chain&#39;s statements will be sent to | 
**statement_media** | **str** | Media type of chain&#39;s statements | 
**address** | [**Address**](Address.md) |  | 
**chain_level_billing** | **bool** | Billing level of new chain | 
**bank_accounts** | [**{str: (BankingInfo,)}**](BankingInfo.md) | Chain&#39;s bank account information. The valid keys are as follows: BILLING, DEPOSIT, LEASE, CHARGEBACK | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


