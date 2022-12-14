# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.acs_info import AcsInfo
from swaggerscarecrow.models.ebt_info import EbtInfo
from swaggerscarecrow.models.ecs_info import EcsInfo
from swaggerscarecrow.models.efs_3_d_secure_info import Efs3dSecureInfo
from swaggerscarecrow.models.fanfare_info import FanfareInfo
from swaggerscarecrow.models.ocm_info import OcmInfo
from swaggerscarecrow.models.on_demand_info import OnDemandInfo
from swaggerscarecrow.models.straight_send_info import StraightSendInfo


class ValueAddedInfo(object):

    """Implementation of the 'ValueAddedInfo' model.

    TODO: type model description here.

    Attributes:
        value_adds (dict): Boolean map to indicate presence of various value
            added services, true if present, false/null if absent.The valid
            keys are as follows: FANFARE, ELECTRONIC_CHECKING_SERVICE,
            CREDIT_CARD_SURCHARGING, CASH_BACK, MERCHANT_CONNECT_PREMIUM,
            CONTACTLESS, CONVERGE_BILLING_AND_INVOICE, CONVERGE_HOSPITALITY,
            E_TOKENIZATION, SECURED_ENCRYPT, HEALTH_CARE_ELIGIBILITY,
            HEALTH_CARE_CLAIMS, HEALTH_CARE_REMITTANCE,
            HEALTH_CARE_ELIGIBILITY_AND_ESTIMATOR,
            HEALTH_CARE_PATIENT_BILLING, FRAUD_SERVICES_3D_SECURE,
            STRAIGHT_SEND, ON_DEMAND
        ebt_info (EbtInfo): TODO: type description here.
        ecs_info (EcsInfo): TODO: type description here.
        acs_info (AcsInfo): TODO: type description here.
        fanfare_info (FanfareInfo): TODO: type description here.
        gsm_prepaid_type (GsmPrepaidTypeEnum): [EU] Additional GSM SIM prepaid
            information
        surcharge_managed_by (string): [NA] Surcharge Managed By
        credit_surcharge_amt (string): [NA] Credit Surcharge Amount
        efs_3_d_secure_info (Efs3dSecureInfo): TODO: type description here.
        straight_send_info (StraightSendInfo): TODO: type description here.
        on_demand_info (OnDemandInfo): TODO: type description here.
        ocm_info (OcmInfo): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "value_adds": 'valueAdds',
        "ebt_info": 'ebtInfo',
        "ecs_info": 'ecsInfo',
        "acs_info": 'acsInfo',
        "fanfare_info": 'fanfareInfo',
        "gsm_prepaid_type": 'gsmPrepaidType',
        "surcharge_managed_by": 'surchargeManagedBy',
        "credit_surcharge_amt": 'creditSurchargeAmt',
        "efs_3_d_secure_info": 'efs3dSecureInfo',
        "straight_send_info": 'straightSendInfo',
        "on_demand_info": 'onDemandInfo',
        "ocm_info": 'ocmInfo'
    }

    _optionals = [
        'value_adds',
        'ebt_info',
        'ecs_info',
        'acs_info',
        'fanfare_info',
        'gsm_prepaid_type',
        'surcharge_managed_by',
        'credit_surcharge_amt',
        'efs_3_d_secure_info',
        'straight_send_info',
        'on_demand_info',
        'ocm_info',
    ]

    def __init__(self,
                 value_adds=APIHelper.SKIP,
                 ebt_info=APIHelper.SKIP,
                 ecs_info=APIHelper.SKIP,
                 acs_info=APIHelper.SKIP,
                 fanfare_info=APIHelper.SKIP,
                 gsm_prepaid_type=APIHelper.SKIP,
                 surcharge_managed_by=APIHelper.SKIP,
                 credit_surcharge_amt=APIHelper.SKIP,
                 efs_3_d_secure_info=APIHelper.SKIP,
                 straight_send_info=APIHelper.SKIP,
                 on_demand_info=APIHelper.SKIP,
                 ocm_info=APIHelper.SKIP):
        """Constructor for the ValueAddedInfo class"""

        # Initialize members of the class
        if value_adds is not APIHelper.SKIP:
            self.value_adds = value_adds 
        if ebt_info is not APIHelper.SKIP:
            self.ebt_info = ebt_info 
        if ecs_info is not APIHelper.SKIP:
            self.ecs_info = ecs_info 
        if acs_info is not APIHelper.SKIP:
            self.acs_info = acs_info 
        if fanfare_info is not APIHelper.SKIP:
            self.fanfare_info = fanfare_info 
        if gsm_prepaid_type is not APIHelper.SKIP:
            self.gsm_prepaid_type = gsm_prepaid_type 
        if surcharge_managed_by is not APIHelper.SKIP:
            self.surcharge_managed_by = surcharge_managed_by 
        if credit_surcharge_amt is not APIHelper.SKIP:
            self.credit_surcharge_amt = credit_surcharge_amt 
        if efs_3_d_secure_info is not APIHelper.SKIP:
            self.efs_3_d_secure_info = efs_3_d_secure_info 
        if straight_send_info is not APIHelper.SKIP:
            self.straight_send_info = straight_send_info 
        if on_demand_info is not APIHelper.SKIP:
            self.on_demand_info = on_demand_info 
        if ocm_info is not APIHelper.SKIP:
            self.ocm_info = ocm_info 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        value_adds = dictionary.get("valueAdds") if "valueAdds" in dictionary.keys() else APIHelper.SKIP
        ebt_info = EbtInfo.from_dictionary(dictionary.get('ebtInfo')) if 'ebtInfo' in dictionary.keys() else APIHelper.SKIP 
        ecs_info = EcsInfo.from_dictionary(dictionary.get('ecsInfo')) if 'ecsInfo' in dictionary.keys() else APIHelper.SKIP 
        acs_info = AcsInfo.from_dictionary(dictionary.get('acsInfo')) if 'acsInfo' in dictionary.keys() else APIHelper.SKIP 
        fanfare_info = FanfareInfo.from_dictionary(dictionary.get('fanfareInfo')) if 'fanfareInfo' in dictionary.keys() else APIHelper.SKIP 
        gsm_prepaid_type = dictionary.get("gsmPrepaidType") if dictionary.get("gsmPrepaidType") else APIHelper.SKIP
        surcharge_managed_by = dictionary.get("surchargeManagedBy") if dictionary.get("surchargeManagedBy") else APIHelper.SKIP
        credit_surcharge_amt = dictionary.get("creditSurchargeAmt") if dictionary.get("creditSurchargeAmt") else APIHelper.SKIP
        efs_3_d_secure_info = Efs3dSecureInfo.from_dictionary(dictionary.get('efs3dSecureInfo')) if 'efs3dSecureInfo' in dictionary.keys() else APIHelper.SKIP 
        straight_send_info = StraightSendInfo.from_dictionary(dictionary.get('straightSendInfo')) if 'straightSendInfo' in dictionary.keys() else APIHelper.SKIP 
        on_demand_info = OnDemandInfo.from_dictionary(dictionary.get('onDemandInfo')) if 'onDemandInfo' in dictionary.keys() else APIHelper.SKIP 
        ocm_info = OcmInfo.from_dictionary(dictionary.get('ocmInfo')) if 'ocmInfo' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(value_adds,
                   ebt_info,
                   ecs_info,
                   acs_info,
                   fanfare_info,
                   gsm_prepaid_type,
                   surcharge_managed_by,
                   credit_surcharge_amt,
                   efs_3_d_secure_info,
                   straight_send_info,
                   on_demand_info,
                   ocm_info)
