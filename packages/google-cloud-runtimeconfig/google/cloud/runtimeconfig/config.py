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

"""Create / interact with Google Cloud RuntimeConfig configs."""

from google.api_core import page_iterator
from google.cloud.exceptions import NotFound

from google.cloud.runtimeconfig._helpers import config_name_from_full_name
from google.cloud.runtimeconfig.variable import Variable


class Config(object):
    """A Config resource in the Cloud RuntimeConfig service.

    This consists of metadata and a hierarchy of variables.

    See
    https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs

    :type client: :class:`google.cloud.runtimeconfig.client.Client`
    :param client: A client which holds credentials and project configuration
                   for the config (which requires a project).

    :type name: str
    :param name: The name of the config.
    """

    def __init__(self, client, name):
        self._client = client
        self.name = name
        self._properties = {}

    def __repr__(self):
        return "<Config: %s>" % (self.name,)

    @property
    def client(self):
        """The client bound to this config."""
        return self._client

    @property
    def description(self):
        """Description of the config object.

        See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs#resource-runtimeconfig

        :rtype: str, or ``NoneType``
        :returns: the description (None until set from the server).
        """
        return self._properties.get("description")

    @property
    def project(self):
        """Project bound to the config.

        :rtype: str
        :returns: the project (derived from the client).
        """
        return self._client.project

    @property
    def full_name(self):
        """Fully-qualified name of this variable.

        Example:
        ``projects/my-project/configs/my-config``

        :rtype: str
        :returns: The full name based on project and config names.

        :raises: :class:`ValueError` if the config is missing a name.
        """
        if not self.name:
            raise ValueError("Missing config name.")
        return "projects/%s/configs/%s" % (self._client.project, self.name)

    @property
    def path(self):
        """URL path for the config's APIs.

        :rtype: str
        :returns: The URL path based on project and config names.
        """
        return "/%s" % (self.full_name,)

    def variable(self, variable_name):
        """Factory constructor for variable object.

        .. note::
          This will not make an HTTP request; it simply instantiates
          a variable object owned by this config.

        :type variable_name: str
        :param variable_name: The name of the variable to be instantiated.

        :rtype: :class:`google.cloud.runtimeconfig.variable.Variable`
        :returns: The variable object created.
        """
        return Variable(name=variable_name, config=self)

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
            client = self._client
        return client

    def _set_properties(self, api_response):
        """Update properties from resource in body of ``api_response``

        :type api_response: dict
        :param api_response: response returned from an API call
        """
        self._properties.clear()
        cleaned = api_response.copy()
        if "name" in cleaned:
            self.name = config_name_from_full_name(cleaned.pop("name"))
        self._properties.update(cleaned)

    def exists(self, client=None):
        """Determines whether or not this config exists.

        :type client: :class:`~google.cloud.runtimeconfig.client.Client`
        :param client:
            (Optional) The client to use.  If not passed, falls back to the
            ``client`` stored on the current config.

        :rtype: bool
        :returns: True if the config exists in Cloud Runtime Configurator.
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
        """API call:  reload the config via a ``GET`` request.

        This method will reload the newest data for the config.

        See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/get

        :type client: :class:`google.cloud.runtimeconfig.client.Client`
        :param client:
            (Optional) The client to use.  If not passed, falls back to the
            client stored on the current config.
        """
        client = self._require_client(client)

        # We assume the config exists. If it doesn't it will raise a NotFound
        # exception.
        resp = client._connection.api_request(method="GET", path=self.path)
        self._set_properties(api_response=resp)

    def get_variable(self, variable_name, client=None):
        """API call:  get a variable via a ``GET`` request.

        This will return None if the variable doesn't exist::

          >>> from google.cloud import runtimeconfig
          >>> client = runtimeconfig.Client()
          >>> config = client.config('my-config')
          >>> print(config.get_variable('variable-name'))
          <Variable: my-config, variable-name>
          >>> print(config.get_variable('does-not-exist'))
          None

        :type variable_name: str
        :param variable_name: The name of the variable to retrieve.

        :type client: :class:`~google.cloud.runtimeconfig.client.Client`
        :param client:
            (Optional) The client to use.  If not passed, falls back to the
            ``client`` stored on the current config.

        :rtype: :class:`google.cloud.runtimeconfig.variable.Variable` or None
        :returns: The variable object if it exists, otherwise None.
        """
        client = self._require_client(client)
        variable = Variable(config=self, name=variable_name)
        try:
            variable.reload(client=client)
            return variable
        except NotFound:
            return None

    def list_variables(self, page_size=None, page_token=None, client=None):
        """API call:  list variables for this config.

        This only lists variable names, not the values.

        See
        https://cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/list

        :type page_size: int
        :param page_size:
            Optional. The maximum number of variables in each page of results
            from this request. Non-positive values are ignored. Defaults
            to a sensible value set by the API.

        :type page_token: str
        :param page_token:
            Optional. If present, return the next batch of variables, using
            the value, which must correspond to the ``nextPageToken`` value
            returned in the previous response.  Deprecated: use the ``pages``
            property of the returned iterator instead of manually passing
            the token.

        :type client: :class:`~google.cloud.runtimeconfig.client.Client`
        :param client:
            (Optional) The client to use.  If not passed, falls back to the
            ``client`` stored on the current config.

        :rtype: :class:`~google.api_core.page_iterator.Iterator`
        :returns:
            Iterator of :class:`~google.cloud.runtimeconfig.variable.Variable`
            belonging to this project.
        """
        path = "%s/variables" % (self.path,)
        client = self._require_client(client)
        iterator = page_iterator.HTTPIterator(
            client=client,
            api_request=client._connection.api_request,
            path=path,
            item_to_value=_item_to_variable,
            items_key="variables",
            page_token=page_token,
            max_results=page_size,
        )
        iterator._MAX_RESULTS = "pageSize"
        iterator.config = self
        return iterator


def _item_to_variable(iterator, resource):
    """Convert a JSON variable to the native object.

    :type iterator: :class:`~google.api_core.page_iterator.Iterator`
    :param iterator: The iterator that has retrieved the item.

    :type resource: dict
    :param resource: An item to be converted to a variable.

    :rtype: :class:`.Variable`
    :returns: The next variable in the page.
    """
    return Variable.from_api_repr(resource, iterator.config)
