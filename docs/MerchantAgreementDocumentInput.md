# MerchantAgreementDocumentInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Language of document to be generated,  ISO 639-1 standard applies | 
**document_id** | **str** | Unique id of document | 
**scarecrow_application** | [**ScarecrowApplication**](ScarecrowApplication.md) |  | 
**vendor_info** | [**ProviderInfo**](ProviderInfo.md) |  | 
**bank_account_details_map** | [**{str: (BankAccountAdditionalInfo,)}**](BankAccountAdditionalInfo.md) | Application&#39;s additional bank account informationThe valid keys are as follows: BILLING, DEPOSIT, LEASE, CHARGEBACK | 
**displayed_currency** | **str** | Application&#39;s currency, ISO 4217 standard applies | 
**agreement_id** | **str** | Merchant id (MID) | [optional] 
**document_packet_id** | **str** | Document packet id | [optional] 
**signed** | **bool** | Boolean flag indicating if document has been signed, true if  YES, false if NO | [optional] 
**grouped_application** | **bool** | Boolean flag indicating if document is of a group of applications, true if  YES, false if NO | [optional] 
**wet_signed** | **bool** | Boolean flag indicating if document is to be wet signed, true if  YES, false if NO | [optional] 
**acting_intermediary_info** | [**ActingIntermediaryInfo**](ActingIntermediaryInfo.md) |  | [optional] 
**is_tax_exempt_equipment** | **bool** | Flag indicating if equipment is to be considered tax exempt, true if exempt YES, false if NOT exept | [optional] 
**talech_egift_only** | **bool** | Flag indicating if equipment is to Talech eGift, true if selected YES, false if NOT selected | [optional] 
**additional_description_info** | [**AdditionalDescriptionInfo**](AdditionalDescriptionInfo.md) |  | [optional] 
**additional_value_added_service_info** | [**ValueAddedServices**](ValueAddedServices.md) |  | [optional] 
**additional_business_info** | [**AdditionalBusinessInfo**](AdditionalBusinessInfo.md) |  | [optional] 
**funding_type** | **str** | Application&#39;s funding type | [optional] 
**integrator_solution_info** | [**IntegratorSolutionInfo**](IntegratorSolutionInfo.md) |  | [optional] 
**additional_lease_info** | [**AdditionalLeaseInfo**](AdditionalLeaseInfo.md) |  | [optional] 
**marketing_data_consent_map** | **{str: (bool,)}** | Application&#39;s consent form (POL).The valid keys are the numerical value of the marketing consent option (1, 2, 3, etc) | [optional] 
**additional_site_survey_info** | [**AdditionalSiteSurveyInfo**](AdditionalSiteSurveyInfo.md) |  | [optional] 
**kyc_quiz_status_map** | **{str: (str,)}** | Status results of the KCY check | [optional] 
**var_other_details** | [**VarOtherDetails**](VarOtherDetails.md) |  | [optional] 
**additional_card_pricing_info** | [**AdditionalCardPricingInfo**](AdditionalCardPricingInfo.md) |  | [optional] 
**sales_office_contact** | [**SalesOfficeContact**](SalesOfficeContact.md) |  | [optional] 
**additional_auth_pricing_program_info** | [**AdditionalAuthPricingProgramInfo**](AdditionalAuthPricingProgramInfo.md) |  | [optional] 
**applicant_email** | **str** | Applicant&#39;s email address | [optional] 
**application_id** | **int** | Application id | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


