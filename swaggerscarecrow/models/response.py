# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.entity_tag import EntityTag
from swaggerscarecrow.models.link import Link
from swaggerscarecrow.models.locale import Locale
from swaggerscarecrow.models.media_type import MediaType
from swaggerscarecrow.models.new_cookie import NewCookie
from swaggerscarecrow.models.status_type import StatusType


class Response(object):

    """Implementation of the 'Response' model.

    TODO: type model description here.

    Attributes:
        last_modified (datetime): TODO: type description here.
        date (datetime): TODO: type description here.
        length (int): TODO: type description here.
        location (string): TODO: type description here.
        language (Locale): TODO: type description here.
        cookies (dict): TODO: type description here.
        media_type (MediaType): TODO: type description here.
        entity (object): TODO: type description here.
        links (list of Link): TODO: type description here.
        status (int): TODO: type description here.
        entity_tag (EntityTag): TODO: type description here.
        string_headers (dict): TODO: type description here.
        metadata (dict): TODO: type description here.
        status_info (StatusType): TODO: type description here.
        allowed_methods (list of string): TODO: type description here.
        headers (dict): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_modified": 'lastModified',
        "date": 'date',
        "length": 'length',
        "location": 'location',
        "language": 'language',
        "cookies": 'cookies',
        "media_type": 'mediaType',
        "entity": 'entity',
        "links": 'links',
        "status": 'status',
        "entity_tag": 'entityTag',
        "string_headers": 'stringHeaders',
        "metadata": 'metadata',
        "status_info": 'statusInfo',
        "allowed_methods": 'allowedMethods',
        "headers": 'headers'
    }

    _optionals = [
        'last_modified',
        'date',
        'length',
        'location',
        'language',
        'cookies',
        'media_type',
        'entity',
        'links',
        'status',
        'entity_tag',
        'string_headers',
        'metadata',
        'status_info',
        'allowed_methods',
        'headers',
    ]

    def __init__(self,
                 last_modified=APIHelper.SKIP,
                 date=APIHelper.SKIP,
                 length=APIHelper.SKIP,
                 location=APIHelper.SKIP,
                 language=APIHelper.SKIP,
                 cookies=APIHelper.SKIP,
                 media_type=APIHelper.SKIP,
                 entity=APIHelper.SKIP,
                 links=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 entity_tag=APIHelper.SKIP,
                 string_headers=APIHelper.SKIP,
                 metadata=APIHelper.SKIP,
                 status_info=APIHelper.SKIP,
                 allowed_methods=APIHelper.SKIP,
                 headers=APIHelper.SKIP):
        """Constructor for the Response class"""

        # Initialize members of the class
        if last_modified is not APIHelper.SKIP:
            self.last_modified = APIHelper.RFC3339DateTime(last_modified) if last_modified else None 
        if date is not APIHelper.SKIP:
            self.date = APIHelper.RFC3339DateTime(date) if date else None 
        if length is not APIHelper.SKIP:
            self.length = length 
        if location is not APIHelper.SKIP:
            self.location = location 
        if language is not APIHelper.SKIP:
            self.language = language 
        if cookies is not APIHelper.SKIP:
            self.cookies = cookies 
        if media_type is not APIHelper.SKIP:
            self.media_type = media_type 
        if entity is not APIHelper.SKIP:
            self.entity = entity 
        if links is not APIHelper.SKIP:
            self.links = links 
        if status is not APIHelper.SKIP:
            self.status = status 
        if entity_tag is not APIHelper.SKIP:
            self.entity_tag = entity_tag 
        if string_headers is not APIHelper.SKIP:
            self.string_headers = string_headers 
        if metadata is not APIHelper.SKIP:
            self.metadata = metadata 
        if status_info is not APIHelper.SKIP:
            self.status_info = status_info 
        if allowed_methods is not APIHelper.SKIP:
            self.allowed_methods = allowed_methods 
        if headers is not APIHelper.SKIP:
            self.headers = headers 

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

        last_modified = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastModified")).datetime if dictionary.get("lastModified") else APIHelper.SKIP
        date = APIHelper.RFC3339DateTime.from_value(dictionary.get("date")).datetime if dictionary.get("date") else APIHelper.SKIP
        length = dictionary.get("length") if dictionary.get("length") else APIHelper.SKIP
        location = dictionary.get("location") if dictionary.get("location") else APIHelper.SKIP
        language = Locale.from_dictionary(dictionary.get('language')) if 'language' in dictionary.keys() else APIHelper.SKIP 
        cookies = NewCookie.from_dictionary(dictionary.get('cookies')) if 'cookies' in dictionary.keys() else APIHelper.SKIP 
        media_type = MediaType.from_dictionary(dictionary.get('mediaType')) if 'mediaType' in dictionary.keys() else APIHelper.SKIP 
        entity = dictionary.get("entity") if dictionary.get("entity") else APIHelper.SKIP
        links = None
        if dictionary.get('links') is not None:
            links = [Link.from_dictionary(x) for x in dictionary.get('links')]
        else:
            links = APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        entity_tag = EntityTag.from_dictionary(dictionary.get('entityTag')) if 'entityTag' in dictionary.keys() else APIHelper.SKIP 
        string_headers = dictionary.get("stringHeaders") if dictionary.get("stringHeaders") else APIHelper.SKIP
        metadata = dictionary.get("metadata") if dictionary.get("metadata") else APIHelper.SKIP
        status_info = StatusType.from_dictionary(dictionary.get('statusInfo')) if 'statusInfo' in dictionary.keys() else APIHelper.SKIP 
        allowed_methods = dictionary.get("allowedMethods") if dictionary.get("allowedMethods") else APIHelper.SKIP
        headers = dictionary.get("headers") if dictionary.get("headers") else APIHelper.SKIP
        # Return an object of this model
        return cls(last_modified,
                   date,
                   length,
                   location,
                   language,
                   cookies,
                   media_type,
                   entity,
                   links,
                   status,
                   entity_tag,
                   string_headers,
                   metadata,
                   status_info,
                   allowed_methods,
                   headers)
