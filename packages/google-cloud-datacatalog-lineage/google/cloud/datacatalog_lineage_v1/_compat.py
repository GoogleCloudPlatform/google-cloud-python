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
"""A compatibility module for older versions of google-api-core."""

import json
import os
import uuid
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

import google.protobuf.message

if TYPE_CHECKING:  # pragma: NO COVER
    import proto  # type: ignore[import-untyped]

from urllib.parse import urlparse, urlunparse

from google.api_core import path_template
from google.api_core.universe import EmptyUniverseError
from google.auth.exceptions import MutualTLSChannelError
from google.protobuf import json_format

try:
    # note: `#type: ignore` is added because the return type for `should_use_client_cert`
    # is different than that of the fallback implementation below. This will be removed once
    # we bump the minimum supported version of google-auth.
    from google.auth.transport.mtls import should_use_client_cert  # type: ignore
except ImportError:  # pragma: NO COVER

    def should_use_client_cert():
        """Returns whether client certificate should be used for mTLS."""
        use_client_cert = os.getenv(
            "GOOGLE_API_USE_CLIENT_CERTIFICATE", "false"
        ).lower()
        if use_client_cert not in ("true", "false"):
            raise ValueError(
                "Environment variable `GOOGLE_API_USE_CLIENT_CERTIFICATE` must be"
                " either `true` or `false`"
            )
        return use_client_cert == "true"


def read_environment_variables():
    """Returns the environment variables used by the client.

    Returns:
        Tuple[bool, str, str]: returns the GOOGLE_API_USE_CLIENT_CERTIFICATE,
        GOOGLE_API_USE_MTLS_ENDPOINT, and GOOGLE_CLOUD_UNIVERSE_DOMAIN environment variables.

    Raises:
        ValueError: If GOOGLE_API_USE_CLIENT_CERTIFICATE is not
            any of ["true", "false"].
        google.auth.exceptions.MutualTLSChannelError: If GOOGLE_API_USE_MTLS_ENDPOINT
            is not any of ["auto", "never", "always"].
    """
    use_client_cert = should_use_client_cert()
    use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto").lower()
    universe_domain_env = os.getenv("GOOGLE_CLOUD_UNIVERSE_DOMAIN")
    if use_mtls_endpoint not in ("auto", "never", "always"):
        raise MutualTLSChannelError(
            "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`,"
            " `auto` or `always`"
        )
    return use_client_cert, use_mtls_endpoint, universe_domain_env


DEFAULT_UNIVERSE = "googleapis.com"

try:
    from google.api_core.universe import get_default_mtls_endpoint
except ImportError:  # pragma: NO COVER

    def get_default_mtls_endpoint(api_endpoint: Optional[str]) -> Optional[str]:
        """Converts api endpoint to mTLS endpoint.

        Convert "*.sandbox.googleapis.com" and "*.googleapis.com" to
        "*.mtls.sandbox.googleapis.com" and "*.mtls.googleapis.com" respectively.
        Other URLs (including those that do not match these domain suffixes or
        already contain '.mtls.') are passed through as-is.

        Args:
            api_endpoint (Optional[str]): the api endpoint to convert.

        Returns:
            Optional[str]: converted mTLS api endpoint.
        """
        if not api_endpoint or ".mtls." in api_endpoint.lower():
            return api_endpoint

        has_scheme = "://" in api_endpoint
        if not has_scheme:
            parsed = urlparse("//" + api_endpoint)
        else:
            parsed = urlparse(api_endpoint)

        host = parsed.hostname
        if not host:
            return api_endpoint

        port = f":{parsed.port}" if parsed.port else ""

        lowered_host = host.lower()
        suffix_sandbox = ".sandbox.googleapis.com"
        suffix_google = ".googleapis.com"
        if lowered_host.endswith(suffix_sandbox):
            new_host = host[: -len(suffix_sandbox)] + ".mtls.sandbox.googleapis.com"
        elif lowered_host.endswith(suffix_google):
            new_host = host[: -len(suffix_google)] + ".mtls.googleapis.com"
        else:
            return api_endpoint

        netloc = new_host + port
        new_parsed = parsed._replace(netloc=netloc)

        if not has_scheme:
            return urlunparse(new_parsed)[2:]
        else:
            return urlunparse(new_parsed)


try:
    from google.api_core.universe import get_api_endpoint
except ImportError:  # pragma: NO COVER

    def get_api_endpoint(
        api_override: Optional[str],
        universe_domain: str,
        default_universe: str,
        default_mtls_endpoint: Optional[str],
        default_endpoint_template: str,
        use_mtls: bool,
    ) -> str:
        """Return the API endpoint used by the client.

        Args:
            api_override (Optional[str]): The API endpoint override. If specified,
                this is always returned.
            universe_domain (str): The universe domain used by the client.
            default_universe (str): The default universe domain.
            default_mtls_endpoint (Optional[str]): The default mTLS endpoint.
            default_endpoint_template (str): The default endpoint template containing
                a placeholder `{UNIVERSE_DOMAIN}`.
            use_mtls (bool): Whether to use the mTLS endpoint.

        Returns:
            str: The API endpoint to be used by the client.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mTLS is requested but
                not supported in the configured universe domain.
            ValueError: If mTLS is requested but no mTLS endpoint is available.
        """
        if api_override is not None:
            return api_override

        if use_mtls:
            if universe_domain.lower() != default_universe.lower():
                raise MutualTLSChannelError(
                    f"mTLS is not supported in any universe other than {default_universe}."
                )
            if not default_mtls_endpoint:
                raise ValueError("mTLS endpoint is not available.")
            return default_mtls_endpoint
        else:
            return default_endpoint_template.format(UNIVERSE_DOMAIN=universe_domain)


try:
    from google.api_core.universe import get_universe_domain
except ImportError:  # pragma: NO COVER

    def get_universe_domain(
        *potential_universes: Optional[str],
        default_universe: str,
    ) -> str:
        """Return the universe domain used by the client.

        Args:
            *potential_universes (Optional[str]): Potential universe domains in order of preference.
            default_universe (str): The default universe domain.

        Returns:
            str: The universe domain to be used by the client.

        Raises:
            EmptyUniverseError: If the resolved universe domain is an empty string.
        """
        resolved = next(
            (x.strip() for x in potential_universes if x is not None),
            default_universe,
        )

        if not resolved:
            raise EmptyUniverseError()
        return resolved


try:
    import google.api_core
    from google.api_core.gapic_v1.requests import setup_request_id

    if tuple(map(int, google.api_core.__version__.split(".")[:2])) < (
        2,
        34,
    ):  # pragma: NO COVER
        # google-api-core < 2.34.0 had a bug in setup_request_id for proto-plus messages.
        # Fall back to the local compatibility implementation for older versions.
        raise ImportError
except ImportError:  # pragma: NO COVER

    def setup_request_id(
        request: Union[google.protobuf.message.Message, "proto.Message", dict, None],
        field_name: str,
        is_proto3_optional: bool,
    ) -> None:
        """Populate a UUID4 field in the request if it is not already set.

        This helper is used to ensure request idempotency by automatically
        generating a unique identifier (such as `request_id`) for requests
        that support it. If a request is retried, the same identifier can be
        sent on subsequent retries, allowing the server to recognize the retried
        request and prevent duplicate processing (e.g., creating duplicate
        resources).

        Args:
            request (Union[google.protobuf.message.Message, proto.Message, dict, None]): The
                request object or dictionary.
            field_name (str): The name of the field to populate (e.g., "request_id").
            is_proto3_optional (bool): Whether the field supports explicit presence
                (defined with `optional` in proto3 syntax). When True, empty strings ("")
                are preserved as explicit user input per AIP-4235, and UUID auto-population
                occurs only if the field is unset. When False, any empty or falsy value is
                populated with a UUID.
        """
        if request is None:
            return

        # Evaluate whether the field is considered "unset" and needs auto-population.
        #
        # According to AIP-4235, optional request ID fields must be populated
        # if and only if they have explicit presence (`is_proto3_optional=True`)
        # and were not set by the user (i.e. unset). Explicitly provided empty
        # strings ('') must be preserved when `is_proto3_optional=True`.
        should_populate = False
        if isinstance(request, dict):
            if is_proto3_optional:
                # Case 1a: Dictionary request with explicit presence (`is_proto3_optional=True`).
                # Per AIP-4235, auto-populate only if the key is completely missing from
                # the dictionary or its value is explicitly set to None.
                # An explicit empty string ('') must NOT be overwritten.
                should_populate = (
                    field_name not in request or request[field_name] is None
                )
            else:
                # Case 1b: Dictionary request without explicit presence (`is_proto3_optional=False`).
                # Auto-populate if the key is missing, None, or falsy (e.g., empty string '').
                should_populate = not request.get(field_name)
        else:
            # Case 2: Object request (proto-plus wrapper or pure protobuf message).
            if is_proto3_optional:
                # Extract the protobuf from proto-plus if wrapped.
                pure_pb: google.protobuf.message.Message = getattr(
                    request, "_pb", request
                )
                try:
                    should_populate = not pure_pb.HasField(field_name)
                except (AttributeError, ValueError):
                    # Fall back if `HasField` fails or is unsupported.
                    should_populate = getattr(pure_pb, field_name, None) is None
            else:
                # Case 2b: Object request without explicit presence (`is_proto3_optional=False`).
                # Auto-populate if the field value is falsy (None or empty string '').
                should_populate = not bool(getattr(request, field_name, False))

        # If the field was found to be empty, set random id
        if should_populate:
            generated_id = str(uuid.uuid4())
            if isinstance(request, dict):
                request[field_name] = generated_id
            else:
                setattr(request, field_name, generated_id)


try:
    from google.api_core.rest_helpers import transcode_request  # type: ignore
except ImportError:  # pragma: NO COVER

    def transcode_request(
        http_options: List[Dict[str, str]],
        request: Any,
        required_fields_default_values: Optional[Dict[str, Any]] = None,
        rest_numeric_enums: bool = False,
    ) -> Tuple[Dict[str, Any], Optional[str], Dict[str, Any]]:
        """Transcodes a request into HTTP method, URI, body, and query parameters.

        Args:
            http_options (List[Dict[str, str]]): List of HTTP transcoding rules.
            request (Any): The protobuf or proto-plus request message.
            required_fields_default_values (Optional[Dict[str, Any]]): Dictionary
                of required fields default values to merge into query parameters if missing.
            rest_numeric_enums (bool): Whether to encode enums as integers.

        Returns:
            Tuple[Dict[str, Any], Optional[str], Dict[str, Any]]: A tuple containing:
                - The raw transcoded request dictionary (containing keys like 'uri', 'method').
                - The serialized request body JSON string, or None if no body.
                - The query parameters dictionary.
        """
        if request is None:
            raise TypeError("request cannot be None")

        # Convert proto-plus message to its underlying protobuf message if needed
        pb_request = getattr(request, "_pb", request)

        transcoded_request = path_template.transcode(http_options, pb_request)

        body_json = None
        if transcoded_request.get("body") is not None:
            body_json = json_format.MessageToJson(
                transcoded_request["body"],
                use_integers_for_enums=rest_numeric_enums,
            )

        query_params_json = {}
        if transcoded_request.get("query_params") is not None:
            query_params_json = json.loads(
                json_format.MessageToJson(
                    transcoded_request["query_params"],
                    use_integers_for_enums=rest_numeric_enums,
                )
            )

        # If required_fields_default_values is provided, we merge default values for missing
        # required fields into the query parameters.
        if required_fields_default_values:
            for k, v in required_fields_default_values.items():
                if k not in query_params_json:
                    query_params_json[k] = v

        if rest_numeric_enums:
            query_params_json["$alt"] = "json;enum-encoding=int"

        return transcoded_request, body_json, query_params_json
