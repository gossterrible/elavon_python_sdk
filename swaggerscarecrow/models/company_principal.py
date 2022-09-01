# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.address_fields import AddressFields
from swaggerscarecrow.models.person_name_fields import PersonNameFields
from swaggerscarecrow.models.phone_fields import PhoneFields
from swaggerscarecrow.models.principal_owner_detail import PrincipalOwnerDetail


class CompanyPrincipal(object):

    """Implementation of the 'CompanyPrincipal' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        gender (string): TODO: type description here.
        date_of_birth (datetime): TODO: type description here.
        address (AddressFields): TODO: type description here.
        positions (list of string): TODO: type description here.
        person_name_fields (PersonNameFields): TODO: type description here.
        phone_fields (PhoneFields): TODO: type description here.
        mobile_phone_fields (PhoneFields): TODO: type description here.
        principal_identifier (string): TODO: type description here.
        principal_owner_detail (PrincipalOwnerDetail): TODO: type description
            here.
        pesel (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "gender": 'gender',
        "date_of_birth": 'dateOfBirth',
        "address": 'address',
        "positions": 'positions',
        "person_name_fields": 'personNameFields',
        "phone_fields": 'phoneFields',
        "mobile_phone_fields": 'mobilePhoneFields',
        "principal_identifier": 'principalIdentifier',
        "principal_owner_detail": 'principalOwnerDetail',
        "pesel": 'pesel'
    }

    _optionals = [
        'name',
        'gender',
        'date_of_birth',
        'address',
        'positions',
        'person_name_fields',
        'phone_fields',
        'mobile_phone_fields',
        'principal_identifier',
        'principal_owner_detail',
        'pesel',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 gender=APIHelper.SKIP,
                 date_of_birth=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 positions=APIHelper.SKIP,
                 person_name_fields=APIHelper.SKIP,
                 phone_fields=APIHelper.SKIP,
                 mobile_phone_fields=APIHelper.SKIP,
                 principal_identifier=APIHelper.SKIP,
                 principal_owner_detail=APIHelper.SKIP,
                 pesel=APIHelper.SKIP):
        """Constructor for the CompanyPrincipal class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if gender is not APIHelper.SKIP:
            self.gender = gender 
        if date_of_birth is not APIHelper.SKIP:
            self.date_of_birth = APIHelper.RFC3339DateTime(date_of_birth) if date_of_birth else None 
        if address is not APIHelper.SKIP:
            self.address = address 
        if positions is not APIHelper.SKIP:
            self.positions = positions 
        if person_name_fields is not APIHelper.SKIP:
            self.person_name_fields = person_name_fields 
        if phone_fields is not APIHelper.SKIP:
            self.phone_fields = phone_fields 
        if mobile_phone_fields is not APIHelper.SKIP:
            self.mobile_phone_fields = mobile_phone_fields 
        if principal_identifier is not APIHelper.SKIP:
            self.principal_identifier = principal_identifier 
        if principal_owner_detail is not APIHelper.SKIP:
            self.principal_owner_detail = principal_owner_detail 
        if pesel is not APIHelper.SKIP:
            self.pesel = pesel 

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
        gender = dictionary.get("gender") if dictionary.get("gender") else APIHelper.SKIP
        date_of_birth = APIHelper.RFC3339DateTime.from_value(dictionary.get("dateOfBirth")).datetime if dictionary.get("dateOfBirth") else APIHelper.SKIP
        address = AddressFields.from_dictionary(dictionary.get('address')) if 'address' in dictionary.keys() else APIHelper.SKIP 
        positions = dictionary.get("positions") if dictionary.get("positions") else APIHelper.SKIP
        person_name_fields = PersonNameFields.from_dictionary(dictionary.get('personNameFields')) if 'personNameFields' in dictionary.keys() else APIHelper.SKIP 
        phone_fields = PhoneFields.from_dictionary(dictionary.get('phoneFields')) if 'phoneFields' in dictionary.keys() else APIHelper.SKIP 
        mobile_phone_fields = PhoneFields.from_dictionary(dictionary.get('mobilePhoneFields')) if 'mobilePhoneFields' in dictionary.keys() else APIHelper.SKIP 
        principal_identifier = dictionary.get("principalIdentifier") if dictionary.get("principalIdentifier") else APIHelper.SKIP
        principal_owner_detail = PrincipalOwnerDetail.from_dictionary(dictionary.get('principalOwnerDetail')) if 'principalOwnerDetail' in dictionary.keys() else APIHelper.SKIP 
        pesel = dictionary.get("pesel") if dictionary.get("pesel") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   gender,
                   date_of_birth,
                   address,
                   positions,
                   person_name_fields,
                   phone_fields,
                   mobile_phone_fields,
                   principal_identifier,
                   principal_owner_detail,
                   pesel)