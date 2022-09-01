"""
    Swagger Scarecrow

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from elavon.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from elavon.exceptions import ApiAttributeError


def lazy_import():
    from elavon.model.acs_info import AcsInfo
    from elavon.model.ebt_info import EbtInfo
    from elavon.model.ecs_info import EcsInfo
    from elavon.model.efs3d_secure_info import Efs3dSecureInfo
    from elavon.model.fanfare_info import FanfareInfo
    from elavon.model.ocm_info import OcmInfo
    from elavon.model.on_demand_info import OnDemandInfo
    from elavon.model.straight_send_info import StraightSendInfo
    globals()['AcsInfo'] = AcsInfo
    globals()['EbtInfo'] = EbtInfo
    globals()['EcsInfo'] = EcsInfo
    globals()['Efs3dSecureInfo'] = Efs3dSecureInfo
    globals()['FanfareInfo'] = FanfareInfo
    globals()['OcmInfo'] = OcmInfo
    globals()['OnDemandInfo'] = OnDemandInfo
    globals()['StraightSendInfo'] = StraightSendInfo


class ValueAddedInfo(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('gsm_prepaid_type',): {
            'EURONET_NO_PAYS': "EURONET_NO_PAYS",
            'BP_EURONET': "BP_EURONET",
            'EURONET': "EURONET",
            'LEW_LEASE': "LEW_LEASE",
            'LEW': "LEW",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'value_adds': ({str: (bool,)},),  # noqa: E501
            'ebt_info': (EbtInfo,),  # noqa: E501
            'ecs_info': (EcsInfo,),  # noqa: E501
            'acs_info': (AcsInfo,),  # noqa: E501
            'fanfare_info': (FanfareInfo,),  # noqa: E501
            'gsm_prepaid_type': (str,),  # noqa: E501
            'surcharge_managed_by': (str,),  # noqa: E501
            'credit_surcharge_amt': (str,),  # noqa: E501
            'efs3d_secure_info': (Efs3dSecureInfo,),  # noqa: E501
            'straight_send_info': (StraightSendInfo,),  # noqa: E501
            'on_demand_info': (OnDemandInfo,),  # noqa: E501
            'ocm_info': (OcmInfo,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'value_adds': 'valueAdds',  # noqa: E501
        'ebt_info': 'ebtInfo',  # noqa: E501
        'ecs_info': 'ecsInfo',  # noqa: E501
        'acs_info': 'acsInfo',  # noqa: E501
        'fanfare_info': 'fanfareInfo',  # noqa: E501
        'gsm_prepaid_type': 'gsmPrepaidType',  # noqa: E501
        'surcharge_managed_by': 'surchargeManagedBy',  # noqa: E501
        'credit_surcharge_amt': 'creditSurchargeAmt',  # noqa: E501
        'efs3d_secure_info': 'efs3dSecureInfo',  # noqa: E501
        'straight_send_info': 'straightSendInfo',  # noqa: E501
        'on_demand_info': 'onDemandInfo',  # noqa: E501
        'ocm_info': 'ocmInfo',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ValueAddedInfo - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            value_adds ({str: (bool,)}): Boolean map to indicate presence of various value added services, true if present, false/null if absent.The valid keys are as follows: FANFARE, ELECTRONIC_CHECKING_SERVICE, CREDIT_CARD_SURCHARGING, CASH_BACK, MERCHANT_CONNECT_PREMIUM, CONTACTLESS, CONVERGE_BILLING_AND_INVOICE, CONVERGE_HOSPITALITY, E_TOKENIZATION, SECURED_ENCRYPT, HEALTH_CARE_ELIGIBILITY, HEALTH_CARE_CLAIMS, HEALTH_CARE_REMITTANCE, HEALTH_CARE_ELIGIBILITY_AND_ESTIMATOR, HEALTH_CARE_PATIENT_BILLING, FRAUD_SERVICES_3D_SECURE, STRAIGHT_SEND, ON_DEMAND. [optional]  # noqa: E501
            ebt_info (EbtInfo): [optional]  # noqa: E501
            ecs_info (EcsInfo): [optional]  # noqa: E501
            acs_info (AcsInfo): [optional]  # noqa: E501
            fanfare_info (FanfareInfo): [optional]  # noqa: E501
            gsm_prepaid_type (str): [EU] Additional GSM SIM prepaid information. [optional]  # noqa: E501
            surcharge_managed_by (str): [NA] Surcharge Managed By. [optional]  # noqa: E501
            credit_surcharge_amt (str): [NA] Credit Surcharge Amount. [optional]  # noqa: E501
            efs3d_secure_info (Efs3dSecureInfo): [optional]  # noqa: E501
            straight_send_info (StraightSendInfo): [optional]  # noqa: E501
            on_demand_info (OnDemandInfo): [optional]  # noqa: E501
            ocm_info (OcmInfo): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ValueAddedInfo - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            value_adds ({str: (bool,)}): Boolean map to indicate presence of various value added services, true if present, false/null if absent.The valid keys are as follows: FANFARE, ELECTRONIC_CHECKING_SERVICE, CREDIT_CARD_SURCHARGING, CASH_BACK, MERCHANT_CONNECT_PREMIUM, CONTACTLESS, CONVERGE_BILLING_AND_INVOICE, CONVERGE_HOSPITALITY, E_TOKENIZATION, SECURED_ENCRYPT, HEALTH_CARE_ELIGIBILITY, HEALTH_CARE_CLAIMS, HEALTH_CARE_REMITTANCE, HEALTH_CARE_ELIGIBILITY_AND_ESTIMATOR, HEALTH_CARE_PATIENT_BILLING, FRAUD_SERVICES_3D_SECURE, STRAIGHT_SEND, ON_DEMAND. [optional]  # noqa: E501
            ebt_info (EbtInfo): [optional]  # noqa: E501
            ecs_info (EcsInfo): [optional]  # noqa: E501
            acs_info (AcsInfo): [optional]  # noqa: E501
            fanfare_info (FanfareInfo): [optional]  # noqa: E501
            gsm_prepaid_type (str): [EU] Additional GSM SIM prepaid information. [optional]  # noqa: E501
            surcharge_managed_by (str): [NA] Surcharge Managed By. [optional]  # noqa: E501
            credit_surcharge_amt (str): [NA] Credit Surcharge Amount. [optional]  # noqa: E501
            efs3d_secure_info (Efs3dSecureInfo): [optional]  # noqa: E501
            straight_send_info (StraightSendInfo): [optional]  # noqa: E501
            on_demand_info (OnDemandInfo): [optional]  # noqa: E501
            ocm_info (OcmInfo): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")