# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.async_context import AsyncContext
from swaggerscarecrow.models.cookie import Cookie
from swaggerscarecrow.models.http_servlet_mapping import HttpServletMapping
from swaggerscarecrow.models.http_session import HttpSession
from swaggerscarecrow.models.locale import Locale
from swaggerscarecrow.models.part import Part
from swaggerscarecrow.models.principal import Principal
from swaggerscarecrow.models.servlet_context import ServletContext
from swaggerscarecrow.models.servlet_input_stream import ServletInputStream


class HttpServletRequest(object):

    """Implementation of the 'HttpServletRequest' model.

    TODO: type model description here.

    Attributes:
        method (string): TODO: type description here.
        session (HttpSession): TODO: type description here.
        cookies (list of Cookie): TODO: type description here.
        request_uri (string): TODO: type description here.
        user_principal (Principal): TODO: type description here.
        context_path (string): TODO: type description here.
        path_info (string): TODO: type description here.
        query_string (string): TODO: type description here.
        remote_user (string): TODO: type description here.
        servlet_path (string): TODO: type description here.
        header_names (object): TODO: type description here.
        requested_session_id (string): TODO: type description here.
        http_servlet_mapping (HttpServletMapping): TODO: type description
            here.
        trailer_fields_ready (bool): TODO: type description here.
        auth_type (string): TODO: type description here.
        path_translated (string): TODO: type description here.
        requested_session_id_valid (bool): TODO: type description here.
        requested_session_id_from_cookie (bool): TODO: type description here.
        requested_session_id_from_url (bool): TODO: type description here.
        parts (list of Part): TODO: type description here.
        request_url (object): TODO: type description here.
        trailer_fields (dict): TODO: type description here.
        content_length (int): TODO: type description here.
        locale (Locale): TODO: type description here.
        protocol (string): TODO: type description here.
        scheme (string): TODO: type description here.
        input_stream (ServletInputStream): TODO: type description here.
        local_name (string): TODO: type description here.
        parameter_names (object): TODO: type description here.
        server_name (string): TODO: type description here.
        attribute_names (object): TODO: type description here.
        parameter_map (dict): TODO: type description here.
        local_addr (string): TODO: type description here.
        remote_port (int): TODO: type description here.
        secure (bool): TODO: type description here.
        local_port (int): TODO: type description here.
        remote_addr (string): TODO: type description here.
        remote_host (string): TODO: type description here.
        reader (object): TODO: type description here.
        server_port (int): TODO: type description here.
        locales (object): TODO: type description here.
        character_encoding (string): TODO: type description here.
        servlet_context (ServletContext): TODO: type description here.
        async_started (bool): TODO: type description here.
        async_supported (bool): TODO: type description here.
        async_context (AsyncContext): TODO: type description here.
        dispatcher_type (DispatcherTypeEnum): TODO: type description here.
        content_length_long (long|int): TODO: type description here.
        content_type (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "method": 'method',
        "session": 'session',
        "cookies": 'cookies',
        "request_uri": 'requestURI',
        "user_principal": 'userPrincipal',
        "context_path": 'contextPath',
        "path_info": 'pathInfo',
        "query_string": 'queryString',
        "remote_user": 'remoteUser',
        "servlet_path": 'servletPath',
        "header_names": 'headerNames',
        "requested_session_id": 'requestedSessionId',
        "http_servlet_mapping": 'httpServletMapping',
        "trailer_fields_ready": 'trailerFieldsReady',
        "auth_type": 'authType',
        "path_translated": 'pathTranslated',
        "requested_session_id_valid": 'requestedSessionIdValid',
        "requested_session_id_from_cookie": 'requestedSessionIdFromCookie',
        "requested_session_id_from_url": 'requestedSessionIdFromURL',
        "parts": 'parts',
        "request_url": 'requestURL',
        "trailer_fields": 'trailerFields',
        "content_length": 'contentLength',
        "locale": 'locale',
        "protocol": 'protocol',
        "scheme": 'scheme',
        "input_stream": 'inputStream',
        "local_name": 'localName',
        "parameter_names": 'parameterNames',
        "server_name": 'serverName',
        "attribute_names": 'attributeNames',
        "parameter_map": 'parameterMap',
        "local_addr": 'localAddr',
        "remote_port": 'remotePort',
        "secure": 'secure',
        "local_port": 'localPort',
        "remote_addr": 'remoteAddr',
        "remote_host": 'remoteHost',
        "reader": 'reader',
        "server_port": 'serverPort',
        "locales": 'locales',
        "character_encoding": 'characterEncoding',
        "servlet_context": 'servletContext',
        "async_started": 'asyncStarted',
        "async_supported": 'asyncSupported',
        "async_context": 'asyncContext',
        "dispatcher_type": 'dispatcherType',
        "content_length_long": 'contentLengthLong',
        "content_type": 'contentType'
    }

    _optionals = [
        'method',
        'session',
        'cookies',
        'request_uri',
        'user_principal',
        'context_path',
        'path_info',
        'query_string',
        'remote_user',
        'servlet_path',
        'header_names',
        'requested_session_id',
        'http_servlet_mapping',
        'trailer_fields_ready',
        'auth_type',
        'path_translated',
        'requested_session_id_valid',
        'requested_session_id_from_cookie',
        'requested_session_id_from_url',
        'parts',
        'request_url',
        'trailer_fields',
        'content_length',
        'locale',
        'protocol',
        'scheme',
        'input_stream',
        'local_name',
        'parameter_names',
        'server_name',
        'attribute_names',
        'parameter_map',
        'local_addr',
        'remote_port',
        'secure',
        'local_port',
        'remote_addr',
        'remote_host',
        'reader',
        'server_port',
        'locales',
        'character_encoding',
        'servlet_context',
        'async_started',
        'async_supported',
        'async_context',
        'dispatcher_type',
        'content_length_long',
        'content_type',
    ]

    def __init__(self,
                 method=APIHelper.SKIP,
                 session=APIHelper.SKIP,
                 cookies=APIHelper.SKIP,
                 request_uri=APIHelper.SKIP,
                 user_principal=APIHelper.SKIP,
                 context_path=APIHelper.SKIP,
                 path_info=APIHelper.SKIP,
                 query_string=APIHelper.SKIP,
                 remote_user=APIHelper.SKIP,
                 servlet_path=APIHelper.SKIP,
                 header_names=APIHelper.SKIP,
                 requested_session_id=APIHelper.SKIP,
                 http_servlet_mapping=APIHelper.SKIP,
                 trailer_fields_ready=APIHelper.SKIP,
                 auth_type=APIHelper.SKIP,
                 path_translated=APIHelper.SKIP,
                 requested_session_id_valid=APIHelper.SKIP,
                 requested_session_id_from_cookie=APIHelper.SKIP,
                 requested_session_id_from_url=APIHelper.SKIP,
                 parts=APIHelper.SKIP,
                 request_url=APIHelper.SKIP,
                 trailer_fields=APIHelper.SKIP,
                 content_length=APIHelper.SKIP,
                 locale=APIHelper.SKIP,
                 protocol=APIHelper.SKIP,
                 scheme=APIHelper.SKIP,
                 input_stream=APIHelper.SKIP,
                 local_name=APIHelper.SKIP,
                 parameter_names=APIHelper.SKIP,
                 server_name=APIHelper.SKIP,
                 attribute_names=APIHelper.SKIP,
                 parameter_map=APIHelper.SKIP,
                 local_addr=APIHelper.SKIP,
                 remote_port=APIHelper.SKIP,
                 secure=APIHelper.SKIP,
                 local_port=APIHelper.SKIP,
                 remote_addr=APIHelper.SKIP,
                 remote_host=APIHelper.SKIP,
                 reader=APIHelper.SKIP,
                 server_port=APIHelper.SKIP,
                 locales=APIHelper.SKIP,
                 character_encoding=APIHelper.SKIP,
                 servlet_context=APIHelper.SKIP,
                 async_started=APIHelper.SKIP,
                 async_supported=APIHelper.SKIP,
                 async_context=APIHelper.SKIP,
                 dispatcher_type=APIHelper.SKIP,
                 content_length_long=APIHelper.SKIP,
                 content_type=APIHelper.SKIP):
        """Constructor for the HttpServletRequest class"""

        # Initialize members of the class
        if method is not APIHelper.SKIP:
            self.method = method 
        if session is not APIHelper.SKIP:
            self.session = session 
        if cookies is not APIHelper.SKIP:
            self.cookies = cookies 
        if request_uri is not APIHelper.SKIP:
            self.request_uri = request_uri 
        if user_principal is not APIHelper.SKIP:
            self.user_principal = user_principal 
        if context_path is not APIHelper.SKIP:
            self.context_path = context_path 
        if path_info is not APIHelper.SKIP:
            self.path_info = path_info 
        if query_string is not APIHelper.SKIP:
            self.query_string = query_string 
        if remote_user is not APIHelper.SKIP:
            self.remote_user = remote_user 
        if servlet_path is not APIHelper.SKIP:
            self.servlet_path = servlet_path 
        if header_names is not APIHelper.SKIP:
            self.header_names = header_names 
        if requested_session_id is not APIHelper.SKIP:
            self.requested_session_id = requested_session_id 
        if http_servlet_mapping is not APIHelper.SKIP:
            self.http_servlet_mapping = http_servlet_mapping 
        if trailer_fields_ready is not APIHelper.SKIP:
            self.trailer_fields_ready = trailer_fields_ready 
        if auth_type is not APIHelper.SKIP:
            self.auth_type = auth_type 
        if path_translated is not APIHelper.SKIP:
            self.path_translated = path_translated 
        if requested_session_id_valid is not APIHelper.SKIP:
            self.requested_session_id_valid = requested_session_id_valid 
        if requested_session_id_from_cookie is not APIHelper.SKIP:
            self.requested_session_id_from_cookie = requested_session_id_from_cookie 
        if requested_session_id_from_url is not APIHelper.SKIP:
            self.requested_session_id_from_url = requested_session_id_from_url 
        if parts is not APIHelper.SKIP:
            self.parts = parts 
        if request_url is not APIHelper.SKIP:
            self.request_url = request_url 
        if trailer_fields is not APIHelper.SKIP:
            self.trailer_fields = trailer_fields 
        if content_length is not APIHelper.SKIP:
            self.content_length = content_length 
        if locale is not APIHelper.SKIP:
            self.locale = locale 
        if protocol is not APIHelper.SKIP:
            self.protocol = protocol 
        if scheme is not APIHelper.SKIP:
            self.scheme = scheme 
        if input_stream is not APIHelper.SKIP:
            self.input_stream = input_stream 
        if local_name is not APIHelper.SKIP:
            self.local_name = local_name 
        if parameter_names is not APIHelper.SKIP:
            self.parameter_names = parameter_names 
        if server_name is not APIHelper.SKIP:
            self.server_name = server_name 
        if attribute_names is not APIHelper.SKIP:
            self.attribute_names = attribute_names 
        if parameter_map is not APIHelper.SKIP:
            self.parameter_map = parameter_map 
        if local_addr is not APIHelper.SKIP:
            self.local_addr = local_addr 
        if remote_port is not APIHelper.SKIP:
            self.remote_port = remote_port 
        if secure is not APIHelper.SKIP:
            self.secure = secure 
        if local_port is not APIHelper.SKIP:
            self.local_port = local_port 
        if remote_addr is not APIHelper.SKIP:
            self.remote_addr = remote_addr 
        if remote_host is not APIHelper.SKIP:
            self.remote_host = remote_host 
        if reader is not APIHelper.SKIP:
            self.reader = reader 
        if server_port is not APIHelper.SKIP:
            self.server_port = server_port 
        if locales is not APIHelper.SKIP:
            self.locales = locales 
        if character_encoding is not APIHelper.SKIP:
            self.character_encoding = character_encoding 
        if servlet_context is not APIHelper.SKIP:
            self.servlet_context = servlet_context 
        if async_started is not APIHelper.SKIP:
            self.async_started = async_started 
        if async_supported is not APIHelper.SKIP:
            self.async_supported = async_supported 
        if async_context is not APIHelper.SKIP:
            self.async_context = async_context 
        if dispatcher_type is not APIHelper.SKIP:
            self.dispatcher_type = dispatcher_type 
        if content_length_long is not APIHelper.SKIP:
            self.content_length_long = content_length_long 
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

        method = dictionary.get("method") if dictionary.get("method") else APIHelper.SKIP
        session = HttpSession.from_dictionary(dictionary.get('session')) if 'session' in dictionary.keys() else APIHelper.SKIP 
        cookies = None
        if dictionary.get('cookies') is not None:
            cookies = [Cookie.from_dictionary(x) for x in dictionary.get('cookies')]
        else:
            cookies = APIHelper.SKIP
        request_uri = dictionary.get("requestURI") if dictionary.get("requestURI") else APIHelper.SKIP
        user_principal = Principal.from_dictionary(dictionary.get('userPrincipal')) if 'userPrincipal' in dictionary.keys() else APIHelper.SKIP 
        context_path = dictionary.get("contextPath") if dictionary.get("contextPath") else APIHelper.SKIP
        path_info = dictionary.get("pathInfo") if dictionary.get("pathInfo") else APIHelper.SKIP
        query_string = dictionary.get("queryString") if dictionary.get("queryString") else APIHelper.SKIP
        remote_user = dictionary.get("remoteUser") if dictionary.get("remoteUser") else APIHelper.SKIP
        servlet_path = dictionary.get("servletPath") if dictionary.get("servletPath") else APIHelper.SKIP
        header_names = dictionary.get("headerNames") if dictionary.get("headerNames") else APIHelper.SKIP
        requested_session_id = dictionary.get("requestedSessionId") if dictionary.get("requestedSessionId") else APIHelper.SKIP
        http_servlet_mapping = HttpServletMapping.from_dictionary(dictionary.get('httpServletMapping')) if 'httpServletMapping' in dictionary.keys() else APIHelper.SKIP 
        trailer_fields_ready = dictionary.get("trailerFieldsReady") if "trailerFieldsReady" in dictionary.keys() else APIHelper.SKIP
        auth_type = dictionary.get("authType") if dictionary.get("authType") else APIHelper.SKIP
        path_translated = dictionary.get("pathTranslated") if dictionary.get("pathTranslated") else APIHelper.SKIP
        requested_session_id_valid = dictionary.get("requestedSessionIdValid") if "requestedSessionIdValid" in dictionary.keys() else APIHelper.SKIP
        requested_session_id_from_cookie = dictionary.get("requestedSessionIdFromCookie") if "requestedSessionIdFromCookie" in dictionary.keys() else APIHelper.SKIP
        requested_session_id_from_url = dictionary.get("requestedSessionIdFromURL") if "requestedSessionIdFromURL" in dictionary.keys() else APIHelper.SKIP
        parts = None
        if dictionary.get('parts') is not None:
            parts = [Part.from_dictionary(x) for x in dictionary.get('parts')]
        else:
            parts = APIHelper.SKIP
        request_url = dictionary.get("requestURL") if dictionary.get("requestURL") else APIHelper.SKIP
        trailer_fields = dictionary.get("trailerFields") if dictionary.get("trailerFields") else APIHelper.SKIP
        content_length = dictionary.get("contentLength") if dictionary.get("contentLength") else APIHelper.SKIP
        locale = Locale.from_dictionary(dictionary.get('locale')) if 'locale' in dictionary.keys() else APIHelper.SKIP 
        protocol = dictionary.get("protocol") if dictionary.get("protocol") else APIHelper.SKIP
        scheme = dictionary.get("scheme") if dictionary.get("scheme") else APIHelper.SKIP
        input_stream = ServletInputStream.from_dictionary(dictionary.get('inputStream')) if 'inputStream' in dictionary.keys() else APIHelper.SKIP 
        local_name = dictionary.get("localName") if dictionary.get("localName") else APIHelper.SKIP
        parameter_names = dictionary.get("parameterNames") if dictionary.get("parameterNames") else APIHelper.SKIP
        server_name = dictionary.get("serverName") if dictionary.get("serverName") else APIHelper.SKIP
        attribute_names = dictionary.get("attributeNames") if dictionary.get("attributeNames") else APIHelper.SKIP
        parameter_map = dictionary.get("parameterMap") if dictionary.get("parameterMap") else APIHelper.SKIP
        local_addr = dictionary.get("localAddr") if dictionary.get("localAddr") else APIHelper.SKIP
        remote_port = dictionary.get("remotePort") if dictionary.get("remotePort") else APIHelper.SKIP
        secure = dictionary.get("secure") if "secure" in dictionary.keys() else APIHelper.SKIP
        local_port = dictionary.get("localPort") if dictionary.get("localPort") else APIHelper.SKIP
        remote_addr = dictionary.get("remoteAddr") if dictionary.get("remoteAddr") else APIHelper.SKIP
        remote_host = dictionary.get("remoteHost") if dictionary.get("remoteHost") else APIHelper.SKIP
        reader = dictionary.get("reader") if dictionary.get("reader") else APIHelper.SKIP
        server_port = dictionary.get("serverPort") if dictionary.get("serverPort") else APIHelper.SKIP
        locales = dictionary.get("locales") if dictionary.get("locales") else APIHelper.SKIP
        character_encoding = dictionary.get("characterEncoding") if dictionary.get("characterEncoding") else APIHelper.SKIP
        servlet_context = ServletContext.from_dictionary(dictionary.get('servletContext')) if 'servletContext' in dictionary.keys() else APIHelper.SKIP 
        async_started = dictionary.get("asyncStarted") if "asyncStarted" in dictionary.keys() else APIHelper.SKIP
        async_supported = dictionary.get("asyncSupported") if "asyncSupported" in dictionary.keys() else APIHelper.SKIP
        async_context = AsyncContext.from_dictionary(dictionary.get('asyncContext')) if 'asyncContext' in dictionary.keys() else APIHelper.SKIP 
        dispatcher_type = dictionary.get("dispatcherType") if dictionary.get("dispatcherType") else APIHelper.SKIP
        content_length_long = dictionary.get("contentLengthLong") if dictionary.get("contentLengthLong") else APIHelper.SKIP
        content_type = dictionary.get("contentType") if dictionary.get("contentType") else APIHelper.SKIP
        # Return an object of this model
        return cls(method,
                   session,
                   cookies,
                   request_uri,
                   user_principal,
                   context_path,
                   path_info,
                   query_string,
                   remote_user,
                   servlet_path,
                   header_names,
                   requested_session_id,
                   http_servlet_mapping,
                   trailer_fields_ready,
                   auth_type,
                   path_translated,
                   requested_session_id_valid,
                   requested_session_id_from_cookie,
                   requested_session_id_from_url,
                   parts,
                   request_url,
                   trailer_fields,
                   content_length,
                   locale,
                   protocol,
                   scheme,
                   input_stream,
                   local_name,
                   parameter_names,
                   server_name,
                   attribute_names,
                   parameter_map,
                   local_addr,
                   remote_port,
                   secure,
                   local_port,
                   remote_addr,
                   remote_host,
                   reader,
                   server_port,
                   locales,
                   character_encoding,
                   servlet_context,
                   async_started,
                   async_supported,
                   async_context,
                   dispatcher_type,
                   content_length_long,
                   content_type)
