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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.appengine_admin_v1.types import app_yaml, deploy

__protobuf__ = proto.module(
    package="google.appengine.v1",
    manifest={
        "InboundServiceType",
        "ServingStatus",
        "Version",
        "EndpointsApiService",
        "AutomaticScaling",
        "BasicScaling",
        "ManualScaling",
        "CpuUtilization",
        "RequestUtilization",
        "DiskUtilization",
        "NetworkUtilization",
        "StandardSchedulerSettings",
        "Network",
        "Volume",
        "Resources",
        "VpcAccessConnector",
        "Entrypoint",
    },
)


class InboundServiceType(proto.Enum):
    r"""Available inbound services.

    Values:
        INBOUND_SERVICE_UNSPECIFIED (0):
            Not specified.
        INBOUND_SERVICE_MAIL (1):
            Allows an application to receive mail.
        INBOUND_SERVICE_MAIL_BOUNCE (2):
            Allows an application to receive email-bound
            notifications.
        INBOUND_SERVICE_XMPP_ERROR (3):
            Allows an application to receive error
            stanzas.
        INBOUND_SERVICE_XMPP_MESSAGE (4):
            Allows an application to receive instant
            messages.
        INBOUND_SERVICE_XMPP_SUBSCRIBE (5):
            Allows an application to receive user
            subscription POSTs.
        INBOUND_SERVICE_XMPP_PRESENCE (6):
            Allows an application to receive a user's
            chat presence.
        INBOUND_SERVICE_CHANNEL_PRESENCE (7):
            Registers an application for notifications
            when a client connects or disconnects from a
            channel.
        INBOUND_SERVICE_WARMUP (9):
            Enables warmup requests.
    """

    INBOUND_SERVICE_UNSPECIFIED = 0
    INBOUND_SERVICE_MAIL = 1
    INBOUND_SERVICE_MAIL_BOUNCE = 2
    INBOUND_SERVICE_XMPP_ERROR = 3
    INBOUND_SERVICE_XMPP_MESSAGE = 4
    INBOUND_SERVICE_XMPP_SUBSCRIBE = 5
    INBOUND_SERVICE_XMPP_PRESENCE = 6
    INBOUND_SERVICE_CHANNEL_PRESENCE = 7
    INBOUND_SERVICE_WARMUP = 9


class ServingStatus(proto.Enum):
    r"""Run states of a version.

    Values:
        SERVING_STATUS_UNSPECIFIED (0):
            Not specified.
        SERVING (1):
            Currently serving. Instances are created
            according to the scaling settings of the
            version.
        STOPPED (2):
            Disabled. No instances will be created and the scaling
            settings are ignored until the state of the version changes
            to ``SERVING``.
    """

    SERVING_STATUS_UNSPECIFIED = 0
    SERVING = 1
    STOPPED = 2


class Version(proto.Message):
    r"""A Version resource is a specific set of source code and
    configuration files that are deployed into a service.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Full path to the Version resource in the API. Example:
            ``apps/myapp/services/default/versions/v1``.

            @OutputOnly
        id (str):
            Relative name of the version within the service. Example:
            ``v1``. Version names can contain only lowercase letters,
            numbers, or hyphens. Reserved names: "default", "latest",
            and any name with the prefix "ah-".
        automatic_scaling (google.cloud.appengine_admin_v1.types.AutomaticScaling):
            Automatic scaling is based on request rate,
            response latencies, and other application
            metrics. Instances are dynamically created and
            destroyed as needed in order to handle traffic.

            This field is a member of `oneof`_ ``scaling``.
        basic_scaling (google.cloud.appengine_admin_v1.types.BasicScaling):
            A service with basic scaling will create an
            instance when the application receives a
            request. The instance will be turned down when
            the app becomes idle. Basic scaling is ideal for
            work that is intermittent or driven by user
            activity.

            This field is a member of `oneof`_ ``scaling``.
        manual_scaling (google.cloud.appengine_admin_v1.types.ManualScaling):
            A service with manual scaling runs
            continuously, allowing you to perform complex
            initialization and rely on the state of its
            memory over time. Manually scaled versions are
            sometimes referred to as "backends".

            This field is a member of `oneof`_ ``scaling``.
        inbound_services (MutableSequence[google.cloud.appengine_admin_v1.types.InboundServiceType]):
            Before an application can receive email or
            XMPP messages, the application must be
            configured to enable the service.
        instance_class (str):
            Instance class that is used to run this version. Valid
            values are:

            - AutomaticScaling: ``F1``, ``F2``, ``F4``, ``F4_1G``
            - ManualScaling or BasicScaling: ``B1``, ``B2``, ``B4``,
              ``B8``, ``B4_1G``

            Defaults to ``F1`` for AutomaticScaling and ``B1`` for
            ManualScaling or BasicScaling.
        network (google.cloud.appengine_admin_v1.types.Network):
            Extra network settings.
            Only applicable in the App Engine flexible
            environment.
        zones (MutableSequence[str]):
            The Google Compute Engine zones that are
            supported by this version in the App Engine
            flexible environment. Deprecated.
        resources (google.cloud.appengine_admin_v1.types.Resources):
            Machine resources for this version.
            Only applicable in the App Engine flexible
            environment.
        runtime (str):
            Desired runtime. Example: ``python27``.
        runtime_channel (str):
            The channel of the runtime to use. Only available for some
            runtimes. Defaults to the ``default`` channel.
        threadsafe (bool):
            Whether multiple requests can be dispatched
            to this version at once.
        vm (bool):
            Whether to deploy this version in a container
            on a virtual machine.
        app_engine_apis (bool):
            Allows App Engine second generation runtimes
            to access the legacy bundled services.
        beta_settings (MutableMapping[str, str]):
            Metadata settings that are supplied to this
            version to enable beta runtime features.
        env (str):
            App Engine execution environment for this version.

            Defaults to ``standard``.
        serving_status (google.cloud.appengine_admin_v1.types.ServingStatus):
            Current serving status of this version. Only the versions
            with a ``SERVING`` status create instances and can be
            billed.

            ``SERVING_STATUS_UNSPECIFIED`` is an invalid value. Defaults
            to ``SERVING``.
        created_by (str):
            Email address of the user who created this
            version.
            @OutputOnly
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time that this version was created.

            @OutputOnly
        disk_usage_bytes (int):
            Total size in bytes of all the files that are
            included in this version and currently hosted on
            the App Engine disk.

            @OutputOnly
        runtime_api_version (str):
            The version of the API in the given runtime
            environment. Please see the app.yaml reference
            for valid values at
            https://cloud.google.com/appengine/docs/standard/<language>/config/appref
        runtime_main_executable_path (str):
            The path or name of the app's main
            executable.
        service_account (str):
            The identity that the deployed version will
            run as. Admin API will use the App Engine
            Appspot service account as default if this field
            is neither provided in app.yaml file nor through
            CLI flag.
        handlers (MutableSequence[google.cloud.appengine_admin_v1.types.UrlMap]):
            An ordered list of URL-matching patterns that should be
            applied to incoming requests. The first matching URL handles
            the request and other request handlers are not attempted.

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        error_handlers (MutableSequence[google.cloud.appengine_admin_v1.types.ErrorHandler]):
            Custom static error pages. Limited to 10KB per page.

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        libraries (MutableSequence[google.cloud.appengine_admin_v1.types.Library]):
            Configuration for third-party Python runtime libraries that
            are required by the application.

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        api_config (google.cloud.appengine_admin_v1.types.ApiConfigHandler):
            Serving configuration for `Google Cloud
            Endpoints <https://cloud.google.com/appengine/docs/python/endpoints/>`__.

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        env_variables (MutableMapping[str, str]):
            Environment variables available to the application.

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        build_env_variables (MutableMapping[str, str]):
            Environment variables available to the build environment.

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        default_expiration (google.protobuf.duration_pb2.Duration):
            Duration that static files should be cached by web proxies
            and browsers. Only applicable if the corresponding
            `StaticFilesHandler <https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StaticFilesHandler>`__
            does not specify its own expiration time.

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        health_check (google.cloud.appengine_admin_v1.types.HealthCheck):
            Configures health checking for instances. Unhealthy
            instances are stopped and replaced with new instances. Only
            applicable in the App Engine flexible environment.

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        readiness_check (google.cloud.appengine_admin_v1.types.ReadinessCheck):
            Configures readiness health checking for instances.
            Unhealthy instances are not put into the backend traffic
            rotation.

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        liveness_check (google.cloud.appengine_admin_v1.types.LivenessCheck):
            Configures liveness health checking for instances. Unhealthy
            instances are stopped and replaced with new instances

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        nobuild_files_regex (str):
            Files that match this pattern will not be built into this
            version. Only applicable for Go runtimes.

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        deployment (google.cloud.appengine_admin_v1.types.Deployment):
            Code and application artifacts that make up this version.

            Only returned in ``GET`` requests if ``view=FULL`` is set.
        version_url (str):
            Serving URL for this version. Example:

            "https://myversion-dot-myservice-dot-myapp.appspot.com"

            @OutputOnly
        endpoints_api_service (google.cloud.appengine_admin_v1.types.EndpointsApiService):
            Cloud Endpoints configuration.

            If endpoints_api_service is set, the Cloud Endpoints
            Extensible Service Proxy will be provided to serve the API
            implemented by the app.
        entrypoint (google.cloud.appengine_admin_v1.types.Entrypoint):
            The entrypoint for the application.
        vpc_access_connector (google.cloud.appengine_admin_v1.types.VpcAccessConnector):
            Enables VPC connectivity for standard apps.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    automatic_scaling: "AutomaticScaling" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="scaling",
        message="AutomaticScaling",
    )
    basic_scaling: "BasicScaling" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="scaling",
        message="BasicScaling",
    )
    manual_scaling: "ManualScaling" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="scaling",
        message="ManualScaling",
    )
    inbound_services: MutableSequence["InboundServiceType"] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum="InboundServiceType",
    )
    instance_class: str = proto.Field(
        proto.STRING,
        number=7,
    )
    network: "Network" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="Network",
    )
    zones: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=118,
    )
    resources: "Resources" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Resources",
    )
    runtime: str = proto.Field(
        proto.STRING,
        number=10,
    )
    runtime_channel: str = proto.Field(
        proto.STRING,
        number=117,
    )
    threadsafe: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    vm: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    app_engine_apis: bool = proto.Field(
        proto.BOOL,
        number=128,
    )
    beta_settings: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=13,
    )
    env: str = proto.Field(
        proto.STRING,
        number=14,
    )
    serving_status: "ServingStatus" = proto.Field(
        proto.ENUM,
        number=15,
        enum="ServingStatus",
    )
    created_by: str = proto.Field(
        proto.STRING,
        number=16,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=17,
        message=timestamp_pb2.Timestamp,
    )
    disk_usage_bytes: int = proto.Field(
        proto.INT64,
        number=18,
    )
    runtime_api_version: str = proto.Field(
        proto.STRING,
        number=21,
    )
    runtime_main_executable_path: str = proto.Field(
        proto.STRING,
        number=22,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=127,
    )
    handlers: MutableSequence[app_yaml.UrlMap] = proto.RepeatedField(
        proto.MESSAGE,
        number=100,
        message=app_yaml.UrlMap,
    )
    error_handlers: MutableSequence[app_yaml.ErrorHandler] = proto.RepeatedField(
        proto.MESSAGE,
        number=101,
        message=app_yaml.ErrorHandler,
    )
    libraries: MutableSequence[app_yaml.Library] = proto.RepeatedField(
        proto.MESSAGE,
        number=102,
        message=app_yaml.Library,
    )
    api_config: app_yaml.ApiConfigHandler = proto.Field(
        proto.MESSAGE,
        number=103,
        message=app_yaml.ApiConfigHandler,
    )
    env_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=104,
    )
    build_env_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=125,
    )
    default_expiration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=105,
        message=duration_pb2.Duration,
    )
    health_check: app_yaml.HealthCheck = proto.Field(
        proto.MESSAGE,
        number=106,
        message=app_yaml.HealthCheck,
    )
    readiness_check: app_yaml.ReadinessCheck = proto.Field(
        proto.MESSAGE,
        number=112,
        message=app_yaml.ReadinessCheck,
    )
    liveness_check: app_yaml.LivenessCheck = proto.Field(
        proto.MESSAGE,
        number=113,
        message=app_yaml.LivenessCheck,
    )
    nobuild_files_regex: str = proto.Field(
        proto.STRING,
        number=107,
    )
    deployment: deploy.Deployment = proto.Field(
        proto.MESSAGE,
        number=108,
        message=deploy.Deployment,
    )
    version_url: str = proto.Field(
        proto.STRING,
        number=109,
    )
    endpoints_api_service: "EndpointsApiService" = proto.Field(
        proto.MESSAGE,
        number=110,
        message="EndpointsApiService",
    )
    entrypoint: "Entrypoint" = proto.Field(
        proto.MESSAGE,
        number=122,
        message="Entrypoint",
    )
    vpc_access_connector: "VpcAccessConnector" = proto.Field(
        proto.MESSAGE,
        number=121,
        message="VpcAccessConnector",
    )


class EndpointsApiService(proto.Message):
    r"""`Cloud Endpoints <https://cloud.google.com/endpoints>`__
    configuration. The Endpoints API Service provides tooling for
    serving Open API and gRPC endpoints via an NGINX proxy. Only valid
    for App Engine Flexible environment deployments.

    The fields here refer to the name and configuration ID of a
    "service" resource in the `Service Management
    API <https://cloud.google.com/service-management/overview>`__.

    Attributes:
        name (str):
            Endpoints service name which is the name of
            the "service" resource in the Service Management
            API. For example
            "myapi.endpoints.myproject.cloud.goog".
        config_id (str):
            Endpoints service configuration ID as specified by the
            Service Management API. For example "2016-09-19r1".

            By default, the rollout strategy for Endpoints is
            ``RolloutStrategy.FIXED``. This means that Endpoints starts
            up with a particular configuration ID. When a new
            configuration is rolled out, Endpoints must be given the new
            configuration ID. The ``config_id`` field is used to give
            the configuration ID and is required in this case.

            Endpoints also has a rollout strategy called
            ``RolloutStrategy.MANAGED``. When using this, Endpoints
            fetches the latest configuration and does not need the
            configuration ID. In this case, ``config_id`` must be
            omitted.
        rollout_strategy (google.cloud.appengine_admin_v1.types.EndpointsApiService.RolloutStrategy):
            Endpoints rollout strategy. If ``FIXED``, ``config_id`` must
            be specified. If ``MANAGED``, ``config_id`` must be omitted.
        disable_trace_sampling (bool):
            Enable or disable trace sampling. By default,
            this is set to false for enabled.
    """

    class RolloutStrategy(proto.Enum):
        r"""Available rollout strategies.

        Values:
            UNSPECIFIED_ROLLOUT_STRATEGY (0):
                Not specified. Defaults to ``FIXED``.
            FIXED (1):
                Endpoints service configuration ID will be fixed to the
                configuration ID specified by ``config_id``.
            MANAGED (2):
                Endpoints service configuration ID will be
                updated with each rollout.
        """

        UNSPECIFIED_ROLLOUT_STRATEGY = 0
        FIXED = 1
        MANAGED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rollout_strategy: RolloutStrategy = proto.Field(
        proto.ENUM,
        number=3,
        enum=RolloutStrategy,
    )
    disable_trace_sampling: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class AutomaticScaling(proto.Message):
    r"""Automatic scaling is based on request rate, response
    latencies, and other application metrics.

    Attributes:
        cool_down_period (google.protobuf.duration_pb2.Duration):
            The time period that the
            `Autoscaler <https://cloud.google.com/compute/docs/autoscaler/>`__
            should wait before it starts collecting information from a
            new instance. This prevents the autoscaler from collecting
            information when the instance is initializing, during which
            the collected usage would not be reliable. Only applicable
            in the App Engine flexible environment.
        cpu_utilization (google.cloud.appengine_admin_v1.types.CpuUtilization):
            Target scaling by CPU usage.
        max_concurrent_requests (int):
            Number of concurrent requests an automatic
            scaling instance can accept before the scheduler
            spawns a new instance.

            Defaults to a runtime-specific value.
        max_idle_instances (int):
            Maximum number of idle instances that should
            be maintained for this version.
        max_total_instances (int):
            Maximum number of instances that should be
            started to handle requests for this version.
        max_pending_latency (google.protobuf.duration_pb2.Duration):
            Maximum amount of time that a request should
            wait in the pending queue before starting a new
            instance to handle it.
        min_idle_instances (int):
            Minimum number of idle instances that should
            be maintained for this version. Only applicable
            for the default version of a service.
        min_total_instances (int):
            Minimum number of running instances that
            should be maintained for this version.
        min_pending_latency (google.protobuf.duration_pb2.Duration):
            Minimum amount of time a request should wait
            in the pending queue before starting a new
            instance to handle it.
        request_utilization (google.cloud.appengine_admin_v1.types.RequestUtilization):
            Target scaling by request utilization.
        disk_utilization (google.cloud.appengine_admin_v1.types.DiskUtilization):
            Target scaling by disk usage.
        network_utilization (google.cloud.appengine_admin_v1.types.NetworkUtilization):
            Target scaling by network usage.
        standard_scheduler_settings (google.cloud.appengine_admin_v1.types.StandardSchedulerSettings):
            Scheduler settings for standard environment.
    """

    cool_down_period: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    cpu_utilization: "CpuUtilization" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CpuUtilization",
    )
    max_concurrent_requests: int = proto.Field(
        proto.INT32,
        number=3,
    )
    max_idle_instances: int = proto.Field(
        proto.INT32,
        number=4,
    )
    max_total_instances: int = proto.Field(
        proto.INT32,
        number=5,
    )
    max_pending_latency: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    min_idle_instances: int = proto.Field(
        proto.INT32,
        number=7,
    )
    min_total_instances: int = proto.Field(
        proto.INT32,
        number=8,
    )
    min_pending_latency: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=9,
        message=duration_pb2.Duration,
    )
    request_utilization: "RequestUtilization" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="RequestUtilization",
    )
    disk_utilization: "DiskUtilization" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="DiskUtilization",
    )
    network_utilization: "NetworkUtilization" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="NetworkUtilization",
    )
    standard_scheduler_settings: "StandardSchedulerSettings" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="StandardSchedulerSettings",
    )


class BasicScaling(proto.Message):
    r"""A service with basic scaling will create an instance when the
    application receives a request. The instance will be turned down
    when the app becomes idle. Basic scaling is ideal for work that
    is intermittent or driven by user activity.

    Attributes:
        idle_timeout (google.protobuf.duration_pb2.Duration):
            Duration of time after the last request that
            an instance must wait before the instance is
            shut down.
        max_instances (int):
            Maximum number of instances to create for
            this version.
    """

    idle_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    max_instances: int = proto.Field(
        proto.INT32,
        number=2,
    )


class ManualScaling(proto.Message):
    r"""A service with manual scaling runs continuously, allowing you
    to perform complex initialization and rely on the state of its
    memory over time.

    Attributes:
        instances (int):
            Number of instances to assign to the service at the start.
            This number can later be altered by using the `Modules
            API <https://cloud.google.com/appengine/docs/python/modules/functions>`__
            ``set_num_instances()`` function.
    """

    instances: int = proto.Field(
        proto.INT32,
        number=1,
    )


class CpuUtilization(proto.Message):
    r"""Target scaling by CPU usage.

    Attributes:
        aggregation_window_length (google.protobuf.duration_pb2.Duration):
            Period of time over which CPU utilization is
            calculated.
        target_utilization (float):
            Target CPU utilization ratio to maintain when
            scaling. Must be between 0 and 1.
    """

    aggregation_window_length: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    target_utilization: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


class RequestUtilization(proto.Message):
    r"""Target scaling by request utilization.
    Only applicable in the App Engine flexible environment.

    Attributes:
        target_request_count_per_second (int):
            Target requests per second.
        target_concurrent_requests (int):
            Target number of concurrent requests.
    """

    target_request_count_per_second: int = proto.Field(
        proto.INT32,
        number=1,
    )
    target_concurrent_requests: int = proto.Field(
        proto.INT32,
        number=2,
    )


class DiskUtilization(proto.Message):
    r"""Target scaling by disk usage.
    Only applicable in the App Engine flexible environment.

    Attributes:
        target_write_bytes_per_second (int):
            Target bytes written per second.
        target_write_ops_per_second (int):
            Target ops written per second.
        target_read_bytes_per_second (int):
            Target bytes read per second.
        target_read_ops_per_second (int):
            Target ops read per seconds.
    """

    target_write_bytes_per_second: int = proto.Field(
        proto.INT32,
        number=14,
    )
    target_write_ops_per_second: int = proto.Field(
        proto.INT32,
        number=15,
    )
    target_read_bytes_per_second: int = proto.Field(
        proto.INT32,
        number=16,
    )
    target_read_ops_per_second: int = proto.Field(
        proto.INT32,
        number=17,
    )


class NetworkUtilization(proto.Message):
    r"""Target scaling by network usage.
    Only applicable in the App Engine flexible environment.

    Attributes:
        target_sent_bytes_per_second (int):
            Target bytes sent per second.
        target_sent_packets_per_second (int):
            Target packets sent per second.
        target_received_bytes_per_second (int):
            Target bytes received per second.
        target_received_packets_per_second (int):
            Target packets received per second.
    """

    target_sent_bytes_per_second: int = proto.Field(
        proto.INT32,
        number=1,
    )
    target_sent_packets_per_second: int = proto.Field(
        proto.INT32,
        number=11,
    )
    target_received_bytes_per_second: int = proto.Field(
        proto.INT32,
        number=12,
    )
    target_received_packets_per_second: int = proto.Field(
        proto.INT32,
        number=13,
    )


class StandardSchedulerSettings(proto.Message):
    r"""Scheduler settings for standard environment.

    Attributes:
        target_cpu_utilization (float):
            Target CPU utilization ratio to maintain when
            scaling.
        target_throughput_utilization (float):
            Target throughput utilization ratio to
            maintain when scaling
        min_instances (int):
            Minimum number of instances to run for this version. Set to
            zero to disable ``min_instances`` configuration.
        max_instances (int):
            Maximum number of instances to run for this version. Set to
            zero to disable ``max_instances`` configuration.
    """

    target_cpu_utilization: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    target_throughput_utilization: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    min_instances: int = proto.Field(
        proto.INT32,
        number=3,
    )
    max_instances: int = proto.Field(
        proto.INT32,
        number=4,
    )


class Network(proto.Message):
    r"""Extra network settings.
    Only applicable in the App Engine flexible environment.

    Attributes:
        forwarded_ports (MutableSequence[str]):
            List of ports, or port pairs, to forward from
            the virtual machine to the application
            container. Only applicable in the App Engine
            flexible environment.
        instance_tag (str):
            Tag to apply to the instance during creation.
            Only applicable in the App Engine flexible
            environment.
        name (str):
            Google Compute Engine network where the virtual machines are
            created. Specify the short name, not the resource path.

            Defaults to ``default``.
        subnetwork_name (str):
            Google Cloud Platform sub-network where the virtual machines
            are created. Specify the short name, not the resource path.

            If a subnetwork name is specified, a network name will also
            be required unless it is for the default network.

            - If the network that the instance is being created in is a
              Legacy network, then the IP address is allocated from the
              IPv4Range.
            - If the network that the instance is being created in is an
              auto Subnet Mode Network, then only network name should be
              specified (not the subnetwork_name) and the IP address is
              created from the IPCidrRange of the subnetwork that exists
              in that zone for that network.
            - If the network that the instance is being created in is a
              custom Subnet Mode Network, then the subnetwork_name must
              be specified and the IP address is created from the
              IPCidrRange of the subnetwork.

            If specified, the subnetwork must exist in the same region
            as the App Engine flexible environment application.
        session_affinity (bool):
            Enable session affinity.
            Only applicable in the App Engine flexible
            environment.
    """

    forwarded_ports: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    instance_tag: str = proto.Field(
        proto.STRING,
        number=2,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    subnetwork_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    session_affinity: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class Volume(proto.Message):
    r"""Volumes mounted within the app container.
    Only applicable in the App Engine flexible environment.

    Attributes:
        name (str):
            Unique name for the volume.
        volume_type (str):
            Underlying volume type, e.g. 'tmpfs'.
        size_gb (float):
            Volume size in gigabytes.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    volume_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    size_gb: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )


class Resources(proto.Message):
    r"""Machine resources for a version.

    Attributes:
        cpu (float):
            Number of CPU cores needed.
        disk_gb (float):
            Disk size (GB) needed.
        memory_gb (float):
            Memory (GB) needed.
        volumes (MutableSequence[google.cloud.appengine_admin_v1.types.Volume]):
            User specified volumes.
        kms_key_reference (str):
            The name of the encryption key that is stored
            in Google Cloud KMS. Only should be used by
            Cloud Composer to encrypt the vm disk
    """

    cpu: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    disk_gb: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    memory_gb: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    volumes: MutableSequence["Volume"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Volume",
    )
    kms_key_reference: str = proto.Field(
        proto.STRING,
        number=5,
    )


class VpcAccessConnector(proto.Message):
    r"""VPC access connector specification.

    Attributes:
        name (str):
            Full Serverless VPC Access Connector name
            e.g.
            /projects/my-project/locations/us-central1/connectors/c1.
        egress_setting (google.cloud.appengine_admin_v1.types.VpcAccessConnector.EgressSetting):
            The egress setting for the connector,
            controlling what traffic is diverted through it.
    """

    class EgressSetting(proto.Enum):
        r"""Available egress settings.

        This controls what traffic is diverted through the VPC Access
        Connector resource. By default PRIVATE_IP_RANGES will be used.

        Values:
            EGRESS_SETTING_UNSPECIFIED (0):
                No description available.
            ALL_TRAFFIC (1):
                Force the use of VPC Access for all egress
                traffic from the function.
            PRIVATE_IP_RANGES (2):
                Use the VPC Access Connector for private IP
                space from RFC1918.
        """

        EGRESS_SETTING_UNSPECIFIED = 0
        ALL_TRAFFIC = 1
        PRIVATE_IP_RANGES = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    egress_setting: EgressSetting = proto.Field(
        proto.ENUM,
        number=2,
        enum=EgressSetting,
    )


class Entrypoint(proto.Message):
    r"""The entrypoint for the application.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        shell (str):
            The format should be a shell command that can be fed to
            ``bash -c``.

            This field is a member of `oneof`_ ``command``.
    """

    shell: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="command",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
