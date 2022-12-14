# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.servlet_request import *
from swaggerscarecrow.models.servlet_response import ServletResponse


class AsyncContext(object):

    """Implementation of the 'AsyncContext' model.

    TODO: type model description here.

    Attributes:
        request (ServletRequest): TODO: type description here.
        timeout (long|int): TODO: type description here.
        response (ServletResponse): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request": 'request',
        "timeout": 'timeout',
        "response": 'response'
    }

    _optionals = [
        'request',
        'timeout',
        'response',
    ]

    def __init__(self,
                 request=APIHelper.SKIP,
                 timeout=APIHelper.SKIP,
                 response=APIHelper.SKIP):
        """Constructor for the AsyncContext class"""

        # Initialize members of the class
        if request is not APIHelper.SKIP:
            self.request = request 
        if timeout is not APIHelper.SKIP:
            self.timeout = timeout 
        if response is not APIHelper.SKIP:
            self.response = response 

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

        request = ServletRequest.from_dictionary(dictionary.get('request')) if 'request' in dictionary.keys() else APIHelper.SKIP 
        timeout = dictionary.get("timeout") if dictionary.get("timeout") else APIHelper.SKIP
        response = ServletResponse.from_dictionary(dictionary.get('response')) if 'response' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(request,
                   timeout,
                   response)
