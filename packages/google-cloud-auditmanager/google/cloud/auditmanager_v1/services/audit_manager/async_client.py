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
import logging as std_logging
import re
from collections import OrderedDict
from typing import (
    Callable,
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.auditmanager_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.auditmanager_v1.services.audit_manager import pagers
from google.cloud.auditmanager_v1.types import auditmanager

from .client import AuditManagerClient
from .transports.base import DEFAULT_CLIENT_INFO, AuditManagerTransport
from .transports.grpc_asyncio import AuditManagerGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class AuditManagerAsyncClient:
    """Service describing handlers for resources"""

    _client: AuditManagerClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = AuditManagerClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = AuditManagerClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = AuditManagerClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = AuditManagerClient._DEFAULT_UNIVERSE

    audit_report_path = staticmethod(AuditManagerClient.audit_report_path)
    parse_audit_report_path = staticmethod(AuditManagerClient.parse_audit_report_path)
    audit_schedule_path = staticmethod(AuditManagerClient.audit_schedule_path)
    parse_audit_schedule_path = staticmethod(
        AuditManagerClient.parse_audit_schedule_path
    )
    audit_scope_report_path = staticmethod(AuditManagerClient.audit_scope_report_path)
    parse_audit_scope_report_path = staticmethod(
        AuditManagerClient.parse_audit_scope_report_path
    )
    enrollment_path = staticmethod(AuditManagerClient.enrollment_path)
    parse_enrollment_path = staticmethod(AuditManagerClient.parse_enrollment_path)
    enrollment_status_scope_path = staticmethod(
        AuditManagerClient.enrollment_status_scope_path
    )
    parse_enrollment_status_scope_path = staticmethod(
        AuditManagerClient.parse_enrollment_status_scope_path
    )
    resource_enrollment_status_path = staticmethod(
        AuditManagerClient.resource_enrollment_status_path
    )
    parse_resource_enrollment_status_path = staticmethod(
        AuditManagerClient.parse_resource_enrollment_status_path
    )
    standard_path = staticmethod(AuditManagerClient.standard_path)
    parse_standard_path = staticmethod(AuditManagerClient.parse_standard_path)
    common_billing_account_path = staticmethod(
        AuditManagerClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        AuditManagerClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(AuditManagerClient.common_folder_path)
    parse_common_folder_path = staticmethod(AuditManagerClient.parse_common_folder_path)
    common_organization_path = staticmethod(AuditManagerClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        AuditManagerClient.parse_common_organization_path
    )
    common_project_path = staticmethod(AuditManagerClient.common_project_path)
    parse_common_project_path = staticmethod(
        AuditManagerClient.parse_common_project_path
    )
    common_location_path = staticmethod(AuditManagerClient.common_location_path)
    parse_common_location_path = staticmethod(
        AuditManagerClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AuditManagerAsyncClient: The constructed client.
        """
        sa_info_func = (
            AuditManagerClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(AuditManagerAsyncClient, info, *args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AuditManagerAsyncClient: The constructed client.
        """
        sa_file_func = (
            AuditManagerClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(AuditManagerAsyncClient, filename, *args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return AuditManagerClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> AuditManagerTransport:
        """Returns the transport used by the client instance.

        Returns:
            AuditManagerTransport: The transport used by the client instance.
        """
        return self._client.transport

    @property
    def api_endpoint(self) -> str:
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._client._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used
                by the client instance.
        """
        return self._client._universe_domain

    get_transport_class = AuditManagerClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, AuditManagerTransport, Callable[..., AuditManagerTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the audit manager async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,AuditManagerTransport,Callable[..., AuditManagerTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the AuditManagerTransport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = AuditManagerClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.auditmanager_v1.AuditManagerAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                    "universeDomain": getattr(
                        self._client._transport._credentials, "universe_domain", ""
                    ),
                    "credentialsType": f"{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}",
                    "credentialsInfo": getattr(
                        self.transport._credentials, "get_cred_info", lambda: None
                    )(),
                }
                if hasattr(self._client._transport, "_credentials")
                else {
                    "serviceName": "google.cloud.auditmanager.v1.AuditManager",
                    "credentialsType": None,
                },
            )

    async def create_audit_schedule(
        self,
        request: Optional[Union[auditmanager.CreateAuditScheduleRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        audit_schedule: Optional[auditmanager.AuditSchedule] = None,
        audit_schedule_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.AuditSchedule:
        r"""Creates a new audit schedule in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_create_audit_schedule():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                audit_schedule = auditmanager_v1.AuditSchedule()
                audit_schedule.gcs_uri = "gcs_uri_value"
                audit_schedule.compliance_framework = "compliance_framework_value"
                audit_schedule.report_format = "AUDIT_REPORT_FORMAT_ODF"
                audit_schedule.schedule_config.frequency = "ANNUALLY"

                request = auditmanager_v1.CreateAuditScheduleRequest(
                    parent="parent_value",
                    audit_schedule=audit_schedule,
                    audit_schedule_id="audit_schedule_id_value",
                )

                # Make the request
                response = await client.create_audit_schedule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.CreateAuditScheduleRequest, dict]]):
                The request object. Request message for
                [CreateAuditSchedule][google.cloud.auditmanager.v1.AuditManager.CreateAuditSchedule].
            parent (:class:`str`):
                Required. Project or folder that this audit schedule is
                for, in one of the following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audit_schedule (:class:`google.cloud.auditmanager_v1.types.AuditSchedule`):
                Required. Audit schedule to create.
                This corresponds to the ``audit_schedule`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audit_schedule_id (:class:`str`):
                Required. ID to use for the audit
                schedule, which becomes the final
                component of the audit schedule's
                resource name.

                This corresponds to the ``audit_schedule_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.auditmanager_v1.types.AuditSchedule:
                An audit schedule, in one of the following formats:

                   - projects/{project}/locations/{location}/auditSchedules/{audit_schedule}
                   - folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, audit_schedule, audit_schedule_id]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.CreateAuditScheduleRequest):
            request = auditmanager.CreateAuditScheduleRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if audit_schedule is not None:
            request.audit_schedule = audit_schedule
        if audit_schedule_id is not None:
            request.audit_schedule_id = audit_schedule_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_audit_schedule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_audit_schedule(
        self,
        request: Optional[Union[auditmanager.UpdateAuditScheduleRequest, dict]] = None,
        *,
        audit_schedule: Optional[auditmanager.AuditSchedule] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.AuditSchedule:
        r"""Updates an existing audit schedule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_update_audit_schedule():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                audit_schedule = auditmanager_v1.AuditSchedule()
                audit_schedule.gcs_uri = "gcs_uri_value"
                audit_schedule.compliance_framework = "compliance_framework_value"
                audit_schedule.report_format = "AUDIT_REPORT_FORMAT_ODF"
                audit_schedule.schedule_config.frequency = "ANNUALLY"

                request = auditmanager_v1.UpdateAuditScheduleRequest(
                    audit_schedule=audit_schedule,
                )

                # Make the request
                response = await client.update_audit_schedule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.UpdateAuditScheduleRequest, dict]]):
                The request object. Request message for
                [UpdateAuditSchedule][google.cloud.auditmanager.v1.AuditManager.UpdateAuditSchedule].
            audit_schedule (:class:`google.cloud.auditmanager_v1.types.AuditSchedule`):
                Required. Audit schedule to update.
                This corresponds to the ``audit_schedule`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. List of fields to update.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.auditmanager_v1.types.AuditSchedule:
                An audit schedule, in one of the following formats:

                   - projects/{project}/locations/{location}/auditSchedules/{audit_schedule}
                   - folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [audit_schedule, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.UpdateAuditScheduleRequest):
            request = auditmanager.UpdateAuditScheduleRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if audit_schedule is not None:
            request.audit_schedule = audit_schedule
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_audit_schedule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("audit_schedule.name", request.audit_schedule.name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_audit_schedule(
        self,
        request: Optional[Union[auditmanager.GetAuditScheduleRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.AuditSchedule:
        r"""Gets details of a single audit schedule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_get_audit_schedule():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                request = auditmanager_v1.GetAuditScheduleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_audit_schedule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.GetAuditScheduleRequest, dict]]):
                The request object. Request message for
                [GetAuditSchedule][google.cloud.auditmanager.v1.AuditManager.GetAuditSchedule].
            name (:class:`str`):
                Required. Name of the audit schedule to retrieve, in one
                of the following formats:

                - ``projects/{project}/locations/{location}/auditSchedules/{audit_schedule}``
                - ``folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}``
                - ``organizations/{organization}/locations/{location}/auditSchedules/{audit_schedule}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.auditmanager_v1.types.AuditSchedule:
                An audit schedule, in one of the following formats:

                   - projects/{project}/locations/{location}/auditSchedules/{audit_schedule}
                   - folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.GetAuditScheduleRequest):
            request = auditmanager.GetAuditScheduleRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_audit_schedule
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_audit_schedules(
        self,
        request: Optional[Union[auditmanager.ListAuditSchedulesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAuditSchedulesAsyncPager:
        r"""Lists audit schedules in a given project and
        location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_list_audit_schedules():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                request = auditmanager_v1.ListAuditSchedulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_audit_schedules(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.ListAuditSchedulesRequest, dict]]):
                The request object. Request message for
                [ListAuditSchedules][google.cloud.auditmanager.v1.AuditManager.ListAuditSchedules].
            parent (:class:`str`):
                Required. Parent for the audit schedule, in one of the
                following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.auditmanager_v1.services.audit_manager.pagers.ListAuditSchedulesAsyncPager:
                Response message for
                   [ListAuditSchedules][google.cloud.auditmanager.v1.AuditManager.ListAuditSchedules].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.ListAuditSchedulesRequest):
            request = auditmanager.ListAuditSchedulesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_audit_schedules
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListAuditSchedulesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def enroll_resource(
        self,
        request: Optional[Union[auditmanager.EnrollResourceRequest, dict]] = None,
        *,
        scope: Optional[str] = None,
        destinations: Optional[
            MutableSequence[auditmanager.EnrollResourceRequest.EligibleDestination]
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.Enrollment:
        r"""Adds your project, folder, or organization to Audit
        Manager. This method creates the Audit Manager service
        agent in your workload and grants required permissions
        to the service agent. If you make this request on a
        workload that's already enrolled, then this method
        overrides the existing set of destinations.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_enroll_resource():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                destinations = auditmanager_v1.EligibleDestination()
                destinations.eligible_gcs_bucket = "eligible_gcs_bucket_value"

                request = auditmanager_v1.EnrollResourceRequest(
                    scope="scope_value",
                    destinations=destinations,
                )

                # Make the request
                response = await client.enroll_resource(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.EnrollResourceRequest, dict]]):
                The request object. Request message for
                [EnrollResource][google.cloud.auditmanager.v1.AuditManager.EnrollResource].
            scope (:class:`str`):
                Required. Organization, folder, or project to enroll in
                Audit Manager, in one of the following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            destinations (:class:`MutableSequence[google.cloud.auditmanager_v1.types.EnrollResourceRequest.EligibleDestination]`):
                Required. Cloud Storage buckets that
                you can upload your audit reports to
                during the audit process.

                When you enroll an organization or
                folder, you can choose a Cloud Storage
                bucket from any project in the
                organization or folder. If you run an
                audit at the project level using the
                service agent at the organization or
                folder level, all the buckets that are
                associated with the service agent are
                available.

                This corresponds to the ``destinations`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.auditmanager_v1.types.Enrollment:
                Organization, folder, or project to
                enroll for audit reports.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, destinations]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.EnrollResourceRequest):
            request = auditmanager.EnrollResourceRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if scope is not None:
            request.scope = scope
        if destinations:
            request.destinations.extend(destinations)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.enroll_resource
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def generate_audit_scope_report(
        self,
        request: Optional[
            Union[auditmanager.GenerateAuditScopeReportRequest, dict]
        ] = None,
        *,
        scope: Optional[str] = None,
        compliance_standard: Optional[str] = None,
        report_format: Optional[
            auditmanager.GenerateAuditScopeReportRequest.AuditScopeReportFormat
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.AuditScopeReport:
        r"""Generates an audit scope report for the given standard.

        The report includes the following:

        - The technical attributes and constraints that Audit Manager
          uses to verify your compliance with a framework.
        - A list of Google Cloud services and resources that are within
          the scope of the framework.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_generate_audit_scope_report():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                request = auditmanager_v1.GenerateAuditScopeReportRequest(
                    scope="scope_value",
                    report_format="AUDIT_SCOPE_REPORT_FORMAT_ODF",
                    compliance_framework="compliance_framework_value",
                )

                # Make the request
                response = await client.generate_audit_scope_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.GenerateAuditScopeReportRequest, dict]]):
                The request object. Request message for
                [GenerateAuditScopeReport][google.cloud.auditmanager.v1.AuditManager.GenerateAuditScopeReport].
            scope (:class:`str`):
                Required. Project or folder that the audit scope report
                is generated for, in one of the following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            compliance_standard (:class:`str`):
                Optional. Deprecated. The standard (industry or
                regulatory requirements) that the audit scope report is
                run against.

                Use the ``compliance_framework`` field instead.

                This corresponds to the ``compliance_standard`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            report_format (:class:`google.cloud.auditmanager_v1.types.GenerateAuditScopeReportRequest.AuditScopeReportFormat`):
                Required. Format for the audit scope
                report.

                This corresponds to the ``report_format`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.auditmanager_v1.types.AuditScopeReport:
                Audit scope report.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, compliance_standard, report_format]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.GenerateAuditScopeReportRequest):
            request = auditmanager.GenerateAuditScopeReportRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if scope is not None:
            request.scope = scope
        if compliance_standard is not None:
            request.compliance_standard = compliance_standard
        if report_format is not None:
            request.report_format = report_format

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.generate_audit_scope_report
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def generate_audit_report(
        self,
        request: Optional[Union[auditmanager.GenerateAuditReportRequest, dict]] = None,
        *,
        scope: Optional[str] = None,
        gcs_uri: Optional[str] = None,
        compliance_standard: Optional[str] = None,
        report_format: Optional[
            auditmanager.GenerateAuditReportRequest.AuditReportFormat
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Registers audit report generation requests. This
        method returns the operation identifier that you can use
        to track the report generation progress.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_generate_audit_report():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                request = auditmanager_v1.GenerateAuditReportRequest(
                    gcs_uri="gcs_uri_value",
                    scope="scope_value",
                    report_format="AUDIT_REPORT_FORMAT_ODF",
                    compliance_framework="compliance_framework_value",
                )

                # Make the request
                operation = await client.generate_audit_report(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.GenerateAuditReportRequest, dict]]):
                The request object. Request message for
                [GenerateAuditReport][google.cloud.auditmanager.v1.AuditManager.GenerateAuditReport].
            scope (:class:`str`):
                Required. Organization, folder, or project that the
                audit applies to, in one of the following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            gcs_uri (:class:`str`):
                URL for the Cloud Storage bucket
                where the report and evidence is
                uploaded. You must select a bucket that
                was provided during the enrollment
                process.

                This corresponds to the ``gcs_uri`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            compliance_standard (:class:`str`):
                Optional. Deprecated. Compliance standard for the audit
                report.

                Use the ``compliance_framework`` field instead.

                This corresponds to the ``compliance_standard`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            report_format (:class:`google.cloud.auditmanager_v1.types.GenerateAuditReportRequest.AuditReportFormat`):
                Required. Format for the audit
                report.

                This corresponds to the ``report_format`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.auditmanager_v1.types.AuditReport`
                An audit report.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, gcs_uri, compliance_standard, report_format]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.GenerateAuditReportRequest):
            request = auditmanager.GenerateAuditReportRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if scope is not None:
            request.scope = scope
        if gcs_uri is not None:
            request.gcs_uri = gcs_uri
        if compliance_standard is not None:
            request.compliance_standard = compliance_standard
        if report_format is not None:
            request.report_format = report_format

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.generate_audit_report
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("scope", request.scope),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            auditmanager.AuditReport,
            metadata_type=auditmanager.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_audit_reports(
        self,
        request: Optional[Union[auditmanager.ListAuditReportsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAuditReportsAsyncPager:
        r"""Lists the audit reports for the organization, folder,
        or project that you specify as the parent scope.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_list_audit_reports():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                request = auditmanager_v1.ListAuditReportsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_audit_reports(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.ListAuditReportsRequest, dict]]):
                The request object. Request message for
                [ListAuditReports][google.cloud.auditmanager.v1.AuditManager.ListAuditReports].
            parent (:class:`str`):
                Required. Parent organization, folder, or project to
                list reports for, in one of the following formats:

                - ``projects/{project}/locations/{location}``
                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.auditmanager_v1.services.audit_manager.pagers.ListAuditReportsAsyncPager:
                Response message for
                   [ListAuditReports][google.cloud.auditmanager.v1.AuditManager.ListAuditReports].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.ListAuditReportsRequest):
            request = auditmanager.ListAuditReportsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_audit_reports
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListAuditReportsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_audit_report(
        self,
        request: Optional[Union[auditmanager.GetAuditReportRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.AuditReport:
        r"""Gets the full metadata and findings for an audit
        report.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_get_audit_report():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                request = auditmanager_v1.GetAuditReportRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_audit_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.GetAuditReportRequest, dict]]):
                The request object. Request message for
                [GetAuditReport][google.cloud.auditmanager.v1.AuditManager.GetAuditReport].
            name (:class:`str`):
                Required. Name of the audit report, in one of the
                following formats:

                - ``projects/{project}/locations/{location}/auditReports/{audit_report}``
                - ``folders/{folder}/locations/{location}/auditReports/{audit_report}``
                - ``organizations/{organization}/locations/{location}/auditReports/{audit_report}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.auditmanager_v1.types.AuditReport:
                An audit report.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.GetAuditReportRequest):
            request = auditmanager.GetAuditReportRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_audit_report
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_resource_enrollment_status(
        self,
        request: Optional[
            Union[auditmanager.GetResourceEnrollmentStatusRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> auditmanager.ResourceEnrollmentStatus:
        r"""Gets a resource and its enrollment status.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_get_resource_enrollment_status():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                request = auditmanager_v1.GetResourceEnrollmentStatusRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_resource_enrollment_status(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.GetResourceEnrollmentStatusRequest, dict]]):
                The request object. Request message for
                [GetResourceEnrollmentStatus][google.cloud.auditmanager.v1.AuditManager.GetResourceEnrollmentStatus].
            name (:class:`str`):
                Required. Name of the resource enrollment status, in one
                of the following formats:

                - ``folders/{folder}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``
                - ``projects/{project}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``
                - ``organizations/{organization}/locations/{location}/resourceEnrollmentStatuses/{resource_enrollment_status}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.auditmanager_v1.types.ResourceEnrollmentStatus:
                An organization, folder, or project
                with its enrollment status.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.GetResourceEnrollmentStatusRequest):
            request = auditmanager.GetResourceEnrollmentStatusRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_resource_enrollment_status
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_resource_enrollment_statuses(
        self,
        request: Optional[
            Union[auditmanager.ListResourceEnrollmentStatusesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListResourceEnrollmentStatusesAsyncPager:
        r"""Lists all the folders and projects in an organization
        or folder, along with their enrollments.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_list_resource_enrollment_statuses():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                request = auditmanager_v1.ListResourceEnrollmentStatusesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_resource_enrollment_statuses(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.ListResourceEnrollmentStatusesRequest, dict]]):
                The request object. Request message for
                [ListResourceEnrollmentStatuses][google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses].
            parent (:class:`str`):
                Required. Parent organization or folder to list
                enrollment statuses for, in one of the following
                formats:

                - ``folders/{folder}/locations/{location}``
                - ``organizations/{organization}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.auditmanager_v1.services.audit_manager.pagers.ListResourceEnrollmentStatusesAsyncPager:
                Response message for
                   [ListResourceEnrollmentStatuses][google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.ListResourceEnrollmentStatusesRequest):
            request = auditmanager.ListResourceEnrollmentStatusesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_resource_enrollment_statuses
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListResourceEnrollmentStatusesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_controls(
        self,
        request: Optional[Union[auditmanager.ListControlsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListControlsAsyncPager:
        r"""Lists the controls that you must implement to become
        compliant to a regulatory standard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import auditmanager_v1

            async def sample_list_controls():
                # Create a client
                client = auditmanager_v1.AuditManagerAsyncClient()

                # Initialize request argument(s)
                request = auditmanager_v1.ListControlsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_controls(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.auditmanager_v1.types.ListControlsRequest, dict]]):
                The request object. Request message for
                [ListControls][google.cloud.auditmanager.v1.AuditManager.ListControls].
            parent (:class:`str`):
                Required. Standard to list controls for, in one of the
                following formats:

                - ``projects/{project}/locations/{location}/standards/{standard}``
                - ``folders/{folder}/locations/{location}/standards/{standard}``
                - ``organizations/{organization}/locations/{location}/standards/{standard}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.auditmanager_v1.services.audit_manager.pagers.ListControlsAsyncPager:
                Response message for
                   [ListControls][google.cloud.auditmanager.v1.AuditManager.ListControls].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, auditmanager.ListControlsRequest):
            request = auditmanager.ListControlsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_controls
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListControlsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_operations(
        self,
        request: Optional[Union[operations_pb2.ListOperationsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.ListOperationsRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.ListOperationsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.list_operations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: Optional[Union[operations_pb2.GetOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.GetOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.GetOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_operation(
        self,
        request: Optional[Union[operations_pb2.DeleteOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a long-running operation.

        This method indicates that the client is no longer interested
        in the operation result. It does not cancel the operation.
        If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.DeleteOperationRequest`):
                The request object. Request message for
                `DeleteOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.DeleteOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.DeleteOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.delete_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def cancel_operation(
        self,
        request: Optional[Union[operations_pb2.CancelOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running operation.

        The server makes a best effort to cancel the operation, but success
        is not guaranteed.  If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.CancelOperationRequest`):
                The request object. Request message for
                `CancelOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.CancelOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.CancelOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.cancel_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def get_location(
        self,
        request: Optional[Union[locations_pb2.GetLocationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.Location:
        r"""Gets information about a location.

        Args:
            request (:class:`~.location_pb2.GetLocationRequest`):
                The request object. Request message for
                `GetLocation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.Location:
                Location object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.GetLocationRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.GetLocationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_location]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_locations(
        self,
        request: Optional[Union[locations_pb2.ListLocationsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.ListLocationsResponse:
        r"""Lists information about the supported locations for this service.

        Args:
            request (:class:`~.location_pb2.ListLocationsRequest`):
                The request object. Request message for
                `ListLocations` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.ListLocationsResponse:
                Response message for ``ListLocations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.ListLocationsRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.ListLocationsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.list_locations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "AuditManagerAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("AuditManagerAsyncClient",)
