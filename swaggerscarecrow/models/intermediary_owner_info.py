# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.intermediary_owner import IntermediaryOwner


class IntermediaryOwnerInfo(object):

    """Implementation of the 'IntermediaryOwnerInfo' model.

    TODO: type model description here.

    Attributes:
        intermediary_owners (list of IntermediaryOwner): Intermediary owners
            listing
        additional_intermediate_owners (bool): Flag indicating if there are
            additional intermediary owners beyond the ones noted here, true if
            YES, false if NO

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "intermediary_owners": 'intermediaryOwners',
        "additional_intermediate_owners": 'additionalIntermediateOwners'
    }

    _optionals = [
        'additional_intermediate_owners',
    ]

    def __init__(self,
                 intermediary_owners=None,
                 additional_intermediate_owners=APIHelper.SKIP):
        """Constructor for the IntermediaryOwnerInfo class"""

        # Initialize members of the class
        self.intermediary_owners = intermediary_owners 
        if additional_intermediate_owners is not APIHelper.SKIP:
            self.additional_intermediate_owners = additional_intermediate_owners 

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

        intermediary_owners = None
        if dictionary.get('intermediaryOwners') is not None:
            intermediary_owners = [IntermediaryOwner.from_dictionary(x) for x in dictionary.get('intermediaryOwners')]
        additional_intermediate_owners = dictionary.get("additionalIntermediateOwners") if "additionalIntermediateOwners" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(intermediary_owners,
                   additional_intermediate_owners)
