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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "CreateSipTrunkRequest",
        "DeleteSipTrunkRequest",
        "ListSipTrunksRequest",
        "ListSipTrunksResponse",
        "GetSipTrunkRequest",
        "UpdateSipTrunkRequest",
        "SipTrunk",
        "Connection",
        "SipHostname",
        "ProbeDetails",
    },
)


class CreateSipTrunkRequest(proto.Message):
    r"""The request message for
    [SipTrunks.CreateSipTrunk][google.cloud.dialogflow.v2beta1.SipTrunks.CreateSipTrunk].

    Attributes:
        parent (str):
            Required. The location to create a SIP trunk for. Format:
            ``projects/<Project ID>/locations/<Location ID>``.
        sip_trunk (google.cloud.dialogflow_v2beta1.types.SipTrunk):
            Required. The SIP trunk to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sip_trunk: "SipTrunk" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SipTrunk",
    )


class DeleteSipTrunkRequest(proto.Message):
    r"""The request message for
    [SipTrunks.DeleteSipTrunk][google.cloud.dialogflow.v2beta1.SipTrunks.DeleteSipTrunk].

    Attributes:
        name (str):
            Required. The name of the SIP trunk to delete. Format:
            ``projects/<Project ID>/locations/<Location ID>/sipTrunks/<SipTrunk ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSipTrunksRequest(proto.Message):
    r"""The request message for
    [SipTrunks.ListSipTrunks][google.cloud.dialogflow.v2beta1.SipTrunks.ListSipTrunks].

    Attributes:
        parent (str):
            Required. The location to list SIP trunks from. Format:
            ``projects/<Project ID>/locations/<Location ID>``.
        page_size (int):
            Optional. The maximum number of items to
            return in a single page. By default 100 and at
            most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListSipTrunksResponse(proto.Message):
    r"""The response message for
    [SipTrunks.ListSipTrunks][google.cloud.dialogflow.v2beta1.SipTrunks.ListSipTrunks].

    Attributes:
        sip_trunks (MutableSequence[google.cloud.dialogflow_v2beta1.types.SipTrunk]):
            The list of SIP trunks.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    sip_trunks: MutableSequence["SipTrunk"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SipTrunk",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetSipTrunkRequest(proto.Message):
    r"""The request message for
    [SipTrunks.GetSipTrunk][google.cloud.dialogflow.v2beta1.SipTrunks.GetSipTrunk].

    Attributes:
        name (str):
            Required. The name of the SIP trunk to delete. Format:
            ``projects/<Project ID>/locations/<Location ID>/sipTrunks/<SipTrunk ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSipTrunkRequest(proto.Message):
    r"""The request message for
    [SipTrunks.UpdateSipTrunk][google.cloud.dialogflow.v2beta1.SipTrunks.UpdateSipTrunk].

    Attributes:
        sip_trunk (google.cloud.dialogflow_v2beta1.types.SipTrunk):
            Required. The SipTrunk to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields
            get updated. If the mask is not present, all
            fields will be updated.
    """

    sip_trunk: "SipTrunk" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SipTrunk",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class SipTrunk(proto.Message):
    r"""SipTrunk is the resource that represents a SIP trunk to
    connect to Google Telephony platform SIP trunking service.

    Attributes:
        name (str):
            Identifier. The unique identifier of the SIP trunk. Format:
            ``projects/<Project ID>/locations/<Location ID>/sipTrunks/<SipTrunk ID>``.
        expected_hostname (MutableSequence[str]):
            Required. The expected hostnames in the peer
            certificate from partner that is used for TLS
            authentication.
        connections (MutableSequence[google.cloud.dialogflow_v2beta1.types.Connection]):
            Output only. Connections of the SIP trunk.
        display_name (str):
            Optional. Human readable alias for this
            trunk.
        peer_hostnames (MutableSequence[google.cloud.dialogflow_v2beta1.types.SipHostname]):
            Required. Peer hostnames of the SIP trunk.
        google_root_cert_file (google.cloud.dialogflow_v2beta1.types.SipTrunk.GoogleRootCertFile):
            Optional. The root certificate file to use
            for this SIP trunk.
    """

    class GoogleRootCertFile(proto.Enum):
        r"""The type of Google root certificate file used for mTLS.

        Values:
            CERT_FILE_UNSPECIFIED (0):
                Unspecified root certificate file.
            EXTERNAL_PRIVATE_CA (5):
                Use external private CA.
        """

        CERT_FILE_UNSPECIFIED = 0
        EXTERNAL_PRIVATE_CA = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expected_hostname: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    connections: MutableSequence["Connection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Connection",
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    peer_hostnames: MutableSequence["SipHostname"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="SipHostname",
    )
    google_root_cert_file: GoogleRootCertFile = proto.Field(
        proto.ENUM,
        number=9,
        enum=GoogleRootCertFile,
    )


class Connection(proto.Message):
    r"""Represents a connection for SIP Trunk.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        connection_id (str):
            Output only. The unique identifier of the SIP
            Trunk connection.
        state (google.cloud.dialogflow_v2beta1.types.Connection.State):
            Output only. State of the connection.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the connection status
            changed.

            This field is a member of `oneof`_ ``_update_time``.
        error_details (google.cloud.dialogflow_v2beta1.types.Connection.ErrorDetails):
            Output only. The error details for the
            connection. Only populated when authentication
            errors occur.

            This field is a member of `oneof`_ ``_error_details``.
    """

    class State(proto.Enum):
        r"""The state of Sip Trunk connection.

        Values:
            STATE_UNSPECIFIED (0):
                SIP Trunk connection state is Not specified.
            CONNECTED (1):
                SIP Trunk connection is connected.
            DISCONNECTED (2):
                SIP Trunk connection is disconnected.
            AUTHENTICATION_FAILED (3):
                SIP Trunk connection has authentication
                error.
            KEEPALIVE (4):
                SIP Trunk connection is keepalive.
        """

        STATE_UNSPECIFIED = 0
        CONNECTED = 1
        DISCONNECTED = 2
        AUTHENTICATION_FAILED = 3
        KEEPALIVE = 4

    class CertificateState(proto.Enum):
        r"""The state of Sip Trunk certificate authentication.

        Values:
            CERTIFICATE_STATE_UNSPECIFIED (0):
                Certificate state is not specified.
            CERTIFICATE_VALID (1):
                Certificate is valid.
            CERTIFICATE_INVALID (2):
                Catch all for any error not specified.
            CERTIFICATE_EXPIRED (3):
                Certificate leaf node has expired.
            CERTIFICATE_HOSTNAME_NOT_FOUND (4):
                There is no hostname defined to authenticate
                in SipTrunkingServer.
            CERTIFICATE_UNAUTHENTICATED (5):
                No path found from the leaf certificate to
                any root.
            CERTIFICATE_TRUST_STORE_NOT_FOUND (6):
                Trust store does not exist.
            CERTIFICATE_HOSTNAME_INVALID_FORMAT (7):
                Hostname has invalid format.
            CERTIFICATE_QUOTA_EXCEEDED (8):
                Certificate has exhausted its quota.
        """

        CERTIFICATE_STATE_UNSPECIFIED = 0
        CERTIFICATE_VALID = 1
        CERTIFICATE_INVALID = 2
        CERTIFICATE_EXPIRED = 3
        CERTIFICATE_HOSTNAME_NOT_FOUND = 4
        CERTIFICATE_UNAUTHENTICATED = 5
        CERTIFICATE_TRUST_STORE_NOT_FOUND = 6
        CERTIFICATE_HOSTNAME_INVALID_FORMAT = 7
        CERTIFICATE_QUOTA_EXCEEDED = 8

    class ErrorDetails(proto.Message):
        r"""The error details of Sip Trunk connection authentication.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            certificate_state (google.cloud.dialogflow_v2beta1.types.Connection.CertificateState):
                Output only. The status of the certificate
                authentication.

                This field is a member of `oneof`_ ``_certificate_state``.
            error_message (str):
                The error message provided from SIP trunking
                auth service

                This field is a member of `oneof`_ ``_error_message``.
        """

        certificate_state: "Connection.CertificateState" = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum="Connection.CertificateState",
        )
        error_message: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )

    connection_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    error_details: ErrorDetails = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=ErrorDetails,
    )


class SipHostname(proto.Message):
    r"""Represents a peer hostname for SIP Trunk.

    Attributes:
        peer_hostname (str):
            Required. Peer hostname name.
        enabled_sip_ping (bool):
            Output only. Peer hostname enabled for SIP
            ping.
        ping_interval (google.protobuf.duration_pb2.Duration):
            Output only. How often the sip ping should
            occur.
        peer_socket_address (str):
            Output only. The peer_socket address of the partner SBC
            pinged.
        probe_details (google.cloud.dialogflow_v2beta1.types.ProbeDetails):
            Output only. The details from the options
            probe.
        connection_state (google.cloud.dialogflow_v2beta1.types.SipHostname.ConnectionState):
            Output only. State of the connection.
        error_details (google.cloud.dialogflow_v2beta1.types.SipHostname.HostnameErrorDetails):
            Output only. The error details for the
            connection. Only populated when authentication
            errors occur.
    """

    class ConnectionState(proto.Enum):
        r"""The state of SBC hostname connection.

        Values:
            CONNECTION_STATE_UNSPECIFIED (0):
                SBC hostname connection state is Not
                specified.
            CONNECTED (1):
                SBC hostname connection is connected.
            DISCONNECTED (2):
                SBC hostname connection is disconnected.
            AUTHENTICATION_FAILED (3):
                SBC hostname connection has authentication
                error.
            KEEPALIVE (4):
                SBC hostname connection is keepalive.
        """

        CONNECTION_STATE_UNSPECIFIED = 0
        CONNECTED = 1
        DISCONNECTED = 2
        AUTHENTICATION_FAILED = 3
        KEEPALIVE = 4

    class HostnameCertificateState(proto.Enum):
        r"""The state of Sip Trunk certificate authentication.

        Values:
            HOSTNAME_CERTIFICATE_STATE_UNSPECIFIED (0):
                Certificate state is not specified.
            VALID (1):
                Certificate is valid.
            INVALID (2):
                Catch all for any error not specified.
            EXPIRED (3):
                Certificate leaf node has expired.
            HOSTNAME_NOT_FOUND (4):
                There is no hostname defined to authenticate
                in SipTrunkingServer.
            UNAUTHENTICATED (5):
                No path found from the leaf certificate to
                any root.
            TRUST_STORE_NOT_FOUND (6):
                Trust store does not exist.
            HOSTNAME_INVALID_FORMAT (7):
                Hostname has invalid format.
            QUOTA_EXCEEDED (8):
                Certificate has exhausted its quota.
        """

        HOSTNAME_CERTIFICATE_STATE_UNSPECIFIED = 0
        VALID = 1
        INVALID = 2
        EXPIRED = 3
        HOSTNAME_NOT_FOUND = 4
        UNAUTHENTICATED = 5
        TRUST_STORE_NOT_FOUND = 6
        HOSTNAME_INVALID_FORMAT = 7
        QUOTA_EXCEEDED = 8

    class HostnameErrorDetails(proto.Message):
        r"""The error details of Sip Trunk hostnameconnection
        authentication.

        Attributes:
            certificate_state (google.cloud.dialogflow_v2beta1.types.SipHostname.HostnameCertificateState):
                Output only. The status of the certificate
                authentication.
            error_message (str):
                Output only. The error message provided from
                SIP trunking auth service
        """

        certificate_state: "SipHostname.HostnameCertificateState" = proto.Field(
            proto.ENUM,
            number=1,
            enum="SipHostname.HostnameCertificateState",
        )
        error_message: str = proto.Field(
            proto.STRING,
            number=2,
        )

    peer_hostname: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enabled_sip_ping: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    ping_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    peer_socket_address: str = proto.Field(
        proto.STRING,
        number=4,
    )
    probe_details: "ProbeDetails" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ProbeDetails",
    )
    connection_state: ConnectionState = proto.Field(
        proto.ENUM,
        number=6,
        enum=ConnectionState,
    )
    error_details: HostnameErrorDetails = proto.Field(
        proto.MESSAGE,
        number=7,
        message=HostnameErrorDetails,
    )


class ProbeDetails(proto.Message):
    r"""The probe details of Sip Trunk peer hostname.

    Attributes:
        options_latency (google.protobuf.duration_pb2.Duration):
            Output only. Duration between OPTIONS send
            and OPTIONS 200 received.
        probe_status (google.cloud.dialogflow_v2beta1.types.ProbeDetails.ProbeStatus):
            Output only. Result of the probe.
        init_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the options probe was
            started.
    """

    class ProbeStatus(proto.Enum):
        r"""The status of InitiateSipOptionsPing to peer hostname.

        Values:
            PROBE_STATUS_UNSPECIFIED (0):
                Peer hostname ping state is not specified.
            PROBE_STATUS_SUCCESS (1):
                Peer hostname ping succeeded.
            PROBE_STATUS_FAILED (2):
                Peer hostname ping failed.
        """

        PROBE_STATUS_UNSPECIFIED = 0
        PROBE_STATUS_SUCCESS = 1
        PROBE_STATUS_FAILED = 2

    options_latency: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    probe_status: ProbeStatus = proto.Field(
        proto.ENUM,
        number=2,
        enum=ProbeStatus,
    )
    init_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
