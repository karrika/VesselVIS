# coding: utf-8

"""
    STM Voyage Information Service SeaSWIM API

    Voyage Information Service API facing SeaSWIM through SSC exposing interfaces to SeaSWIM stakeholders

    OpenAPI spec version: 1.0.0
    Contact: per.lofbom@sjofartsverket.se
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.response_obj import ResponseObj


class TestResponseObj(unittest.TestCase):
    """ ResponseObj unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseObj(self):
        """
        Test ResponseObj
        """
        model = swagger_client.models.response_obj.ResponseObj()


if __name__ == '__main__':
    unittest.main()