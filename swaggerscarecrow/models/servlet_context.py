# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.class_loader import ClassLoader
from swaggerscarecrow.models.filter_registration import FilterRegistration
from swaggerscarecrow.models.jsp_config_descriptor import JspConfigDescriptor
from swaggerscarecrow.models.servlet_registration import ServletRegistration
from swaggerscarecrow.models.session_cookie_config import SessionCookieConfig


class ServletContext(object):

    """Implementation of the 'ServletContext' model.

    TODO: type model description here.

    Attributes:
        major_version (int): TODO: type description here.
        minor_version (int): TODO: type description here.
        class_loader (ClassLoader): TODO: type description here.
        servlet_names (object): TODO: type description here.
        attribute_names (object): TODO: type description here.
        context_path (string): TODO: type description here.
        session_timeout (int): TODO: type description here.
        servlet_context_name (string): TODO: type description here.
        server_info (string): TODO: type description here.
        init_parameter_names (object): TODO: type description here.
        request_character_encoding (string): TODO: type description here.
        response_character_encoding (string): TODO: type description here.
        servlets (object): TODO: type description here.
        session_cookie_config (SessionCookieConfig): TODO: type description
            here.
        servlet_registrations (dict): TODO: type description here.
        filter_registrations (dict): TODO: type description here.
        default_session_tracking_modes (list of
            DefaultSessionTrackingModeEnum): TODO: type description here.
        effective_session_tracking_modes (list of
            EffectiveSessionTrackingModeEnum): TODO: type description here.
        jsp_config_descriptor (JspConfigDescriptor): TODO: type description
            here.
        virtual_server_name (string): TODO: type description here.
        effective_major_version (int): TODO: type description here.
        effective_minor_version (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "major_version": 'majorVersion',
        "minor_version": 'minorVersion',
        "class_loader": 'classLoader',
        "servlet_names": 'servletNames',
        "attribute_names": 'attributeNames',
        "context_path": 'contextPath',
        "session_timeout": 'sessionTimeout',
        "servlet_context_name": 'servletContextName',
        "server_info": 'serverInfo',
        "init_parameter_names": 'initParameterNames',
        "request_character_encoding": 'requestCharacterEncoding',
        "response_character_encoding": 'responseCharacterEncoding',
        "servlets": 'servlets',
        "session_cookie_config": 'sessionCookieConfig',
        "servlet_registrations": 'servletRegistrations',
        "filter_registrations": 'filterRegistrations',
        "default_session_tracking_modes": 'defaultSessionTrackingModes',
        "effective_session_tracking_modes": 'effectiveSessionTrackingModes',
        "jsp_config_descriptor": 'jspConfigDescriptor',
        "virtual_server_name": 'virtualServerName',
        "effective_major_version": 'effectiveMajorVersion',
        "effective_minor_version": 'effectiveMinorVersion'
    }

    _optionals = [
        'major_version',
        'minor_version',
        'class_loader',
        'servlet_names',
        'attribute_names',
        'context_path',
        'session_timeout',
        'servlet_context_name',
        'server_info',
        'init_parameter_names',
        'request_character_encoding',
        'response_character_encoding',
        'servlets',
        'session_cookie_config',
        'servlet_registrations',
        'filter_registrations',
        'default_session_tracking_modes',
        'effective_session_tracking_modes',
        'jsp_config_descriptor',
        'virtual_server_name',
        'effective_major_version',
        'effective_minor_version',
    ]

    def __init__(self,
                 major_version=APIHelper.SKIP,
                 minor_version=APIHelper.SKIP,
                 class_loader=APIHelper.SKIP,
                 servlet_names=APIHelper.SKIP,
                 attribute_names=APIHelper.SKIP,
                 context_path=APIHelper.SKIP,
                 session_timeout=APIHelper.SKIP,
                 servlet_context_name=APIHelper.SKIP,
                 server_info=APIHelper.SKIP,
                 init_parameter_names=APIHelper.SKIP,
                 request_character_encoding=APIHelper.SKIP,
                 response_character_encoding=APIHelper.SKIP,
                 servlets=APIHelper.SKIP,
                 session_cookie_config=APIHelper.SKIP,
                 servlet_registrations=APIHelper.SKIP,
                 filter_registrations=APIHelper.SKIP,
                 default_session_tracking_modes=APIHelper.SKIP,
                 effective_session_tracking_modes=APIHelper.SKIP,
                 jsp_config_descriptor=APIHelper.SKIP,
                 virtual_server_name=APIHelper.SKIP,
                 effective_major_version=APIHelper.SKIP,
                 effective_minor_version=APIHelper.SKIP):
        """Constructor for the ServletContext class"""

        # Initialize members of the class
        if major_version is not APIHelper.SKIP:
            self.major_version = major_version 
        if minor_version is not APIHelper.SKIP:
            self.minor_version = minor_version 
        if class_loader is not APIHelper.SKIP:
            self.class_loader = class_loader 
        if servlet_names is not APIHelper.SKIP:
            self.servlet_names = servlet_names 
        if attribute_names is not APIHelper.SKIP:
            self.attribute_names = attribute_names 
        if context_path is not APIHelper.SKIP:
            self.context_path = context_path 
        if session_timeout is not APIHelper.SKIP:
            self.session_timeout = session_timeout 
        if servlet_context_name is not APIHelper.SKIP:
            self.servlet_context_name = servlet_context_name 
        if server_info is not APIHelper.SKIP:
            self.server_info = server_info 
        if init_parameter_names is not APIHelper.SKIP:
            self.init_parameter_names = init_parameter_names 
        if request_character_encoding is not APIHelper.SKIP:
            self.request_character_encoding = request_character_encoding 
        if response_character_encoding is not APIHelper.SKIP:
            self.response_character_encoding = response_character_encoding 
        if servlets is not APIHelper.SKIP:
            self.servlets = servlets 
        if session_cookie_config is not APIHelper.SKIP:
            self.session_cookie_config = session_cookie_config 
        if servlet_registrations is not APIHelper.SKIP:
            self.servlet_registrations = servlet_registrations 
        if filter_registrations is not APIHelper.SKIP:
            self.filter_registrations = filter_registrations 
        if default_session_tracking_modes is not APIHelper.SKIP:
            self.default_session_tracking_modes = default_session_tracking_modes 
        if effective_session_tracking_modes is not APIHelper.SKIP:
            self.effective_session_tracking_modes = effective_session_tracking_modes 
        if jsp_config_descriptor is not APIHelper.SKIP:
            self.jsp_config_descriptor = jsp_config_descriptor 
        if virtual_server_name is not APIHelper.SKIP:
            self.virtual_server_name = virtual_server_name 
        if effective_major_version is not APIHelper.SKIP:
            self.effective_major_version = effective_major_version 
        if effective_minor_version is not APIHelper.SKIP:
            self.effective_minor_version = effective_minor_version 

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

        major_version = dictionary.get("majorVersion") if dictionary.get("majorVersion") else APIHelper.SKIP
        minor_version = dictionary.get("minorVersion") if dictionary.get("minorVersion") else APIHelper.SKIP
        class_loader = ClassLoader.from_dictionary(dictionary.get('classLoader')) if 'classLoader' in dictionary.keys() else APIHelper.SKIP 
        servlet_names = dictionary.get("servletNames") if dictionary.get("servletNames") else APIHelper.SKIP
        attribute_names = dictionary.get("attributeNames") if dictionary.get("attributeNames") else APIHelper.SKIP
        context_path = dictionary.get("contextPath") if dictionary.get("contextPath") else APIHelper.SKIP
        session_timeout = dictionary.get("sessionTimeout") if dictionary.get("sessionTimeout") else APIHelper.SKIP
        servlet_context_name = dictionary.get("servletContextName") if dictionary.get("servletContextName") else APIHelper.SKIP
        server_info = dictionary.get("serverInfo") if dictionary.get("serverInfo") else APIHelper.SKIP
        init_parameter_names = dictionary.get("initParameterNames") if dictionary.get("initParameterNames") else APIHelper.SKIP
        request_character_encoding = dictionary.get("requestCharacterEncoding") if dictionary.get("requestCharacterEncoding") else APIHelper.SKIP
        response_character_encoding = dictionary.get("responseCharacterEncoding") if dictionary.get("responseCharacterEncoding") else APIHelper.SKIP
        servlets = dictionary.get("servlets") if dictionary.get("servlets") else APIHelper.SKIP
        session_cookie_config = SessionCookieConfig.from_dictionary(dictionary.get('sessionCookieConfig')) if 'sessionCookieConfig' in dictionary.keys() else APIHelper.SKIP 
        servlet_registrations = ServletRegistration.from_dictionary(dictionary.get('servletRegistrations')) if 'servletRegistrations' in dictionary.keys() else APIHelper.SKIP 
        filter_registrations = FilterRegistration.from_dictionary(dictionary.get('filterRegistrations')) if 'filterRegistrations' in dictionary.keys() else APIHelper.SKIP 
        default_session_tracking_modes = dictionary.get("defaultSessionTrackingModes") if dictionary.get("defaultSessionTrackingModes") else APIHelper.SKIP
        effective_session_tracking_modes = dictionary.get("effectiveSessionTrackingModes") if dictionary.get("effectiveSessionTrackingModes") else APIHelper.SKIP
        jsp_config_descriptor = JspConfigDescriptor.from_dictionary(dictionary.get('jspConfigDescriptor')) if 'jspConfigDescriptor' in dictionary.keys() else APIHelper.SKIP 
        virtual_server_name = dictionary.get("virtualServerName") if dictionary.get("virtualServerName") else APIHelper.SKIP
        effective_major_version = dictionary.get("effectiveMajorVersion") if dictionary.get("effectiveMajorVersion") else APIHelper.SKIP
        effective_minor_version = dictionary.get("effectiveMinorVersion") if dictionary.get("effectiveMinorVersion") else APIHelper.SKIP
        # Return an object of this model
        return cls(major_version,
                   minor_version,
                   class_loader,
                   servlet_names,
                   attribute_names,
                   context_path,
                   session_timeout,
                   servlet_context_name,
                   server_info,
                   init_parameter_names,
                   request_character_encoding,
                   response_character_encoding,
                   servlets,
                   session_cookie_config,
                   servlet_registrations,
                   filter_registrations,
                   default_session_tracking_modes,
                   effective_session_tracking_modes,
                   jsp_config_descriptor,
                   virtual_server_name,
                   effective_major_version,
                   effective_minor_version)
