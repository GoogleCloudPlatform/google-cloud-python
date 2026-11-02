# Copyright 2014 Google LLC
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

"""Create / interact with Google Cloud Storage connections."""

import functools
import logging
import re
import time
from contextvars import ContextVar

from google.api_core import exceptions as api_exceptions
from google.cloud.exceptions import NotFound

from google.cloud import _http
from google.cloud.storage import __version__, _helpers, _opentelemetry_metrics
from google.cloud.storage._opentelemetry_tracing import (
    HAS_OPENTELEMETRY,
    _is_bucket_metadata_disabled,
    create_trace_span,
    enable_otel_traces,
)

logger = logging.getLogger(__name__)

_IN_API_REQUEST = ContextVar("_gcs_in_api_request", default=False)
_LAST_ATTEMPT_RESPONSE = ContextVar("_gcs_last_attempt_response", default=None)


class Connection(_http.JSONConnection):
    """A connection to Google Cloud Storage via the JSON REST API.

    Mutual TLS will be enabled if the "GOOGLE_API_USE_CLIENT_CERTIFICATE"
    environment variable is set to the exact string "true" (case-sensitive).

    Mutual TLS is not compatible with any API endpoint or universe domain
    override at this time. If such settings are enabled along with
    "GOOGLE_API_USE_CLIENT_CERTIFICATE", a ValueError will be raised.

    :type client: :class:`~google.cloud.storage.client.Client`
    :param client: The client that owns the current connection.

    :type client_info: :class:`~google.api_core.client_info.ClientInfo`
    :param client_info: (Optional) instance used to generate user agent.

    :type api_endpoint: str
    :param api_endpoint: (Optional) api endpoint to use.
    """

    DEFAULT_API_ENDPOINT = _helpers._get_default_storage_base_url()
    DEFAULT_API_MTLS_ENDPOINT = "https://storage.mtls.googleapis.com"
    _IS_BATCH = False

    def __init__(self, client, client_info=None, api_endpoint=None):
        super(Connection, self).__init__(client, client_info)
        self.API_BASE_URL = api_endpoint or self.DEFAULT_API_ENDPOINT
        self.API_BASE_MTLS_URL = self.DEFAULT_API_MTLS_ENDPOINT
        self.ALLOW_AUTO_SWITCH_TO_MTLS_URL = api_endpoint is None
        self._client_info.client_library_version = __version__

        # TODO: When metrics all use gccl, this should be removed #9552
        if self._client_info.user_agent is None:  # pragma: no branch
            self._client_info.user_agent = ""
        agent_version = f"gcloud-python/{__version__}"
        if agent_version not in self._client_info.user_agent:
            self._client_info.user_agent += f" {agent_version} "

    API_VERSION = _helpers._API_VERSION
    """The version of the API, used in building the API call's URL."""

    API_URL_TEMPLATE = "{api_base_url}/storage/{api_version}{path}"
    """A template for the URL of a particular API call."""

    def _make_request(self, method, url, *args, **kwargs):
        if (
            getattr(self, "_IS_BATCH", False) is True
            or _helpers._SUPPRESS_INTERNAL_METRICS.get()
        ):
            return super(Connection, self)._make_request(method, url, *args, **kwargs)

        recorder = _opentelemetry_metrics.get_active_recorder(self._client)
        if recorder is None:
            return super(Connection, self)._make_request(method, url, *args, **kwargs)

        if _IN_API_REQUEST.get():
            req_start = time.perf_counter()
            response = super(Connection, self)._make_request(
                method, url, *args, **kwargs
            )
            _LAST_ATTEMPT_RESPONSE.set((response, time.perf_counter() - req_start, url))
            return response

        url_template = _opentelemetry_metrics.normalize_url_template(url)
        attempt_start = time.perf_counter()
        try:
            response = super(Connection, self)._make_request(
                method, url, *args, **kwargs
            )
        except BaseException as exc:
            recorder.record_http_attempt(
                duration=time.perf_counter() - attempt_start,
                http_method=method,
                url_template=url_template,
                status_code=None,
                error_type=_opentelemetry_metrics.classify_error_type(exc),
                network_path="cloudpath",
            )
            raise

        duration = time.perf_counter() - attempt_start
        raw_sc = getattr(response, "status_code", None)
        status_code = (
            raw_sc
            if (isinstance(raw_sc, int) and not isinstance(raw_sc, bool))
            else None
        )
        if status_code is not None:
            recorder.record_ttfb(duration, network_path="cloudpath")
        error_type = _opentelemetry_metrics.classify_error_type(
            None, status_code=status_code
        )
        recorder.record_http_attempt(
            duration=duration,
            http_method=method,
            url_template=url_template,
            status_code=status_code,
            error_type=error_type,
            network_path="cloudpath",
        )
        return response

    def api_request(self, *args, **kwargs):
        retry = kwargs.pop("retry", None)
        invocation_id = _helpers._get_invocation_id()
        kwargs["extra_api_info"] = invocation_id
        span_attributes = {
            "gccl-invocation-id": invocation_id,
        }
        client = self._client
        if (
            HAS_OPENTELEMETRY
            and enable_otel_traces
            and hasattr(client, "_bucket_metadata_cache")
            and client._bucket_metadata_cache
            and not _is_bucket_metadata_disabled()
        ):
            path = kwargs.get("path") or ""
            match = re.search(r"/b/([^/?#]+)", path)
            if match:
                try:
                    cached = client._bucket_metadata_cache.get(match.group(1))
                    if cached and isinstance(cached, tuple) and len(cached) == 2:
                        dest_id, loc = cached
                        span_attributes["gcp.resource.destination.id"] = dest_id
                        span_attributes["gcp.resource.destination.location"] = loc
                except Exception as e:
                    logger.debug(f"Failed cache.get_or_queue_fetch in api_request: {e}")

        base_call = functools.partial(
            super(Connection, self).api_request, *args, **kwargs
        )
        recorder = (
            None
            if (
                getattr(self, "_IS_BATCH", False) is True
                or _helpers._SUPPRESS_INTERNAL_METRICS.get()
            )
            else _opentelemetry_metrics.get_active_recorder(client)
        )

        if recorder is not None:
            http_method = args[0] if len(args) >= 1 else kwargs.get("method", "")
            raw_path = args[1] if len(args) >= 2 else kwargs.get("path", "")
            fallback_template = _opentelemetry_metrics.normalize_url_template(raw_path)

            def _timed_attempt():
                _LAST_ATTEMPT_RESPONSE.set(None)
                attempt_start = time.perf_counter()
                try:
                    result = base_call()
                except BaseException as exc:
                    duration = time.perf_counter() - attempt_start
                    stashed = _LAST_ATTEMPT_RESPONSE.get()
                    _LAST_ATTEMPT_RESPONSE.set(None)
                    if stashed is not None:
                        resp, ttfb_dur, req_url = stashed
                        raw_sc = getattr(resp, "status_code", None)
                        status_code = (
                            raw_sc
                            if (
                                isinstance(raw_sc, int) and not isinstance(raw_sc, bool)
                            )
                            else None
                        )
                        url_template = (
                            _opentelemetry_metrics.normalize_url_template(req_url)
                            if req_url
                            else fallback_template
                        )
                        if status_code is not None:
                            recorder.record_ttfb(ttfb_dur, network_path="cloudpath")
                        err_type = _opentelemetry_metrics.classify_error_type(
                            exc, status_code=status_code
                        )
                    else:
                        status_code = None
                        url_template = fallback_template
                        err_type = _opentelemetry_metrics.classify_error_type(exc)
                    recorder.record_http_attempt(
                        duration=duration,
                        http_method=http_method,
                        url_template=url_template,
                        status_code=status_code,
                        error_type=err_type,
                        network_path="cloudpath",
                    )
                    raise

                duration = time.perf_counter() - attempt_start
                stashed = _LAST_ATTEMPT_RESPONSE.get()
                _LAST_ATTEMPT_RESPONSE.set(None)
                status_code = 200
                url_template = fallback_template
                if stashed is not None:
                    resp, ttfb_dur, req_url = stashed
                    raw_sc = getattr(resp, "status_code", None)
                    status_code = (
                        raw_sc
                        if (isinstance(raw_sc, int) and not isinstance(raw_sc, bool))
                        else None
                    )
                    if req_url:
                        url_template = _opentelemetry_metrics.normalize_url_template(
                            req_url
                        )
                    if status_code is not None:
                        recorder.record_ttfb(ttfb_dur, network_path="cloudpath")
                else:
                    recorder.record_ttfb(duration, network_path="cloudpath")

                recorder.record_http_attempt(
                    duration=duration,
                    http_method=http_method,
                    url_template=url_template,
                    status_code=status_code,
                    error_type="OK",
                    network_path="cloudpath",
                )
                return result

            call = _timed_attempt
        else:
            call = base_call

        with create_trace_span(
            name="Storage.Connection.api_request",
            attributes=span_attributes,
            client=client,
            api_request=kwargs,
            retry=retry,
        ):
            if retry:
                # If this is a ConditionalRetryPolicy, check conditions.
                try:
                    retry = retry.get_retry_policy_if_conditions_met(**kwargs)
                except AttributeError:  # This is not a ConditionalRetryPolicy.
                    pass
                if retry:
                    call = retry(call)
            in_api_token = _IN_API_REQUEST.set(True) if recorder is not None else None
            try:
                return call()
            except (NotFound, api_exceptions.NotFound):
                if (
                    HAS_OPENTELEMETRY
                    and enable_otel_traces
                    and hasattr(client, "_bucket_metadata_cache")
                    and client._bucket_metadata_cache
                ):
                    path = kwargs.get("path") or ""
                    match = re.search(r"/b/([^/?#]+)", path)
                    if match:
                        try:
                            client._bucket_metadata_cache.check_and_evict(
                                match.group(1)
                            )
                        except Exception as e:
                            logger.debug(
                                f"Failed cache.check_and_evict on 404 in api_request: {e}"
                            )
                raise
            finally:
                if in_api_token is not None:
                    _IN_API_REQUEST.reset(in_api_token)
                    _LAST_ATTEMPT_RESPONSE.set(None)
                    current_op = _opentelemetry_metrics.get_current_operation()
                    if current_op is not None:
                        current_op.last_failure_error_type = None
