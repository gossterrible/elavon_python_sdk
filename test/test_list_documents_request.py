"""
    Swagger Scarecrow

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import elavon
from elavon.model.banking_info import BankingInfo
from elavon.model.business_info import BusinessInfo
from elavon.model.card_pricing import CardPricing
from elavon.model.equipment_info import EquipmentInfo
from elavon.model.person import Person
globals()['BankingInfo'] = BankingInfo
globals()['BusinessInfo'] = BusinessInfo
globals()['CardPricing'] = CardPricing
globals()['EquipmentInfo'] = EquipmentInfo
globals()['Person'] = Person
from elavon.model.list_documents_request import ListDocumentsRequest


class TestListDocumentsRequest(unittest.TestCase):
    """ListDocumentsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListDocumentsRequest(self):
        """Test ListDocumentsRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListDocumentsRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
