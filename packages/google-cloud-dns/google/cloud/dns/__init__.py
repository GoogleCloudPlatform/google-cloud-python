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

"""Google Cloud DNS API wrapper.

The main concepts with this API are:

- :class:`~google.cloud.DNS.zone.ManagedZone` represents an collection of
  tables.
- :class:`~google.cloud.DNS.resource_record_set.ResourceRecordSet` represents
  a single resource definition within a zone.
- :class:`~google.cloud.DNS.changes.Changes` represents a set of changes
  (adding/deleting resource record sets) to a zone.
"""

from google.cloud.dns import version

__version__ = version.__version__

from google.cloud.dns.client import Client
from google.cloud.dns.resource_record_set import ResourceRecordSet
from google.cloud.dns.zone import Changes, ManagedZone

SCOPE = Client.SCOPE


__all__ = [
    "__version__",
    "Changes",
    "Client",
    "ManagedZone",
    "ResourceRecordSet",
    "SCOPE",
]
