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
    package="google.api.apikeys.v2",
    manifest={
        "Key",
        "Restrictions",
        "BrowserKeyRestrictions",
        "ServerKeyRestrictions",
        "AndroidKeyRestrictions",
        "AndroidApplication",
        "IosKeyRestrictions",
        "ApiTarget",
    },
)


class Key(proto.Message):
    r"""The representation of a key managed by the API Keys API.

    Attributes:
        name (str):
            Output only. The resource name of the key. The ``name`` has
            the form:
            ``projects/<PROJECT_NUMBER>/locations/global/keys/<KEY_ID>``.
            For example:
            ``projects/123456867718/locations/global/keys/b7ff1f9f-8275-410a-94dd-3855ee9b5dd2``

            NOTE: Key is a global resource; hence the only supported
            value for location is ``global``.
        uid (str):
            Output only. Unique id in UUID4 format.
        display_name (str):
            Human-readable display name of this key that
            you can modify. The maximum length is 63
            characters.
        key_string (str):
            Output only. An encrypted and signed value held by this key.
            This field can be accessed only through the ``GetKeyString``
            method.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. A timestamp identifying the time
            this key was originally created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. A timestamp identifying the time
            this key was last updated.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. A timestamp when this key was
            deleted. If the resource is not deleted, this
            must be empty.
        annotations (MutableMapping[str, str]):
            Annotations is an unstructured key-value map
            stored with a policy that may be set by external
            tools to store and retrieve arbitrary metadata.
            They are not queryable and should be preserved
            when modifying objects.
        restrictions (google.cloud.api_keys_v2.types.Restrictions):
            Key restrictions.
        etag (str):
            Output only. A checksum computed by the
            server based on the current value of the Key
            resource. This may be sent on update and delete
            requests to ensure the client has an up-to-date
            value before proceeding. See
            https://google.aip.dev/154.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    key_string: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    restrictions: "Restrictions" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Restrictions",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
    )


class Restrictions(proto.Message):
    r"""Describes the restrictions on the key.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        browser_key_restrictions (google.cloud.api_keys_v2.types.BrowserKeyRestrictions):
            The HTTP referrers (websites) that are
            allowed to use the key.

            This field is a member of `oneof`_ ``client_restrictions``.
        server_key_restrictions (google.cloud.api_keys_v2.types.ServerKeyRestrictions):
            The IP addresses of callers that are allowed
            to use the key.

            This field is a member of `oneof`_ ``client_restrictions``.
        android_key_restrictions (google.cloud.api_keys_v2.types.AndroidKeyRestrictions):
            The Android apps that are allowed to use the
            key.

            This field is a member of `oneof`_ ``client_restrictions``.
        ios_key_restrictions (google.cloud.api_keys_v2.types.IosKeyRestrictions):
            The iOS apps that are allowed to use the key.

            This field is a member of `oneof`_ ``client_restrictions``.
        api_targets (MutableSequence[google.cloud.api_keys_v2.types.ApiTarget]):
            A restriction for a specific service and
            optionally one or more specific methods.
            Requests are allowed if they match any of these
            restrictions. If no restrictions are specified,
            all targets are allowed.
    """

    browser_key_restrictions: "BrowserKeyRestrictions" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="client_restrictions",
        message="BrowserKeyRestrictions",
    )
    server_key_restrictions: "ServerKeyRestrictions" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="client_restrictions",
        message="ServerKeyRestrictions",
    )
    android_key_restrictions: "AndroidKeyRestrictions" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="client_restrictions",
        message="AndroidKeyRestrictions",
    )
    ios_key_restrictions: "IosKeyRestrictions" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="client_restrictions",
        message="IosKeyRestrictions",
    )
    api_targets: MutableSequence["ApiTarget"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ApiTarget",
    )


class BrowserKeyRestrictions(proto.Message):
    r"""The HTTP referrers (websites) that are allowed to use the
    key.

    Attributes:
        allowed_referrers (MutableSequence[str]):
            A list of regular expressions for the
            referrer URLs that are allowed to make API calls
            with this key.
    """

    allowed_referrers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ServerKeyRestrictions(proto.Message):
    r"""The IP addresses of callers that are allowed to use the key.

    Attributes:
        allowed_ips (MutableSequence[str]):
            A list of the caller IP addresses that are
            allowed to make API calls with this key.
    """

    allowed_ips: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class AndroidKeyRestrictions(proto.Message):
    r"""The Android apps that are allowed to use the key.

    Attributes:
        allowed_applications (MutableSequence[google.cloud.api_keys_v2.types.AndroidApplication]):
            A list of Android applications that are
            allowed to make API calls with this key.
    """

    allowed_applications: MutableSequence["AndroidApplication"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AndroidApplication",
    )


class AndroidApplication(proto.Message):
    r"""Identifier of an Android application for key use.

    Attributes:
        sha1_fingerprint (str):
            The SHA1 fingerprint of the application. For
            example, both sha1 formats are acceptable :
            DA:39:A3:EE:5E:6B:4B:0D:32:55:BF:EF:95:60:18:90:AF:D8:07:09
            or DA39A3EE5E6B4B0D3255BFEF95601890AFD80709.
            Output format is the latter.
        package_name (str):
            The package name of the application.
    """

    sha1_fingerprint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    package_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class IosKeyRestrictions(proto.Message):
    r"""The iOS apps that are allowed to use the key.

    Attributes:
        allowed_bundle_ids (MutableSequence[str]):
            A list of bundle IDs that are allowed when
            making API calls with this key.
    """

    allowed_bundle_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ApiTarget(proto.Message):
    r"""A restriction for a specific service and optionally one or
    multiple specific methods. Both fields are case insensitive.

    Attributes:
        service (str):
            The service for this restriction. It should be the canonical
            service name, for example: ``translate.googleapis.com``. You
            can use
            ```gcloud services list`` </sdk/gcloud/reference/services/list>`__
            to get a list of services that are enabled in the project.
        methods (MutableSequence[str]):
            Optional. List of one or more methods that can be called. If
            empty, all methods for the service are allowed. A wildcard
            (\*) can be used as the last symbol. Valid examples:
            ``google.cloud.translate.v2.TranslateService.GetSupportedLanguage``
            ``TranslateText`` ``Get*`` ``translate.googleapis.com.Get*``
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    methods: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
