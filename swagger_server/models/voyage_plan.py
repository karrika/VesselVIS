# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class VoyagePlan(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, route: str=None):
        """
        VoyagePlan - a model defined in Swagger

        :param route: The route of this VoyagePlan.
        :type route: str
        """
        self.swagger_types = {
            'route': str
        }

        self.attribute_map = {
            'route': 'route'
        }

        self._route = route

    @classmethod
    def from_dict(cls, dikt) -> 'VoyagePlan':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The voyagePlan of this VoyagePlan.
        :rtype: VoyagePlan
        """
        return deserialize_model(dikt, cls)

    @property
    def route(self) -> str:
        """
        Gets the route of this VoyagePlan.

        :return: The route of this VoyagePlan.
        :rtype: str
        """
        return self._route

    @route.setter
    def route(self, route: str):
        """
        Sets the route of this VoyagePlan.

        :param route: The route of this VoyagePlan.
        :type route: str
        """
        if route is None:
            raise ValueError("Invalid value for `route`, must not be `None`")

        self._route = route

