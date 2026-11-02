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

import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.shopping.merchant.datasources.v1beta",
    manifest={
        "FileInput",
    },
)


class FileInput(proto.Message):
    r"""The data specific for file data sources. This field is empty
    for other data source inputs.

    Attributes:
        fetch_settings (google.shopping.merchant_datasources_v1beta.types.FileInput.FetchSettings):
            Optional. Fetch details to deliver the data source. It
            contains settings for ``FETCH`` and ``GOOGLE_SHEETS`` file
            input types. The required fields vary based on the frequency
            of fetching.
        file_name (str):
            Optional. The file name of the data source. Required for
            ``UPLOAD`` file input type.
        file_input_type (google.shopping.merchant_datasources_v1beta.types.FileInput.FileInputType):
            Output only. The type of file input.
    """

    class FileInputType(proto.Enum):
        r"""The method of file delivery.

        Values:
            FILE_INPUT_TYPE_UNSPECIFIED (0):
                File input type unspecified.
            UPLOAD (1):
                The file is uploaded through SFTP, Google
                Cloud Storage or manually in the Merchant
                Center.
            FETCH (2):
                The file is fetched from the configured
                [fetch_uri][google.shopping.merchant.datasources.v1beta.FileInput.FetchSettings.fetch_uri].
            GOOGLE_SHEETS (3):
                The file is fetched from Google Sheets specified in the
                [fetch_uri][google.shopping.merchant.datasources.v1beta.FileInput.FetchSettings.fetch_uri].
        """

        FILE_INPUT_TYPE_UNSPECIFIED = 0
        UPLOAD = 1
        FETCH = 2
        GOOGLE_SHEETS = 3

    class FetchSettings(proto.Message):
        r"""Fetch details to deliver the data source.

        Attributes:
            enabled (bool):
                Optional. Enables or pauses the fetch
                schedule.
            day_of_month (int):
                Optional. The day of the month when the data
                source file should be fetched (1-31). This field
                can only be set for monthly frequency.
            time_of_day (google.type.timeofday_pb2.TimeOfDay):
                Optional. The hour of the day when the data
                source file should be fetched. Minutes and
                seconds are not supported and will be ignored.
            day_of_week (google.type.dayofweek_pb2.DayOfWeek):
                Optional. The day of the week when the data
                source file should be fetched. This field can
                only be set for weekly frequency.
            time_zone (str):
                Optional. `Time zone <https://cldr.unicode.org>`__ used for
                schedule. UTC by default. For example,
                "America/Los_Angeles".
            frequency (google.shopping.merchant_datasources_v1beta.types.FileInput.FetchSettings.Frequency):
                Required. The frequency describing fetch
                schedule.
            fetch_uri (str):
                Optional. The URL where the data source file
                can be fetched. Google Merchant Center supports
                automatic scheduled uploads using the HTTP,
                HTTPS or SFTP protocols, so the value will need
                to be a valid link using one of those three
                protocols. Immutable for Google Sheets files.
            username (str):
                Optional. An optional user name for
                [fetch_uri][google.shopping.merchant.datasources.v1beta.FileInput.FetchSettings.fetch_uri].
                Used for `submitting data sources through
                SFTP <https://support.google.com/merchants/answer/13813117>`__.
            password (str):
                Optional. An optional password for
                [fetch_uri][google.shopping.merchant.datasources.v1beta.FileInput.FetchSettings.fetch_uri].
                Used for `submitting data sources through
                SFTP <https://support.google.com/merchants/answer/13813117>`__.
        """

        class Frequency(proto.Enum):
            r"""The required fields vary based on the frequency of fetching. For a
            monthly fetch schedule, [day of
            month][google.shopping.content.bundles.DataSources.FileInput.FetchSchedule.day_of_month]
            and [hour of
            day][google.shopping.content.bundles.DataSources.FileInput.FetchSchedule.time_of_day]
            are required. For a weekly fetch schedule, [day of
            week][google.shopping.content.bundles.DataSources.FileInput.FetchSchedule.day_of_week]
            and [hour of
            day][google.shopping.content.bundles.DataSources.FileInput.FetchSchedule.time_of_day]
            are required. For a daily fetch schedule, only an [hour of
            day][google.shopping.content.bundles.DataSources.FileInput.FetchSchedule.time_of_day]
            is required.

            Values:
                FREQUENCY_UNSPECIFIED (0):
                    Frequency unspecified.
                FREQUENCY_DAILY (1):
                    The fetch happens every day.
                FREQUENCY_WEEKLY (2):
                    The fetch happens every week.
                FREQUENCY_MONTHLY (3):
                    The fetch happens every month.
            """

            FREQUENCY_UNSPECIFIED = 0
            FREQUENCY_DAILY = 1
            FREQUENCY_WEEKLY = 2
            FREQUENCY_MONTHLY = 3

        enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        day_of_month: int = proto.Field(
            proto.INT32,
            number=2,
        )
        time_of_day: timeofday_pb2.TimeOfDay = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timeofday_pb2.TimeOfDay,
        )
        day_of_week: dayofweek_pb2.DayOfWeek = proto.Field(
            proto.ENUM,
            number=4,
            enum=dayofweek_pb2.DayOfWeek,
        )
        time_zone: str = proto.Field(
            proto.STRING,
            number=5,
        )
        frequency: "FileInput.FetchSettings.Frequency" = proto.Field(
            proto.ENUM,
            number=6,
            enum="FileInput.FetchSettings.Frequency",
        )
        fetch_uri: str = proto.Field(
            proto.STRING,
            number=7,
        )
        username: str = proto.Field(
            proto.STRING,
            number=8,
        )
        password: str = proto.Field(
            proto.STRING,
            number=9,
        )

    fetch_settings: FetchSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=FetchSettings,
    )
    file_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    file_input_type: FileInputType = proto.Field(
        proto.ENUM,
        number=3,
        enum=FileInputType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
