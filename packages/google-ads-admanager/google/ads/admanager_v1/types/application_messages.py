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

from google.ads.admanager_v1.types import application_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Application",
    },
)


class Application(proto.Message):
    r"""An application that has been added to or "claimed" by the
    network to be used for targeting purposes. These mobile apps can
    come from various app stores.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``Application``.
            Format:
            ``networks/{network_code}/applications/{application_id}``
        display_name (str):
            Required. The display name of the
            application.

            This field is a member of `oneof`_ ``_display_name``.
        app_store_id (str):
            Optional. The app store ID of the app to
            claim.

            This field is a member of `oneof`_ ``_app_store_id``.
        app_stores (MutableSequence[google.ads.admanager_v1.types.ApplicationStoreEnum.ApplicationStore]):
            Optional. The app stores the application
            belongs to. This attribute is mutable to allow
            for third party app store linking.
        archived (bool):
            Output only. The archival status of the application.

            When true, an application cannot be targeted and will not
            serve ads, regardless of its ``status``.

            This field is a member of `oneof`_ ``_archived``.
        app_store_display_name (str):
            Output only. The name of the application on
            the app store.

            This field is a member of `oneof`_ ``_app_store_display_name``.
        application_code (str):
            Output only. The application code used to
            identify the app in the SDK.
            Note that the UI refers to this as "App ID".

            This field is a member of `oneof`_ ``_application_code``.
        developer (str):
            Output only. The name of the developer of the
            application.

            This field is a member of `oneof`_ ``_developer``.
        platform (google.ads.admanager_v1.types.ApplicationPlatformEnum.ApplicationPlatform):
            Output only. The platform the application
            runs on.

            This field is a member of `oneof`_ ``_platform``.
        free (bool):
            Output only. Whether the application is free
            on the app store it belongs to.

            This field is a member of `oneof`_ ``_free``.
        download_url (str):
            Output only. The download URL of the
            application on the app store it belongs to.

            This field is a member of `oneof`_ ``_download_url``.
        approval_status (google.ads.admanager_v1.types.ApplicationApprovalStatusEnum.ApplicationApprovalStatus):
            Output only. The approval status for the
            application.

            This field is a member of `oneof`_ ``_approval_status``.
        webview_claiming_status (google.ads.admanager_v1.types.WebviewClaimingStatusEnum.WebviewClaimingStatus):
            Output only. The webview claiming status for
            the application.

            This field is a member of `oneof`_ ``_webview_claiming_status``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    app_store_id: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    app_stores: MutableSequence[
        application_enums.ApplicationStoreEnum.ApplicationStore
    ] = proto.RepeatedField(
        proto.ENUM,
        number=7,
        enum=application_enums.ApplicationStoreEnum.ApplicationStore,
    )
    archived: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    app_store_display_name: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    application_code: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    developer: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    platform: application_enums.ApplicationPlatformEnum.ApplicationPlatform = (
        proto.Field(
            proto.ENUM,
            number=12,
            optional=True,
            enum=application_enums.ApplicationPlatformEnum.ApplicationPlatform,
        )
    )
    free: bool = proto.Field(
        proto.BOOL,
        number=13,
        optional=True,
    )
    download_url: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    approval_status: application_enums.ApplicationApprovalStatusEnum.ApplicationApprovalStatus = proto.Field(
        proto.ENUM,
        number=15,
        optional=True,
        enum=application_enums.ApplicationApprovalStatusEnum.ApplicationApprovalStatus,
    )
    webview_claiming_status: application_enums.WebviewClaimingStatusEnum.WebviewClaimingStatus = proto.Field(
        proto.ENUM,
        number=16,
        optional=True,
        enum=application_enums.WebviewClaimingStatusEnum.WebviewClaimingStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
