# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.name import Name


class Signer(object):

    """Implementation of the 'Signer' model.

    TODO: type model description here.

    Attributes:
        signer_id (string): The unique signer identifier
        signer (Name): TODO: type description here.
        email_address (string): Email Address of signer
        principal (bool): Indicator for signer is principal for business
            entity
        signing_complete_url (string): The redirect URL for completed signing
        signing_decline_url (string): The redirect URL for declined signing
        signing_expired_url (string): The redirect URL for expired signing
        language (string): The signer's preferred language
        opt_in_out_1 (bool): Indicator for opt in/out for checkobox1
        opt_in_out_2 (bool): Indicator for opt in/out for checkobox2
        opt_in_out_3 (bool): Indicator for opt in/out for checkobox3

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "signer_id": 'signerId',
        "signer": 'signer',
        "principal": 'principal',
        "email_address": 'emailAddress',
        "signing_complete_url": 'signingCompleteUrl',
        "signing_decline_url": 'signingDeclineUrl',
        "signing_expired_url": 'signingExpiredUrl',
        "language": 'language',
        "opt_in_out_1": 'optInOut1',
        "opt_in_out_2": 'optInOut2',
        "opt_in_out_3": 'optInOut3'
    }

    _optionals = [
        'email_address',
        'signing_complete_url',
        'signing_decline_url',
        'signing_expired_url',
        'language',
        'opt_in_out_1',
        'opt_in_out_2',
        'opt_in_out_3',
    ]

    def __init__(self,
                 signer_id=None,
                 signer=None,
                 principal=None,
                 email_address=APIHelper.SKIP,
                 signing_complete_url=APIHelper.SKIP,
                 signing_decline_url=APIHelper.SKIP,
                 signing_expired_url=APIHelper.SKIP,
                 language=APIHelper.SKIP,
                 opt_in_out_1=APIHelper.SKIP,
                 opt_in_out_2=APIHelper.SKIP,
                 opt_in_out_3=APIHelper.SKIP):
        """Constructor for the Signer class"""

        # Initialize members of the class
        self.signer_id = signer_id 
        self.signer = signer 
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        self.principal = principal 
        if signing_complete_url is not APIHelper.SKIP:
            self.signing_complete_url = signing_complete_url 
        if signing_decline_url is not APIHelper.SKIP:
            self.signing_decline_url = signing_decline_url 
        if signing_expired_url is not APIHelper.SKIP:
            self.signing_expired_url = signing_expired_url 
        if language is not APIHelper.SKIP:
            self.language = language 
        if opt_in_out_1 is not APIHelper.SKIP:
            self.opt_in_out_1 = opt_in_out_1 
        if opt_in_out_2 is not APIHelper.SKIP:
            self.opt_in_out_2 = opt_in_out_2 
        if opt_in_out_3 is not APIHelper.SKIP:
            self.opt_in_out_3 = opt_in_out_3 

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

        signer_id = dictionary.get("signerId") if dictionary.get("signerId") else None
        signer = Name.from_dictionary(dictionary.get('signer')) if dictionary.get('signer') else None
        principal = dictionary.get("principal") if "principal" in dictionary.keys() else None
        email_address = dictionary.get("emailAddress") if dictionary.get("emailAddress") else APIHelper.SKIP
        signing_complete_url = dictionary.get("signingCompleteUrl") if dictionary.get("signingCompleteUrl") else APIHelper.SKIP
        signing_decline_url = dictionary.get("signingDeclineUrl") if dictionary.get("signingDeclineUrl") else APIHelper.SKIP
        signing_expired_url = dictionary.get("signingExpiredUrl") if dictionary.get("signingExpiredUrl") else APIHelper.SKIP
        language = dictionary.get("language") if dictionary.get("language") else APIHelper.SKIP
        opt_in_out_1 = dictionary.get("optInOut1") if "optInOut1" in dictionary.keys() else APIHelper.SKIP
        opt_in_out_2 = dictionary.get("optInOut2") if "optInOut2" in dictionary.keys() else APIHelper.SKIP
        opt_in_out_3 = dictionary.get("optInOut3") if "optInOut3" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(signer_id,
                   signer,
                   principal,
                   email_address,
                   signing_complete_url,
                   signing_decline_url,
                   signing_expired_url,
                   language,
                   opt_in_out_1,
                   opt_in_out_2,
                   opt_in_out_3)