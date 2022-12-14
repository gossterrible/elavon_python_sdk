# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.jsp_property_group_descriptor import JspPropertyGroupDescriptor
from swaggerscarecrow.models.taglib_descriptor import TaglibDescriptor


class JspConfigDescriptor(object):

    """Implementation of the 'JspConfigDescriptor' model.

    TODO: type model description here.

    Attributes:
        taglibs (list of TaglibDescriptor): TODO: type description here.
        jsp_property_groups (list of JspPropertyGroupDescriptor): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "taglibs": 'taglibs',
        "jsp_property_groups": 'jspPropertyGroups'
    }

    _optionals = [
        'taglibs',
        'jsp_property_groups',
    ]

    def __init__(self,
                 taglibs=APIHelper.SKIP,
                 jsp_property_groups=APIHelper.SKIP):
        """Constructor for the JspConfigDescriptor class"""

        # Initialize members of the class
        if taglibs is not APIHelper.SKIP:
            self.taglibs = taglibs 
        if jsp_property_groups is not APIHelper.SKIP:
            self.jsp_property_groups = jsp_property_groups 

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

        taglibs = None
        if dictionary.get('taglibs') is not None:
            taglibs = [TaglibDescriptor.from_dictionary(x) for x in dictionary.get('taglibs')]
        else:
            taglibs = APIHelper.SKIP
        jsp_property_groups = None
        if dictionary.get('jspPropertyGroups') is not None:
            jsp_property_groups = [JspPropertyGroupDescriptor.from_dictionary(x) for x in dictionary.get('jspPropertyGroups')]
        else:
            jsp_property_groups = APIHelper.SKIP
        # Return an object of this model
        return cls(taglibs,
                   jsp_property_groups)
