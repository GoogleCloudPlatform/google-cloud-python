# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
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
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "ExternalExposure",
    },
)


class ExternalExposure(proto.Message):
    r"""Details about the externally exposed resource associated with
    the finding.

    Attributes:
        private_ip_address (str):
            Private IP address of the exposed endpoint.
        private_port (str):
            Port number associated with private IP
            address.
        exposed_service (str):
            The name and version of the service, for
            example, "Jupyter Notebook 6.14.0".
        public_ip_address (str):
            Public IP address of the exposed endpoint.
        public_port (str):
            Public port number of the exposed endpoint.
        exposed_endpoint (str):
            The resource which is running the exposed
            service, for example,
            "//compute.googleapis.com/projects/{project-id}/zones/{zone}/instances/{instance}.”
        load_balancer_firewall_policy (str):
            The full resource name of the load balancer
            firewall policy, for example,
            "//compute.googleapis.com/projects/{project-id}/global/firewallPolicies/{policy-name}".
        service_firewall_policy (str):
            The full resource name of the firewall policy
            of the exposed service, for example,
            "//compute.googleapis.com/projects/{project-id}/global/firewallPolicies/{policy-name}".
        forwarding_rule (str):
            The full resource name of the forwarding
            rule, for example,
            "//compute.googleapis.com/projects/{project-id}/global/forwardingRules/{forwarding-rule-name}".
        backend_service (str):
            The full resource name of load balancer
            backend service, for example,
            "//compute.googleapis.com/projects/{project-id}/global/backendServices/{name}".
        instance_group (str):
            The full resource name of the instance group,
            for example,
            "//compute.googleapis.com/projects/{project-id}/global/instanceGroups/{name}".
        network_endpoint_group (str):
            The full resource name of the network
            endpoint group, for example,
            "//compute.googleapis.com/projects/{project-id}/global/networkEndpointGroups/{name}".
    """

    private_ip_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_port: str = proto.Field(
        proto.STRING,
        number=2,
    )
    exposed_service: str = proto.Field(
        proto.STRING,
        number=3,
    )
    public_ip_address: str = proto.Field(
        proto.STRING,
        number=4,
    )
    public_port: str = proto.Field(
        proto.STRING,
        number=5,
    )
    exposed_endpoint: str = proto.Field(
        proto.STRING,
        number=6,
    )
    load_balancer_firewall_policy: str = proto.Field(
        proto.STRING,
        number=7,
    )
    service_firewall_policy: str = proto.Field(
        proto.STRING,
        number=8,
    )
    forwarding_rule: str = proto.Field(
        proto.STRING,
        number=9,
    )
    backend_service: str = proto.Field(
        proto.STRING,
        number=10,
    )
    instance_group: str = proto.Field(
        proto.STRING,
        number=11,
    )
    network_endpoint_group: str = proto.Field(
        proto.STRING,
        number=12,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
