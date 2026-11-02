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
    package="google.devicesandservices.health.v4",
    manifest={
        "DataSource",
    },
)


class DataSource(proto.Message):
    r"""Data Source definition to track the origin of data.

    Each health data point, regardless of the complexity or data
    model (whether a simple step count or a detailed sleep session)
    must retain information about its source of origin (e.g. the
    device or app that collected it).

    Attributes:
        recording_method (google.devicesandservices.health_v4.types.DataSource.RecordingMethod):
            Optional. Captures how the data was recorded.
        device (google.devicesandservices.health_v4.types.DataSource.Device):
            Optional. Captures metadata for raw data
            points originating from devices. We expect this
            data source to be used for data points written
            on device sync.
        application (google.devicesandservices.health_v4.types.DataSource.Application):
            Output only. Captures metadata for the
            application that provided this data.
        platform (google.devicesandservices.health_v4.types.DataSource.Platform):
            Output only. Captures the platform that
            uploaded the data.
    """

    class RecordingMethod(proto.Enum):
        r"""The method by which the data was recorded.

        Values:
            RECORDING_METHOD_UNSPECIFIED (0):
                The recording method is unspecified.
            MANUAL (1):
                The data was manually entered by the user.
            PASSIVELY_MEASURED (2):
                The data was passively measured by a device.
            DERIVED (3):
                The data was derived from other data, e.g.,
                by an algorithm in the backend.
            ACTIVELY_MEASURED (4):
                The data was actively measured by a device.
            UNKNOWN (5):
                The recording method is unknown. This is set
                when the data is uploaded from a third party app
                that does not provide this information.
        """

        RECORDING_METHOD_UNSPECIFIED = 0
        MANUAL = 1
        PASSIVELY_MEASURED = 2
        DERIVED = 3
        ACTIVELY_MEASURED = 4
        UNKNOWN = 5

    class Platform(proto.Enum):
        r"""The platform that uploaded the data.
        Additional values may be added in the future. Clients should be
        prepared to handle unknown values gracefully.

        Values:
            PLATFORM_UNSPECIFIED (0):
                The platform is unspecified.
            FITBIT (1):
                The data was uploaded from Fitbit.
            HEALTH_CONNECT (2):
                The data was uploaded from Health Connect.
            HEALTH_KIT (3):
                The data was uploaded from Health Kit.
            FIT (4):
                The data was uploaded from Google Fit.
            FITBIT_WEB_API (5):
                The data was uploaded from Fitbit legacy Web
                API.
            NEST (6):
                The data was uploaded from Nest devices.
            GOOGLE_WEB_API (7):
                The data was uploaded from Google Health API.
            GOOGLE_PARTNER_INTEGRATION (8):
                The data was uploaded from Google Partner
                Integrations.
        """

        PLATFORM_UNSPECIFIED = 0
        FITBIT = 1
        HEALTH_CONNECT = 2
        HEALTH_KIT = 3
        FIT = 4
        FITBIT_WEB_API = 5
        NEST = 6
        GOOGLE_WEB_API = 7
        GOOGLE_PARTNER_INTEGRATION = 8

    class Device(proto.Message):
        r"""Captures metadata about the device that recorded the
        measurement.

        Attributes:
            form_factor (google.devicesandservices.health_v4.types.DataSource.Device.FormFactor):
                Optional. Captures the form factor of the
                device.
            manufacturer (str):
                Optional. An optional manufacturer of the
                device.
            display_name (str):
                Optional. An optional name for the device.
        """

        class FormFactor(proto.Enum):
            r"""Form factor of the device, e.g. phone, watch, band, etc.

            Values:
                FORM_FACTOR_UNSPECIFIED (0):
                    The form factor is unspecified.
                FITNESS_BAND (1):
                    The device is a fitness band.
                WATCH (2):
                    The device is a watch.
                PHONE (3):
                    The device is a phone.
                RING (4):
                    The device is a ring.
                CHEST_STRAP (5):
                    The device is a chest strap.
                SCALE (6):
                    The device is a scale.
                TABLET (7):
                    The device is a tablet.
                HEAD_MOUNTED (8):
                    The device is a head mounted device.
                SMART_DISPLAY (9):
                    The device is a smart display.
            """

            FORM_FACTOR_UNSPECIFIED = 0
            FITNESS_BAND = 1
            WATCH = 2
            PHONE = 3
            RING = 4
            CHEST_STRAP = 5
            SCALE = 6
            TABLET = 7
            HEAD_MOUNTED = 8
            SMART_DISPLAY = 9

        form_factor: "DataSource.Device.FormFactor" = proto.Field(
            proto.ENUM,
            number=1,
            enum="DataSource.Device.FormFactor",
        )
        manufacturer: str = proto.Field(
            proto.STRING,
            number=2,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class Application(proto.Message):
        r"""Optional metadata for the application that provided this
        data.

        Attributes:
            package_name (str):
                Output only. A unique identifier for the mobile application
                that was the source of the data.

                This is typically the application's package name on Android
                (e.g., ``com.google.fitbit``) or the bundle ID on iOS. This
                field is informational and helps trace data origin. This
                field is system-populated when the data is uploaded from the
                Fitbit mobile application, Health Connect or Health Kit.
            web_client_id (str):
                Output only. The client ID of the application that recorded
                the data.

                This ID is a legacy Fitbit API client ID, which is different
                from a Google OAuth client ID. Example format: ``ABC123``.
                This field is system-populated and used for tracing data
                from legacy Fitbit API integrations. This field is
                system-populated when the data is uploaded from a legacy
                Fitbit API integration.
            google_web_client_id (str):
                Output only. The Google OAuth 2.0 client ID
                of the web application or service that recorded
                the data.

                This is the client ID used during the Google
                OAuth flow to obtain user credentials. This
                field is system-populated when the data is
                uploaded from Google Web API.
        """

        package_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        web_client_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        google_web_client_id: str = proto.Field(
            proto.STRING,
            number=3,
        )

    recording_method: RecordingMethod = proto.Field(
        proto.ENUM,
        number=1,
        enum=RecordingMethod,
    )
    device: Device = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Device,
    )
    application: Application = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Application,
    )
    platform: Platform = proto.Field(
        proto.ENUM,
        number=4,
        enum=Platform,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
