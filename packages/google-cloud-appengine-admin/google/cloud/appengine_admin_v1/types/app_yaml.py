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
        "AuthFailAction",
        "LoginRequirement",
        "SecurityLevel",
        "ApiConfigHandler",
        "ErrorHandler",
        "UrlMap",
        "StaticFilesHandler",
        "ScriptHandler",
        "ApiEndpointHandler",
        "HealthCheck",
        "ReadinessCheck",
        "LivenessCheck",
        "Library",
    },
)


class AuthFailAction(proto.Enum):
    r"""Actions to take when the user is not logged in.

    Values:
        AUTH_FAIL_ACTION_UNSPECIFIED (0):
            Not specified. ``AUTH_FAIL_ACTION_REDIRECT`` is assumed.
        AUTH_FAIL_ACTION_REDIRECT (1):
            Redirects user to "accounts.google.com". The
            user is redirected back to the application URL
            after signing in or creating an account.
        AUTH_FAIL_ACTION_UNAUTHORIZED (2):
            Rejects request with a ``401`` HTTP status code and an error
            message.
    """

    AUTH_FAIL_ACTION_UNSPECIFIED = 0
    AUTH_FAIL_ACTION_REDIRECT = 1
    AUTH_FAIL_ACTION_UNAUTHORIZED = 2


class LoginRequirement(proto.Enum):
    r"""Methods to restrict access to a URL based on login status.

    Values:
        LOGIN_UNSPECIFIED (0):
            Not specified. ``LOGIN_OPTIONAL`` is assumed.
        LOGIN_OPTIONAL (1):
            Does not require that the user is signed in.
        LOGIN_ADMIN (2):
            If the user is not signed in, the ``auth_fail_action`` is
            taken. In addition, if the user is not an administrator for
            the application, they are given an error message regardless
            of ``auth_fail_action``. If the user is an administrator,
            the handler proceeds.
        LOGIN_REQUIRED (3):
            If the user has signed in, the handler proceeds normally.
            Otherwise, the auth_fail_action is taken.
    """

    LOGIN_UNSPECIFIED = 0
    LOGIN_OPTIONAL = 1
    LOGIN_ADMIN = 2
    LOGIN_REQUIRED = 3


class SecurityLevel(proto.Enum):
    r"""Methods to enforce security (HTTPS) on a URL.

    Values:
        SECURE_UNSPECIFIED (0):
            Not specified.
        SECURE_DEFAULT (0):
            Both HTTP and HTTPS requests with URLs that
            match the handler succeed without redirects. The
            application can examine the request to determine
            which protocol was used, and respond
            accordingly.
        SECURE_NEVER (1):
            Requests for a URL that match this handler
            that use HTTPS are automatically redirected to
            the HTTP equivalent URL.
        SECURE_OPTIONAL (2):
            Both HTTP and HTTPS requests with URLs that
            match the handler succeed without redirects. The
            application can examine the request to determine
            which protocol was used and respond accordingly.
        SECURE_ALWAYS (3):
            Requests for a URL that match this handler
            that do not use HTTPS are automatically
            redirected to the HTTPS URL with the same path.
            Query parameters are reserved for the redirect.
    """

    _pb_options = {"allow_alias": True}
    SECURE_UNSPECIFIED = 0
    SECURE_DEFAULT = 0
    SECURE_NEVER = 1
    SECURE_OPTIONAL = 2
    SECURE_ALWAYS = 3


class ApiConfigHandler(proto.Message):
    r"""`Google Cloud
    Endpoints <https://cloud.google.com/appengine/docs/python/endpoints/>`__
    configuration for API handlers.

    Attributes:
        auth_fail_action (google.cloud.appengine_admin_v1.types.AuthFailAction):
            Action to take when users access resources that require
            authentication. Defaults to ``redirect``.
        login (google.cloud.appengine_admin_v1.types.LoginRequirement):
            Level of login required to access this resource. Defaults to
            ``optional``.
        script (str):
            Path to the script from the application root
            directory.
        security_level (google.cloud.appengine_admin_v1.types.SecurityLevel):
            Security (HTTPS) enforcement for this URL.
        url (str):
            URL to serve the endpoint at.
    """

    auth_fail_action: "AuthFailAction" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AuthFailAction",
    )
    login: "LoginRequirement" = proto.Field(
        proto.ENUM,
        number=2,
        enum="LoginRequirement",
    )
    script: str = proto.Field(
        proto.STRING,
        number=3,
    )
    security_level: "SecurityLevel" = proto.Field(
        proto.ENUM,
        number=4,
        enum="SecurityLevel",
    )
    url: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ErrorHandler(proto.Message):
    r"""Custom static error page to be served when an error occurs.

    Attributes:
        error_code (google.cloud.appengine_admin_v1.types.ErrorHandler.ErrorCode):
            Error condition this handler applies to.
        static_file (str):
            Static file content to be served for this
            error.
        mime_type (str):
            MIME type of file. Defaults to ``text/html``.
    """

    class ErrorCode(proto.Enum):
        r"""Error codes.

        Values:
            ERROR_CODE_UNSPECIFIED (0):
                Not specified. ERROR_CODE_DEFAULT is assumed.
            ERROR_CODE_DEFAULT (0):
                All other error types.
            ERROR_CODE_OVER_QUOTA (1):
                Application has exceeded a resource quota.
            ERROR_CODE_DOS_API_DENIAL (2):
                Client blocked by the application's Denial of
                Service protection configuration.
            ERROR_CODE_TIMEOUT (3):
                Deadline reached before the application
                responds.
        """

        _pb_options = {"allow_alias": True}
        ERROR_CODE_UNSPECIFIED = 0
        ERROR_CODE_DEFAULT = 0
        ERROR_CODE_OVER_QUOTA = 1
        ERROR_CODE_DOS_API_DENIAL = 2
        ERROR_CODE_TIMEOUT = 3

    error_code: ErrorCode = proto.Field(
        proto.ENUM,
        number=1,
        enum=ErrorCode,
    )
    static_file: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UrlMap(proto.Message):
    r"""URL pattern and description of how the URL should be handled.
    App Engine can handle URLs by executing application code or by
    serving static files uploaded with the version, such as images,
    CSS, or JavaScript.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        url_regex (str):
            URL prefix. Uses regular expression syntax,
            which means regexp special characters must be
            escaped, but should not contain groupings. All
            URLs that begin with this prefix are handled by
            this handler, using the portion of the URL after
            the prefix as part of the file path.
        static_files (google.cloud.appengine_admin_v1.types.StaticFilesHandler):
            Returns the contents of a file, such as an
            image, as the response.

            This field is a member of `oneof`_ ``handler_type``.
        script (google.cloud.appengine_admin_v1.types.ScriptHandler):
            Executes a script to handle the requests that match this URL
            pattern. Only the ``auto`` value is supported for Node.js in
            the App Engine standard environment, for example
            ``"script": "auto"``.

            This field is a member of `oneof`_ ``handler_type``.
        api_endpoint (google.cloud.appengine_admin_v1.types.ApiEndpointHandler):
            Uses API Endpoints to handle requests.

            This field is a member of `oneof`_ ``handler_type``.
        security_level (google.cloud.appengine_admin_v1.types.SecurityLevel):
            Security (HTTPS) enforcement for this URL.
        login (google.cloud.appengine_admin_v1.types.LoginRequirement):
            Level of login required to access this
            resource. Not supported for Node.js in the App
            Engine standard environment.
        auth_fail_action (google.cloud.appengine_admin_v1.types.AuthFailAction):
            Action to take when users access resources that require
            authentication. Defaults to ``redirect``.
        redirect_http_response_code (google.cloud.appengine_admin_v1.types.UrlMap.RedirectHttpResponseCode):
            ``30x`` code to use when performing redirects for the
            ``secure`` field. Defaults to ``302``.
    """

    class RedirectHttpResponseCode(proto.Enum):
        r"""Redirect codes.

        Values:
            REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED (0):
                Not specified. ``302`` is assumed.
            REDIRECT_HTTP_RESPONSE_CODE_301 (1):
                ``301 Moved Permanently`` code.
            REDIRECT_HTTP_RESPONSE_CODE_302 (2):
                ``302 Moved Temporarily`` code.
            REDIRECT_HTTP_RESPONSE_CODE_303 (3):
                ``303 See Other`` code.
            REDIRECT_HTTP_RESPONSE_CODE_307 (4):
                ``307 Temporary Redirect`` code.
        """

        REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED = 0
        REDIRECT_HTTP_RESPONSE_CODE_301 = 1
        REDIRECT_HTTP_RESPONSE_CODE_302 = 2
        REDIRECT_HTTP_RESPONSE_CODE_303 = 3
        REDIRECT_HTTP_RESPONSE_CODE_307 = 4

    url_regex: str = proto.Field(
        proto.STRING,
        number=1,
    )
    static_files: "StaticFilesHandler" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="handler_type",
        message="StaticFilesHandler",
    )
    script: "ScriptHandler" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="handler_type",
        message="ScriptHandler",
    )
    api_endpoint: "ApiEndpointHandler" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="handler_type",
        message="ApiEndpointHandler",
    )
    security_level: "SecurityLevel" = proto.Field(
        proto.ENUM,
        number=5,
        enum="SecurityLevel",
    )
    login: "LoginRequirement" = proto.Field(
        proto.ENUM,
        number=6,
        enum="LoginRequirement",
    )
    auth_fail_action: "AuthFailAction" = proto.Field(
        proto.ENUM,
        number=7,
        enum="AuthFailAction",
    )
    redirect_http_response_code: RedirectHttpResponseCode = proto.Field(
        proto.ENUM,
        number=8,
        enum=RedirectHttpResponseCode,
    )


class StaticFilesHandler(proto.Message):
    r"""Files served directly to the user for a given URL, such as
    images, CSS stylesheets, or JavaScript source files. Static file
    handlers describe which files in the application directory are
    static files, and which URLs serve them.

    Attributes:
        path (str):
            Path to the static files matched by the URL
            pattern, from the application root directory.
            The path can refer to text matched in groupings
            in the URL pattern.
        upload_path_regex (str):
            Regular expression that matches the file
            paths for all files that should be referenced by
            this handler.
        http_headers (MutableMapping[str, str]):
            HTTP headers to use for all responses from
            these URLs.
        mime_type (str):
            MIME type used to serve all files served by
            this handler.
            Defaults to file-specific MIME types, which are
            derived from each file's filename extension.
        expiration (google.protobuf.duration_pb2.Duration):
            Time a static file served by this handler
            should be cached by web proxies and browsers.
        require_matching_file (bool):
            Whether this handler should match the request
            if the file referenced by the handler does not
            exist.
        application_readable (bool):
            Whether files should also be uploaded as code
            data. By default, files declared in static file
            handlers are uploaded as static data and are
            only served to end users; they cannot be read by
            the application. If enabled, uploads are charged
            against both your code and static data storage
            resource quotas.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    upload_path_regex: str = proto.Field(
        proto.STRING,
        number=2,
    )
    http_headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    expiration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    require_matching_file: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    application_readable: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class ScriptHandler(proto.Message):
    r"""Executes a script to handle the request that matches the URL
    pattern.

    Attributes:
        script_path (str):
            Path to the script from the application root
            directory.
    """

    script_path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ApiEndpointHandler(proto.Message):
    r"""Uses Google Cloud Endpoints to handle requests.

    Attributes:
        script_path (str):
            Path to the script from the application root
            directory.
    """

    script_path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class HealthCheck(proto.Message):
    r"""Health checking configuration for VM instances. Unhealthy
    instances are killed and replaced with new instances. Only
    applicable for instances in App Engine flexible environment.

    Attributes:
        disable_health_check (bool):
            Whether to explicitly disable health checks
            for this instance.
        host (str):
            Host header to send when performing an HTTP
            health check. Example: "myapp.appspot.com".
        healthy_threshold (int):
            Number of consecutive successful health
            checks required before receiving traffic.
        unhealthy_threshold (int):
            Number of consecutive failed health checks
            required before removing traffic.
        restart_threshold (int):
            Number of consecutive failed health checks
            required before an instance is restarted.
        check_interval (google.protobuf.duration_pb2.Duration):
            Interval between health checks.
        timeout (google.protobuf.duration_pb2.Duration):
            Time before the health check is considered
            failed.
    """

    disable_health_check: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    host: str = proto.Field(
        proto.STRING,
        number=2,
    )
    healthy_threshold: int = proto.Field(
        proto.UINT32,
        number=3,
    )
    unhealthy_threshold: int = proto.Field(
        proto.UINT32,
        number=4,
    )
    restart_threshold: int = proto.Field(
        proto.UINT32,
        number=5,
    )
    check_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )


class ReadinessCheck(proto.Message):
    r"""Readiness checking configuration for VM instances. Unhealthy
    instances are removed from traffic rotation.

    Attributes:
        path (str):
            The request path.
        host (str):
            Host header to send when performing a HTTP
            Readiness check. Example: "myapp.appspot.com".
        failure_threshold (int):
            Number of consecutive failed checks required
            before removing traffic.
        success_threshold (int):
            Number of consecutive successful checks
            required before receiving traffic.
        check_interval (google.protobuf.duration_pb2.Duration):
            Interval between health checks.
        timeout (google.protobuf.duration_pb2.Duration):
            Time before the check is considered failed.
        app_start_timeout (google.protobuf.duration_pb2.Duration):
            A maximum time limit on application
            initialization, measured from moment the
            application successfully replies to a
            healthcheck until it is ready to serve traffic.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    host: str = proto.Field(
        proto.STRING,
        number=2,
    )
    failure_threshold: int = proto.Field(
        proto.UINT32,
        number=3,
    )
    success_threshold: int = proto.Field(
        proto.UINT32,
        number=4,
    )
    check_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    app_start_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )


class LivenessCheck(proto.Message):
    r"""Health checking configuration for VM instances. Unhealthy
    instances are killed and replaced with new instances.

    Attributes:
        path (str):
            The request path.
        host (str):
            Host header to send when performing a HTTP
            Liveness check. Example: "myapp.appspot.com".
        failure_threshold (int):
            Number of consecutive failed checks required
            before considering the VM unhealthy.
        success_threshold (int):
            Number of consecutive successful checks
            required before considering the VM healthy.
        check_interval (google.protobuf.duration_pb2.Duration):
            Interval between health checks.
        timeout (google.protobuf.duration_pb2.Duration):
            Time before the check is considered failed.
        initial_delay (google.protobuf.duration_pb2.Duration):
            The initial delay before starting to execute
            the checks.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    host: str = proto.Field(
        proto.STRING,
        number=2,
    )
    failure_threshold: int = proto.Field(
        proto.UINT32,
        number=3,
    )
    success_threshold: int = proto.Field(
        proto.UINT32,
        number=4,
    )
    check_interval: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    initial_delay: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )


class Library(proto.Message):
    r"""Third-party Python runtime library that is required by the
    application.

    Attributes:
        name (str):
            Name of the library. Example: "django".
        version (str):
            Version of the library to select, or
            "latest".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
