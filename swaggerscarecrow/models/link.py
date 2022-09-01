# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class Link(object):

    """Implementation of the 'Link' model.

    TODO: type model description here.

    Attributes:
        mtype (string): TODO: type description here.
        title (string): TODO: type description here.
        params (dict): TODO: type description here.
        uri_builder (object): TODO: type description here.
        rel (string): TODO: type description here.
        rels (list of string): TODO: type description here.
        uri (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "title": 'title',
        "params": 'params',
        "uri_builder": 'uriBuilder',
        "rel": 'rel',
        "rels": 'rels',
        "uri": 'uri'
    }

    _optionals = [
        'mtype',
        'title',
        'params',
        'uri_builder',
        'rel',
        'rels',
        'uri',
    ]

    def __init__(self,
                 mtype=APIHelper.SKIP,
                 title=APIHelper.SKIP,
                 params=APIHelper.SKIP,
                 uri_builder=APIHelper.SKIP,
                 rel=APIHelper.SKIP,
                 rels=APIHelper.SKIP,
                 uri=APIHelper.SKIP):
        """Constructor for the Link class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if title is not APIHelper.SKIP:
            self.title = title 
        if params is not APIHelper.SKIP:
            self.params = params 
        if uri_builder is not APIHelper.SKIP:
            self.uri_builder = uri_builder 
        if rel is not APIHelper.SKIP:
            self.rel = rel 
        if rels is not APIHelper.SKIP:
            self.rels = rels 
        if uri is not APIHelper.SKIP:
            self.uri = uri 

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
        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        params = dictionary.get("params") if dictionary.get("params") else APIHelper.SKIP
        uri_builder = dictionary.get("uriBuilder") if dictionary.get("uriBuilder") else APIHelper.SKIP
        rel = dictionary.get("rel") if dictionary.get("rel") else APIHelper.SKIP
        rels = dictionary.get("rels") if dictionary.get("rels") else APIHelper.SKIP
        uri = dictionary.get("uri") if dictionary.get("uri") else APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   title,
                   params,
                   uri_builder,
                   rel,
                   rels,
                   uri)