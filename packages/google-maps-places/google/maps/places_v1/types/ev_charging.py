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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.places.v1",
    manifest={
        "EVConnectorType",
        "EVChargeOptions",
    },
)


class EVConnectorType(proto.Enum):
    r"""See
    http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6872107 for
    additional information/context on EV charging connector types.

    Values:
        EV_CONNECTOR_TYPE_UNSPECIFIED (0):
            Unspecified connector.
        EV_CONNECTOR_TYPE_OTHER (1):
            Other connector types.
        EV_CONNECTOR_TYPE_J1772 (2):
            J1772 type 1 connector.
        EV_CONNECTOR_TYPE_TYPE_2 (3):
            IEC 62196 type 2 connector. Often referred to
            as MENNEKES.
        EV_CONNECTOR_TYPE_CHADEMO (4):
            CHAdeMO type connector.
        EV_CONNECTOR_TYPE_CCS_COMBO_1 (5):
            Combined Charging System (AC and DC). Based
            on SAE.  Type-1 J-1772 connector
        EV_CONNECTOR_TYPE_CCS_COMBO_2 (6):
            Combined Charging System (AC and DC). Based
            on Type-2 Mennekes connector
        EV_CONNECTOR_TYPE_TESLA (7):
            The generic TESLA connector. This is NACS in
            the North America but can be non-NACS in other
            parts of the world (e.g. CCS Combo 2 (CCS2) or
            GB/T). This value is less representative of an
            actual connector type, and more represents the
            ability to charge a Tesla brand vehicle at a
            Tesla owned charging station.
        EV_CONNECTOR_TYPE_UNSPECIFIED_GB_T (8):
            GB/T type corresponds to the GB/T standard in China. This
            type covers all GB_T types.
        EV_CONNECTOR_TYPE_UNSPECIFIED_WALL_OUTLET (9):
            Unspecified wall outlet.
        EV_CONNECTOR_TYPE_NACS (10):
            The North American Charging System (NACS),
            standardized as SAE J3400.
    """

    EV_CONNECTOR_TYPE_UNSPECIFIED = 0
    EV_CONNECTOR_TYPE_OTHER = 1
    EV_CONNECTOR_TYPE_J1772 = 2
    EV_CONNECTOR_TYPE_TYPE_2 = 3
    EV_CONNECTOR_TYPE_CHADEMO = 4
    EV_CONNECTOR_TYPE_CCS_COMBO_1 = 5
    EV_CONNECTOR_TYPE_CCS_COMBO_2 = 6
    EV_CONNECTOR_TYPE_TESLA = 7
    EV_CONNECTOR_TYPE_UNSPECIFIED_GB_T = 8
    EV_CONNECTOR_TYPE_UNSPECIFIED_WALL_OUTLET = 9
    EV_CONNECTOR_TYPE_NACS = 10


class EVChargeOptions(proto.Message):
    r"""Information about the EV Charge Station hosted in Place. Terminology
    follows
    https://afdc.energy.gov/fuels/electricity_infrastructure.html One
    port could charge one car at a time. One port has one or more
    connectors. One station has one or more ports.

    Attributes:
        connector_count (int):
            Number of connectors at this station.
            However, because some ports can have multiple
            connectors but only be able to charge one car at
            a time (e.g.) the number of connectors may be
            greater than the total number of cars which can
            charge simultaneously.
        connector_aggregation (MutableSequence[google.maps.places_v1.types.EVChargeOptions.ConnectorAggregation]):
            A list of EV charging connector aggregations
            that contain connectors of the same type and
            same charge rate.
    """

    class ConnectorAggregation(proto.Message):
        r"""EV charging information grouped by [type, max_charge_rate_kw]. Shows
        EV charge aggregation of connectors that have the same type and max
        charge rate in kw.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            type_ (google.maps.places_v1.types.EVConnectorType):
                The connector type of this aggregation.
            max_charge_rate_kw (float):
                The static max charging rate in kw of each
                connector in the aggregation.
            count (int):
                Number of connectors in this aggregation.
            available_count (int):
                Number of connectors in this aggregation that
                are currently available.

                This field is a member of `oneof`_ ``_available_count``.
            out_of_service_count (int):
                Number of connectors in this aggregation that
                are currently out of service.

                This field is a member of `oneof`_ ``_out_of_service_count``.
            availability_last_update_time (google.protobuf.timestamp_pb2.Timestamp):
                The timestamp when the connector availability
                information in this aggregation was last
                updated.
        """

        type_: "EVConnectorType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="EVConnectorType",
        )
        max_charge_rate_kw: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )
        count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        available_count: int = proto.Field(
            proto.INT32,
            number=4,
            optional=True,
        )
        out_of_service_count: int = proto.Field(
            proto.INT32,
            number=5,
            optional=True,
        )
        availability_last_update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=6,
            message=timestamp_pb2.Timestamp,
        )

    connector_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    connector_aggregation: MutableSequence[ConnectorAggregation] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=ConnectorAggregation,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
