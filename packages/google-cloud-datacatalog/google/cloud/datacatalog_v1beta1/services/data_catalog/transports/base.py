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
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.datacatalog_v1beta1 import gapic_version as package_version
from google.cloud.datacatalog_v1beta1.types import datacatalog, tags

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DataCatalogTransport(abc.ABC):
    """Abstract transport class for DataCatalog."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "datacatalog.googleapis.com"

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
                 The hostname to connect to (default: 'datacatalog.googleapis.com').
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
            self.search_catalog: gapic_v1.method.wrap_method(
                self.search_catalog,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_entry_group: gapic_v1.method.wrap_method(
                self.create_entry_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_entry_group: gapic_v1.method.wrap_method(
                self.update_entry_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_entry_group: gapic_v1.method.wrap_method(
                self.get_entry_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_entry_group: gapic_v1.method.wrap_method(
                self.delete_entry_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_entry_groups: gapic_v1.method.wrap_method(
                self.list_entry_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_entry: gapic_v1.method.wrap_method(
                self.create_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_entry: gapic_v1.method.wrap_method(
                self.update_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_entry: gapic_v1.method.wrap_method(
                self.delete_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_entry: gapic_v1.method.wrap_method(
                self.get_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.lookup_entry: gapic_v1.method.wrap_method(
                self.lookup_entry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_entries: gapic_v1.method.wrap_method(
                self.list_entries,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_tag_template: gapic_v1.method.wrap_method(
                self.create_tag_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_tag_template: gapic_v1.method.wrap_method(
                self.get_tag_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_tag_template: gapic_v1.method.wrap_method(
                self.update_tag_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_tag_template: gapic_v1.method.wrap_method(
                self.delete_tag_template,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_tag_template_field: gapic_v1.method.wrap_method(
                self.create_tag_template_field,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_tag_template_field: gapic_v1.method.wrap_method(
                self.update_tag_template_field,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_tag_template_field: gapic_v1.method.wrap_method(
                self.rename_tag_template_field,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rename_tag_template_field_enum_value: gapic_v1.method.wrap_method(
                self.rename_tag_template_field_enum_value,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_tag_template_field: gapic_v1.method.wrap_method(
                self.delete_tag_template_field,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_tag: gapic_v1.method.wrap_method(
                self.create_tag,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_tag: gapic_v1.method.wrap_method(
                self.update_tag,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_tag: gapic_v1.method.wrap_method(
                self.delete_tag,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_tags: gapic_v1.method.wrap_method(
                self.list_tags,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
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
    def search_catalog(
        self,
    ) -> Callable[
        [datacatalog.SearchCatalogRequest],
        Union[
            datacatalog.SearchCatalogResponse,
            Awaitable[datacatalog.SearchCatalogResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_entry_group(
        self,
    ) -> Callable[
        [datacatalog.CreateEntryGroupRequest],
        Union[datacatalog.EntryGroup, Awaitable[datacatalog.EntryGroup]],
    ]:
        raise NotImplementedError()

    @property
    def update_entry_group(
        self,
    ) -> Callable[
        [datacatalog.UpdateEntryGroupRequest],
        Union[datacatalog.EntryGroup, Awaitable[datacatalog.EntryGroup]],
    ]:
        raise NotImplementedError()

    @property
    def get_entry_group(
        self,
    ) -> Callable[
        [datacatalog.GetEntryGroupRequest],
        Union[datacatalog.EntryGroup, Awaitable[datacatalog.EntryGroup]],
    ]:
        raise NotImplementedError()

    @property
    def delete_entry_group(
        self,
    ) -> Callable[
        [datacatalog.DeleteEntryGroupRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_entry_groups(
        self,
    ) -> Callable[
        [datacatalog.ListEntryGroupsRequest],
        Union[
            datacatalog.ListEntryGroupsResponse,
            Awaitable[datacatalog.ListEntryGroupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_entry(
        self,
    ) -> Callable[
        [datacatalog.CreateEntryRequest],
        Union[datacatalog.Entry, Awaitable[datacatalog.Entry]],
    ]:
        raise NotImplementedError()

    @property
    def update_entry(
        self,
    ) -> Callable[
        [datacatalog.UpdateEntryRequest],
        Union[datacatalog.Entry, Awaitable[datacatalog.Entry]],
    ]:
        raise NotImplementedError()

    @property
    def delete_entry(
        self,
    ) -> Callable[
        [datacatalog.DeleteEntryRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_entry(
        self,
    ) -> Callable[
        [datacatalog.GetEntryRequest],
        Union[datacatalog.Entry, Awaitable[datacatalog.Entry]],
    ]:
        raise NotImplementedError()

    @property
    def lookup_entry(
        self,
    ) -> Callable[
        [datacatalog.LookupEntryRequest],
        Union[datacatalog.Entry, Awaitable[datacatalog.Entry]],
    ]:
        raise NotImplementedError()

    @property
    def list_entries(
        self,
    ) -> Callable[
        [datacatalog.ListEntriesRequest],
        Union[
            datacatalog.ListEntriesResponse, Awaitable[datacatalog.ListEntriesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_tag_template(
        self,
    ) -> Callable[
        [datacatalog.CreateTagTemplateRequest],
        Union[tags.TagTemplate, Awaitable[tags.TagTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def get_tag_template(
        self,
    ) -> Callable[
        [datacatalog.GetTagTemplateRequest],
        Union[tags.TagTemplate, Awaitable[tags.TagTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def update_tag_template(
        self,
    ) -> Callable[
        [datacatalog.UpdateTagTemplateRequest],
        Union[tags.TagTemplate, Awaitable[tags.TagTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def delete_tag_template(
        self,
    ) -> Callable[
        [datacatalog.DeleteTagTemplateRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_tag_template_field(
        self,
    ) -> Callable[
        [datacatalog.CreateTagTemplateFieldRequest],
        Union[tags.TagTemplateField, Awaitable[tags.TagTemplateField]],
    ]:
        raise NotImplementedError()

    @property
    def update_tag_template_field(
        self,
    ) -> Callable[
        [datacatalog.UpdateTagTemplateFieldRequest],
        Union[tags.TagTemplateField, Awaitable[tags.TagTemplateField]],
    ]:
        raise NotImplementedError()

    @property
    def rename_tag_template_field(
        self,
    ) -> Callable[
        [datacatalog.RenameTagTemplateFieldRequest],
        Union[tags.TagTemplateField, Awaitable[tags.TagTemplateField]],
    ]:
        raise NotImplementedError()

    @property
    def rename_tag_template_field_enum_value(
        self,
    ) -> Callable[
        [datacatalog.RenameTagTemplateFieldEnumValueRequest],
        Union[tags.TagTemplateField, Awaitable[tags.TagTemplateField]],
    ]:
        raise NotImplementedError()

    @property
    def delete_tag_template_field(
        self,
    ) -> Callable[
        [datacatalog.DeleteTagTemplateFieldRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_tag(
        self,
    ) -> Callable[[datacatalog.CreateTagRequest], Union[tags.Tag, Awaitable[tags.Tag]]]:
        raise NotImplementedError()

    @property
    def update_tag(
        self,
    ) -> Callable[[datacatalog.UpdateTagRequest], Union[tags.Tag, Awaitable[tags.Tag]]]:
        raise NotImplementedError()

    @property
    def delete_tag(
        self,
    ) -> Callable[
        [datacatalog.DeleteTagRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_tags(
        self,
    ) -> Callable[
        [datacatalog.ListTagsRequest],
        Union[datacatalog.ListTagsResponse, Awaitable[datacatalog.ListTagsResponse]],
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
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("DataCatalogTransport",)
