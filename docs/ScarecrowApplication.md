# ScarecrowApplication


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client id of application submission, to be provided to partners | 
**unique_id** | **str** | Unique identifier of application submission, alphanumeric. Provided by the client.The uniqueId must be wholly original and never repeated. The client&#39;s name followed by a millisecond timestamp would work well. | 
**country** | **str** | Country of application submission, ISO 3166-1 alpha-3 standard applies | 
**principal** | [**Person**](Person.md) |  | 
**business_info** | [**BusinessInfo**](BusinessInfo.md) |  | 
**financial_info** | [**FinancialInfo**](FinancialInfo.md) |  | 
**sales_rep_code** | **str** | Identifier of sales representative responsible for submission | 
**contact** | [**Person**](Person.md) |  | 
**bank_accounts** | [**{str: (BankingInfo,)}**](BankingInfo.md) | Bank account container. Valid keys are as follows: BILLING, DEPOSIT, LEASE, CHARGEBACK | 
**card_pricing** | [**CardPricing**](CardPricing.md) |  | 
**parent_entity** | **str** | Entity that is parent to submisssion, forms a pair with client group, to be provided to partners | 
**client_group_number** | **str** | Client group number of application submission, paris with parent entity, to be provided to partners, required in NA | [optional] 
**banker_id** | **str** | [EU] Identifier of banker responsible for submission | [optional] 
**banker_partner_id** | **str** | [EU] Identifier of banker partner responsible for submission | [optional] 
**additional_shareholders** | [**[Person]**](Person.md) |  | [optional] 
**fees** | [**[Fee]**](Fee.md) |  | [optional] 
**monetary_pricing_program** | **str** | Pricing program also called MPP/NPP, to be provided to partners, required in EU | [optional] 
**authenticate_pricing_program** | **str** | Pricing program also called APP, to be provided to partners, required in EU | [optional] 
**short_name** | **str** | [NA] | [optional] 
**fraud_check_result** | [**FraudCheckResult**](FraudCheckResult.md) |  | [optional] 
**site_survey** | [**SiteSurvey**](SiteSurvey.md) |  | [optional] 
**dynamic_currency_conversion** | [**DynamicCurrencyConversion**](DynamicCurrencyConversion.md) |  | [optional] 
**billing_statement** | [**BillingStatement**](BillingStatement.md) |  | [optional] 
**funding_statement** | [**FundingStatement**](FundingStatement.md) |  | [optional] 
**electronic_statement** | [**ElectronicStatement**](ElectronicStatement.md) |  | [optional] 
**vat_invoice_statement** | [**VatInvoiceStatement**](VatInvoiceStatement.md) |  | [optional] 
**billing_method** | **str** | [NA] NETCREDIT or GROSS | [optional] 
**referrer_name** | **str** | Application submission&#39;s referrer name, to be provided to partners, required in NA | [optional] 
**referrer_reference_number** | **str** | The reference number associated with the referrer, known by Elavon. | [optional] 
**previous_processor** | **str** | [NA] Customer&#39;s previous payment processor | [optional] 
**value_added_info** | [**ValueAddedInfo**](ValueAddedInfo.md) |  | [optional] 
**equipment_info** | [**EquipmentInfo**](EquipmentInfo.md) |  | [optional] 
**branch_number** | **str** | Bank branch number associated with application submission | [optional] 
**branch_code** | **str** | Bank branch code associated with application submission | [optional] 
**self_boarded_external** | **bool** | [NA] Flag indicating if application is self boarded externally, suppresses forms of post-boarding contact | [optional] 
**employee_number** | **str** | Number used to identify a specific employee | [optional] 
**rep_referral_number** | **str** | Number used to identify a specific representative | [optional] 
**promotional_code** | **str** | A discount/promotional code | [optional] 
**chain_info** | [**ChainInfo**](ChainInfo.md) |  | [optional] 
**distributions** | [**{str: (DistributionInfo,)}**](DistributionInfo.md) | Distribution container for chargebacks and retrievals. The valid keys are as follows: CHARGEBACK, RETRIEVAL | [optional] 
**additional_location_info** | [**AdditionalLocationInfo**](AdditionalLocationInfo.md) |  | [optional] 
**signed_date** | [**DateComponents**](DateComponents.md) |  | [optional] 
**signed_type** | **str** | [NA] How application was signed | [optional] 
**intermediary_owner_info** | [**IntermediaryOwnerInfo**](IntermediaryOwnerInfo.md) |  | [optional] 
**revenue_share_info** | [**RevenueShareInfo**](RevenueShareInfo.md) |  | [optional] 
**elavon_contract** | **str** | [EU] Determine which Merchant Agreement customer will sign | [optional] 
**internal_use_info** | [**InternalUseInfo**](InternalUseInfo.md) |  | [optional] 
**eframe_info** | [**EframeInfo**](EframeInfo.md) |  | [optional] 
**partner_info** | [**PartnerInfo**](PartnerInfo.md) |  | [optional] 
**alternative_payment_methods** | [**[ApmAcquirer]**](ApmAcquirer.md) | [EU] List of Alternative Payment Method Acquirers container | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


