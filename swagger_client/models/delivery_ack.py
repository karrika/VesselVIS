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


class DeliveryAck(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, reference_id=None, time_of_delivery=None, from_id=None, from_name=None, to_id=None, to_name=None, ack_result=None):
        """
        DeliveryAck - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'reference_id': 'str',
            'time_of_delivery': 'datetime',
            'from_id': 'str',
            'from_name': 'str',
            'to_id': 'str',
            'to_name': 'str',
            'ack_result': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'reference_id': 'referenceId',
            'time_of_delivery': 'timeOfDelivery',
            'from_id': 'fromId',
            'from_name': 'fromName',
            'to_id': 'toId',
            'to_name': 'toName',
            'ack_result': 'ackResult'
        }

        self._id = id
        self._reference_id = reference_id
        self._time_of_delivery = time_of_delivery
        self._from_id = from_id
        self._from_name = from_name
        self._to_id = to_id
        self._to_name = to_name
        self._ack_result = ack_result

    @property
    def id(self):
        """
        Gets the id of this DeliveryAck.
        Id for the ACK

        :return: The id of this DeliveryAck.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeliveryAck.
        Id for the ACK

        :param id: The id of this DeliveryAck.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def reference_id(self):
        """
        Gets the reference_id of this DeliveryAck.
        Reference to delivered message (URN)

        :return: The reference_id of this DeliveryAck.
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """
        Sets the reference_id of this DeliveryAck.
        Reference to delivered message (URN)

        :param reference_id: The reference_id of this DeliveryAck.
        :type: str
        """
        if reference_id is None:
            raise ValueError("Invalid value for `reference_id`, must not be `None`")
        if reference_id is not None and not re.search('urn:mrn:', reference_id):
            raise ValueError("Invalid value for `reference_id`, must be a follow pattern or equal to `/urn:mrn:/`")

        self._reference_id = reference_id

    @property
    def time_of_delivery(self):
        """
        Gets the time_of_delivery of this DeliveryAck.
        Time of delivery

        :return: The time_of_delivery of this DeliveryAck.
        :rtype: datetime
        """
        return self._time_of_delivery

    @time_of_delivery.setter
    def time_of_delivery(self, time_of_delivery):
        """
        Sets the time_of_delivery of this DeliveryAck.
        Time of delivery

        :param time_of_delivery: The time_of_delivery of this DeliveryAck.
        :type: datetime
        """
        if time_of_delivery is None:
            raise ValueError("Invalid value for `time_of_delivery`, must not be `None`")

        self._time_of_delivery = time_of_delivery

    @property
    def from_id(self):
        """
        Gets the from_id of this DeliveryAck.
        Identity of source (sender) of message that have been delivered (URN)

        :return: The from_id of this DeliveryAck.
        :rtype: str
        """
        return self._from_id

    @from_id.setter
    def from_id(self, from_id):
        """
        Sets the from_id of this DeliveryAck.
        Identity of source (sender) of message that have been delivered (URN)

        :param from_id: The from_id of this DeliveryAck.
        :type: str
        """
        if from_id is None:
            raise ValueError("Invalid value for `from_id`, must not be `None`")
        if from_id is not None and not re.search('urn:mrn:', from_id):
            raise ValueError("Invalid value for `from_id`, must be a follow pattern or equal to `/urn:mrn:/`")

        self._from_id = from_id

    @property
    def from_name(self):
        """
        Gets the from_name of this DeliveryAck.
        Friendly name of sender

        :return: The from_name of this DeliveryAck.
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """
        Sets the from_name of this DeliveryAck.
        Friendly name of sender

        :param from_name: The from_name of this DeliveryAck.
        :type: str
        """
        if from_name is None:
            raise ValueError("Invalid value for `from_name`, must not be `None`")

        self._from_name = from_name

    @property
    def to_id(self):
        """
        Gets the to_id of this DeliveryAck.
        Identity of target (recipient) of message delivery (URN)

        :return: The to_id of this DeliveryAck.
        :rtype: str
        """
        return self._to_id

    @to_id.setter
    def to_id(self, to_id):
        """
        Sets the to_id of this DeliveryAck.
        Identity of target (recipient) of message delivery (URN)

        :param to_id: The to_id of this DeliveryAck.
        :type: str
        """
        if to_id is None:
            raise ValueError("Invalid value for `to_id`, must not be `None`")
        if to_id is not None and not re.search('urn:mrn:', to_id):
            raise ValueError("Invalid value for `to_id`, must be a follow pattern or equal to `/urn:mrn:/`")

        self._to_id = to_id

    @property
    def to_name(self):
        """
        Gets the to_name of this DeliveryAck.
        Friendly name of recipient

        :return: The to_name of this DeliveryAck.
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name):
        """
        Sets the to_name of this DeliveryAck.
        Friendly name of recipient

        :param to_name: The to_name of this DeliveryAck.
        :type: str
        """
        if to_name is None:
            raise ValueError("Invalid value for `to_name`, must not be `None`")

        self._to_name = to_name

    @property
    def ack_result(self):
        """
        Gets the ack_result of this DeliveryAck.

        :return: The ack_result of this DeliveryAck.
        :rtype: str
        """
        return self._ack_result

    @ack_result.setter
    def ack_result(self, ack_result):
        """
        Sets the ack_result of this DeliveryAck.

        :param ack_result: The ack_result of this DeliveryAck.
        :type: str
        """
        if ack_result is None:
            raise ValueError("Invalid value for `ack_result`, must not be `None`")

        self._ack_result = ack_result

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
