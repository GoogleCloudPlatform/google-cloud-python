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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.appengine.v1",
    manifest={
        "Application",
        "UrlDispatchRule",
    },
)


class Application(proto.Message):
    r"""An Application resource contains the top-level configuration
    of an App Engine application.

    Attributes:
        name (str):
            Full path to the Application resource in the API. Example:
            ``apps/myapp``.

            @OutputOnly
        id (str):
            Identifier of the Application resource. This identifier is
            equivalent to the project ID of the Google Cloud Platform
            project where you want to deploy your application. Example:
            ``myapp``.
        dispatch_rules (MutableSequence[google.cloud.appengine_admin_v1.types.UrlDispatchRule]):
            HTTP path dispatch rules for requests to the
            application that do not explicitly target a
            service or version. Rules are order-dependent.
            Up to 20 dispatch rules can be supported.
        auth_domain (str):
            Google Apps authentication domain that
            controls which users can access this
            application.

            Defaults to open access for any Google Account.
        location_id (str):
            Location from which this application runs. Application
            instances run out of the data centers in the specified
            location, which is also where all of the application's end
            user content is stored.

            Defaults to ``us-central``.

            View the list of `supported
            locations <https://cloud.google.com/appengine/docs/locations>`__.
        code_bucket (str):
            Google Cloud Storage bucket that can be used
            for storing files associated with this
            application. This bucket is associated with the
            application and can be used by the gcloud
            deployment commands.

            @OutputOnly
        default_cookie_expiration (google.protobuf.duration_pb2.Duration):
            Cookie expiration policy for this
            application.
        serving_status (google.cloud.appengine_admin_v1.types.Application.ServingStatus):
            Serving status of this application.
        default_hostname (str):
            Hostname used to reach this application, as
            resolved by App Engine.
            @OutputOnly
        default_bucket (str):
            Google Cloud Storage bucket that can be used
            by this application to store content.

            @OutputOnly
        service_account (str):
            The service account associated with the
            application. This is the app-level default
            identity. If no identity provided during create
            version, Admin API will fallback to this one.
        iap (google.cloud.appengine_admin_v1.types.Application.IdentityAwareProxy):

        gcr_domain (str):
            The Google Container Registry domain used for
            storing managed build docker images for this
            application.
        database_type (google.cloud.appengine_admin_v1.types.Application.DatabaseType):
            The type of the Cloud Firestore or Cloud
            Datastore database associated with this
            application.
        feature_settings (google.cloud.appengine_admin_v1.types.Application.FeatureSettings):
            The feature specific settings to be used in
            the application.
    """

    class ServingStatus(proto.Enum):
        r"""

        Values:
            UNSPECIFIED (0):
                Serving status is unspecified.
            SERVING (1):
                Application is serving.
            USER_DISABLED (2):
                Application has been disabled by the user.
            SYSTEM_DISABLED (3):
                Application has been disabled by the system.
        """

        UNSPECIFIED = 0
        SERVING = 1
        USER_DISABLED = 2
        SYSTEM_DISABLED = 3

    class DatabaseType(proto.Enum):
        r"""

        Values:
            DATABASE_TYPE_UNSPECIFIED (0):
                Database type is unspecified.
            CLOUD_DATASTORE (1):
                Cloud Datastore
            CLOUD_FIRESTORE (2):
                Cloud Firestore Native
            CLOUD_DATASTORE_COMPATIBILITY (3):
                Cloud Firestore in Datastore Mode
        """

        DATABASE_TYPE_UNSPECIFIED = 0
        CLOUD_DATASTORE = 1
        CLOUD_FIRESTORE = 2
        CLOUD_DATASTORE_COMPATIBILITY = 3

    class IdentityAwareProxy(proto.Message):
        r"""Identity-Aware Proxy

        Attributes:
            enabled (bool):
                Whether the serving infrastructure will authenticate and
                authorize all incoming requests.

                If true, the ``oauth2_client_id`` and
                ``oauth2_client_secret`` fields must be non-empty.
            oauth2_client_id (str):
                OAuth2 client ID to use for the
                authentication flow.
            oauth2_client_secret (str):
                OAuth2 client secret to use for the authentication flow.

                For security reasons, this value cannot be retrieved via the
                API. Instead, the SHA-256 hash of the value is returned in
                the ``oauth2_client_secret_sha256`` field.

                @InputOnly
            oauth2_client_secret_sha256 (str):
                Hex-encoded SHA-256 hash of the client
                secret.
                @OutputOnly
        """

        enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        oauth2_client_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        oauth2_client_secret: str = proto.Field(
            proto.STRING,
            number=3,
        )
        oauth2_client_secret_sha256: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class FeatureSettings(proto.Message):
        r"""The feature specific settings to be used in the application.
        These define behaviors that are user configurable.

        Attributes:
            split_health_checks (bool):
                Boolean value indicating if split health checks should be
                used instead of the legacy health checks. At an app.yaml
                level, this means defaulting to 'readiness_check' and
                'liveness_check' values instead of 'health_check' ones. Once
                the legacy 'health_check' behavior is deprecated, and this
                value is always true, this setting can be removed.
            use_container_optimized_os (bool):
                If true, use `Container-Optimized
                OS <https://cloud.google.com/container-optimized-os/>`__
                base image for VMs, rather than a base Debian image.
        """

        split_health_checks: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        use_container_optimized_os: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dispatch_rules: MutableSequence["UrlDispatchRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="UrlDispatchRule",
    )
    auth_domain: str = proto.Field(
        proto.STRING,
        number=6,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    code_bucket: str = proto.Field(
        proto.STRING,
        number=8,
    )
    default_cookie_expiration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=9,
        message=duration_pb2.Duration,
    )
    serving_status: ServingStatus = proto.Field(
        proto.ENUM,
        number=10,
        enum=ServingStatus,
    )
    default_hostname: str = proto.Field(
        proto.STRING,
        number=11,
    )
    default_bucket: str = proto.Field(
        proto.STRING,
        number=12,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=13,
    )
    iap: IdentityAwareProxy = proto.Field(
        proto.MESSAGE,
        number=14,
        message=IdentityAwareProxy,
    )
    gcr_domain: str = proto.Field(
        proto.STRING,
        number=16,
    )
    database_type: DatabaseType = proto.Field(
        proto.ENUM,
        number=17,
        enum=DatabaseType,
    )
    feature_settings: FeatureSettings = proto.Field(
        proto.MESSAGE,
        number=18,
        message=FeatureSettings,
    )


class UrlDispatchRule(proto.Message):
    r"""Rules to match an HTTP request and dispatch that request to a
    service.

    Attributes:
        domain (str):
            Domain name to match against. The wildcard "``*``" is
            supported if specified before a period: "``*.``".

            Defaults to matching all domains: "``*``".
        path (str):
            Pathname within the host. Must start with a "``/``". A
            single "``*``" can be included at the end of the path.

            The sum of the lengths of the domain and path may not exceed
            100 characters.
        service (str):
            Resource ID of a service in this application that should
            serve the matched request. The service must already exist.
            Example: ``default``.
    """

    domain: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
