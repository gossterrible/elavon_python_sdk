# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class FundingStatement(object):

    """Implementation of the 'FundingStatement' model.

    TODO: type model description here.

    Attributes:
        mtype (Type3Enum): TODO: type description here.
        media (Media1Enum): TODO: type description here.
        email_address (string): [EU] email address
        frequency (Frequency2Enum): [EU] DAILY, WEEKLY, MONTHLY

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "media": 'media',
        "email_address": 'emailAddress',
        "frequency": 'frequency'
    }

    _optionals = [
        'mtype',
        'media',
        'email_address',
        'frequency',
    ]

    def __init__(self,
                 mtype=APIHelper.SKIP,
                 media=APIHelper.SKIP,
                 email_address=APIHelper.SKIP,
                 frequency=APIHelper.SKIP):
        """Constructor for the FundingStatement class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if media is not APIHelper.SKIP:
            self.media = media 
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        if frequency is not APIHelper.SKIP:
            self.frequency = frequency 

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

        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        media = dictionary.get("media") if dictionary.get("media") else APIHelper.SKIP
        email_address = dictionary.get("emailAddress") if dictionary.get("emailAddress") else APIHelper.SKIP
        frequency = dictionary.get("frequency") if dictionary.get("frequency") else APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   media,
                   email_address,
                   frequency)
