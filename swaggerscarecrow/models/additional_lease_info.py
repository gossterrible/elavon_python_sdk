# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.lease_details import LeaseDetails


class AdditionalLeaseInfo(object):

    """Implementation of the 'AdditionalLeaseInfo' model.

    TODO: type model description here.

    Attributes:
        lease_details_map (dict): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "lease_details_map": 'leaseDetailsMap'
    }

    _optionals = [
        'lease_details_map',
    ]

    def __init__(self,
                 lease_details_map=APIHelper.SKIP):
        """Constructor for the AdditionalLeaseInfo class"""

        # Initialize members of the class
        if lease_details_map is not APIHelper.SKIP:
            self.lease_details_map = lease_details_map 

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

        lease_details_map = LeaseDetails.from_dictionary(dictionary.get('leaseDetailsMap')) if 'leaseDetailsMap' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(lease_details_map)
