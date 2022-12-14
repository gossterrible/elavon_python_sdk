# -*- coding: utf-8 -*-

"""
swaggerscarecrow

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerscarecrow.api_helper import APIHelper
from swaggerscarecrow.models.date_components import DateComponents
from swaggerscarecrow.models.equipment_pricing import EquipmentPricing
from swaggerscarecrow.models.exception_item import ExceptionItem
from swaggerscarecrow.models.item_settings import ItemSettings


class EquipmentItem(object):

    """Implementation of the 'EquipmentItem' model.

    TODO: type model description here.

    Attributes:
        code (string): SKU of product
        quantity (int): Number of product being chosen
        pricing_items (list of EquipmentPricing): Product pricinging listing
        item_settings (ItemSettings): TODO: type description here.
        exception_items (list of ExceptionItem): [EU] Exception pricing to be
            sent for equipment pricing
        service_fee (float): TODO: type description here.
        trx_free_month (int): Free transaction per month per terminal
        future_effective_date (DateComponents): A container that holds the
            date (day, month, and year)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "quantity": 'quantity',
        "pricing_items": 'pricingItems',
        "trx_free_month": 'trxFreeMonth',
        "item_settings": 'itemSettings',
        "exception_items": 'exceptionItems',
        "service_fee": 'serviceFee',
        "future_effective_date": 'futureEffectiveDate'
    }

    _optionals = [
        'item_settings',
        'exception_items',
        'service_fee',
        'future_effective_date',
    ]

    def __init__(self,
                 code=None,
                 quantity=None,
                 pricing_items=None,
                 trx_free_month=None,
                 item_settings=APIHelper.SKIP,
                 exception_items=APIHelper.SKIP,
                 service_fee=APIHelper.SKIP,
                 future_effective_date=APIHelper.SKIP):
        """Constructor for the EquipmentItem class"""

        # Initialize members of the class
        self.code = code 
        self.quantity = quantity 
        self.pricing_items = pricing_items 
        if item_settings is not APIHelper.SKIP:
            self.item_settings = item_settings 
        if exception_items is not APIHelper.SKIP:
            self.exception_items = exception_items 
        if service_fee is not APIHelper.SKIP:
            self.service_fee = service_fee 
        self.trx_free_month = trx_free_month 
        if future_effective_date is not APIHelper.SKIP:
            self.future_effective_date = future_effective_date 

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

        code = dictionary.get("code") if dictionary.get("code") else None
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else None
        pricing_items = None
        if dictionary.get('pricingItems') is not None:
            pricing_items = [EquipmentPricing.from_dictionary(x) for x in dictionary.get('pricingItems')]
        trx_free_month = dictionary.get("trxFreeMonth") if dictionary.get("trxFreeMonth") else None
        item_settings = ItemSettings.from_dictionary(dictionary.get('itemSettings')) if 'itemSettings' in dictionary.keys() else APIHelper.SKIP 
        exception_items = None
        if dictionary.get('exceptionItems') is not None:
            exception_items = [ExceptionItem.from_dictionary(x) for x in dictionary.get('exceptionItems')]
        else:
            exception_items = APIHelper.SKIP
        service_fee = dictionary.get("serviceFee") if dictionary.get("serviceFee") else APIHelper.SKIP
        future_effective_date = DateComponents.from_dictionary(dictionary.get('futureEffectiveDate')) if 'futureEffectiveDate' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(code,
                   quantity,
                   pricing_items,
                   trx_free_month,
                   item_settings,
                   exception_items,
                   service_fee,
                   future_effective_date)
