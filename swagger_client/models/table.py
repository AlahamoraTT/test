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

class Table(object):
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
        'id': 'int',
        'name': 'OneOfTableName',
        'is_available': 'bool',
        'place_id': 'int',
        'available_date_time': 'datetime',
        'tag': 'TableTag'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_available': 'isAvailable',
        'place_id': 'placeId',
        'available_date_time': 'availableDateTime',
        'tag': 'Tag'
    }

    def __init__(self, id=None, name=None, is_available=None, place_id=None, available_date_time=None, tag=None):  # noqa: E501
        """Table - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._is_available = None
        self._place_id = None
        self._available_date_time = None
        self._tag = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.is_available = is_available
        self.place_id = place_id
        self.available_date_time = available_date_time
        if tag is not None:
            self.tag = tag

    @property
    def id(self):
        """Gets the id of this Table.  # noqa: E501

        Уникальный ID столика (сквозной идентификатор по всем ресторанам в системе)  # noqa: E501

        :return: The id of this Table.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Table.

        Уникальный ID столика (сквозной идентификатор по всем ресторанам в системе)  # noqa: E501

        :param id: The id of this Table.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Table.  # noqa: E501

        Название или номер столика в ресторане  # noqa: E501

        :return: The name of this Table.  # noqa: E501
        :rtype: OneOfTableName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Table.

        Название или номер столика в ресторане  # noqa: E501

        :param name: The name of this Table.  # noqa: E501
        :type: OneOfTableName
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_available(self):
        """Gets the is_available of this Table.  # noqa: E501

        Доступность столика для бронирования  # noqa: E501

        :return: The is_available of this Table.  # noqa: E501
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        """Sets the is_available of this Table.

        Доступность столика для бронирования  # noqa: E501

        :param is_available: The is_available of this Table.  # noqa: E501
        :type: bool
        """
        if is_available is None:
            raise ValueError("Invalid value for `is_available`, must not be `None`")  # noqa: E501

        self._is_available = is_available

    @property
    def place_id(self):
        """Gets the place_id of this Table.  # noqa: E501

        Уникальный ID ресторана  # noqa: E501

        :return: The place_id of this Table.  # noqa: E501
        :rtype: int
        """
        return self._place_id

    @place_id.setter
    def place_id(self, place_id):
        """Sets the place_id of this Table.

        Уникальный ID ресторана  # noqa: E501

        :param place_id: The place_id of this Table.  # noqa: E501
        :type: int
        """
        if place_id is None:
            raise ValueError("Invalid value for `place_id`, must not be `None`")  # noqa: E501

        self._place_id = place_id

    @property
    def available_date_time(self):
        """Gets the available_date_time of this Table.  # noqa: E501

        Дата и время свободные для бронирования  # noqa: E501

        :return: The available_date_time of this Table.  # noqa: E501
        :rtype: datetime
        """
        return self._available_date_time

    @available_date_time.setter
    def available_date_time(self, available_date_time):
        """Sets the available_date_time of this Table.

        Дата и время свободные для бронирования  # noqa: E501

        :param available_date_time: The available_date_time of this Table.  # noqa: E501
        :type: datetime
        """
        if available_date_time is None:
            raise ValueError("Invalid value for `available_date_time`, must not be `None`")  # noqa: E501

        self._available_date_time = available_date_time

    @property
    def tag(self):
        """Gets the tag of this Table.  # noqa: E501


        :return: The tag of this Table.  # noqa: E501
        :rtype: TableTag
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Table.


        :param tag: The tag of this Table.  # noqa: E501
        :type: TableTag
        """

        self._tag = tag

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
        if issubclass(Table, dict):
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
        if not isinstance(other, Table):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
