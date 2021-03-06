# coding: utf-8

"""
    Houmwork

    Houmwork for OTUS TTA  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.error_message import ErrorMessage  # noqa: F401,E501

class ExtendedErrorMessage(ErrorMessage):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tech_info': 'str',
        'trace_id': 'str'
    }
    if hasattr(ErrorMessage, "swagger_types"):
        swagger_types.update(ErrorMessage.swagger_types)

    attribute_map = {
        'tech_info': 'techInfo',
        'trace_id': 'traceID'
    }
    if hasattr(ErrorMessage, "attribute_map"):
        attribute_map.update(ErrorMessage.attribute_map)

    def __init__(self, tech_info=None, trace_id=None, *args, **kwargs):  # noqa: E501
        """ExtendedErrorMessage - a model defined in Swagger"""  # noqa: E501
        self._tech_info = None
        self._trace_id = None
        self.discriminator = None
        self.tech_info = tech_info
        self.trace_id = trace_id
        ErrorMessage.__init__(self, *args, **kwargs)

    @property
    def tech_info(self):
        """Gets the tech_info of this ExtendedErrorMessage.  # noqa: E501


        :return: The tech_info of this ExtendedErrorMessage.  # noqa: E501
        :rtype: str
        """
        return self._tech_info

    @tech_info.setter
    def tech_info(self, tech_info):
        """Sets the tech_info of this ExtendedErrorMessage.


        :param tech_info: The tech_info of this ExtendedErrorMessage.  # noqa: E501
        :type: str
        """
        if tech_info is None:
            raise ValueError("Invalid value for `tech_info`, must not be `None`")  # noqa: E501

        self._tech_info = tech_info

    @property
    def trace_id(self):
        """Gets the trace_id of this ExtendedErrorMessage.  # noqa: E501


        :return: The trace_id of this ExtendedErrorMessage.  # noqa: E501
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this ExtendedErrorMessage.


        :param trace_id: The trace_id of this ExtendedErrorMessage.  # noqa: E501
        :type: str
        """
        if trace_id is None:
            raise ValueError("Invalid value for `trace_id`, must not be `None`")  # noqa: E501

        self._trace_id = trace_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ExtendedErrorMessage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExtendedErrorMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
