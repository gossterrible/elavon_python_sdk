# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper


class DateComponents(object):

    """Implementation of the 'DateComponents' model.

    A container that holds the date (day, month, and year)

    Attributes:
        year (int): TODO: type description here.
        month (MonthEnum): TODO: type description here.
        day (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "year": 'year',
        "month": 'month',
        "day": 'day'
    }

    _optionals = [
        'year',
        'month',
        'day',
    ]

    def __init__(self,
                 year=APIHelper.SKIP,
                 month=APIHelper.SKIP,
                 day=APIHelper.SKIP):
        """Constructor for the DateComponents class"""

        # Initialize members of the class
        if year is not APIHelper.SKIP:
            self.year = year 
        if month is not APIHelper.SKIP:
            self.month = month 
        if day is not APIHelper.SKIP:
            self.day = day 

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

        year = dictionary.get("year") if dictionary.get("year") else APIHelper.SKIP
        month = dictionary.get("month") if dictionary.get("month") else APIHelper.SKIP
        day = dictionary.get("day") if dictionary.get("day") else APIHelper.SKIP
        # Return an object of this model
        return cls(year,
                   month,
                   day)