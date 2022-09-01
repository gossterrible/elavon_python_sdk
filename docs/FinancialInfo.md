# FinancialInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_sale_amount** | **str** | Average Transaction Value (ATV) | 
**monthly_card_sales** | **str** | Predicted monthly credit card sales | 
**card_present_acceptance_percent** | **str** | The percentage split of card present transactions | 
**internet_acceptance_percent** | **str** | The percentage split of internet/ecom transactions | 
**moto_acceptance_percent** | **str** | The percentage split of mail-order/telephone-order transactions | 
**annual_card_sales** | **str** | [EU] Projected yearly card sales | [optional] 
**annual_revenue** | **str** | Projected yearly gross revenue | [optional] 
**highest_ticket_amount** | **str** | [NA] Highest estimated ticket amount | [optional] 
**highest_ticket_frequency** | **int** | [NA] Frequency with which highest ticket is received annually | [optional] 
**funding_currency** | **str** | Funding currency of business | [optional] 
**business_email_address** | **str** | [EU] Business email contact, required if internetAcceptancePercent &gt; 0 | [optional] 
**business_website_url** | **str** | Business URL, required if internetAcceptancePercent &gt; 0 | [optional] 
**customer_service_phone** | [**PhoneNumber**](PhoneNumber.md) |  | [optional] 
**not_present_delay_days** | **int** | [NA] Card Not Present delay for something | [optional] 
**deposit_frequency** | **str** | [EU] | [optional] 
**deposit_size_percent** | **str** | [EU] | [optional] 
**deposit_balance_days** | **str** | [EU] | [optional] 
**deposit_fulfillment_days** | **str** | [EU] | [optional] 
**full_payment_percent** | **str** | [EU] | [optional] 
**full_payment_fulfillment** | **str** | [EU] | [optional] 
**utilize_cvv2** | **bool** | [EU] | [optional] 
**recurring_transactions** | **bool** | [EU] | [optional] 
**contract_term_type** | **str** | [EU] ZERO_MONTH, TWELVE_MONTHS, TWENTY_FOUR_MONTHS, or THIRTY_SIX_MONTHS | [optional] 
**months_closed** | **[str]** | List containing months business is closed, for seasonal businesses | [optional] 
**monetary_billing_method** | **str** | [NA] string, CARD_DISCOUNT or DIA | [optional] 
**authorization_included** | **bool** | [NA] | [optional] 
**annual_fee_month_start** | **str** | [NA] The month in which annual fee is applied | [optional] 
**money_services** | **bool** | [EU] | [optional] 
**payment_services** | **bool** |  | [optional] 
**third_party_processor** | **bool** |  | [optional] 
**non_government_non_profit** | **bool** | [EU] | [optional] 
**daily_discount** | **bool** | [NA] | [optional] 
**non_bank_atm** | **bool** | Does business operate its own ATM (not associated with a bank) | [optional] 
**embassy** | **bool** | Deprecated | [optional] 
**high_inter_annual_trans_ngo** | **bool** | Deprecated | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


