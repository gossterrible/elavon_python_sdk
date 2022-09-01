# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class AdditionalBusinessInfo(object):

    """Implementation of the 'AdditionalBusinessInfo' model.

    TODO: type model description here.

    Attributes:
        ownership_years_over_range (string): Years over max allowed ownership
            length
        is_max_establishment_year (bool): True if business establishment year
            is older than 1906
        has_government_incentive (bool): True if business has a government
            incentive

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ownership_years_over_range": 'ownershipYearsOverRange',
        "is_max_establishment_year": 'isMaxEstablishmentYear',
        "has_government_incentive": 'hasGovernmentIncentive'
    }

    _optionals = [
        'ownership_years_over_range',
        'is_max_establishment_year',
        'has_government_incentive',
    ]

    def __init__(self,
                 ownership_years_over_range=APIHelper.SKIP,
                 is_max_establishment_year=APIHelper.SKIP,
                 has_government_incentive=APIHelper.SKIP):
        """Constructor for the AdditionalBusinessInfo class"""

        # Initialize members of the class
        if ownership_years_over_range is not APIHelper.SKIP:
            self.ownership_years_over_range = ownership_years_over_range 
        if is_max_establishment_year is not APIHelper.SKIP:
            self.is_max_establishment_year = is_max_establishment_year 
        if has_government_incentive is not APIHelper.SKIP:
            self.has_government_incentive = has_government_incentive 

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

        ownership_years_over_range = dictionary.get("ownershipYearsOverRange") if dictionary.get("ownershipYearsOverRange") else APIHelper.SKIP
        is_max_establishment_year = dictionary.get("isMaxEstablishmentYear") if "isMaxEstablishmentYear" in dictionary.keys() else APIHelper.SKIP
        has_government_incentive = dictionary.get("hasGovernmentIncentive") if "hasGovernmentIncentive" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(ownership_years_over_range,
                   is_max_establishment_year,
                   has_government_incentive)
