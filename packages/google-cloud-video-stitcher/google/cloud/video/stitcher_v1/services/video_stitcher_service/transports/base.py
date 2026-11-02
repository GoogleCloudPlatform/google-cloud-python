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
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.video.stitcher_v1 import gapic_version as package_version
from google.cloud.video.stitcher_v1.types import (
    ad_tag_details,
    cdn_keys,
    live_configs,
    sessions,
    slates,
    stitch_details,
    video_stitcher_service,
    vod_configs,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class VideoStitcherServiceTransport(abc.ABC):
    """Abstract transport class for VideoStitcherService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "videostitcher.googleapis.com"

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
                 The hostname to connect to (default: 'videostitcher.googleapis.com').
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
            self.create_cdn_key: gapic_v1.method.wrap_method(
                self.create_cdn_key,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_cdn_keys: gapic_v1.method.wrap_method(
                self.list_cdn_keys,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_cdn_key: gapic_v1.method.wrap_method(
                self.get_cdn_key,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_cdn_key: gapic_v1.method.wrap_method(
                self.delete_cdn_key,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_cdn_key: gapic_v1.method.wrap_method(
                self.update_cdn_key,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_vod_session: gapic_v1.method.wrap_method(
                self.create_vod_session,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_vod_session: gapic_v1.method.wrap_method(
                self.get_vod_session,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_vod_stitch_details: gapic_v1.method.wrap_method(
                self.list_vod_stitch_details,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_vod_stitch_detail: gapic_v1.method.wrap_method(
                self.get_vod_stitch_detail,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_vod_ad_tag_details: gapic_v1.method.wrap_method(
                self.list_vod_ad_tag_details,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_vod_ad_tag_detail: gapic_v1.method.wrap_method(
                self.get_vod_ad_tag_detail,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_live_ad_tag_details: gapic_v1.method.wrap_method(
                self.list_live_ad_tag_details,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_live_ad_tag_detail: gapic_v1.method.wrap_method(
                self.get_live_ad_tag_detail,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_slate: gapic_v1.method.wrap_method(
                self.create_slate,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_slates: gapic_v1.method.wrap_method(
                self.list_slates,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_slate: gapic_v1.method.wrap_method(
                self.get_slate,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_slate: gapic_v1.method.wrap_method(
                self.update_slate,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_slate: gapic_v1.method.wrap_method(
                self.delete_slate,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_live_session: gapic_v1.method.wrap_method(
                self.create_live_session,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_live_session: gapic_v1.method.wrap_method(
                self.get_live_session,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_live_config: gapic_v1.method.wrap_method(
                self.create_live_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_live_configs: gapic_v1.method.wrap_method(
                self.list_live_configs,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_live_config: gapic_v1.method.wrap_method(
                self.get_live_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_live_config: gapic_v1.method.wrap_method(
                self.delete_live_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_live_config: gapic_v1.method.wrap_method(
                self.update_live_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_vod_config: gapic_v1.method.wrap_method(
                self.create_vod_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_vod_configs: gapic_v1.method.wrap_method(
                self.list_vod_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_vod_config: gapic_v1.method.wrap_method(
                self.get_vod_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_vod_config: gapic_v1.method.wrap_method(
                self.delete_vod_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_vod_config: gapic_v1.method.wrap_method(
                self.update_vod_config,
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
    def create_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateCdnKeyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_cdn_keys(
        self,
    ) -> Callable[
        [video_stitcher_service.ListCdnKeysRequest],
        Union[
            video_stitcher_service.ListCdnKeysResponse,
            Awaitable[video_stitcher_service.ListCdnKeysResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.GetCdnKeyRequest],
        Union[cdn_keys.CdnKey, Awaitable[cdn_keys.CdnKey]],
    ]:
        raise NotImplementedError()

    @property
    def delete_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteCdnKeyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_cdn_key(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateCdnKeyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_vod_session(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateVodSessionRequest],
        Union[sessions.VodSession, Awaitable[sessions.VodSession]],
    ]:
        raise NotImplementedError()

    @property
    def get_vod_session(
        self,
    ) -> Callable[
        [video_stitcher_service.GetVodSessionRequest],
        Union[sessions.VodSession, Awaitable[sessions.VodSession]],
    ]:
        raise NotImplementedError()

    @property
    def list_vod_stitch_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListVodStitchDetailsRequest],
        Union[
            video_stitcher_service.ListVodStitchDetailsResponse,
            Awaitable[video_stitcher_service.ListVodStitchDetailsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_vod_stitch_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetVodStitchDetailRequest],
        Union[
            stitch_details.VodStitchDetail, Awaitable[stitch_details.VodStitchDetail]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_vod_ad_tag_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListVodAdTagDetailsRequest],
        Union[
            video_stitcher_service.ListVodAdTagDetailsResponse,
            Awaitable[video_stitcher_service.ListVodAdTagDetailsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_vod_ad_tag_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetVodAdTagDetailRequest],
        Union[ad_tag_details.VodAdTagDetail, Awaitable[ad_tag_details.VodAdTagDetail]],
    ]:
        raise NotImplementedError()

    @property
    def list_live_ad_tag_details(
        self,
    ) -> Callable[
        [video_stitcher_service.ListLiveAdTagDetailsRequest],
        Union[
            video_stitcher_service.ListLiveAdTagDetailsResponse,
            Awaitable[video_stitcher_service.ListLiveAdTagDetailsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_live_ad_tag_detail(
        self,
    ) -> Callable[
        [video_stitcher_service.GetLiveAdTagDetailRequest],
        Union[
            ad_tag_details.LiveAdTagDetail, Awaitable[ad_tag_details.LiveAdTagDetail]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateSlateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_slates(
        self,
    ) -> Callable[
        [video_stitcher_service.ListSlatesRequest],
        Union[
            video_stitcher_service.ListSlatesResponse,
            Awaitable[video_stitcher_service.ListSlatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.GetSlateRequest],
        Union[slates.Slate, Awaitable[slates.Slate]],
    ]:
        raise NotImplementedError()

    @property
    def update_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateSlateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_slate(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteSlateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_live_session(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateLiveSessionRequest],
        Union[sessions.LiveSession, Awaitable[sessions.LiveSession]],
    ]:
        raise NotImplementedError()

    @property
    def get_live_session(
        self,
    ) -> Callable[
        [video_stitcher_service.GetLiveSessionRequest],
        Union[sessions.LiveSession, Awaitable[sessions.LiveSession]],
    ]:
        raise NotImplementedError()

    @property
    def create_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateLiveConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_live_configs(
        self,
    ) -> Callable[
        [video_stitcher_service.ListLiveConfigsRequest],
        Union[
            video_stitcher_service.ListLiveConfigsResponse,
            Awaitable[video_stitcher_service.ListLiveConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.GetLiveConfigRequest],
        Union[live_configs.LiveConfig, Awaitable[live_configs.LiveConfig]],
    ]:
        raise NotImplementedError()

    @property
    def delete_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteLiveConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_live_config(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateLiveConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_vod_config(
        self,
    ) -> Callable[
        [video_stitcher_service.CreateVodConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_vod_configs(
        self,
    ) -> Callable[
        [video_stitcher_service.ListVodConfigsRequest],
        Union[
            video_stitcher_service.ListVodConfigsResponse,
            Awaitable[video_stitcher_service.ListVodConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_vod_config(
        self,
    ) -> Callable[
        [video_stitcher_service.GetVodConfigRequest],
        Union[vod_configs.VodConfig, Awaitable[vod_configs.VodConfig]],
    ]:
        raise NotImplementedError()

    @property
    def delete_vod_config(
        self,
    ) -> Callable[
        [video_stitcher_service.DeleteVodConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_vod_config(
        self,
    ) -> Callable[
        [video_stitcher_service.UpdateVodConfigRequest],
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
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("VideoStitcherServiceTransport",)
