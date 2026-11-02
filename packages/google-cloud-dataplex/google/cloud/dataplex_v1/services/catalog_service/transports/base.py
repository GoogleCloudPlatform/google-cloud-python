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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
import google.auth  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.dataplex_v1 import gapic_version as package_version
from google.cloud.dataplex_v1.types import catalog

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class CatalogServiceTransport(abc.ABC):
    """Abstract transport class for CatalogService."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/cloud-platform.read-only",
        "https://www.googleapis.com/auth/dataplex.read-write",
        "https://www.googleapis.com/auth/dataplex.readonly",
    )

    DEFAULT_HOST: str = "dataplex.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dataplex.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """

        # Save the scopes.
        self._scopes = scopes
        if not hasattr(self, "_ignore_credentials"):
            self._ignore_credentials: bool = False

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file,
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.create_entry_type: gapic_v1.method.wrap_method(
                self.create_entry_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_entry_type: gapic_v1.method.wrap_method(
                self.update_entry_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_entry_type: gapic_v1.method.wrap_method(
                self.delete_entry_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_entry_types: gapic_v1.method.wrap_method(
                self.list_entry_types,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_entry_type: gapic_v1.method.wrap_method(
                self.get_entry_type,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_aspect_type: gapic_v1.method.wrap_method(
                self.create_aspect_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_aspect_type: gapic_v1.method.wrap_method(
                self.update_aspect_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_aspect_type: gapic_v1.method.wrap_method(
                self.delete_aspect_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_aspect_types: gapic_v1.method.wrap_method(
                self.list_aspect_types,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_aspect_type: gapic_v1.method.wrap_method(
                self.get_aspect_type,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_entry_group: gapic_v1.method.wrap_method(
                self.create_entry_group,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_entry_group: gapic_v1.method.wrap_method(
                self.update_entry_group,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_entry_group: gapic_v1.method.wrap_method(
                self.delete_entry_group,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_entry_groups: gapic_v1.method.wrap_method(
                self.list_entry_groups,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_entry_group: gapic_v1.method.wrap_method(
                self.get_entry_group,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_entry: gapic_v1.method.wrap_method(
                self.create_entry,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_entry: gapic_v1.method.wrap_method(
                self.update_entry,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_entry: gapic_v1.method.wrap_method(
                self.delete_entry,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_entries: gapic_v1.method.wrap_method(
                self.list_entries,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.get_entry: gapic_v1.method.wrap_method(
                self.get_entry,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.lookup_entry: gapic_v1.method.wrap_method(
                self.lookup_entry,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.modify_entry: gapic_v1.method.wrap_method(
                self.modify_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_entries: gapic_v1.method.wrap_method(
                self.search_entries,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_metadata_job: gapic_v1.method.wrap_method(
                self.create_metadata_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_metadata_job: gapic_v1.method.wrap_method(
                self.get_metadata_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_metadata_jobs: gapic_v1.method.wrap_method(
                self.list_metadata_jobs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_metadata_job: gapic_v1.method.wrap_method(
                self.cancel_metadata_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_entry_link: gapic_v1.method.wrap_method(
                self.create_entry_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_entry_link: gapic_v1.method.wrap_method(
                self.update_entry_link,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_entry_link: gapic_v1.method.wrap_method(
                self.delete_entry_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.lookup_entry_links: gapic_v1.method.wrap_method(
                self.lookup_entry_links,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.lookup_context: gapic_v1.method.wrap_method(
                self.lookup_context,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_entry_link: gapic_v1.method.wrap_method(
                self.get_entry_link,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=20.0,
                ),
                default_timeout=20.0,
                client_info=client_info,
            ),
            self.create_metadata_feed: gapic_v1.method.wrap_method(
                self.create_metadata_feed,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_metadata_feed: gapic_v1.method.wrap_method(
                self.get_metadata_feed,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_metadata_feeds: gapic_v1.method.wrap_method(
                self.list_metadata_feeds,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_metadata_feed: gapic_v1.method.wrap_method(
                self.delete_metadata_feed,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_metadata_feed: gapic_v1.method.wrap_method(
                self.update_metadata_feed,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: gapic_v1.method.wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: gapic_v1.method.wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: gapic_v1.method.wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: gapic_v1.method.wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: gapic_v1.method.wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def create_entry_type(
        self,
    ) -> Callable[
        [catalog.CreateEntryTypeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_entry_type(
        self,
    ) -> Callable[
        [catalog.UpdateEntryTypeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_entry_type(
        self,
    ) -> Callable[
        [catalog.DeleteEntryTypeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_entry_types(
        self,
    ) -> Callable[
        [catalog.ListEntryTypesRequest],
        Union[
            catalog.ListEntryTypesResponse, Awaitable[catalog.ListEntryTypesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_entry_type(
        self,
    ) -> Callable[
        [catalog.GetEntryTypeRequest],
        Union[catalog.EntryType, Awaitable[catalog.EntryType]],
    ]:
        raise NotImplementedError()

    @property
    def create_aspect_type(
        self,
    ) -> Callable[
        [catalog.CreateAspectTypeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_aspect_type(
        self,
    ) -> Callable[
        [catalog.UpdateAspectTypeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_aspect_type(
        self,
    ) -> Callable[
        [catalog.DeleteAspectTypeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_aspect_types(
        self,
    ) -> Callable[
        [catalog.ListAspectTypesRequest],
        Union[
            catalog.ListAspectTypesResponse, Awaitable[catalog.ListAspectTypesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_aspect_type(
        self,
    ) -> Callable[
        [catalog.GetAspectTypeRequest],
        Union[catalog.AspectType, Awaitable[catalog.AspectType]],
    ]:
        raise NotImplementedError()

    @property
    def create_entry_group(
        self,
    ) -> Callable[
        [catalog.CreateEntryGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_entry_group(
        self,
    ) -> Callable[
        [catalog.UpdateEntryGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_entry_group(
        self,
    ) -> Callable[
        [catalog.DeleteEntryGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_entry_groups(
        self,
    ) -> Callable[
        [catalog.ListEntryGroupsRequest],
        Union[
            catalog.ListEntryGroupsResponse, Awaitable[catalog.ListEntryGroupsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_entry_group(
        self,
    ) -> Callable[
        [catalog.GetEntryGroupRequest],
        Union[catalog.EntryGroup, Awaitable[catalog.EntryGroup]],
    ]:
        raise NotImplementedError()

    @property
    def create_entry(
        self,
    ) -> Callable[
        [catalog.CreateEntryRequest], Union[catalog.Entry, Awaitable[catalog.Entry]]
    ]:
        raise NotImplementedError()

    @property
    def update_entry(
        self,
    ) -> Callable[
        [catalog.UpdateEntryRequest], Union[catalog.Entry, Awaitable[catalog.Entry]]
    ]:
        raise NotImplementedError()

    @property
    def delete_entry(
        self,
    ) -> Callable[
        [catalog.DeleteEntryRequest], Union[catalog.Entry, Awaitable[catalog.Entry]]
    ]:
        raise NotImplementedError()

    @property
    def list_entries(
        self,
    ) -> Callable[
        [catalog.ListEntriesRequest],
        Union[catalog.ListEntriesResponse, Awaitable[catalog.ListEntriesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_entry(
        self,
    ) -> Callable[
        [catalog.GetEntryRequest], Union[catalog.Entry, Awaitable[catalog.Entry]]
    ]:
        raise NotImplementedError()

    @property
    def lookup_entry(
        self,
    ) -> Callable[
        [catalog.LookupEntryRequest], Union[catalog.Entry, Awaitable[catalog.Entry]]
    ]:
        raise NotImplementedError()

    @property
    def modify_entry(
        self,
    ) -> Callable[
        [catalog.ModifyEntryRequest], Union[catalog.Entry, Awaitable[catalog.Entry]]
    ]:
        raise NotImplementedError()

    @property
    def search_entries(
        self,
    ) -> Callable[
        [catalog.SearchEntriesRequest],
        Union[catalog.SearchEntriesResponse, Awaitable[catalog.SearchEntriesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def create_metadata_job(
        self,
    ) -> Callable[
        [catalog.CreateMetadataJobRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_metadata_job(
        self,
    ) -> Callable[
        [catalog.GetMetadataJobRequest],
        Union[catalog.MetadataJob, Awaitable[catalog.MetadataJob]],
    ]:
        raise NotImplementedError()

    @property
    def list_metadata_jobs(
        self,
    ) -> Callable[
        [catalog.ListMetadataJobsRequest],
        Union[
            catalog.ListMetadataJobsResponse,
            Awaitable[catalog.ListMetadataJobsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def cancel_metadata_job(
        self,
    ) -> Callable[
        [catalog.CancelMetadataJobRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_entry_link(
        self,
    ) -> Callable[
        [catalog.CreateEntryLinkRequest],
        Union[catalog.EntryLink, Awaitable[catalog.EntryLink]],
    ]:
        raise NotImplementedError()

    @property
    def update_entry_link(
        self,
    ) -> Callable[
        [catalog.UpdateEntryLinkRequest],
        Union[catalog.EntryLink, Awaitable[catalog.EntryLink]],
    ]:
        raise NotImplementedError()

    @property
    def delete_entry_link(
        self,
    ) -> Callable[
        [catalog.DeleteEntryLinkRequest],
        Union[catalog.EntryLink, Awaitable[catalog.EntryLink]],
    ]:
        raise NotImplementedError()

    @property
    def lookup_entry_links(
        self,
    ) -> Callable[
        [catalog.LookupEntryLinksRequest],
        Union[
            catalog.LookupEntryLinksResponse,
            Awaitable[catalog.LookupEntryLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def lookup_context(
        self,
    ) -> Callable[
        [catalog.LookupContextRequest],
        Union[catalog.LookupContextResponse, Awaitable[catalog.LookupContextResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_entry_link(
        self,
    ) -> Callable[
        [catalog.GetEntryLinkRequest],
        Union[catalog.EntryLink, Awaitable[catalog.EntryLink]],
    ]:
        raise NotImplementedError()

    @property
    def create_metadata_feed(
        self,
    ) -> Callable[
        [catalog.CreateMetadataFeedRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_metadata_feed(
        self,
    ) -> Callable[
        [catalog.GetMetadataFeedRequest],
        Union[catalog.MetadataFeed, Awaitable[catalog.MetadataFeed]],
    ]:
        raise NotImplementedError()

    @property
    def list_metadata_feeds(
        self,
    ) -> Callable[
        [catalog.ListMetadataFeedsRequest],
        Union[
            catalog.ListMetadataFeedsResponse,
            Awaitable[catalog.ListMetadataFeedsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_metadata_feed(
        self,
    ) -> Callable[
        [catalog.DeleteMetadataFeedRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_metadata_feed(
        self,
    ) -> Callable[
        [catalog.UpdateMetadataFeedRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[
            operations_pb2.ListOperationsResponse,
            Awaitable[operations_pb2.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[
        [operations_pb2.CancelOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Union[
            iam_policy_pb2.TestIamPermissionsResponse,
            Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("CatalogServiceTransport",)
