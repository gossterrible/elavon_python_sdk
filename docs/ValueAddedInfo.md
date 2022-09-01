# ValueAddedInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_adds** | **{str: (bool,)}** | Boolean map to indicate presence of various value added services, true if present, false/null if absent.The valid keys are as follows: FANFARE, ELECTRONIC_CHECKING_SERVICE, CREDIT_CARD_SURCHARGING, CASH_BACK, MERCHANT_CONNECT_PREMIUM, CONTACTLESS, CONVERGE_BILLING_AND_INVOICE, CONVERGE_HOSPITALITY, E_TOKENIZATION, SECURED_ENCRYPT, HEALTH_CARE_ELIGIBILITY, HEALTH_CARE_CLAIMS, HEALTH_CARE_REMITTANCE, HEALTH_CARE_ELIGIBILITY_AND_ESTIMATOR, HEALTH_CARE_PATIENT_BILLING, FRAUD_SERVICES_3D_SECURE, STRAIGHT_SEND, ON_DEMAND | [optional] 
**ebt_info** | [**EbtInfo**](EbtInfo.md) |  | [optional] 
**ecs_info** | [**EcsInfo**](EcsInfo.md) |  | [optional] 
**acs_info** | [**AcsInfo**](AcsInfo.md) |  | [optional] 
**fanfare_info** | [**FanfareInfo**](FanfareInfo.md) |  | [optional] 
**gsm_prepaid_type** | **str** | [EU] Additional GSM SIM prepaid information | [optional] 
**surcharge_managed_by** | **str** | [NA] Surcharge Managed By | [optional] 
**credit_surcharge_amt** | **str** | [NA] Credit Surcharge Amount | [optional] 
**efs3d_secure_info** | [**Efs3dSecureInfo**](Efs3dSecureInfo.md) |  | [optional] 
**straight_send_info** | [**StraightSendInfo**](StraightSendInfo.md) |  | [optional] 
**on_demand_info** | [**OnDemandInfo**](OnDemandInfo.md) |  | [optional] 
**ocm_info** | [**OcmInfo**](OcmInfo.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


