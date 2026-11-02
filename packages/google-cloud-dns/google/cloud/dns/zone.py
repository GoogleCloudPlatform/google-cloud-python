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

"""Define API ManagedZones."""

from google.api_core import page_iterator
from google.cloud._helpers import _rfc3339_to_datetime
from google.cloud.exceptions import NotFound

from google.cloud.dns.changes import Changes
from google.cloud.dns.resource_record_set import ResourceRecordSet


class ManagedZone(object):
    """ManagedZones are containers for DNS resource records.

    See
    https://cloud.google.com/dns/api/v1/managedZones

    :type name: str
    :param name: the name of the zone

    :type dns_name: str
    :param dns_name:
        (Optional) the DNS name of the zone.  If not passed, then calls to
        :meth:`create` will fail.

    :type client: :class:`google.cloud.dns.client.Client`
    :param client: A client which holds credentials and project configuration
                   for the zone (which requires a project).

    :type description: str
    :param description:
        (Optional) the description for the zone.  If not passed, defaults to
        the value of 'dns_name'.
    """

    def __init__(self, name, dns_name=None, client=None, description=None):
        self.name = name
        self.dns_name = dns_name
        self._client = client
        self._properties = {}
        if description is None:
            description = dns_name
        self.description = description

    @classmethod
    def from_api_repr(cls, resource, client):
        """Factory:  construct a zone given its API representation

        :type resource: dict
        :param resource: zone resource representation returned from the API

        :type client: :class:`google.cloud.dns.client.Client`
        :param client: Client which holds credentials and project
                       configuration for the zone.

        :rtype: :class:`google.cloud.dns.zone.ManagedZone`
        :returns: Zone parsed from ``resource``.
        """
        name = resource.get("name")
        dns_name = resource.get("dnsName")
        if name is None or dns_name is None:
            raise KeyError(
                'Resource lacks required identity information:["name"]["dnsName"]'
            )
        zone = cls(name, dns_name, client=client)
        zone._set_properties(resource)
        return zone

    @property
    def project(self):
        """Project bound to the zone.

        :rtype: str
        :returns: the project (derived from the client).
        """
        return self._client.project

    @property
    def path(self):
        """URL path for the zone's APIs.

        :rtype: str
        :returns: the path based on project and dataste name.
        """
        return "/projects/%s/managedZones/%s" % (self.project, self.name)

    @property
    def created(self):
        """Datetime at which the zone was created.

        :rtype: ``datetime.datetime``, or ``NoneType``
        :returns: the creation time (None until set from the server).
        """
        return self._properties.get("creationTime")

    @property
    def name_servers(self):
        """Datetime at which the zone was created.

        :rtype: list of strings, or ``NoneType``.
        :returns: the assigned name servers (None until set from the server).
        """
        return self._properties.get("nameServers")

    @property
    def zone_id(self):
        """ID for the zone resource.

        :rtype: str, or ``NoneType``
        :returns: the ID (None until set from the server).
        """
        return self._properties.get("id")

    @property
    def description(self):
        """Description of the zone.

        :rtype: str, or ``NoneType``
        :returns: The description as set by the user, or None (the default).
        """
        return self._properties.get("description")

    @description.setter
    def description(self, value):
        """Update description of the zone.

        :type value: str
        :param value: (Optional) new description

        :raises: ValueError for invalid value types.
        """
        if not isinstance(value, str) and value is not None:
            raise ValueError("Pass a string, or None")
        self._properties["description"] = value

    @property
    def name_server_set(self):
        """Named set of DNS name servers that all host the same ManagedZones.

        Most users will leave this blank.

        See
        https://cloud.google.com/dns/api/v1/managedZones#nameServerSet

        :rtype: str, or ``NoneType``
        :returns: The name as set by the user, or None (the default).
        """
        return self._properties.get("nameServerSet")

    @name_server_set.setter
    def name_server_set(self, value):
        """Update named set of DNS name servers.

        :type value: str
        :param value: (Optional) new title

        :raises: ValueError for invalid value types.
        """
        if not isinstance(value, str) and value is not None:
            raise ValueError("Pass a string, or None")
        self._properties["nameServerSet"] = value

    def resource_record_set(self, name, record_type, ttl, rrdatas):
        """Construct a resource record set bound to this zone.

        :type name: str
        :param name: Name of the record set.

        :type record_type: str
        :param record_type: RR type

        :type ttl: int
        :param ttl: TTL for the RR, in seconds

        :type rrdatas: list of string
        :param rrdatas: resource data for the RR

        :rtype: :class:`google.cloud.dns.resource_record_set.ResourceRecordSet`
        :returns: a new ``ResourceRecordSet`` instance
        """
        return ResourceRecordSet(name, record_type, ttl, rrdatas, zone=self)

    def changes(self):
        """Construct a change set bound to this zone.

        :rtype: :class:`google.cloud.dns.changes.Changes`
        :returns: a new ``Changes`` instance
        """
        return Changes(zone=self)

    def _require_client(self, client):
        """Check client or verify over-ride.

        :type client: :class:`google.cloud.dns.client.Client`
        :param client:
            (Optional) the client to use.  If not passed, falls back to the
            ``client`` stored on the current zone.

        :rtype: :class:`google.cloud.dns.client.Client`
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
        self.dns_name = cleaned.pop("dnsName", None)
        if "creationTime" in cleaned:
            cleaned["creationTime"] = _rfc3339_to_datetime(cleaned["creationTime"])
        self._properties.update(cleaned)

    def _build_resource(self):
        """Generate a resource for ``create`` or ``update``."""
        resource = {"name": self.name}

        if self.dns_name is not None:
            resource["dnsName"] = self.dns_name

        if self.description is not None:
            resource["description"] = self.description

        if self.name_server_set is not None:
            resource["nameServerSet"] = self.name_server_set

        return resource

    def create(self, client=None):
        """API call:  create the zone via a PUT request

        See
        https://cloud.google.com/dns/api/v1/managedZones/create

        :type client: :class:`google.cloud.dns.client.Client`
        :param client:
            (Optional) the client to use.  If not passed, falls back to the
            ``client`` stored on the current zone.
        """
        client = self._require_client(client)
        path = "/projects/%s/managedZones" % (self.project,)
        api_response = client._connection.api_request(
            method="POST", path=path, data=self._build_resource()
        )
        self._set_properties(api_response)

    def exists(self, client=None):
        """API call:  test for the existence of the zone via a GET request

        See
        https://cloud.google.com/dns/api/v1/managedZones/get

        :type client: :class:`google.cloud.dns.client.Client`
        :param client:
            (Optional) the client to use.  If not passed, falls back to the
            ``client`` stored on the current zone.

        :rtype: bool
        :returns: Boolean indicating existence of the managed zone.
        """
        client = self._require_client(client)

        try:
            client._connection.api_request(method="GET", path=self.path)
        except NotFound:
            return False
        else:
            return True

    def reload(self, client=None):
        """API call:  refresh zone properties via a GET request

        See
        https://cloud.google.com/dns/api/v1/managedZones/get

        :type client: :class:`google.cloud.dns.client.Client`
        :param client:
            (Optional) the client to use.  If not passed, falls back to the
            ``client`` stored on the current zone.
        """
        client = self._require_client(client)

        api_response = client._connection.api_request(method="GET", path=self.path)
        self._set_properties(api_response)

    def delete(self, client=None):
        """API call:  delete the zone via a DELETE request

        See
        https://cloud.google.com/dns/api/v1/managedZones/delete

        :type client: :class:`google.cloud.dns.client.Client`
        :param client:
            (Optional) the client to use.  If not passed, falls back to the
            ``client`` stored on the current zone.
        """
        client = self._require_client(client)
        client._connection.api_request(method="DELETE", path=self.path)

    def list_resource_record_sets(self, max_results=None, page_token=None, client=None):
        """List resource record sets for this zone.

        See
        https://cloud.google.com/dns/api/v1/resourceRecordSets/list

        :type max_results: int
        :param max_results: Optional. The maximum number of resource record
                            sets to return. Defaults to a sensible value
                            set by the API.

        :type page_token: str
        :param page_token: Optional. If present, return the next batch of
            resource record sets, using the value, which must correspond to
            the ``nextPageToken`` value returned in the previous response.
            Deprecated: use the ``pages`` property of the returned iterator
            instead of manually passing the token.

        :type client: :class:`google.cloud.dns.client.Client`
        :param client:
            (Optional) the client to use.  If not passed, falls back to the
            ``client`` stored on the current zone.

        :rtype: :class:`~google.api_core.page_iterator.Iterator`
        :returns: Iterator of :class:`~.resource_record_set.ResourceRecordSet`
                  belonging to this zone.
        """
        client = self._require_client(client)
        path = "/projects/%s/managedZones/%s/rrsets" % (self.project, self.name)
        iterator = page_iterator.HTTPIterator(
            client=client,
            api_request=client._connection.api_request,
            path=path,
            item_to_value=_item_to_resource_record_set,
            items_key="rrsets",
            page_token=page_token,
            max_results=max_results,
        )
        iterator.zone = self
        return iterator

    def list_changes(self, max_results=None, page_token=None, client=None):
        """List change sets for this zone.

        See
        https://cloud.google.com/dns/api/v1/resourceRecordSets/list

        :type max_results: int
        :param max_results: Optional. The maximum number of change sets
            to return. Defaults to a sensible value set by the API.

        :type page_token: str
        :param page_token: Optional. If present, return the next batch of
            change sets, using the value, which must correspond to the
            ``nextPageToken`` value returned in the previous response.
            Deprecated: use the ``pages`` property of the returned iterator
            instead of manually passing the token.

        :type client: :class:`google.cloud.dns.client.Client`
        :param client:
            (Optional) the client to use.  If not passed, falls back to the
            ``client`` stored on the current zone.

        :rtype: :class:`~google.api_core.page_iterator.Iterator`
        :returns: Iterator of :class:`~.changes.Changes`
                  belonging to this zone.
        """
        client = self._require_client(client)
        path = "/projects/%s/managedZones/%s/changes" % (self.project, self.name)
        iterator = page_iterator.HTTPIterator(
            client=client,
            api_request=client._connection.api_request,
            path=path,
            item_to_value=_item_to_changes,
            items_key="changes",
            page_token=page_token,
            max_results=max_results,
        )
        iterator.zone = self
        return iterator


def _item_to_resource_record_set(iterator, resource):
    """Convert a JSON resource record set value to the native object.

    :type iterator: :class:`~google.api_core.page_iterator.Iterator`
    :param iterator: The iterator that has retrieved the item.

    :type resource: dict
    :param resource: An item to be converted to a resource record set.

    :rtype: :class:`~.resource_record_set.ResourceRecordSet`
    :returns: The next resource record set in the page.
    """
    return ResourceRecordSet.from_api_repr(resource, iterator.zone)


def _item_to_changes(iterator, resource):
    """Convert a JSON "changes" value to the native object.

    :type iterator: :class:`~google.api_core.page_iterator.Iterator`
    :param iterator: The iterator that has retrieved the item.

    :type resource: dict
    :param resource: An item to be converted to a "changes".

    :rtype: :class:`.Changes`
    :returns: The next "changes" in the page.
    """
    return Changes.from_api_repr(resource, iterator.zone)
