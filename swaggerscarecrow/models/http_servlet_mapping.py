# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class HttpServletMapping(object):

    """Implementation of the 'HttpServletMapping' model.

    TODO: type model description here.

    Attributes:
        pattern (string): TODO: type description here.
        servlet_name (string): TODO: type description here.
        match_value (string): TODO: type description here.
        mapping_match (MappingMatchEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pattern": 'pattern',
        "servlet_name": 'servletName',
        "match_value": 'matchValue',
        "mapping_match": 'mappingMatch'
    }

    _optionals = [
        'pattern',
        'servlet_name',
        'match_value',
        'mapping_match',
    ]

    def __init__(self,
                 pattern=APIHelper.SKIP,
                 servlet_name=APIHelper.SKIP,
                 match_value=APIHelper.SKIP,
                 mapping_match=APIHelper.SKIP):
        """Constructor for the HttpServletMapping class"""

        # Initialize members of the class
        if pattern is not APIHelper.SKIP:
            self.pattern = pattern 
        if servlet_name is not APIHelper.SKIP:
            self.servlet_name = servlet_name 
        if match_value is not APIHelper.SKIP:
            self.match_value = match_value 
        if mapping_match is not APIHelper.SKIP:
            self.mapping_match = mapping_match 

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

        pattern = dictionary.get("pattern") if dictionary.get("pattern") else APIHelper.SKIP
        servlet_name = dictionary.get("servletName") if dictionary.get("servletName") else APIHelper.SKIP
        match_value = dictionary.get("matchValue") if dictionary.get("matchValue") else APIHelper.SKIP
        mapping_match = dictionary.get("mappingMatch") if dictionary.get("mappingMatch") else APIHelper.SKIP
        # Return an object of this model
        return cls(pattern,
                   servlet_name,
                   match_value,
                   mapping_match)
