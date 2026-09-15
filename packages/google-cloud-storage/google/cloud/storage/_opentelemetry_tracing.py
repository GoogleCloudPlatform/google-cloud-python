# Copyright 2024 Google LLC
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

"""Manages OpenTelemetry tracing span creation and handling. This is a PREVIEW FEATURE: Coverage and functionality may change."""

import logging
import os
from urllib.parse import urlparse

from google.api_core import exceptions as api_exceptions
from google.api_core import retry as api_retry

from google.cloud.storage import __version__
from google.cloud.storage.retry import ConditionalRetryPolicy

ENABLE_OTEL_TRACES_ENV_VAR = "ENABLE_GCS_PYTHON_CLIENT_OTEL_TRACES"
_DEFAULT_ENABLE_OTEL_TRACES_VALUE = False
DISABLE_BUCKET_MD_ENV_VAR = "DISABLE_GCS_PYTHON_CLIENT_OTEL_BUCKET_METADATA"


def _parse_bool_env(name: str, default: bool = False) -> bool:
    val = os.environ.get(name, None)
    if val is None:
        return default
    return str(val).strip().lower() in {"1", "true", "yes", "on"}


def _is_bucket_metadata_disabled() -> bool:
    return _parse_bool_env(DISABLE_BUCKET_MD_ENV_VAR, False)


enable_otel_traces = _parse_bool_env(
    ENABLE_OTEL_TRACES_ENV_VAR, _DEFAULT_ENABLE_OTEL_TRACES_VALUE
)
logger = logging.getLogger(__name__)


try:
    from opentelemetry import trace

    HAS_OPENTELEMETRY = True

except ImportError:
    logger.debug(
        "This service is instrumented using OpenTelemetry. "
        "OpenTelemetry or one of its components could not be imported; "
        "please add compatible versions of opentelemetry-api and "
        "opentelemetry-instrumentation packages in order to get Storage "
        "Tracing data."
    )
    HAS_OPENTELEMETRY = False

_default_attributes = {
    "rpc.service": "CloudStorage",
    "rpc.system": "http",
    "user_agent.original": f"gcloud-python/{__version__}",
}

_cloud_trace_adoption_attrs = {
    "gcp.client.service": "storage",
    "gcp.client.version": __version__,
    "gcp.client.repo": "googleapis/python-storage",
}


class _TraceSpanContext:
    """Context manager supporting both sync and async tracing spans."""

    def __init__(
        self,
        name,
        attributes=None,
        client=None,
        api_request=None,
        retry=None,
        rpc_system="http",
    ):
        self.name = name
        self.attributes = attributes
        self.client = client
        self.api_request = api_request
        self.retry = retry
        self.rpc_system = rpc_system
        self._span_cm = None
        self._span = None

    def __enter__(self):
        if not HAS_OPENTELEMETRY or not enable_otel_traces:
            return None

        tracer = trace.get_tracer(__name__)
        final_attributes = _get_final_attributes(
            self.attributes,
            self.client,
            self.api_request,
            self.retry,
            rpc_system=self.rpc_system,
        )
        self._span_cm = tracer.start_as_current_span(
            name=self.name, kind=trace.SpanKind.CLIENT, attributes=final_attributes
        )
        self._span = self._span_cm.__enter__()
        return self._span

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._span_cm is not None:
            if exc_val is not None and isinstance(
                exc_val, api_exceptions.GoogleAPICallError
            ):
                self._span.set_status(trace.Status(trace.StatusCode.ERROR))
                self._span.record_exception(exc_val)
            return self._span_cm.__exit__(exc_type, exc_val, exc_tb)
        return False

    async def __aenter__(self):
        return self.__enter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return self.__exit__(exc_type, exc_val, exc_tb)


def create_trace_span(
    name,
    attributes=None,
    client=None,
    api_request=None,
    retry=None,
    rpc_system="http",
):
    """Creates a context manager for a new span and set it as the current span
    in the configured tracer. Supports both sync and async context managers.
    If no configuration exists yields None."""
    return _TraceSpanContext(
        name=name,
        attributes=attributes,
        client=client,
        api_request=api_request,
        retry=retry,
        rpc_system=rpc_system,
    )


def _get_final_attributes(
    attributes=None, client=None, api_request=None, retry=None, rpc_system="http"
):
    collected_attr = _default_attributes.copy()
    collected_attr["rpc.system"] = rpc_system
    collected_attr.update(_cloud_trace_adoption_attrs)
    if api_request:
        collected_attr.update(_set_api_request_attr(api_request, client))
    if isinstance(retry, api_retry.Retry):
        collected_attr.update(_set_retry_attr(retry))
    if isinstance(retry, ConditionalRetryPolicy):
        collected_attr.update(
            _set_retry_attr(retry.retry_policy, retry.conditional_predicate)
        )
    if attributes:
        collected_attr.update(attributes)
    final_attributes = {k: v for k, v in collected_attr.items() if v is not None}
    return final_attributes


def _set_api_request_attr(request, client):
    attr = {}
    if request.get("method"):
        attr["http.request.method"] = request.get("method")
    if request.get("path"):
        full_url = client._connection.build_api_url(request.get("path"))
        attr.update(_get_opentelemetry_attributes_from_url(full_url, strip_query=True))
    if "timeout" in request:
        attr["connect_timeout,read_timeout"] = str(request.get("timeout"))
    return attr


def _set_retry_attr(retry, conditional_predicate=None):
    predicate = conditional_predicate if conditional_predicate else retry._predicate
    retry_info = f"multiplier{retry._multiplier}/deadline{retry._deadline}/max{retry._maximum}/initial{retry._initial}/predicate{predicate}"
    return {"retry": retry_info}


def _get_opentelemetry_attributes_from_url(url, strip_query=True):
    """Helper to assemble OpenTelemetry span attributes from a URL."""
    u = urlparse(url)
    netloc = u.netloc
    # u.hostname is always lowercase. We parse netloc to preserve casing.
    # netloc format: [userinfo@]host[:port]
    if "@" in netloc:
        netloc = netloc.split("@", 1)[1]
    if ":" in netloc and not netloc.endswith("]"):  # Handle IPv6 literal
        netloc = netloc.split(":", 1)[0]

    attributes = {
        "server.address": netloc,
        "server.port": u.port,
        "url.scheme": u.scheme,
        "url.path": u.path,
    }
    if not strip_query:
        attributes["url.query"] = u.query

    return attributes
