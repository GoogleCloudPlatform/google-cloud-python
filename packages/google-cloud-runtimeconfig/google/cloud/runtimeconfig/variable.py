# Copyright 2016 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Create / interact with Google Cloud RuntimeConfig variables.

.. data:: STATE_UNSPECIFIED

    The default variable state.  See
    https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables#VariableState

.. data:: STATE_UPDATED

    Indicates the variable was updated, while `variables.watch` was executing.
    See
    https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables#VariableState

.. data:: STATE_DELETED

    Indicates the variable was deleted, while `variables.watch`_ was executing.
    See
    https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables#VariableState

.. _variables.watch:
    https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/watch
"""

import base64
import datetime

from google.api_core import datetime_helpers
from google.cloud.exceptions import Conflict, NotFound

from google.cloud.runtimeconfig._helpers import variable_name_from_full_name
from google.cloud.runtimeconfig.exceptions import Error

STATE_UNSPECIFIED = "VARIABLE_STATE_UNSPECIFIED"
STATE_UPDATED = "UPDATED"
STATE_DELETED = "DELETED"


class Variable(object):
    """A variable in the Cloud RuntimeConfig service.

    See
    https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables

    :type name: str
    :param name: The name of the variable.  This corresponds to the
                 unique path of the variable in the config.

    :type config: :class:`google.cloud.runtimeconfig.config.Config`
    :param config: The config to which this variable belongs.
    """

    def __init__(self, name, config):
        self.name = name
        self.config = config
        self._properties = {}

    @classmethod
    def from_api_repr(cls, resource, config):
        """Factory:  construct a Variable given its API representation

        :type resource: dict
        :param resource: change set representation returned from the API.

        :type config: :class:`google.cloud.runtimeconfig.config.Config`
        :param config: The config to which this variable belongs.

        :rtype: :class:`google.cloud.runtimeconfig.variable.Variable`
        :returns: Variable parsed from ``resource``.
        """
        name = variable_name_from_full_name(resource.get("name"))
        variable = cls(name=name, config=config)
        variable._set_properties(resource=resource)
        return variable

    @property
    def full_name(self):
        """Fully-qualified name of this variable.

        Example:
        ``projects/my-project/configs/my-config/variables/my-var``

        :rtype: str
        :returns: The full name based on config and variable names.

        :raises: :class:`ValueError` if the variable is missing a name.
        """
        if not self.name:
            raise ValueError("Missing variable name.")
        return "%s/variables/%s" % (self.config.full_name, self.name)

    @property
    def path(self):
        """URL path for the variable's APIs.

        :rtype: str
        :returns: The URL path based on config and variable names.
        """
        return "/%s" % (self.full_name,)

    @property
    def client(self):
        """The client bound to this variable."""
        return self.config.client

    @property
    def text(self):
        """Text of the variable, as string.

        See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables

        :rtype: str or ``NoneType``
        :returns: The text of the variable or ``None`` if the property
                  is not set locally.
        """
        return self._properties.get("text")

    @text.setter
    def text(self, value):
        """Set text property.

        If the variable is already using value, this will raise
        exceptions.Error since text and value are mutually exclusive.
        To persist the change, call create() or update().

        :type value: str
        :param value: The new value for the text property.
        """
        if "value" in self._properties:
            raise Error("Value and text are mutually exclusive.")
        self._properties["text"] = value

    @property
    def value(self):
        """Value of the variable, as bytes.

        See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables

        :rtype: bytes or ``NoneType``
        :returns: The value of the variable or ``None`` if the property
                  is not set locally.
        """
        value = self._properties.get("value")
        if value is not None:
            value = base64.b64decode(value)
        return value

    @value.setter
    def value(self, value):
        """Set value property.

        If the variable is already using text, this will raise exceptions.Error
        since text and value are mutually exclusive.
        To persist the change, call create() or update().

        :type value: bytes
        :param value: The new value for the value property.
        """
        if "text" in self._properties:
            raise Error("Value and text are mutually exclusive.")
        self._properties["value"] = value

    @property
    def state(self):
        """Retrieve the state of the variable.

        See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables#VariableState

        :rtype: str
        :returns:
            If set, one of "UPDATED", "DELETED", or defaults to
            "VARIABLE_STATE_UNSPECIFIED".
        """
        return self._properties.get("state", STATE_UNSPECIFIED)

    @property
    def update_time(self):
        """Retrieve the timestamp at which the variable was updated.

        See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables

        Returns:
            :class:`~api_core.datetime_helpers.DatetimeWithNanoseconds`,
            :class:`datetime.datetime` or ``NoneType``:
            Datetime object parsed from RFC3339 valid timestamp, or
            ``None`` if the property is not set locally.

        Raises:
            ValueError: if value is not a valid RFC3339 timestamp
        """
        value = self._properties.get("updateTime")
        if value is not None:
            try:
                value = datetime.datetime.strptime(
                    value, datetime_helpers._RFC3339_MICROS
                ).replace(tzinfo=datetime.timezone.utc)
            except ValueError:
                DatetimeNS = datetime_helpers.DatetimeWithNanoseconds
                value = DatetimeNS.from_rfc3339(value)
        return value

    def _require_client(self, client):
        """Check client or verify over-ride.

        :type client: :class:`google.cloud.runtimconfig.client.Client`
        :param client:
            (Optional) The client to use.  If not passed, falls back to the
            ``client`` stored on the current zone.

        :rtype: :class:`google.cloud.runtimeconfig.client.Client`
        :returns: The client passed in or the currently bound client.
        """
        if client is None:
            client = self.client
        return client

    def _set_properties(self, resource):
        """Update properties from resource in body of ``api_response``

        :type resource: dict
        :param resource: variable representation returned from the API.
        """
        self._properties.clear()
        cleaned = resource.copy()
        if "name" in cleaned:
            self.name = variable_name_from_full_name(cleaned.pop("name"))
        self._properties.update(cleaned)

    def _get_payload(self):
        """Return the payload for create and update operations

        :rtype: dict
        :returns: payload for API call with name and text or value attributes
        """
        data = {"name": self.full_name}
        if "text" in self._properties:
            data["text"] = self._properties["text"]
        elif "value" in self._properties:
            value = self._properties["value"]
            data["value"] = base64.b64encode(value).decode("utf-8")
        else:
            raise Error("No text or value set.")
        return data

    def create(self, client=None):
        """API call:  create the variable via a POST request

        See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/create

        :type client: :class:`~google.cloud.runtimeconfig.client.Client`
        :param client:
            (Optional) The client to use.  If not passed, falls back to the
            ``client`` stored on the variable's config.

        :rtype: bool
        :returns: True if the variable has been created, False on error.
        """
        client = self._require_client(client)
        path = "%s/variables" % self.config.path
        data = self._get_payload()
        try:
            resp = client._connection.api_request(method="POST", path=path, data=data)
        except Conflict:
            return False
        self._set_properties(resp)
        return True

    def update(self, client=None):
        """API call:  update the variable via a PUT request

        See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/update

        :type client: :class:`~google.cloud.runtimeconfig.client.Client`
        :param client:
            (Optional) The client to use.  If not passed, falls back to the
            ``client`` stored on the variable's config.

        :rtype: bool
        :returns: True if the variable has been created, False on error.
        """
        client = self._require_client(client)
        data = self._get_payload()
        try:
            resp = client._connection.api_request(
                method="PUT", path=self.path, data=data
            )
        except NotFound:
            return False
        self._set_properties(resp)
        return True

    def exists(self, client=None):
        """API call:  test for the existence of the variable via a GET request

        See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/get

        :type client: :class:`~google.cloud.runtimeconfig.client.Client`
        :param client:
            (Optional) The client to use.  If not passed, falls back to the
            ``client`` stored on the variable's config.

        :rtype: bool
        :returns: True if the variable exists in Cloud RuntimeConfig.
        """
        client = self._require_client(client)
        try:
            # We only need the status code (200 or not) so we seek to
            # minimize the returned payload.
            query_params = {"fields": "name"}
            client._connection.api_request(
                method="GET", path=self.path, query_params=query_params
            )
            return True
        except NotFound:
            return False

    def reload(self, client=None):
        """API call:  reload the variable via a ``GET`` request.

        This method will reload the newest data for the variable.

        See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/get

        :type client: :class:`google.cloud.runtimeconfig.client.Client`
        :param client:
            (Optional) The client to use.  If not passed, falls back to the
            client stored on the current config.
        """
        client = self._require_client(client)

        # We assume the variable exists. If it doesn't it will raise a NotFound
        # exception.
        resp = client._connection.api_request(method="GET", path=self.path)
        self._set_properties(resource=resp)
