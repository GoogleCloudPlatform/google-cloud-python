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
    package="google.cloud.scheduler.v1beta1",
    manifest={
        "HttpMethod",
        "HttpTarget",
        "AppEngineHttpTarget",
        "PubsubTarget",
        "AppEngineRouting",
        "OAuthToken",
        "OidcToken",
    },
)


class HttpMethod(proto.Enum):
    r"""The HTTP method used to execute the job.

    Values:
        HTTP_METHOD_UNSPECIFIED (0):
            HTTP method unspecified. Defaults to POST.
        POST (1):
            HTTP POST
        GET (2):
            HTTP GET
        HEAD (3):
            HTTP HEAD
        PUT (4):
            HTTP PUT
        DELETE (5):
            HTTP DELETE
        PATCH (6):
            HTTP PATCH
        OPTIONS (7):
            HTTP OPTIONS
    """

    HTTP_METHOD_UNSPECIFIED = 0
    POST = 1
    GET = 2
    HEAD = 3
    PUT = 4
    DELETE = 5
    PATCH = 6
    OPTIONS = 7


class HttpTarget(proto.Message):
    r"""Http target. The job will be pushed to the job handler by means of
    an HTTP request via an
    [http_method][google.cloud.scheduler.v1beta1.HttpTarget.http_method]
    such as HTTP POST, HTTP GET, etc. The job is acknowledged by means
    of an HTTP response code in the range [200 - 299]. A failure to
    receive a response constitutes a failed execution. For a redirected
    request, the response returned by the redirected request is
    considered.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uri (str):
            Required. The full URI path that the request will be sent
            to. This string must begin with either "http://" or
            "https://". Some examples of valid values for
            [uri][google.cloud.scheduler.v1beta1.HttpTarget.uri] are:
            ``http://acme.com`` and ``https://acme.com/sales:8080``.
            Cloud Scheduler will encode some characters for safety and
            compatibility. The maximum allowed URL length is 2083
            characters after encoding.
        http_method (google.cloud.scheduler_v1beta1.types.HttpMethod):
            Which HTTP method to use for the request.
        headers (MutableMapping[str, str]):
            The user can specify HTTP request headers to send with the
            job's HTTP request. This map contains the header field names
            and values. Repeated headers are not supported, but a header
            value can contain commas. These headers represent a subset
            of the headers that will accompany the job's HTTP request.
            Some HTTP request headers will be ignored or replaced. A
            partial list of headers that will be ignored or replaced is
            below:

            - Host: This will be computed by Cloud Scheduler and derived
              from [uri][google.cloud.scheduler.v1beta1.HttpTarget.uri].

            - ``Content-Length``: This will be computed by Cloud
              Scheduler.
            - ``User-Agent``: This will be set to
              ``"Google-Cloud-Scheduler"``.
            - ``X-Google-*``: Google internal use only.
            - ``X-AppEngine-*``: Google internal use only.
            - ``X-CloudScheduler``: This header will be set to true.
            - ``X-CloudScheduler-JobName``: This header will contain the
              job name.
            - ``X-CloudScheduler-ScheduleTime``: For Cloud Scheduler
              jobs specified in the unix-cron format, this header will
              contain the job schedule as an offset of UTC parsed
              according to RFC3339.

            The total size of headers must be less than 80KB.
        body (bytes):
            HTTP request body. A request body is allowed only if the
            HTTP method is POST, PUT, or PATCH. It is an error to set
            body on a job with an incompatible
            [HttpMethod][google.cloud.scheduler.v1beta1.HttpMethod].
        oauth_token (google.cloud.scheduler_v1beta1.types.OAuthToken):
            If specified, an `OAuth
            token <https://developers.google.com/identity/protocols/OAuth2>`__
            will be generated and attached as an ``Authorization``
            header in the HTTP request.

            This type of authorization should generally only be used
            when calling Google APIs hosted on \*.googleapis.com.

            This field is a member of `oneof`_ ``authorization_header``.
        oidc_token (google.cloud.scheduler_v1beta1.types.OidcToken):
            If specified, an
            `OIDC <https://developers.google.com/identity/protocols/OpenIDConnect>`__
            token will be generated and attached as an ``Authorization``
            header in the HTTP request.

            This type of authorization can be used for many scenarios,
            including calling Cloud Run, or endpoints where you intend
            to validate the token yourself.

            This field is a member of `oneof`_ ``authorization_header``.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    http_method: "HttpMethod" = proto.Field(
        proto.ENUM,
        number=2,
        enum="HttpMethod",
    )
    headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    body: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    oauth_token: "OAuthToken" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="authorization_header",
        message="OAuthToken",
    )
    oidc_token: "OidcToken" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="authorization_header",
        message="OidcToken",
    )


class AppEngineHttpTarget(proto.Message):
    r"""App Engine target. The job will be pushed to a job handler by means
    of an HTTP request via an
    [http_method][google.cloud.scheduler.v1beta1.AppEngineHttpTarget.http_method]
    such as HTTP POST, HTTP GET, etc. The job is acknowledged by means
    of an HTTP response code in the range [200 - 299]. Error 503 is
    considered an App Engine system error instead of an application
    error. Requests returning error 503 will be retried regardless of
    retry configuration and not counted against retry counts. Any other
    response code, or a failure to receive a response before the
    deadline, constitutes a failed attempt.

    Attributes:
        http_method (google.cloud.scheduler_v1beta1.types.HttpMethod):
            The HTTP method to use for the request. PATCH
            and OPTIONS are not permitted.
        app_engine_routing (google.cloud.scheduler_v1beta1.types.AppEngineRouting):
            App Engine Routing setting for the job.
        relative_uri (str):
            The relative URI.

            The relative URL must begin with "/" and must be a valid
            HTTP relative URL. It can contain a path, query string
            arguments, and ``#`` fragments. If the relative URL is
            empty, then the root path "/" will be used. No spaces are
            allowed, and the maximum length allowed is 2083 characters.
        headers (MutableMapping[str, str]):
            HTTP request headers.

            This map contains the header field names and values. Headers
            can be set when the job is created.

            Cloud Scheduler sets some headers to default values:

            - ``User-Agent``: By default, this header is
              ``"AppEngine-Google; (+http://code.google.com/appengine)"``.
              This header can be modified, but Cloud Scheduler will
              append
              ``"AppEngine-Google; (+http://code.google.com/appengine)"``
              to the modified ``User-Agent``.
            - ``X-CloudScheduler``: This header will be set to true.
            - ``X-CloudScheduler-JobName``: This header will contain the
              job name.
            - ``X-CloudScheduler-ScheduleTime``: For Cloud Scheduler
              jobs specified in the unix-cron format, this header will
              contain the job schedule as an offset of UTC parsed
              according to RFC3339.

            If the job has an
            [body][google.cloud.scheduler.v1beta1.AppEngineHttpTarget.body],
            Cloud Scheduler sets the following headers:

            - ``Content-Type``: By default, the ``Content-Type`` header
              is set to ``"application/octet-stream"``. The default can
              be overridden by explictly setting ``Content-Type`` to a
              particular media type when the job is created. For
              example, ``Content-Type`` can be set to
              ``"application/json"``.
            - ``Content-Length``: This is computed by Cloud Scheduler.
              This value is output only. It cannot be changed.

            The headers below are output only. They cannot be set or
            overridden:

            - ``X-Google-*``: For Google internal use only.
            - ``X-AppEngine-*``: For Google internal use only.

            In addition, some App Engine headers, which contain
            job-specific information, are also be sent to the job
            handler.
        body (bytes):
            Body.

            HTTP request body. A request body is allowed only if the
            HTTP method is POST or PUT. It will result in invalid
            argument error to set a body on a job with an incompatible
            [HttpMethod][google.cloud.scheduler.v1beta1.HttpMethod].
    """

    http_method: "HttpMethod" = proto.Field(
        proto.ENUM,
        number=1,
        enum="HttpMethod",
    )
    app_engine_routing: "AppEngineRouting" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AppEngineRouting",
    )
    relative_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    body: bytes = proto.Field(
        proto.BYTES,
        number=5,
    )


class PubsubTarget(proto.Message):
    r"""Pub/Sub target. The job will be delivered by publishing a
    message to the given Pub/Sub topic.

    Attributes:
        topic_name (str):
            Required. The name of the Cloud Pub/Sub topic to which
            messages will be published when a job is delivered. The
            topic name must be in the same format as required by
            Pub/Sub's
            `PublishRequest.name <https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#publishrequest>`__,
            for example ``projects/PROJECT_ID/topics/TOPIC_ID``.

            The topic must be in the same project as the Cloud Scheduler
            job.
        data (bytes):
            The message payload for PubsubMessage.

            Pubsub message must contain either non-empty
            data, or at least one attribute.
        attributes (MutableMapping[str, str]):
            Attributes for PubsubMessage.

            Pubsub message must contain either non-empty
            data, or at least one attribute.
    """

    topic_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


class AppEngineRouting(proto.Message):
    r"""App Engine Routing.

    For more information about services, versions, and instances see `An
    Overview of App
    Engine <https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine>`__,
    `Microservices Architecture on Google App
    Engine <https://cloud.google.com/appengine/docs/python/microservices-on-app-engine>`__,
    `App Engine Standard request
    routing <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__,
    and `App Engine Flex request
    routing <https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed>`__.

    Attributes:
        service (str):
            App service.

            By default, the job is sent to the service which
            is the default service when the job is
            attempted.
        version (str):
            App version.

            By default, the job is sent to the version which
            is the default version when the job is
            attempted.
        instance (str):
            App instance.

            By default, the job is sent to an instance which is
            available when the job is attempted.

            Requests can only be sent to a specific instance if `manual
            scaling is used in App Engine
            Standard <https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine?#scaling_types_and_instance_classes>`__.
            App Engine Flex does not support instances. For more
            information, see `App Engine Standard request
            routing <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__
            and `App Engine Flex request
            routing <https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed>`__.
        host (str):
            Output only. The host that the job is sent to.

            For more information about how App Engine requests are
            routed, see
            `here <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__.

            The host is constructed as:

            - ``host = [application_domain_name]``\
              ``| [service] + '.' + [application_domain_name]``\
              ``| [version] + '.' + [application_domain_name]``\
              ``| [version_dot_service]+ '.' + [application_domain_name]``\
              ``| [instance] + '.' + [application_domain_name]``\
              ``| [instance_dot_service] + '.' + [application_domain_name]``\
              ``| [instance_dot_version] + '.' + [application_domain_name]``\
              ``| [instance_dot_version_dot_service] + '.' + [application_domain_name]``

            - ``application_domain_name`` = The domain name of the app,
              for example .appspot.com, which is associated with the
              job's project ID.

            - ``service =``
              [service][google.cloud.scheduler.v1beta1.AppEngineRouting.service]

            - ``version =``
              [version][google.cloud.scheduler.v1beta1.AppEngineRouting.version]

            - ``version_dot_service =``
              [version][google.cloud.scheduler.v1beta1.AppEngineRouting.version]
              ``+ '.' +``
              [service][google.cloud.scheduler.v1beta1.AppEngineRouting.service]

            - ``instance =``
              [instance][google.cloud.scheduler.v1beta1.AppEngineRouting.instance]

            - ``instance_dot_service =``
              [instance][google.cloud.scheduler.v1beta1.AppEngineRouting.instance]
              ``+ '.' +``
              [service][google.cloud.scheduler.v1beta1.AppEngineRouting.service]

            - ``instance_dot_version =``
              [instance][google.cloud.scheduler.v1beta1.AppEngineRouting.instance]
              ``+ '.' +``
              [version][google.cloud.scheduler.v1beta1.AppEngineRouting.version]

            - ``instance_dot_version_dot_service =``
              [instance][google.cloud.scheduler.v1beta1.AppEngineRouting.instance]
              ``+ '.' +``
              [version][google.cloud.scheduler.v1beta1.AppEngineRouting.version]
              ``+ '.' +``
              [service][google.cloud.scheduler.v1beta1.AppEngineRouting.service]

            If
            [service][google.cloud.scheduler.v1beta1.AppEngineRouting.service]
            is empty, then the job will be sent to the service which is
            the default service when the job is attempted.

            If
            [version][google.cloud.scheduler.v1beta1.AppEngineRouting.version]
            is empty, then the job will be sent to the version which is
            the default version when the job is attempted.

            If
            [instance][google.cloud.scheduler.v1beta1.AppEngineRouting.instance]
            is empty, then the job will be sent to an instance which is
            available when the job is attempted.

            If
            [service][google.cloud.scheduler.v1beta1.AppEngineRouting.service],
            [version][google.cloud.scheduler.v1beta1.AppEngineRouting.version],
            or
            [instance][google.cloud.scheduler.v1beta1.AppEngineRouting.instance]
            is invalid, then the job will be sent to the default version
            of the default service when the job is attempted.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=3,
    )
    host: str = proto.Field(
        proto.STRING,
        number=4,
    )


class OAuthToken(proto.Message):
    r"""Contains information needed for generating an `OAuth
    token <https://developers.google.com/identity/protocols/OAuth2>`__.
    This type of authorization should generally only be used when
    calling Google APIs hosted on \*.googleapis.com.

    Attributes:
        service_account_email (str):
            `Service account
            email <https://cloud.google.com/iam/docs/service-accounts>`__
            to be used for generating OAuth token. The service account
            must be within the same project as the job. The caller must
            have iam.serviceAccounts.actAs permission for the service
            account.
        scope (str):
            OAuth scope to be used for generating OAuth
            access token. If not specified,
            "https://www.googleapis.com/auth/cloud-platform"
            will be used.
    """

    service_account_email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OidcToken(proto.Message):
    r"""Contains information needed for generating an `OpenID Connect
    token <https://developers.google.com/identity/protocols/OpenIDConnect>`__.
    This type of authorization can be used for many scenarios, including
    calling Cloud Run, or endpoints where you intend to validate the
    token yourself.

    Attributes:
        service_account_email (str):
            `Service account
            email <https://cloud.google.com/iam/docs/service-accounts>`__
            to be used for generating OIDC token. The service account
            must be within the same project as the job. The caller must
            have iam.serviceAccounts.actAs permission for the service
            account.
        audience (str):
            Audience to be used when generating OIDC
            token. If not specified, the URI specified in
            target will be used.
    """

    service_account_email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    audience: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
