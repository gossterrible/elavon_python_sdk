# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class JspPropertyGroupDescriptor(object):

    """Implementation of the 'JspPropertyGroupDescriptor' model.

    TODO: type model description here.

    Attributes:
        buffer (string): TODO: type description here.
        url_patterns (list of string): TODO: type description here.
        el_ignored (string): TODO: type description here.
        page_encoding (string): TODO: type description here.
        scripting_invalid (string): TODO: type description here.
        is_xml (string): TODO: type description here.
        include_preludes (list of string): TODO: type description here.
        include_codas (list of string): TODO: type description here.
        deferred_syntax_allowed_as_literal (string): TODO: type description
            here.
        trim_directive_whitespaces (string): TODO: type description here.
        default_content_type (string): TODO: type description here.
        error_on_undeclared_namespace (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "buffer": 'buffer',
        "url_patterns": 'urlPatterns',
        "el_ignored": 'elIgnored',
        "page_encoding": 'pageEncoding',
        "scripting_invalid": 'scriptingInvalid',
        "is_xml": 'isXml',
        "include_preludes": 'includePreludes',
        "include_codas": 'includeCodas',
        "deferred_syntax_allowed_as_literal": 'deferredSyntaxAllowedAsLiteral',
        "trim_directive_whitespaces": 'trimDirectiveWhitespaces',
        "default_content_type": 'defaultContentType',
        "error_on_undeclared_namespace": 'errorOnUndeclaredNamespace'
    }

    _optionals = [
        'buffer',
        'url_patterns',
        'el_ignored',
        'page_encoding',
        'scripting_invalid',
        'is_xml',
        'include_preludes',
        'include_codas',
        'deferred_syntax_allowed_as_literal',
        'trim_directive_whitespaces',
        'default_content_type',
        'error_on_undeclared_namespace',
    ]

    def __init__(self,
                 buffer=APIHelper.SKIP,
                 url_patterns=APIHelper.SKIP,
                 el_ignored=APIHelper.SKIP,
                 page_encoding=APIHelper.SKIP,
                 scripting_invalid=APIHelper.SKIP,
                 is_xml=APIHelper.SKIP,
                 include_preludes=APIHelper.SKIP,
                 include_codas=APIHelper.SKIP,
                 deferred_syntax_allowed_as_literal=APIHelper.SKIP,
                 trim_directive_whitespaces=APIHelper.SKIP,
                 default_content_type=APIHelper.SKIP,
                 error_on_undeclared_namespace=APIHelper.SKIP):
        """Constructor for the JspPropertyGroupDescriptor class"""

        # Initialize members of the class
        if buffer is not APIHelper.SKIP:
            self.buffer = buffer 
        if url_patterns is not APIHelper.SKIP:
            self.url_patterns = url_patterns 
        if el_ignored is not APIHelper.SKIP:
            self.el_ignored = el_ignored 
        if page_encoding is not APIHelper.SKIP:
            self.page_encoding = page_encoding 
        if scripting_invalid is not APIHelper.SKIP:
            self.scripting_invalid = scripting_invalid 
        if is_xml is not APIHelper.SKIP:
            self.is_xml = is_xml 
        if include_preludes is not APIHelper.SKIP:
            self.include_preludes = include_preludes 
        if include_codas is not APIHelper.SKIP:
            self.include_codas = include_codas 
        if deferred_syntax_allowed_as_literal is not APIHelper.SKIP:
            self.deferred_syntax_allowed_as_literal = deferred_syntax_allowed_as_literal 
        if trim_directive_whitespaces is not APIHelper.SKIP:
            self.trim_directive_whitespaces = trim_directive_whitespaces 
        if default_content_type is not APIHelper.SKIP:
            self.default_content_type = default_content_type 
        if error_on_undeclared_namespace is not APIHelper.SKIP:
            self.error_on_undeclared_namespace = error_on_undeclared_namespace 

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

        buffer = dictionary.get("buffer") if dictionary.get("buffer") else APIHelper.SKIP
        url_patterns = dictionary.get("urlPatterns") if dictionary.get("urlPatterns") else APIHelper.SKIP
        el_ignored = dictionary.get("elIgnored") if dictionary.get("elIgnored") else APIHelper.SKIP
        page_encoding = dictionary.get("pageEncoding") if dictionary.get("pageEncoding") else APIHelper.SKIP
        scripting_invalid = dictionary.get("scriptingInvalid") if dictionary.get("scriptingInvalid") else APIHelper.SKIP
        is_xml = dictionary.get("isXml") if dictionary.get("isXml") else APIHelper.SKIP
        include_preludes = dictionary.get("includePreludes") if dictionary.get("includePreludes") else APIHelper.SKIP
        include_codas = dictionary.get("includeCodas") if dictionary.get("includeCodas") else APIHelper.SKIP
        deferred_syntax_allowed_as_literal = dictionary.get("deferredSyntaxAllowedAsLiteral") if dictionary.get("deferredSyntaxAllowedAsLiteral") else APIHelper.SKIP
        trim_directive_whitespaces = dictionary.get("trimDirectiveWhitespaces") if dictionary.get("trimDirectiveWhitespaces") else APIHelper.SKIP
        default_content_type = dictionary.get("defaultContentType") if dictionary.get("defaultContentType") else APIHelper.SKIP
        error_on_undeclared_namespace = dictionary.get("errorOnUndeclaredNamespace") if dictionary.get("errorOnUndeclaredNamespace") else APIHelper.SKIP
        # Return an object of this model
        return cls(buffer,
                   url_patterns,
                   el_ignored,
                   page_encoding,
                   scripting_invalid,
                   is_xml,
                   include_preludes,
                   include_codas,
                   deferred_syntax_allowed_as_literal,
                   trim_directive_whitespaces,
                   default_content_type,
                   error_on_undeclared_namespace)
