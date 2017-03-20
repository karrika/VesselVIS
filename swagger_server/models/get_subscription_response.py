# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class GetSubscriptionResponse(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, data_id: str=None):
        """
        GetSubscriptionResponse - a model defined in Swagger

        :param data_id: The data_id of this GetSubscriptionResponse.
        :type data_id: str
        """
        self.swagger_types = {
            'data_id': str
        }

        self.attribute_map = {
            'data_id': 'DataId'
        }

        self._data_id = data_id

    @classmethod
    def from_dict(cls, dikt) -> 'GetSubscriptionResponse':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetSubscriptionResponse of this GetSubscriptionResponse.
        :rtype: GetSubscriptionResponse
        """
        return deserialize_model(dikt, cls)

    @property
    def data_id(self) -> str:
        """
        Gets the data_id of this GetSubscriptionResponse.
        Unique identity (URN) of a voyageplan

        :return: The data_id of this GetSubscriptionResponse.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id: str):
        """
        Sets the data_id of this GetSubscriptionResponse.
        Unique identity (URN) of a voyageplan

        :param data_id: The data_id of this GetSubscriptionResponse.
        :type data_id: str
        """

        self._data_id = data_id

