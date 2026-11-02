# Copyright 2015 Google LLC
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

"""Client for interacting with the Google Cloud DNS API."""

from google.api_core import client_options as client_options_mod
from google.api_core import page_iterator
from google.cloud.client import ClientWithProject

from google.cloud.dns._http import Connection
from google.cloud.dns.zone import ManagedZone


class Client(ClientWithProject):
    """Client to bundle configuration needed for API requests.

    :type project: str
    :param project: the project which the client acts on behalf of. Will be
                    passed when creating a zone.  If not passed,
                    falls back to the default inferred from the environment.

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

    SCOPE = ("https://www.googleapis.com/auth/ndev.clouddns.readwrite",)
    """The scopes required for authenticating as a Cloud DNS consumer."""

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

        kwargs = {"client_info": client_info}
        if client_options:
            if isinstance(client_options, dict):
                client_options = client_options_mod.from_dict(client_options)

            if client_options.api_endpoint:
                kwargs["api_endpoint"] = client_options.api_endpoint

        self._connection = Connection(self, **kwargs)

    def quotas(self):
        """Return DNS quotas for the project associated with this client.

        See
        https://cloud.google.com/dns/api/v1/projects/get

        :rtype: mapping
        :returns: keys for the mapping correspond to those of the ``quota``
                  sub-mapping of the project resource. ``kind`` is stripped
                  from the results.
        """
        path = "/projects/%s" % (self.project,)
        resp = self._connection.api_request(method="GET", path=path)

        quotas = resp["quota"]
        # Remove the key "kind"
        # https://cloud.google.com/dns/docs/reference/v1/projects#resource
        quotas.pop("kind", None)
        if "whitelistedKeySpecs" in quotas:
            # whitelistedKeySpecs is a list of dicts that represent keyspecs
            # Remove "kind" here as well
            for key_spec in quotas["whitelistedKeySpecs"]:
                key_spec.pop("kind", None)

        return quotas

    def list_zones(self, max_results=None, page_token=None):
        """List zones for the project associated with this client.

        See
        https://cloud.google.com/dns/api/v1/managedZones/list

        :type max_results: int
        :param max_results: maximum number of zones to return, If not
                            passed, defaults to a value set by the API.

        :type page_token: str
        :param page_token: Optional. If present, return the next batch of
            zones, using the value, which must correspond to the
            ``nextPageToken`` value returned in the previous response.
            Deprecated: use the ``pages`` property of the returned iterator
            instead of manually passing the token.

        :rtype: :class:`~google.api_core.page_iterator.Iterator`
        :returns: Iterator of :class:`~google.cloud.dns.zone.ManagedZone`
                  belonging to this project.
        """
        path = "/projects/%s/managedZones" % (self.project,)
        return page_iterator.HTTPIterator(
            client=self,
            api_request=self._connection.api_request,
            path=path,
            item_to_value=_item_to_zone,
            items_key="managedZones",
            page_token=page_token,
            max_results=max_results,
        )

    def zone(self, name, dns_name=None, description=None):
        """Construct a zone bound to this client.

        :type name: str
        :param name: Name of the zone.

        :type dns_name: str
        :param dns_name:
            (Optional) DNS name of the zone.  If not passed, then calls to
            :meth:`zone.create` will fail.

        :type description: str
        :param description:
            (Optional) the description for the zone.  If not passed, defaults
            to the value of 'dns_name'.

        :rtype: :class:`google.cloud.dns.zone.ManagedZone`
        :returns: a new ``ManagedZone`` instance.
        """
        return ManagedZone(name, dns_name, client=self, description=description)


def _item_to_zone(iterator, resource):
    """Convert a JSON managed zone to the native object.

    :type iterator: :class:`~google.api_core.page_iterator.Iterator`
    :param iterator: The iterator that has retrieved the item.

    :type resource: dict
    :param resource: An item to be converted to a managed zone.

    :rtype: :class:`.ManagedZone`
    :returns: The next managed zone in the page.
    """
    return ManagedZone.from_api_repr(resource, iterator.client)
