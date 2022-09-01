# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.company_info_bundle import CompanyInfoBundle
from swaggerscarecrow.models.timings import Timings


class BusinessDetailQueryResponse(object):

    """Implementation of the 'BusinessDetailQueryResponse' model.

    TODO: type model description here.

    Attributes:
        response_id (int): TODO: type description here.
        company_info_bundle (CompanyInfoBundle): TODO: type description here.
        error (string): TODO: type description here.
        status_code (string): TODO: type description here.
        timings (Timings): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "response_id": 'responseId',
        "company_info_bundle": 'companyInfoBundle',
        "error": 'error',
        "status_code": 'statusCode',
        "timings": 'timings'
    }

    _optionals = [
        'response_id',
        'company_info_bundle',
        'error',
        'status_code',
        'timings',
    ]

    def __init__(self,
                 response_id=APIHelper.SKIP,
                 company_info_bundle=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 status_code=APIHelper.SKIP,
                 timings=APIHelper.SKIP):
        """Constructor for the BusinessDetailQueryResponse class"""

        # Initialize members of the class
        if response_id is not APIHelper.SKIP:
            self.response_id = response_id 
        if company_info_bundle is not APIHelper.SKIP:
            self.company_info_bundle = company_info_bundle 
        if error is not APIHelper.SKIP:
            self.error = error 
        if status_code is not APIHelper.SKIP:
            self.status_code = status_code 
        if timings is not APIHelper.SKIP:
            self.timings = timings 

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

        response_id = dictionary.get("responseId") if dictionary.get("responseId") else APIHelper.SKIP
        company_info_bundle = CompanyInfoBundle.from_dictionary(dictionary.get('companyInfoBundle')) if 'companyInfoBundle' in dictionary.keys() else APIHelper.SKIP 
        error = dictionary.get("error") if dictionary.get("error") else APIHelper.SKIP
        status_code = dictionary.get("statusCode") if dictionary.get("statusCode") else APIHelper.SKIP
        timings = Timings.from_dictionary(dictionary.get('timings')) if 'timings' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(response_id,
                   company_info_bundle,
                   error,
                   status_code,
                   timings)