# coding: utf-8

"""
    STM Voyage Information Service SeaSWIM API

    Voyage Information Service API facing SeaSWIM through SSC exposing interfaces to SeaSWIM stakeholders

    OpenAPI spec version: 1.0.0
    Contact: per.lofbom@sjofartsverket.se
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ErrorModel(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, error_model_id=None, code=None, message=None):
        """
        ErrorModel - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error_model_id': 'int',
            'code': 'int',
            'message': 'str'
        }

        self.attribute_map = {
            'error_model_id': 'errorModelId',
            'code': 'code',
            'message': 'message'
        }

        self._error_model_id = error_model_id
        self._code = code
        self._message = message

    @property
    def error_model_id(self):
        """
        Gets the error_model_id of this ErrorModel.

        :return: The error_model_id of this ErrorModel.
        :rtype: int
        """
        return self._error_model_id

    @error_model_id.setter
    def error_model_id(self, error_model_id):
        """
        Sets the error_model_id of this ErrorModel.

        :param error_model_id: The error_model_id of this ErrorModel.
        :type: int
        """
        if error_model_id is None:
            raise ValueError("Invalid value for `error_model_id`, must not be `None`")

        self._error_model_id = error_model_id

    @property
    def code(self):
        """
        Gets the code of this ErrorModel.

        :return: The code of this ErrorModel.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ErrorModel.

        :param code: The code of this ErrorModel.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this ErrorModel.

        :return: The message of this ErrorModel.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ErrorModel.

        :param message: The message of this ErrorModel.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
