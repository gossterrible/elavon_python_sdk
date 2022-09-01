# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.address_fields import AddressFields


class CompanyIdentification(object):

    """Implementation of the 'CompanyIdentification' model.

    TODO: type model description here.

    Attributes:
        business_name (string): TODO: type description here.
        registered_company_name (string): TODO: type description here.
        country (string): TODO: type description here.
        country_code (string): TODO: type description here.
        company_registration_number (string): TODO: type description here.
        vat_registration_number (string): TODO: type description here.
        date_of_company_registration (datetime): TODO: type description here.
        date_of_starting_operation (datetime): TODO: type description here.
        contact_address (AddressFields): TODO: type description here.
        owner_type (string): TODO: type description here.
        tax_id_type (string): TODO: type description here.
        tax_id_number (string): TODO: type description here.
        fed_tax_id (string): TODO: type description here.
        certification_date (datetime): TODO: type description here.
        customer_centric_flag (bool): TODO: type description here.
        mid (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "business_name": 'businessName',
        "registered_company_name": 'registeredCompanyName',
        "country": 'country',
        "country_code": 'countryCode',
        "company_registration_number": 'companyRegistrationNumber',
        "vat_registration_number": 'vatRegistrationNumber',
        "date_of_company_registration": 'dateOfCompanyRegistration',
        "date_of_starting_operation": 'dateOfStartingOperation',
        "contact_address": 'contactAddress',
        "owner_type": 'ownerType',
        "tax_id_type": 'taxIdType',
        "tax_id_number": 'taxIdNumber',
        "fed_tax_id": 'fedTaxId',
        "certification_date": 'certificationDate',
        "customer_centric_flag": 'customerCentricFlag',
        "mid": 'mid'
    }

    _optionals = [
        'business_name',
        'registered_company_name',
        'country',
        'country_code',
        'company_registration_number',
        'vat_registration_number',
        'date_of_company_registration',
        'date_of_starting_operation',
        'contact_address',
        'owner_type',
        'tax_id_type',
        'tax_id_number',
        'fed_tax_id',
        'certification_date',
        'customer_centric_flag',
        'mid',
    ]

    def __init__(self,
                 business_name=APIHelper.SKIP,
                 registered_company_name=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 country_code=APIHelper.SKIP,
                 company_registration_number=APIHelper.SKIP,
                 vat_registration_number=APIHelper.SKIP,
                 date_of_company_registration=APIHelper.SKIP,
                 date_of_starting_operation=APIHelper.SKIP,
                 contact_address=APIHelper.SKIP,
                 owner_type=APIHelper.SKIP,
                 tax_id_type=APIHelper.SKIP,
                 tax_id_number=APIHelper.SKIP,
                 fed_tax_id=APIHelper.SKIP,
                 certification_date=APIHelper.SKIP,
                 customer_centric_flag=APIHelper.SKIP,
                 mid=APIHelper.SKIP):
        """Constructor for the CompanyIdentification class"""

        # Initialize members of the class
        if business_name is not APIHelper.SKIP:
            self.business_name = business_name 
        if registered_company_name is not APIHelper.SKIP:
            self.registered_company_name = registered_company_name 
        if country is not APIHelper.SKIP:
            self.country = country 
        if country_code is not APIHelper.SKIP:
            self.country_code = country_code 
        if company_registration_number is not APIHelper.SKIP:
            self.company_registration_number = company_registration_number 
        if vat_registration_number is not APIHelper.SKIP:
            self.vat_registration_number = vat_registration_number 
        if date_of_company_registration is not APIHelper.SKIP:
            self.date_of_company_registration = APIHelper.RFC3339DateTime(date_of_company_registration) if date_of_company_registration else None 
        if date_of_starting_operation is not APIHelper.SKIP:
            self.date_of_starting_operation = APIHelper.RFC3339DateTime(date_of_starting_operation) if date_of_starting_operation else None 
        if contact_address is not APIHelper.SKIP:
            self.contact_address = contact_address 
        if owner_type is not APIHelper.SKIP:
            self.owner_type = owner_type 
        if tax_id_type is not APIHelper.SKIP:
            self.tax_id_type = tax_id_type 
        if tax_id_number is not APIHelper.SKIP:
            self.tax_id_number = tax_id_number 
        if fed_tax_id is not APIHelper.SKIP:
            self.fed_tax_id = fed_tax_id 
        if certification_date is not APIHelper.SKIP:
            self.certification_date = APIHelper.RFC3339DateTime(certification_date) if certification_date else None 
        if customer_centric_flag is not APIHelper.SKIP:
            self.customer_centric_flag = customer_centric_flag 
        if mid is not APIHelper.SKIP:
            self.mid = mid 

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

        business_name = dictionary.get("businessName") if dictionary.get("businessName") else APIHelper.SKIP
        registered_company_name = dictionary.get("registeredCompanyName") if dictionary.get("registeredCompanyName") else APIHelper.SKIP
        country = dictionary.get("country") if dictionary.get("country") else APIHelper.SKIP
        country_code = dictionary.get("countryCode") if dictionary.get("countryCode") else APIHelper.SKIP
        company_registration_number = dictionary.get("companyRegistrationNumber") if dictionary.get("companyRegistrationNumber") else APIHelper.SKIP
        vat_registration_number = dictionary.get("vatRegistrationNumber") if dictionary.get("vatRegistrationNumber") else APIHelper.SKIP
        date_of_company_registration = APIHelper.RFC3339DateTime.from_value(dictionary.get("dateOfCompanyRegistration")).datetime if dictionary.get("dateOfCompanyRegistration") else APIHelper.SKIP
        date_of_starting_operation = APIHelper.RFC3339DateTime.from_value(dictionary.get("dateOfStartingOperation")).datetime if dictionary.get("dateOfStartingOperation") else APIHelper.SKIP
        contact_address = AddressFields.from_dictionary(dictionary.get('contactAddress')) if 'contactAddress' in dictionary.keys() else APIHelper.SKIP 
        owner_type = dictionary.get("ownerType") if dictionary.get("ownerType") else APIHelper.SKIP
        tax_id_type = dictionary.get("taxIdType") if dictionary.get("taxIdType") else APIHelper.SKIP
        tax_id_number = dictionary.get("taxIdNumber") if dictionary.get("taxIdNumber") else APIHelper.SKIP
        fed_tax_id = dictionary.get("fedTaxId") if dictionary.get("fedTaxId") else APIHelper.SKIP
        certification_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("certificationDate")).datetime if dictionary.get("certificationDate") else APIHelper.SKIP
        customer_centric_flag = dictionary.get("customerCentricFlag") if "customerCentricFlag" in dictionary.keys() else APIHelper.SKIP
        mid = dictionary.get("mid") if dictionary.get("mid") else APIHelper.SKIP
        # Return an object of this model
        return cls(business_name,
                   registered_company_name,
                   country,
                   country_code,
                   company_registration_number,
                   vat_registration_number,
                   date_of_company_registration,
                   date_of_starting_operation,
                   contact_address,
                   owner_type,
                   tax_id_type,
                   tax_id_number,
                   fed_tax_id,
                   certification_date,
                   customer_centric_flag,
                   mid)
