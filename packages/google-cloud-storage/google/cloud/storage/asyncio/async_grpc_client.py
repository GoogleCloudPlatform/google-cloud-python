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

"""An async client for interacting with Google Cloud Storage using the gRPC API."""

import inspect

import grpc
from google.auth import credentials as auth_credentials

from google.cloud import _storage_v2 as storage_v2
from google.cloud._storage_v2.services.storage.transports.base import (
    DEFAULT_CLIENT_INFO,
)
from google.cloud.storage import __version__, _opentelemetry_metrics
from google.cloud.storage.grpc_client import (
    _DEFAULT_HOST,
    _resolve_direct_path_interconnect,
    _rewrite_host_for_interconnect,
)


class _AttemptDirectPathDefault:
    """Sentinel for an omitted ``attempt_direct_path`` (behaves as ``True``).

    It lets the client tell ``AsyncGrpcClient()`` apart from an explicit
    ``AsyncGrpcClient(attempt_direct_path=True)`` (which enforces DirectPath) while the
    public signature still reports ``attempt_direct_path=True``.
    """

    def __bool__(self):
        return True

    def __repr__(self):
        return "True"


_ATTEMPT_DIRECT_PATH_DEFAULT = _AttemptDirectPathDefault()


def _uds_mode():
    """Returns the Rust Core SDK UDS backend mode ("off", "auto" or "force")."""
    from google.cloud.storage.asyncio._uds import _config

    return _config.uds_mode()


def _validate_metadata(metadata):
    """Validates that metadata is a sequence of (key, value) pairs."""
    if metadata is None:
        return
    if not isinstance(metadata, (list, tuple)):
        raise TypeError("metadata must be a list or tuple of (key, value) pairs.")
    for item in metadata:
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            raise ValueError(
                "Each element in metadata must be a list or tuple of exactly 2 strings (key, value)."
            )
        key, value = item
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("Both key and value in metadata pairs must be strings.")


class AsyncGrpcClient:
    """An asynchronous client for interacting with Google Cloud Storage using the gRPC API.

    :type credentials: :class:`~google.auth.credentials.Credentials`
    :param credentials: (Optional) The OAuth2 Credentials to use for this
                        client. If not passed, falls back to the default
                        inferred from the environment.

    :type client_info: :class:`~google.api_core.client_info.ClientInfo`
    :param client_info:
        The client info used to send a user-agent string along with API
        requests. If ``None``, then default info will be used.

    :type client_options: :class:`~google.api_core.client_options.ClientOptions`
    :param client_options: (Optional) Client options used to set user options
        on the client.

    :type attempt_direct_path: bool
    :param attempt_direct_path:
        (Optional) Whether to attempt to use DirectPath for gRPC connections.
        Defaults to ``True``.

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
        credentials=None,
        client_info=None,
        client_options=None,
        *,
        attempt_direct_path=_ATTEMPT_DIRECT_PATH_DEFAULT,
        attempt_direct_path_xds_over_interconnect=False,
        enable_metrics=None,
        enable_debug_metrics=None,
    ):
        # Remember constructor inputs privately (used by the opt-in UDS backend).
        self._credentials = credentials
        self._client_options = client_options
        self._client_info = client_info
        self._direct_path_enforced = (
            attempt_direct_path is not _ATTEMPT_DIRECT_PATH_DEFAULT
            and attempt_direct_path is True
        )
        uds_enabled = _uds_mode() != "off"
        if attempt_direct_path is _ATTEMPT_DIRECT_PATH_DEFAULT:
            # The Rust Core SDK only supports gRPC CloudPath; when its UDS backend is
            # enabled, the un-enforced default uses CloudPath for the GAPIC (non-bidi)
            # calls too. With the backend off, the default stays `True` (unchanged).
            attempt_direct_path = not uds_enabled
        if uds_enabled:
            from google.cloud.storage.asyncio._uds import _config

            _config.check_direct_path_not_enforced(
                self._direct_path_enforced, client_options
            )
        self._attempt_direct_path = attempt_direct_path
        self._enable_metrics = enable_metrics
        self._enable_debug_metrics = enable_debug_metrics
        self._metrics_enabled = _opentelemetry_metrics.is_metrics_enabled(
            enable_metrics
        )
        self._debug_metrics_enabled = _opentelemetry_metrics.is_debug_metrics_enabled(
            enable_debug_metrics
        )

        if isinstance(credentials, auth_credentials.AnonymousCredentials):
            if client_options is None or client_options.api_endpoint is None:
                raise ValueError(
                    "Either client_options or `client_option.api_endpoint` is None. Please provide api_endpoint when `AnonymousCredentials` is used "
                )
            self._grpc_client = self._create_anonymous_client(
                client_options, credentials
            )
            return

        if client_info is None:
            client_info = DEFAULT_CLIENT_INFO
        client_info.client_library_version = __version__
        if client_info.user_agent is None:
            client_info.user_agent = ""
        agent_version = f"gcloud-python/{__version__}"
        if agent_version not in client_info.user_agent:
            client_info.user_agent += f" {agent_version} "
        self._client_info = client_info

        use_dp_interconnect = _resolve_direct_path_interconnect(
            attempt_direct_path_xds_over_interconnect
        )
        if uds_enabled and use_dp_interconnect:
            from google.cloud.storage.asyncio._uds import _config

            raise _config._core_errors()(
                "DirectPath over Cloud Interconnect is enforced but the Rust Core SDK "
                "UDS backend only supports gRPC CloudPath."
            )

        self._grpc_client = self._create_async_grpc_client(
            credentials=credentials,
            client_info=client_info,
            client_options=client_options,
            attempt_direct_path=attempt_direct_path,
            attempt_direct_path_xds_over_interconnect=use_dp_interconnect,
        )
        if uds_enabled and _prewarm_requested():
            _prewarm_uds(self)

    @property
    def metrics_enabled(self) -> bool:
        """(Experimental) Returns ``True`` if OpenTelemetry metrics recording is active for this client."""
        return self._metrics_enabled

    @property
    def debug_metrics_enabled(self) -> bool:
        """(Experimental) Returns ``True`` if debug metrics recording is active for this client."""
        return self._debug_metrics_enabled

    def _create_anonymous_client(self, client_options, credentials):
        channel = grpc.aio.insecure_channel(client_options.api_endpoint)
        transport = storage_v2.services.storage.transports.StorageGrpcAsyncIOTransport(
            channel=channel, credentials=credentials
        )
        return storage_v2.StorageAsyncClient(transport=transport)

    @classmethod
    def _create_insecure_grpc_client(cls, client_options):
        return cls(
            credentials=auth_credentials.AnonymousCredentials(),
            client_options=client_options,
            attempt_direct_path=False,
        )

    def _create_async_grpc_client(
        self,
        credentials=None,
        client_info=None,
        client_options=None,
        attempt_direct_path=True,
        attempt_direct_path_xds_over_interconnect=False,
    ):
        transport_cls = storage_v2.StorageAsyncClient.get_transport_class(
            "grpc_asyncio"
        )

        primary_user_agent = client_info.to_user_agent()

        host = _DEFAULT_HOST
        quota_project_id = None
        if isinstance(client_options, dict):
            host = client_options.get("api_endpoint") or _DEFAULT_HOST
            quota_project_id = client_options.get("quota_project_id")
        elif client_options:
            host = getattr(client_options, "api_endpoint", None) or _DEFAULT_HOST
            quota_project_id = getattr(client_options, "quota_project_id", None)

        if attempt_direct_path_xds_over_interconnect:
            host = _rewrite_host_for_interconnect(host)
            channel = transport_cls.create_channel(
                host=host,
                quota_project_id=quota_project_id,
                attempt_direct_path=True,
                attempt_direct_path_xds_over_interconnect=True,
                credentials=credentials,
                options=(("grpc.primary_user_agent", primary_user_agent),),
            )
        else:
            channel = transport_cls.create_channel(
                host=host,
                quota_project_id=quota_project_id,
                attempt_direct_path=attempt_direct_path,
                credentials=credentials,
                options=(("grpc.primary_user_agent", primary_user_agent),),
            )
        transport = transport_cls(channel=channel)

        return storage_v2.StorageAsyncClient(
            transport=transport,
            client_info=client_info,
            client_options=client_options,
        )

    @property
    def grpc_client(self):
        """The underlying gRPC client.

        This property gives users direct access to the `_storage_v2.StorageAsyncClient`
         instance. This can be useful for accessing
        newly added or experimental RPCs that are not yet exposed through
        the high-level GrpcClient.
        Returns:
            google.cloud._storage_v2.StorageAsyncClient: The configured GAPIC client.
        """
        return self._grpc_client

    async def delete_object(
        self,
        bucket_name,
        object_name,
        generation=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        metadata=(),
        timeout=None,
        retry=None,
        **kwargs,
    ):
        """Deletes an object and its metadata.

        :type bucket_name: str
        :param bucket_name: The name of the bucket in which the object resides.

        :type object_name: str
        :param object_name: The name of the object to delete.

        :type generation: int
        :param generation:
            (Optional) If present, permanently deletes a specific generation
            of an object.

        :type if_generation_match: int
        :param if_generation_match: (Optional)

        :type if_generation_not_match: int
        :param if_generation_not_match: (Optional)

        :type if_metageneration_match: int
        :param if_metageneration_match: (Optional)

        :type if_metageneration_not_match: int
        :param if_metageneration_not_match: (Optional)

        :type metadata: Sequence[Tuple[str, str]]
        :param metadata: (Optional) Additional metadata that is provided to the method.

        :type timeout: float or None
        :param timeout:
            (Optional) The amount of time, in seconds, to wait for the request to
            complete.

        :type retry: :class:`~google.api_core.retry_async.AsyncRetry` or None
        :param retry: (Optional) Designation of what errors, if any, should be retried.
        """
        _validate_metadata(metadata)
        # The gRPC API requires the bucket name to be in the format "projects/_/buckets/bucket_name"
        bucket_path = f"projects/_/buckets/{bucket_name}"
        request = storage_v2.DeleteObjectRequest(
            bucket=bucket_path,
            object=object_name,
            generation=generation,
            if_generation_match=if_generation_match,
            if_generation_not_match=if_generation_not_match,
            if_metageneration_match=if_metageneration_match,
            if_metageneration_not_match=if_metageneration_not_match,
            **kwargs,
        )
        await self._grpc_client.delete_object(
            request=request,
            metadata=metadata,
            timeout=timeout,
            retry=retry,
        )

    async def get_object(
        self,
        bucket_name,
        object_name,
        generation=None,
        if_generation_match=None,
        if_generation_not_match=None,
        if_metageneration_match=None,
        if_metageneration_not_match=None,
        soft_deleted=None,
        metadata=(),
        timeout=None,
        retry=None,
        **kwargs,
    ):
        """Retrieves an object's metadata.

        In the gRPC API, this is performed by the GetObject RPC, which
        returns the object resource (metadata) without the object's data.

        :type bucket_name: str
        :param bucket_name: The name of the bucket in which the object resides.

        :type object_name: str
        :param object_name: The name of the object.

        :type generation: int
        :param generation:
            (Optional) If present, selects a specific generation of an object.

        :type if_generation_match: int
        :param if_generation_match: (Optional) Precondition for object generation match.

        :type if_generation_not_match: int
        :param if_generation_not_match: (Optional) Precondition for object generation mismatch.

        :type if_metageneration_match: int
        :param if_metageneration_match: (Optional) Precondition for metageneration match.

        :type if_metageneration_not_match: int
        :param if_metageneration_not_match: (Optional) Precondition for metageneration mismatch.

        :type soft_deleted: bool
        :param soft_deleted:
            (Optional) If True, return the soft-deleted version of this object.

        :type metadata: Sequence[Tuple[str, str]]
        :param metadata: (Optional) Additional metadata that is provided to the method.

        :type timeout: float or None
        :param timeout:
            (Optional) The amount of time, in seconds, to wait for the request to
            complete.

        :type retry: :class:`~google.api_core.retry_async.AsyncRetry` or None
        :param retry: (Optional) Designation of what errors, if any, should be retried.

        :rtype: :class:`google.cloud._storage_v2.types.Object`
        :returns: The object metadata resource.
        """
        _validate_metadata(metadata)
        bucket_path = f"projects/_/buckets/{bucket_name}"

        request = storage_v2.GetObjectRequest(
            bucket=bucket_path,
            object=object_name,
            generation=generation,
            if_generation_match=if_generation_match,
            if_generation_not_match=if_generation_not_match,
            if_metageneration_match=if_metageneration_match,
            if_metageneration_not_match=if_metageneration_not_match,
            soft_deleted=soft_deleted or False,
            **kwargs,
        )

        # Calls the underlying GAPIC StorageAsyncClient.get_object method
        return await self._grpc_client.get_object(
            request=request,
            metadata=metadata,
            timeout=timeout,
            retry=retry,
        )


# Keep the public signature byte-identical (`attempt_direct_path=True`) while the
# implementation uses a private sentinel to detect an explicit `True`.
_INIT_SIGNATURE = inspect.signature(AsyncGrpcClient.__init__)
AsyncGrpcClient.__init__.__signature__ = _INIT_SIGNATURE.replace(
    parameters=[
        p.replace(default=True) if p.name == "attempt_direct_path" else p
        for p in _INIT_SIGNATURE.parameters.values()
    ]
)


def _prewarm_requested():
    import os

    return os.environ.get("GOOGLE_CLOUD_STORAGE_UDS_PREWARM", "").strip().lower() in (
        "1",
        "true",
    )


def _prewarm_uds(client):
    """Starts (non-blocking) the UDS daemon attach-or-spawn for ``client``."""
    import threading

    def _run():
        try:
            from google.cloud.storage.asyncio._uds import runtime, server_manager

            endpoint, _anon, _creds, _quota = runtime._client_config(client)
            server_manager.ServerManager(endpoint=endpoint).ensure_server()
        except Exception as exc:  # pragma: NO COVER - best effort
            import logging

            logging.getLogger(__name__).debug("UDS prewarm failed: %s", exc)

    threading.Thread(target=_run, name="gcs-uds-prewarm", daemon=True).start()
