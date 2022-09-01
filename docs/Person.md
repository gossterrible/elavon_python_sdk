# Person


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Name**](Name.md) |  | 
**positions** | **{str: (bool,)}** | Boolean map representing positions of person, if position applies true should be value given for position key. The valid keys are as follows: OFFICER, PARTNER, DIRECTOR, OWNER, SECRETARY, OTHER, BENEFICIAL_OWNER, AUTHORIZED_SIGNER, SOLE_PROP | 
**contact_info** | [**ContactInfo**](ContactInfo.md) |  | [optional] 
**dob** | [**DateComponents**](DateComponents.md) |  | [optional] 
**ownership_pct** | **str** | Ownership percentage of person | [optional] 
**ids** | [**[Identification]**](Identification.md) | Id listing of person | [optional] 
**title_type** | **str** | [NA] Title type of person | [optional] 
**title** | **str** | Free text of person&#39;s title, should title type not provide correct option (NA OTHER) | [optional] 
**signing_personal_guarantee** | **bool** | [NA] Flag indicating if person is signing personal gurantee, true if YES, false if NO | [optional] 
**responsible_party** | **bool** | Flag indicating if person is a responsible party of the business, true if YES, false if NO | [optional] 
**related_party** | **bool** | Flag indicating if person is a related party of the business, true if YES, false if NO | [optional] 
**residing_country** | **str** | Current country of residence of person, ISO 3166-1 alpha-3 standard applies | [optional] 
**primary_nationality** | **str** | Primary citizenship/nationality of person, ISO 3166-1 alpha-3 standard applies | [optional] 
**secondary_nationality** | **str** | Secondary citizenship/nationality of person, ISO 3166-1 alpha-3 standard applies | [optional] 
**documentary_info** | [**DocumentaryInfo**](DocumentaryInfo.md) |  | [optional] 
**alternate_address_info** | [**AlternateAddressInfo**](AlternateAddressInfo.md) |  | [optional] 
**is_new_owner** | **bool** | [EU] Flag indicating if person is a new owner of the buisness, true if YES, false if NO | [optional] 
**directional_ownership_type** | **str** | [EU] Indicator if person has direct or indirect ownership of business | [optional] 
**signing_agreement** | **bool** | Flag indicating if person if signing the agreement, true if YES, false if NO | [optional] 
**us_person** | **bool** | [NA] Flag indicating if person is a US citizen, true if YES, false if NO | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


