# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.models.apm_acquirer_type import ApmAcquirerType


class ApmAcquirer(object):

    """Implementation of the 'ApmAcquirer' model.

    TODO: type model description here.

    Attributes:
        acquirer_code (string): Acquirer Code of the Alternative Payment
            Method
        acquirer_types (list of ApmAcquirerType): Acquirer Type of the
            Alternative Payment Method

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acquirer_code": 'acquirerCode',
        "acquirer_types": 'acquirerTypes'
    }

    def __init__(self,
                 acquirer_code=None,
                 acquirer_types=None):
        """Constructor for the ApmAcquirer class"""

        # Initialize members of the class
        self.acquirer_code = acquirer_code 
        self.acquirer_types = acquirer_types 

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

        acquirer_code = dictionary.get("acquirerCode") if dictionary.get("acquirerCode") else None
        acquirer_types = None
        if dictionary.get('acquirerTypes') is not None:
            acquirer_types = [ApmAcquirerType.from_dictionary(x) for x in dictionary.get('acquirerTypes')]
        # Return an object of this model
        return cls(acquirer_code,
                   acquirer_types)