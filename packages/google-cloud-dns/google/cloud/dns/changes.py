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

"""Define API ResourceRecordSets."""

from google.cloud._helpers import _rfc3339_to_datetime
from google.cloud.exceptions import NotFound

from google.cloud.dns.resource_record_set import ResourceRecordSet


class Changes(object):
    """Changes are bundled additions / deletions of DNS resource records.

    Changes are owned by a :class:`google.cloud.dns.zone.ManagedZone` instance.

    See
    https://cloud.google.com/dns/api/v1/changes

    :type zone: :class:`google.cloud.dns.zone.ManagedZone`
    :param zone: A zone which holds one or more record sets.
    """

    def __init__(self, zone):
        self.zone = zone
        self._properties = {}
        self._additions = self._deletions = ()

    @classmethod
    def from_api_repr(cls, resource, zone):
        """Factory:  construct a change set given its API representation

        :type resource: dict
        :param resource: change set representation returned from the API.

        :type zone: :class:`google.cloud.dns.zone.ManagedZone`
        :param zone: A zone which holds zero or more change sets.

        :rtype: :class:`google.cloud.dns.changes.Changes`
        :returns: RRS parsed from ``resource``.
        """
        changes = cls(zone=zone)
        changes._set_properties(resource)
        return changes

    def _set_properties(self, resource):
        """Helper method for :meth:`from_api_repr`, :meth:`create`, etc.

        :type resource: dict
        :param resource: change set representation returned from the API.
        """
        resource = resource.copy()
        self._additions = tuple(
            [
                ResourceRecordSet.from_api_repr(added_res, self.zone)
                for added_res in resource.pop("additions", ())
            ]
        )
        self._deletions = tuple(
            [
                ResourceRecordSet.from_api_repr(added_res, self.zone)
                for added_res in resource.pop("deletions", ())
            ]
        )
        self._properties = resource

    @property
    def path(self):
        """URL path for change set APIs.

        :rtype: str
        :returns: the path based on project, zone, and change set names.
        """
        return "/projects/%s/managedZones/%s/changes/%s" % (
            self.zone.project,
            self.zone.name,
            self.name,
        )

    @property
    def name(self):
        """Name of the change set.

        :rtype: str or ``NoneType``
        :returns: Name, as set by the back-end, or None.
        """
        return self._properties.get("id")

    @name.setter
    def name(self, value):
        """Update name of the change set.

        :type value: str
        :param value: New name for the changeset.
        """
        if not isinstance(value, str):
            raise ValueError("Pass a string")
        self._properties["id"] = value

    @property
    def status(self):
        """Status of the change set.

        :rtype: str or ``NoneType``
        :returns: Status, as set by the back-end, or None.
        """
        return self._properties.get("status")

    @property
    def started(self):
        """Time when the change set was started.

        :rtype: ``datetime.datetime`` or ``NoneType``
        :returns: Time, as set by the back-end, or None.
        """
        stamp = self._properties.get("startTime")
        if stamp is not None:
            return _rfc3339_to_datetime(stamp)

    @property
    def additions(self):
        """Resource record sets to be added to the zone.

        :rtype: sequence of
                :class:`google.cloud.dns.resource_record_set.ResourceRecordSet`.
        :returns: record sets appended via :meth:`add_record_set`.
        """
        return self._additions

    @property
    def deletions(self):
        """Resource record sets to be deleted from the zone.

        :rtype: sequence of
                :class:`google.cloud.dns.resource_record_set.ResourceRecordSet`.
        :returns: record sets appended via :meth:`delete_record_set`.
        """
        return self._deletions

    def add_record_set(self, record_set):
        """Append a record set to the 'additions' for the change set.

        :type record_set:
            :class:`google.cloud.dns.resource_record_set.ResourceRecordSet`
        :param record_set: the record set to append.

        :raises: ``ValueError`` if ``record_set`` is not of the required type.
        """
        if not isinstance(record_set, ResourceRecordSet):
            raise ValueError("Pass a ResourceRecordSet")
        self._additions += (record_set,)

    def delete_record_set(self, record_set):
        """Append a record set to the 'deletions' for the change set.

        :type record_set:
            :class:`google.cloud.dns.resource_record_set.ResourceRecordSet`
        :param record_set: the record set to append.

        :raises: ``ValueError`` if ``record_set`` is not of the required type.
        """
        if not isinstance(record_set, ResourceRecordSet):
            raise ValueError("Pass a ResourceRecordSet")
        self._deletions += (record_set,)

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
            client = self.zone._client
        return client

    def _build_resource(self):
        """Generate a resource for ``create``."""
        additions = [
            {
                "name": added.name,
                "type": added.record_type,
                "ttl": str(added.ttl),
                "rrdatas": added.rrdatas,
            }
            for added in self.additions
        ]

        deletions = [
            {
                "name": deleted.name,
                "type": deleted.record_type,
                "ttl": str(deleted.ttl),
                "rrdatas": deleted.rrdatas,
            }
            for deleted in self.deletions
        ]

        return {"additions": additions, "deletions": deletions}

    def create(self, client=None):
        """API call:  create the change set via a POST request.

        See
        https://cloud.google.com/dns/api/v1/changes/create

        :type client: :class:`google.cloud.dns.client.Client`
        :param client:
            (Optional) the client to use.  If not passed, falls back to the
            ``client`` stored on the current zone.
        """
        if len(self.additions) == 0 and len(self.deletions) == 0:
            raise ValueError("No record sets added or deleted")
        client = self._require_client(client)
        path = "/projects/%s/managedZones/%s/changes" % (
            self.zone.project,
            self.zone.name,
        )
        api_response = client._connection.api_request(
            method="POST", path=path, data=self._build_resource()
        )
        self._set_properties(api_response)

    def exists(self, client=None):
        """API call: test for the existence of the change set via a GET request.

        See
        https://cloud.google.com/dns/api/v1/changes/get

        :type client: :class:`google.cloud.dns.client.Client`
        :param client:
            (Optional) the client to use.  If not passed, falls back to the
            ``client`` stored on the current zone.

        :rtype: bool
        :returns: Boolean indicating existence of the changes.
        """
        client = self._require_client(client)
        try:
            client._connection.api_request(
                method="GET", path=self.path, query_params={"fields": "id"}
            )
        except NotFound:
            return False
        else:
            return True

    def reload(self, client=None):
        """API call:  refresh zone properties via a GET request.

        See
        https://cloud.google.com/dns/api/v1/changes/get

        :type client: :class:`google.cloud.dns.client.Client`
        :param client:
            (Optional) the client to use.  If not passed, falls back to the
            ``client`` stored on the current zone.
        """
        client = self._require_client(client)

        api_response = client._connection.api_request(method="GET", path=self.path)
        self._set_properties(api_response)
