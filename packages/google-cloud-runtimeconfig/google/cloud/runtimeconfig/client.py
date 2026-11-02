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

"""Client for interacting with the Google Cloud RuntimeConfig API."""

import google.api_core.client_options
from google.cloud.client import ClientWithProject

from google.cloud.runtimeconfig._http import Connection
from google.cloud.runtimeconfig.config import Config


class Client(ClientWithProject):
    """Client to bundle configuration needed for API requests.

    :type project: str
    :param project:
        (Optional) The project which the client acts on behalf of.  If not
        passed, falls back to the default inferred from the environment.

    :type credentials: :class:`~google.auth.credentials.Credentials`
    :param credentials: (Optional) The OAuth2 Credentials to use for this
                        client. If not passed (and if no ``_http`` object is
                        passed), falls back to the default inferred from the
                        environment.

    :type _http: :class:`~requests.Session`
    :param _http: (Optional) HTTP object to make requests. Can be any object
                  that defines ``request()`` with the same interface as
                  :meth:`requests.Session.request`. If not passed, an
                  ``_http`` object is created that is bound to the
                  ``credentials`` for the current object.
                  This parameter should be considered private, and could
                  change in the future.

    :type client_info: :class:`~google.api_core.client_info.ClientInfo`
    :param client_info:
        The client info used to send a user-agent string along with API
        requests. If ``None``, then default info will be used. Generally,
        you only need to set this if you're developing your own library
        or partner tool.
    :type client_options: :class:`~google.api_core.client_options.ClientOptions`
        or :class:`dict`
    :param client_options: (Optional) Client options used to set user options
        on the client. API Endpoint should be set through client_options.
    """

    SCOPE = ("https://www.googleapis.com/auth/cloudruntimeconfig",)
    """The scopes required for authenticating as a RuntimeConfig consumer."""

    def __init__(
        self,
        project=None,
        credentials=None,
        _http=None,
        client_info=None,
        client_options=None,
    ):
        super(Client, self).__init__(
            project=project, credentials=credentials, _http=_http
        )

        kw_args = {"client_info": client_info}
        if client_options:
            if isinstance(client_options, dict):
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint
                kw_args["api_endpoint"] = api_endpoint

        self._connection = Connection(self, **kw_args)

    def config(self, config_name):
        """Factory constructor for config object.

        .. note::
          This will not make an HTTP request; it simply instantiates
          a config object owned by this client.

        :type config_name: str
        :param config_name: The name of the config to be instantiated.

        :rtype: :class:`google.cloud.runtimeconfig.config.Config`
        :returns: The config object created.
        """
        return Config(client=self, name=config_name)
