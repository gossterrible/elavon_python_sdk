# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class Package(object):

    """Implementation of the 'Package' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        specification_title (string): TODO: type description here.
        specification_version (string): TODO: type description here.
        specification_vendor (string): TODO: type description here.
        implementation_title (string): TODO: type description here.
        implementation_version (string): TODO: type description here.
        implementation_vendor (string): TODO: type description here.
        annotations (list of object): TODO: type description here.
        declared_annotations (list of object): TODO: type description here.
        sealed (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "specification_title": 'specificationTitle',
        "specification_version": 'specificationVersion',
        "specification_vendor": 'specificationVendor',
        "implementation_title": 'implementationTitle',
        "implementation_version": 'implementationVersion',
        "implementation_vendor": 'implementationVendor',
        "annotations": 'annotations',
        "declared_annotations": 'declaredAnnotations',
        "sealed": 'sealed'
    }

    _optionals = [
        'name',
        'specification_title',
        'specification_version',
        'specification_vendor',
        'implementation_title',
        'implementation_version',
        'implementation_vendor',
        'annotations',
        'declared_annotations',
        'sealed',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 specification_title=APIHelper.SKIP,
                 specification_version=APIHelper.SKIP,
                 specification_vendor=APIHelper.SKIP,
                 implementation_title=APIHelper.SKIP,
                 implementation_version=APIHelper.SKIP,
                 implementation_vendor=APIHelper.SKIP,
                 annotations=APIHelper.SKIP,
                 declared_annotations=APIHelper.SKIP,
                 sealed=APIHelper.SKIP):
        """Constructor for the Package class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if specification_title is not APIHelper.SKIP:
            self.specification_title = specification_title 
        if specification_version is not APIHelper.SKIP:
            self.specification_version = specification_version 
        if specification_vendor is not APIHelper.SKIP:
            self.specification_vendor = specification_vendor 
        if implementation_title is not APIHelper.SKIP:
            self.implementation_title = implementation_title 
        if implementation_version is not APIHelper.SKIP:
            self.implementation_version = implementation_version 
        if implementation_vendor is not APIHelper.SKIP:
            self.implementation_vendor = implementation_vendor 
        if annotations is not APIHelper.SKIP:
            self.annotations = annotations 
        if declared_annotations is not APIHelper.SKIP:
            self.declared_annotations = declared_annotations 
        if sealed is not APIHelper.SKIP:
            self.sealed = sealed 

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
        specification_title = dictionary.get("specificationTitle") if dictionary.get("specificationTitle") else APIHelper.SKIP
        specification_version = dictionary.get("specificationVersion") if dictionary.get("specificationVersion") else APIHelper.SKIP
        specification_vendor = dictionary.get("specificationVendor") if dictionary.get("specificationVendor") else APIHelper.SKIP
        implementation_title = dictionary.get("implementationTitle") if dictionary.get("implementationTitle") else APIHelper.SKIP
        implementation_version = dictionary.get("implementationVersion") if dictionary.get("implementationVersion") else APIHelper.SKIP
        implementation_vendor = dictionary.get("implementationVendor") if dictionary.get("implementationVendor") else APIHelper.SKIP
        annotations = dictionary.get("annotations") if dictionary.get("annotations") else APIHelper.SKIP
        declared_annotations = dictionary.get("declaredAnnotations") if dictionary.get("declaredAnnotations") else APIHelper.SKIP
        sealed = dictionary.get("sealed") if "sealed" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   specification_title,
                   specification_version,
                   specification_vendor,
                   implementation_title,
                   implementation_version,
                   implementation_vendor,
                   annotations,
                   declared_annotations,
                   sealed)