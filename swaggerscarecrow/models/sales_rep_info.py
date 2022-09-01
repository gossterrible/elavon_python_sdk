# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class SalesRepInfo(object):

    """Implementation of the 'SalesRepInfo' model.

    TODO: type model description here.

    Attributes:
        sales_rep_code (string): Identifier of sales representative
            responsible for submission
        name (string): Name of the sales rep
        email (string): email of the sales rep
        submitted (bool): Flag if the app has been submitted

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sales_rep_code": 'salesRepCode',
        "name": 'name',
        "email": 'email',
        "submitted": 'submitted'
    }

    _optionals = [
        'name',
        'email',
        'submitted',
    ]

    def __init__(self,
                 sales_rep_code=None,
                 name=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 submitted=APIHelper.SKIP):
        """Constructor for the SalesRepInfo class"""

        # Initialize members of the class
        self.sales_rep_code = sales_rep_code 
        if name is not APIHelper.SKIP:
            self.name = name 
        if email is not APIHelper.SKIP:
            self.email = email 
        if submitted is not APIHelper.SKIP:
            self.submitted = submitted 

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

        sales_rep_code = dictionary.get("salesRepCode") if dictionary.get("salesRepCode") else None
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        email = dictionary.get("email") if dictionary.get("email") else APIHelper.SKIP
        submitted = dictionary.get("submitted") if "submitted" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(sales_rep_code,
                   name,
                   email,
                   submitted)
