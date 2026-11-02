# Copyright 2025 Google LLC
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

"""A client for interacting with Google Cloud Storage using the gRPC API."""

import os

from google.cloud.client import ClientWithProject

from google.cloud import _storage_v2 as storage_v2
from google.cloud.storage import _opentelemetry_metrics

_marker = object()
_DEFAULT_HOST = "storage.googleapis.com"
_DEFAULT_HOST_DIRECT_PATH = "storage-direct.googleapis.com"
_DIRECT_PATH_INTERCONNECT_ENV = "GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS_OVER_INTERCONNECT"


def _resolve_direct_path_interconnect(option_value: bool) -> bool:
    """Resolves DirectPath over Interconnect flag from env var or parameter."""
    env_val = os.environ.get(_DIRECT_PATH_INTERCONNECT_ENV)
    if env_val is not None:
        env_val_clean = env_val.strip().lower()
        if env_val_clean == "true":
            return True
        elif env_val_clean == "false":
            return False
        else:
            raise ValueError(
                f"Invalid value for {_DIRECT_PATH_INTERCONNECT_ENV}: {env_val}"
            )
    return bool(option_value)


def _rewrite_host_for_interconnect(
    host: str,
    old_host: str = _DEFAULT_HOST,
    new_host: str = _DEFAULT_HOST_DIRECT_PATH,
) -> str:
    """Rewrites the default GCS endpoint to the DirectPath over Interconnect host."""
    if not host:
        return new_host
    for prefix in ("", "https://", "http://", "dns:///"):
        candidate = f"{prefix}{old_host}"
        if host.startswith(candidate):
            rest = host[len(candidate) :]
            if not rest or rest[0] in (":", "/", "?", "#"):
                return f"{prefix}{new_host}{rest}"
    return host


class GrpcClient(ClientWithProject):
    """A client for interacting with Google Cloud Storage using the gRPC API.

    :type project: str or None
    :param project: The project which the client acts on behalf of. If not
                    passed, falls back to the default inferred from the
                    environment.

    :type credentials: :class:`~google.auth.credentials.Credentials`
    :param credentials: (Optional) The OAuth2 Credentials to use for this
                        client. If not passed, falls back to the default
                        inferred from the environment.

    :type client_info: :class:`~google.api_core.client_info.ClientInfo`
    :param client_info:
        The client info used to send a user-agent string along with API
        requests. If ``None``, then default info will be used. Generally,
        you only need to set this if you're developing your own library
        or partner tool.

    :type client_options: :class:`~google.api_core.client_options.ClientOptions` or :class:`dict`
    :param client_options: (Optional) Client options used to set user options
        on the client. A non-default universe domain or API endpoint should be
        set through client_options.

    :type api_key: string
    :param api_key:
        (Optional) An API key. Mutually exclusive with any other credentials.
        This parameter is an alias for setting `client_options.api_key` and
        will supersede any API key set in the `client_options` parameter.

    :type attempt_direct_path: bool
    :param attempt_direct_path:
        (Optional) Whether to attempt to use DirectPath for gRPC connections.
        This provides a direct, unproxied connection to GCS for lower latency
        and higher throughput, and is highly recommended when running on Google
        Cloud infrastructure. Defaults to ``True``.

    :type attempt_direct_path_xds_over_interconnect: bool
    :param attempt_direct_path_xds_over_interconnect:
        (Optional) Whether to attempt DirectPath over Cloud Interconnect
        using xDS and standard TLS. Can also be overridden via the
        ``GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS_OVER_INTERCONNECT`` environment
        variable (``"true"`` or ``"false"``). Defaults to ``False``.

    :type enable_metrics: bool or None
    :param enable_metrics:
        (Optional, Experimental) Whether to enable OpenTelemetry metrics. If
        ``None``, falls back to the ``GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS``
        environment variable, or ``False`` if unset.

    :type enable_debug_metrics: bool or None
    :param enable_debug_metrics:
        (Optional, Experimental) Whether to enable debug OpenTelemetry
        metrics. If ``None``, falls back to the
        ``GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS`` environment variable,
        or ``False`` if unset.
    """

    def __init__(
        self,
        project=_marker,
        credentials=None,
        client_info=None,
        client_options=None,
        *,
        api_key=None,
        attempt_direct_path=True,
        attempt_direct_path_xds_over_interconnect=False,
        enable_metrics=None,
        enable_debug_metrics=None,
    ):
        super(GrpcClient, self).__init__(project=project, credentials=credentials)

        self._enable_metrics = enable_metrics
        self._enable_debug_metrics = enable_debug_metrics
        self._metrics_enabled = _opentelemetry_metrics.is_metrics_enabled(
            enable_metrics
        )
        self._debug_metrics_enabled = _opentelemetry_metrics.is_debug_metrics_enabled(
            enable_debug_metrics
        )

        if isinstance(client_options, dict):
            if api_key:
                client_options["api_key"] = api_key
        elif client_options is None:
            client_options = {} if not api_key else {"api_key": api_key}
        elif api_key:
            client_options.api_key = api_key

        use_dp_interconnect = _resolve_direct_path_interconnect(
            attempt_direct_path_xds_over_interconnect
        )

        self._grpc_client = self._create_gapic_client(
            credentials=credentials,
            client_info=client_info,
            client_options=client_options,
            attempt_direct_path=attempt_direct_path,
            attempt_direct_path_xds_over_interconnect=use_dp_interconnect,
        )

    @property
    def metrics_enabled(self) -> bool:
        """(Experimental) Returns ``True`` if OpenTelemetry metrics recording is active for this client."""
        return self._metrics_enabled

    @property
    def debug_metrics_enabled(self) -> bool:
        """(Experimental) Returns ``True`` if debug metrics recording is active for this client."""
        return self._debug_metrics_enabled

    def _create_gapic_client(
        self,
        credentials=None,
        client_info=None,
        client_options=None,
        attempt_direct_path=True,
        attempt_direct_path_xds_over_interconnect=False,
    ):
        """Creates and configures the low-level GAPIC `storage_v2` client."""
        transport_cls = storage_v2.StorageClient.get_transport_class("grpc")

        if attempt_direct_path_xds_over_interconnect:
            host = _DEFAULT_HOST
            quota_project_id = None
            if isinstance(client_options, dict):
                host = client_options.get("api_endpoint") or _DEFAULT_HOST
                quota_project_id = client_options.get("quota_project_id")
            elif client_options is not None:
                host = getattr(client_options, "api_endpoint", None) or _DEFAULT_HOST
                quota_project_id = getattr(client_options, "quota_project_id", None)
            host = _rewrite_host_for_interconnect(host)
            channel_kwargs = {
                "host": host,
                "credentials": credentials,
                "attempt_direct_path": True,
                "attempt_direct_path_xds_over_interconnect": True,
            }
            if quota_project_id is not None:
                channel_kwargs["quota_project_id"] = quota_project_id
            channel = transport_cls.create_channel(**channel_kwargs)
        else:
            channel = transport_cls.create_channel(
                attempt_direct_path=attempt_direct_path
            )

        transport = transport_cls(credentials=credentials, channel=channel)

        return storage_v2.StorageClient(
            credentials=credentials,
            transport=transport,
            client_info=client_info,
            client_options=client_options,
        )

    @property
    def grpc_client(self):
        """The underlying gRPC client.

        This property gives users direct access to the `storage_v2.StorageClient`
         instance. This can be useful for accessing
        newly added or experimental RPCs that are not yet exposed through
        the high-level GrpcClient.

        Returns:
            google.cloud.storage_v2.StorageClient: The configured GAPIC client.
        """
        return self._grpc_client
