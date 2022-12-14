# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.health_care_eligibility_info import HealthCareEligibilityInfo
from swaggerscarecrow.models.payments import Payments


class IntegratorSolutionInfo(object):

    """Implementation of the 'IntegratorSolutionInfo' model.

    TODO: type model description here.

    Attributes:
        health_care_eligibility_selection_map (dict): Map of health care
            service to related info. The valid keys are as follows:
            HEALTH_CARE_ELIGIBILITY, HEALTH_CARE_CLAIMS,
            HEALTH_CARE_REMITTANCEHEALTH_CARE_ELIGIBILITY_AND_ESTIMATOR,
            HEALTH_CARE_PATIENT_BILLING
        payments (Payments): TODO: type description here.
        has_ecs_only (bool): TODO: type description here.
        sku (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "health_care_eligibility_selection_map": 'healthCareEligibilitySelectionMap',
        "payments": 'payments',
        "has_ecs_only": 'hasEcsOnly',
        "sku": 'sku'
    }

    _optionals = [
        'health_care_eligibility_selection_map',
        'payments',
        'has_ecs_only',
        'sku',
    ]

    def __init__(self,
                 health_care_eligibility_selection_map=APIHelper.SKIP,
                 payments=APIHelper.SKIP,
                 has_ecs_only=APIHelper.SKIP,
                 sku=APIHelper.SKIP):
        """Constructor for the IntegratorSolutionInfo class"""

        # Initialize members of the class
        if health_care_eligibility_selection_map is not APIHelper.SKIP:
            self.health_care_eligibility_selection_map = health_care_eligibility_selection_map 
        if payments is not APIHelper.SKIP:
            self.payments = payments 
        if has_ecs_only is not APIHelper.SKIP:
            self.has_ecs_only = has_ecs_only 
        if sku is not APIHelper.SKIP:
            self.sku = sku 

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

        health_care_eligibility_selection_map = HealthCareEligibilityInfo.from_dictionary(dictionary.get('healthCareEligibilitySelectionMap')) if 'healthCareEligibilitySelectionMap' in dictionary.keys() else APIHelper.SKIP 
        payments = Payments.from_dictionary(dictionary.get('payments')) if 'payments' in dictionary.keys() else APIHelper.SKIP 
        has_ecs_only = dictionary.get("hasEcsOnly") if "hasEcsOnly" in dictionary.keys() else APIHelper.SKIP
        sku = dictionary.get("sku") if dictionary.get("sku") else APIHelper.SKIP
        # Return an object of this model
        return cls(health_care_eligibility_selection_map,
                   payments,
                   has_ecs_only,
                   sku)
