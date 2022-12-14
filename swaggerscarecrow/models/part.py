# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class Part(object):

    """Implementation of the 'Part' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        size (long|int): TODO: type description here.
        input_stream (object): TODO: type description here.
        header_names (list of string): TODO: type description here.
        submitted_file_name (string): TODO: type description here.
        content_type (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "size": 'size',
        "input_stream": 'inputStream',
        "header_names": 'headerNames',
        "submitted_file_name": 'submittedFileName',
        "content_type": 'contentType'
    }

    _optionals = [
        'name',
        'size',
        'input_stream',
        'header_names',
        'submitted_file_name',
        'content_type',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 size=APIHelper.SKIP,
                 input_stream=APIHelper.SKIP,
                 header_names=APIHelper.SKIP,
                 submitted_file_name=APIHelper.SKIP,
                 content_type=APIHelper.SKIP):
        """Constructor for the Part class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if size is not APIHelper.SKIP:
            self.size = size 
        if input_stream is not APIHelper.SKIP:
            self.input_stream = input_stream 
        if header_names is not APIHelper.SKIP:
            self.header_names = header_names 
        if submitted_file_name is not APIHelper.SKIP:
            self.submitted_file_name = submitted_file_name 
        if content_type is not APIHelper.SKIP:
            self.content_type = content_type 

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

        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        size = dictionary.get("size") if dictionary.get("size") else APIHelper.SKIP
        input_stream = dictionary.get("inputStream") if dictionary.get("inputStream") else APIHelper.SKIP
        header_names = dictionary.get("headerNames") if dictionary.get("headerNames") else APIHelper.SKIP
        submitted_file_name = dictionary.get("submittedFileName") if dictionary.get("submittedFileName") else APIHelper.SKIP
        content_type = dictionary.get("contentType") if dictionary.get("contentType") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   size,
                   input_stream,
                   header_names,
                   submitted_file_name,
                   content_type)
