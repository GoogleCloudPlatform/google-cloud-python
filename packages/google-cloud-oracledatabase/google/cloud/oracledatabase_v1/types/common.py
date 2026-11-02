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
    package="google.cloud.oracledatabase.v1",
    manifest={
        "ComputeModel",
        "CustomerContact",
        "IdentityConnector",
        "DataCollectionOptionsCommon",
    },
)


class ComputeModel(proto.Enum):
    r"""The compute model of the Exadata Infrastructure, VM Cluster
    and Autonomous Database.

    Values:
        COMPUTE_MODEL_UNSPECIFIED (0):
            Unspecified compute model.
        COMPUTE_MODEL_ECPU (1):
            Abstract measure of compute resources. ECPUs
            are based on the number of cores elastically
            allocated from a pool of compute and storage
            servers.
        COMPUTE_MODEL_OCPU (2):
            Physical measure of compute resources. OCPUs
            are based on the physical core of a processor.
    """

    COMPUTE_MODEL_UNSPECIFIED = 0
    COMPUTE_MODEL_ECPU = 1
    COMPUTE_MODEL_OCPU = 2


class CustomerContact(proto.Message):
    r"""The CustomerContact reference as defined by Oracle.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/CustomerContact

    Attributes:
        email (str):
            Required. The email address used by Oracle to
            send notifications regarding databases and
            infrastructure.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )


class IdentityConnector(proto.Message):
    r"""The identity connector details which will allow OCI to
    securely access the resources in the customer project.

    Attributes:
        service_agent_email (str):
            Output only. A google managed service account on which
            customers can grant roles to access resources in the
            customer project. Example:
            ``p176944527254-55-75119d87fd8f@gcp-sa-oci.iam.gserviceaccount.com``
        connection_state (google.cloud.oracledatabase_v1.types.IdentityConnector.ConnectionState):
            Output only. The connection state of the
            identity connector.
    """

    class ConnectionState(proto.Enum):
        r"""The various connection states of the
        WorkloadIdentityPoolConnection.

        Values:
            CONNECTION_STATE_UNSPECIFIED (0):
                Default unspecified value.
            CONNECTED (1):
                The identity pool connection is connected.
            PARTIALLY_CONNECTED (2):
                The identity pool connection is partially
                connected.
            DISCONNECTED (3):
                The identity pool connection is disconnected.
            UNKNOWN (4):
                The identity pool connection is in an unknown
                state.
        """

        CONNECTION_STATE_UNSPECIFIED = 0
        CONNECTED = 1
        PARTIALLY_CONNECTED = 2
        DISCONNECTED = 3
        UNKNOWN = 4

    service_agent_email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_state: ConnectionState = proto.Field(
        proto.ENUM,
        number=2,
        enum=ConnectionState,
    )


class DataCollectionOptionsCommon(proto.Message):
    r"""Data collection options for diagnostics.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/DataCollectionOptions

    Attributes:
        is_diagnostics_events_enabled (bool):
            Optional. Indicates whether to enable data
            collection for diagnostics.
        is_health_monitoring_enabled (bool):
            Optional. Indicates whether to enable health
            monitoring.
        is_incident_logs_enabled (bool):
            Optional. Indicates whether to enable
            incident logs and trace collection.
    """

    is_diagnostics_events_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    is_health_monitoring_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    is_incident_logs_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
