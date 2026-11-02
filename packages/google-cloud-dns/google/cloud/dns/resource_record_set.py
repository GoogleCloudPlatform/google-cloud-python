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


class ResourceRecordSet(object):
    """ResourceRecordSets are DNS resource records.

    RRS are owned by a :class:`google.cloud.dns.zone.ManagedZone` instance.

    See
    https://cloud.google.com/dns/api/v1/resourceRecordSets

    :type name: str
    :param name: the name of the record set.

    :type record_type: str
    :param record_type: the RR type of the zone.

    :type ttl: int
    :param ttl: TTL (in seconds) for caching the record sets.

    :type rrdatas: list of string
    :param rrdatas: one or more lines containing the resource data.

    :type zone: :class:`google.cloud.dns.zone.ManagedZone`
    :param zone: A zone which holds one or more record sets.
    """

    def __init__(self, name, record_type, ttl, rrdatas, zone):
        self.name = name
        self.record_type = record_type
        self.ttl = ttl
        self.rrdatas = rrdatas
        self.zone = zone

    @classmethod
    def from_api_repr(cls, resource, zone):
        """Factory:  construct a record set given its API representation

        :type resource: dict
        :param resource: record sets representation returned from the API

        :type zone: :class:`google.cloud.dns.zone.ManagedZone`
        :param zone: A zone which holds one or more record sets.

        :rtype: :class:`google.cloud.dns.zone.ResourceRecordSet`
        :returns: RRS parsed from ``resource``.
        """
        name = resource["name"]
        record_type = resource["type"]
        ttl = int(resource["ttl"])
        rrdatas = resource["rrdatas"]
        return cls(name, record_type, ttl, rrdatas, zone=zone)
