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
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.analytics.admin_v1alpha import gapic_version as package_version
from google.analytics.admin_v1alpha.types import (
    analytics_admin,
    audience,
    channel_group,
    event_create_and_edit,
    expanded_data_set,
    resources,
    subproperty_event_filter,
)
from google.analytics.admin_v1alpha.types import audience as gaa_audience
from google.analytics.admin_v1alpha.types import channel_group as gaa_channel_group
from google.analytics.admin_v1alpha.types import (
    expanded_data_set as gaa_expanded_data_set,
)
from google.analytics.admin_v1alpha.types import (
    subproperty_event_filter as gaa_subproperty_event_filter,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class AnalyticsAdminServiceTransport(abc.ABC):
    """Abstract transport class for AnalyticsAdminService."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/analytics.edit",
        "https://www.googleapis.com/auth/analytics.manage.users",
        "https://www.googleapis.com/auth/analytics.manage.users.readonly",
        "https://www.googleapis.com/auth/analytics.readonly",
    )

    DEFAULT_HOST: str = "analyticsadmin.googleapis.com"

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
                 The hostname to connect to (default: 'analyticsadmin.googleapis.com').
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
            self.get_account: gapic_v1.method.wrap_method(
                self.get_account,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_accounts: gapic_v1.method.wrap_method(
                self.list_accounts,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_account: gapic_v1.method.wrap_method(
                self.delete_account,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_account: gapic_v1.method.wrap_method(
                self.update_account,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.provision_account_ticket: gapic_v1.method.wrap_method(
                self.provision_account_ticket,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_account_summaries: gapic_v1.method.wrap_method(
                self.list_account_summaries,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_property: gapic_v1.method.wrap_method(
                self.get_property,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_properties: gapic_v1.method.wrap_method(
                self.list_properties,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_property: gapic_v1.method.wrap_method(
                self.create_property,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_property: gapic_v1.method.wrap_method(
                self.delete_property,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_property: gapic_v1.method.wrap_method(
                self.update_property,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_firebase_link: gapic_v1.method.wrap_method(
                self.create_firebase_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_firebase_link: gapic_v1.method.wrap_method(
                self.delete_firebase_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_firebase_links: gapic_v1.method.wrap_method(
                self.list_firebase_links,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_global_site_tag: gapic_v1.method.wrap_method(
                self.get_global_site_tag,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_google_ads_link: gapic_v1.method.wrap_method(
                self.create_google_ads_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_google_ads_link: gapic_v1.method.wrap_method(
                self.update_google_ads_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_google_ads_link: gapic_v1.method.wrap_method(
                self.delete_google_ads_link,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_google_ads_links: gapic_v1.method.wrap_method(
                self.list_google_ads_links,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_data_sharing_settings: gapic_v1.method.wrap_method(
                self.get_data_sharing_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_measurement_protocol_secret: gapic_v1.method.wrap_method(
                self.get_measurement_protocol_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_measurement_protocol_secrets: gapic_v1.method.wrap_method(
                self.list_measurement_protocol_secrets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_measurement_protocol_secret: gapic_v1.method.wrap_method(
                self.create_measurement_protocol_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_measurement_protocol_secret: gapic_v1.method.wrap_method(
                self.delete_measurement_protocol_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_measurement_protocol_secret: gapic_v1.method.wrap_method(
                self.update_measurement_protocol_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.acknowledge_user_data_collection: gapic_v1.method.wrap_method(
                self.acknowledge_user_data_collection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_sk_ad_network_conversion_value_schema: gapic_v1.method.wrap_method(
                self.get_sk_ad_network_conversion_value_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_sk_ad_network_conversion_value_schema: gapic_v1.method.wrap_method(
                self.create_sk_ad_network_conversion_value_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_sk_ad_network_conversion_value_schema: gapic_v1.method.wrap_method(
                self.delete_sk_ad_network_conversion_value_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_sk_ad_network_conversion_value_schema: gapic_v1.method.wrap_method(
                self.update_sk_ad_network_conversion_value_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_sk_ad_network_conversion_value_schemas: gapic_v1.method.wrap_method(
                self.list_sk_ad_network_conversion_value_schemas,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_change_history_events: gapic_v1.method.wrap_method(
                self.search_change_history_events,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_google_signals_settings: gapic_v1.method.wrap_method(
                self.get_google_signals_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_google_signals_settings: gapic_v1.method.wrap_method(
                self.update_google_signals_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_conversion_event: gapic_v1.method.wrap_method(
                self.create_conversion_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_conversion_event: gapic_v1.method.wrap_method(
                self.update_conversion_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_conversion_event: gapic_v1.method.wrap_method(
                self.get_conversion_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_conversion_event: gapic_v1.method.wrap_method(
                self.delete_conversion_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_conversion_events: gapic_v1.method.wrap_method(
                self.list_conversion_events,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_key_event: gapic_v1.method.wrap_method(
                self.create_key_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_key_event: gapic_v1.method.wrap_method(
                self.update_key_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_key_event: gapic_v1.method.wrap_method(
                self.get_key_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_key_event: gapic_v1.method.wrap_method(
                self.delete_key_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_key_events: gapic_v1.method.wrap_method(
                self.list_key_events,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_display_video360_advertiser_link: gapic_v1.method.wrap_method(
                self.get_display_video360_advertiser_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_display_video360_advertiser_links: gapic_v1.method.wrap_method(
                self.list_display_video360_advertiser_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_display_video360_advertiser_link: gapic_v1.method.wrap_method(
                self.create_display_video360_advertiser_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_display_video360_advertiser_link: gapic_v1.method.wrap_method(
                self.delete_display_video360_advertiser_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_display_video360_advertiser_link: gapic_v1.method.wrap_method(
                self.update_display_video360_advertiser_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_display_video360_advertiser_link_proposal: gapic_v1.method.wrap_method(
                self.get_display_video360_advertiser_link_proposal,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_display_video360_advertiser_link_proposals: gapic_v1.method.wrap_method(
                self.list_display_video360_advertiser_link_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_display_video360_advertiser_link_proposal: gapic_v1.method.wrap_method(
                self.create_display_video360_advertiser_link_proposal,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_display_video360_advertiser_link_proposal: gapic_v1.method.wrap_method(
                self.delete_display_video360_advertiser_link_proposal,
                default_timeout=None,
                client_info=client_info,
            ),
            self.approve_display_video360_advertiser_link_proposal: gapic_v1.method.wrap_method(
                self.approve_display_video360_advertiser_link_proposal,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_display_video360_advertiser_link_proposal: gapic_v1.method.wrap_method(
                self.cancel_display_video360_advertiser_link_proposal,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_custom_dimension: gapic_v1.method.wrap_method(
                self.create_custom_dimension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_custom_dimension: gapic_v1.method.wrap_method(
                self.update_custom_dimension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_custom_dimensions: gapic_v1.method.wrap_method(
                self.list_custom_dimensions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.archive_custom_dimension: gapic_v1.method.wrap_method(
                self.archive_custom_dimension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_custom_dimension: gapic_v1.method.wrap_method(
                self.get_custom_dimension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_custom_metric: gapic_v1.method.wrap_method(
                self.create_custom_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_custom_metric: gapic_v1.method.wrap_method(
                self.update_custom_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_custom_metrics: gapic_v1.method.wrap_method(
                self.list_custom_metrics,
                default_timeout=None,
                client_info=client_info,
            ),
            self.archive_custom_metric: gapic_v1.method.wrap_method(
                self.archive_custom_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_custom_metric: gapic_v1.method.wrap_method(
                self.get_custom_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_data_retention_settings: gapic_v1.method.wrap_method(
                self.get_data_retention_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_data_retention_settings: gapic_v1.method.wrap_method(
                self.update_data_retention_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_data_stream: gapic_v1.method.wrap_method(
                self.create_data_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_data_stream: gapic_v1.method.wrap_method(
                self.delete_data_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_data_stream: gapic_v1.method.wrap_method(
                self.update_data_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_data_streams: gapic_v1.method.wrap_method(
                self.list_data_streams,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_data_stream: gapic_v1.method.wrap_method(
                self.get_data_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_audience: gapic_v1.method.wrap_method(
                self.get_audience,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_audiences: gapic_v1.method.wrap_method(
                self.list_audiences,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_audience: gapic_v1.method.wrap_method(
                self.create_audience,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_audience: gapic_v1.method.wrap_method(
                self.update_audience,
                default_timeout=None,
                client_info=client_info,
            ),
            self.archive_audience: gapic_v1.method.wrap_method(
                self.archive_audience,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_search_ads360_link: gapic_v1.method.wrap_method(
                self.get_search_ads360_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_search_ads360_links: gapic_v1.method.wrap_method(
                self.list_search_ads360_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_search_ads360_link: gapic_v1.method.wrap_method(
                self.create_search_ads360_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_search_ads360_link: gapic_v1.method.wrap_method(
                self.delete_search_ads360_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_search_ads360_link: gapic_v1.method.wrap_method(
                self.update_search_ads360_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_attribution_settings: gapic_v1.method.wrap_method(
                self.get_attribution_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_attribution_settings: gapic_v1.method.wrap_method(
                self.update_attribution_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.run_access_report: gapic_v1.method.wrap_method(
                self.run_access_report,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_access_binding: gapic_v1.method.wrap_method(
                self.create_access_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_access_binding: gapic_v1.method.wrap_method(
                self.get_access_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_access_binding: gapic_v1.method.wrap_method(
                self.update_access_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_access_binding: gapic_v1.method.wrap_method(
                self.delete_access_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_access_bindings: gapic_v1.method.wrap_method(
                self.list_access_bindings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_create_access_bindings: gapic_v1.method.wrap_method(
                self.batch_create_access_bindings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_get_access_bindings: gapic_v1.method.wrap_method(
                self.batch_get_access_bindings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_update_access_bindings: gapic_v1.method.wrap_method(
                self.batch_update_access_bindings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_delete_access_bindings: gapic_v1.method.wrap_method(
                self.batch_delete_access_bindings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_expanded_data_set: gapic_v1.method.wrap_method(
                self.get_expanded_data_set,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_expanded_data_sets: gapic_v1.method.wrap_method(
                self.list_expanded_data_sets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_expanded_data_set: gapic_v1.method.wrap_method(
                self.create_expanded_data_set,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_expanded_data_set: gapic_v1.method.wrap_method(
                self.update_expanded_data_set,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_expanded_data_set: gapic_v1.method.wrap_method(
                self.delete_expanded_data_set,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_channel_group: gapic_v1.method.wrap_method(
                self.get_channel_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_channel_groups: gapic_v1.method.wrap_method(
                self.list_channel_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_channel_group: gapic_v1.method.wrap_method(
                self.create_channel_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_channel_group: gapic_v1.method.wrap_method(
                self.update_channel_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_channel_group: gapic_v1.method.wrap_method(
                self.delete_channel_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_big_query_link: gapic_v1.method.wrap_method(
                self.create_big_query_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_big_query_link: gapic_v1.method.wrap_method(
                self.get_big_query_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_big_query_links: gapic_v1.method.wrap_method(
                self.list_big_query_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_big_query_link: gapic_v1.method.wrap_method(
                self.delete_big_query_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_big_query_link: gapic_v1.method.wrap_method(
                self.update_big_query_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_enhanced_measurement_settings: gapic_v1.method.wrap_method(
                self.get_enhanced_measurement_settings,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_enhanced_measurement_settings: gapic_v1.method.wrap_method(
                self.update_enhanced_measurement_settings,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_ad_sense_link: gapic_v1.method.wrap_method(
                self.get_ad_sense_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_ad_sense_link: gapic_v1.method.wrap_method(
                self.create_ad_sense_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_ad_sense_link: gapic_v1.method.wrap_method(
                self.delete_ad_sense_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_ad_sense_links: gapic_v1.method.wrap_method(
                self.list_ad_sense_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_event_create_rule: gapic_v1.method.wrap_method(
                self.get_event_create_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_event_create_rules: gapic_v1.method.wrap_method(
                self.list_event_create_rules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_event_create_rule: gapic_v1.method.wrap_method(
                self.create_event_create_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_event_create_rule: gapic_v1.method.wrap_method(
                self.update_event_create_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_event_create_rule: gapic_v1.method.wrap_method(
                self.delete_event_create_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_event_edit_rule: gapic_v1.method.wrap_method(
                self.get_event_edit_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_event_edit_rules: gapic_v1.method.wrap_method(
                self.list_event_edit_rules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_event_edit_rule: gapic_v1.method.wrap_method(
                self.create_event_edit_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_event_edit_rule: gapic_v1.method.wrap_method(
                self.update_event_edit_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_event_edit_rule: gapic_v1.method.wrap_method(
                self.delete_event_edit_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reorder_event_edit_rules: gapic_v1.method.wrap_method(
                self.reorder_event_edit_rules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_data_redaction_settings: gapic_v1.method.wrap_method(
                self.update_data_redaction_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_data_redaction_settings: gapic_v1.method.wrap_method(
                self.get_data_redaction_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_calculated_metric: gapic_v1.method.wrap_method(
                self.get_calculated_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_calculated_metric: gapic_v1.method.wrap_method(
                self.create_calculated_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_calculated_metrics: gapic_v1.method.wrap_method(
                self.list_calculated_metrics,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_calculated_metric: gapic_v1.method.wrap_method(
                self.update_calculated_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_calculated_metric: gapic_v1.method.wrap_method(
                self.delete_calculated_metric,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_rollup_property: gapic_v1.method.wrap_method(
                self.create_rollup_property,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_rollup_property_source_link: gapic_v1.method.wrap_method(
                self.get_rollup_property_source_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_rollup_property_source_links: gapic_v1.method.wrap_method(
                self.list_rollup_property_source_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_rollup_property_source_link: gapic_v1.method.wrap_method(
                self.create_rollup_property_source_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_rollup_property_source_link: gapic_v1.method.wrap_method(
                self.delete_rollup_property_source_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.provision_subproperty: gapic_v1.method.wrap_method(
                self.provision_subproperty,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_subproperty_event_filter: gapic_v1.method.wrap_method(
                self.create_subproperty_event_filter,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_subproperty_event_filter: gapic_v1.method.wrap_method(
                self.get_subproperty_event_filter,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_subproperty_event_filters: gapic_v1.method.wrap_method(
                self.list_subproperty_event_filters,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_subproperty_event_filter: gapic_v1.method.wrap_method(
                self.update_subproperty_event_filter,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_subproperty_event_filter: gapic_v1.method.wrap_method(
                self.delete_subproperty_event_filter,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_reporting_data_annotation: gapic_v1.method.wrap_method(
                self.create_reporting_data_annotation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_reporting_data_annotation: gapic_v1.method.wrap_method(
                self.get_reporting_data_annotation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_reporting_data_annotations: gapic_v1.method.wrap_method(
                self.list_reporting_data_annotations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_reporting_data_annotation: gapic_v1.method.wrap_method(
                self.update_reporting_data_annotation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_reporting_data_annotation: gapic_v1.method.wrap_method(
                self.delete_reporting_data_annotation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.submit_user_deletion: gapic_v1.method.wrap_method(
                self.submit_user_deletion,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_subproperty_sync_configs: gapic_v1.method.wrap_method(
                self.list_subproperty_sync_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_subproperty_sync_config: gapic_v1.method.wrap_method(
                self.update_subproperty_sync_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_subproperty_sync_config: gapic_v1.method.wrap_method(
                self.get_subproperty_sync_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_reporting_identity_settings: gapic_v1.method.wrap_method(
                self.get_reporting_identity_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_reporting_identity_settings: gapic_v1.method.wrap_method(
                self.update_reporting_identity_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_user_provided_data_settings: gapic_v1.method.wrap_method(
                self.get_user_provided_data_settings,
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
    def get_account(
        self,
    ) -> Callable[
        [analytics_admin.GetAccountRequest],
        Union[resources.Account, Awaitable[resources.Account]],
    ]:
        raise NotImplementedError()

    @property
    def list_accounts(
        self,
    ) -> Callable[
        [analytics_admin.ListAccountsRequest],
        Union[
            analytics_admin.ListAccountsResponse,
            Awaitable[analytics_admin.ListAccountsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_account(
        self,
    ) -> Callable[
        [analytics_admin.DeleteAccountRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_account(
        self,
    ) -> Callable[
        [analytics_admin.UpdateAccountRequest],
        Union[resources.Account, Awaitable[resources.Account]],
    ]:
        raise NotImplementedError()

    @property
    def provision_account_ticket(
        self,
    ) -> Callable[
        [analytics_admin.ProvisionAccountTicketRequest],
        Union[
            analytics_admin.ProvisionAccountTicketResponse,
            Awaitable[analytics_admin.ProvisionAccountTicketResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_account_summaries(
        self,
    ) -> Callable[
        [analytics_admin.ListAccountSummariesRequest],
        Union[
            analytics_admin.ListAccountSummariesResponse,
            Awaitable[analytics_admin.ListAccountSummariesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_property(
        self,
    ) -> Callable[
        [analytics_admin.GetPropertyRequest],
        Union[resources.Property, Awaitable[resources.Property]],
    ]:
        raise NotImplementedError()

    @property
    def list_properties(
        self,
    ) -> Callable[
        [analytics_admin.ListPropertiesRequest],
        Union[
            analytics_admin.ListPropertiesResponse,
            Awaitable[analytics_admin.ListPropertiesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_property(
        self,
    ) -> Callable[
        [analytics_admin.CreatePropertyRequest],
        Union[resources.Property, Awaitable[resources.Property]],
    ]:
        raise NotImplementedError()

    @property
    def delete_property(
        self,
    ) -> Callable[
        [analytics_admin.DeletePropertyRequest],
        Union[resources.Property, Awaitable[resources.Property]],
    ]:
        raise NotImplementedError()

    @property
    def update_property(
        self,
    ) -> Callable[
        [analytics_admin.UpdatePropertyRequest],
        Union[resources.Property, Awaitable[resources.Property]],
    ]:
        raise NotImplementedError()

    @property
    def create_firebase_link(
        self,
    ) -> Callable[
        [analytics_admin.CreateFirebaseLinkRequest],
        Union[resources.FirebaseLink, Awaitable[resources.FirebaseLink]],
    ]:
        raise NotImplementedError()

    @property
    def delete_firebase_link(
        self,
    ) -> Callable[
        [analytics_admin.DeleteFirebaseLinkRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_firebase_links(
        self,
    ) -> Callable[
        [analytics_admin.ListFirebaseLinksRequest],
        Union[
            analytics_admin.ListFirebaseLinksResponse,
            Awaitable[analytics_admin.ListFirebaseLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_global_site_tag(
        self,
    ) -> Callable[
        [analytics_admin.GetGlobalSiteTagRequest],
        Union[resources.GlobalSiteTag, Awaitable[resources.GlobalSiteTag]],
    ]:
        raise NotImplementedError()

    @property
    def create_google_ads_link(
        self,
    ) -> Callable[
        [analytics_admin.CreateGoogleAdsLinkRequest],
        Union[resources.GoogleAdsLink, Awaitable[resources.GoogleAdsLink]],
    ]:
        raise NotImplementedError()

    @property
    def update_google_ads_link(
        self,
    ) -> Callable[
        [analytics_admin.UpdateGoogleAdsLinkRequest],
        Union[resources.GoogleAdsLink, Awaitable[resources.GoogleAdsLink]],
    ]:
        raise NotImplementedError()

    @property
    def delete_google_ads_link(
        self,
    ) -> Callable[
        [analytics_admin.DeleteGoogleAdsLinkRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_google_ads_links(
        self,
    ) -> Callable[
        [analytics_admin.ListGoogleAdsLinksRequest],
        Union[
            analytics_admin.ListGoogleAdsLinksResponse,
            Awaitable[analytics_admin.ListGoogleAdsLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_data_sharing_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetDataSharingSettingsRequest],
        Union[resources.DataSharingSettings, Awaitable[resources.DataSharingSettings]],
    ]:
        raise NotImplementedError()

    @property
    def get_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.GetMeasurementProtocolSecretRequest],
        Union[
            resources.MeasurementProtocolSecret,
            Awaitable[resources.MeasurementProtocolSecret],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_measurement_protocol_secrets(
        self,
    ) -> Callable[
        [analytics_admin.ListMeasurementProtocolSecretsRequest],
        Union[
            analytics_admin.ListMeasurementProtocolSecretsResponse,
            Awaitable[analytics_admin.ListMeasurementProtocolSecretsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.CreateMeasurementProtocolSecretRequest],
        Union[
            resources.MeasurementProtocolSecret,
            Awaitable[resources.MeasurementProtocolSecret],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.DeleteMeasurementProtocolSecretRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_measurement_protocol_secret(
        self,
    ) -> Callable[
        [analytics_admin.UpdateMeasurementProtocolSecretRequest],
        Union[
            resources.MeasurementProtocolSecret,
            Awaitable[resources.MeasurementProtocolSecret],
        ],
    ]:
        raise NotImplementedError()

    @property
    def acknowledge_user_data_collection(
        self,
    ) -> Callable[
        [analytics_admin.AcknowledgeUserDataCollectionRequest],
        Union[
            analytics_admin.AcknowledgeUserDataCollectionResponse,
            Awaitable[analytics_admin.AcknowledgeUserDataCollectionResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_sk_ad_network_conversion_value_schema(
        self,
    ) -> Callable[
        [analytics_admin.GetSKAdNetworkConversionValueSchemaRequest],
        Union[
            resources.SKAdNetworkConversionValueSchema,
            Awaitable[resources.SKAdNetworkConversionValueSchema],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_sk_ad_network_conversion_value_schema(
        self,
    ) -> Callable[
        [analytics_admin.CreateSKAdNetworkConversionValueSchemaRequest],
        Union[
            resources.SKAdNetworkConversionValueSchema,
            Awaitable[resources.SKAdNetworkConversionValueSchema],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_sk_ad_network_conversion_value_schema(
        self,
    ) -> Callable[
        [analytics_admin.DeleteSKAdNetworkConversionValueSchemaRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_sk_ad_network_conversion_value_schema(
        self,
    ) -> Callable[
        [analytics_admin.UpdateSKAdNetworkConversionValueSchemaRequest],
        Union[
            resources.SKAdNetworkConversionValueSchema,
            Awaitable[resources.SKAdNetworkConversionValueSchema],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_sk_ad_network_conversion_value_schemas(
        self,
    ) -> Callable[
        [analytics_admin.ListSKAdNetworkConversionValueSchemasRequest],
        Union[
            analytics_admin.ListSKAdNetworkConversionValueSchemasResponse,
            Awaitable[analytics_admin.ListSKAdNetworkConversionValueSchemasResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_change_history_events(
        self,
    ) -> Callable[
        [analytics_admin.SearchChangeHistoryEventsRequest],
        Union[
            analytics_admin.SearchChangeHistoryEventsResponse,
            Awaitable[analytics_admin.SearchChangeHistoryEventsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_google_signals_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetGoogleSignalsSettingsRequest],
        Union[
            resources.GoogleSignalsSettings, Awaitable[resources.GoogleSignalsSettings]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_google_signals_settings(
        self,
    ) -> Callable[
        [analytics_admin.UpdateGoogleSignalsSettingsRequest],
        Union[
            resources.GoogleSignalsSettings, Awaitable[resources.GoogleSignalsSettings]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_conversion_event(
        self,
    ) -> Callable[
        [analytics_admin.CreateConversionEventRequest],
        Union[resources.ConversionEvent, Awaitable[resources.ConversionEvent]],
    ]:
        raise NotImplementedError()

    @property
    def update_conversion_event(
        self,
    ) -> Callable[
        [analytics_admin.UpdateConversionEventRequest],
        Union[resources.ConversionEvent, Awaitable[resources.ConversionEvent]],
    ]:
        raise NotImplementedError()

    @property
    def get_conversion_event(
        self,
    ) -> Callable[
        [analytics_admin.GetConversionEventRequest],
        Union[resources.ConversionEvent, Awaitable[resources.ConversionEvent]],
    ]:
        raise NotImplementedError()

    @property
    def delete_conversion_event(
        self,
    ) -> Callable[
        [analytics_admin.DeleteConversionEventRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_conversion_events(
        self,
    ) -> Callable[
        [analytics_admin.ListConversionEventsRequest],
        Union[
            analytics_admin.ListConversionEventsResponse,
            Awaitable[analytics_admin.ListConversionEventsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_key_event(
        self,
    ) -> Callable[
        [analytics_admin.CreateKeyEventRequest],
        Union[resources.KeyEvent, Awaitable[resources.KeyEvent]],
    ]:
        raise NotImplementedError()

    @property
    def update_key_event(
        self,
    ) -> Callable[
        [analytics_admin.UpdateKeyEventRequest],
        Union[resources.KeyEvent, Awaitable[resources.KeyEvent]],
    ]:
        raise NotImplementedError()

    @property
    def get_key_event(
        self,
    ) -> Callable[
        [analytics_admin.GetKeyEventRequest],
        Union[resources.KeyEvent, Awaitable[resources.KeyEvent]],
    ]:
        raise NotImplementedError()

    @property
    def delete_key_event(
        self,
    ) -> Callable[
        [analytics_admin.DeleteKeyEventRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_key_events(
        self,
    ) -> Callable[
        [analytics_admin.ListKeyEventsRequest],
        Union[
            analytics_admin.ListKeyEventsResponse,
            Awaitable[analytics_admin.ListKeyEventsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_display_video360_advertiser_link(
        self,
    ) -> Callable[
        [analytics_admin.GetDisplayVideo360AdvertiserLinkRequest],
        Union[
            resources.DisplayVideo360AdvertiserLink,
            Awaitable[resources.DisplayVideo360AdvertiserLink],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_display_video360_advertiser_links(
        self,
    ) -> Callable[
        [analytics_admin.ListDisplayVideo360AdvertiserLinksRequest],
        Union[
            analytics_admin.ListDisplayVideo360AdvertiserLinksResponse,
            Awaitable[analytics_admin.ListDisplayVideo360AdvertiserLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_display_video360_advertiser_link(
        self,
    ) -> Callable[
        [analytics_admin.CreateDisplayVideo360AdvertiserLinkRequest],
        Union[
            resources.DisplayVideo360AdvertiserLink,
            Awaitable[resources.DisplayVideo360AdvertiserLink],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_display_video360_advertiser_link(
        self,
    ) -> Callable[
        [analytics_admin.DeleteDisplayVideo360AdvertiserLinkRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_display_video360_advertiser_link(
        self,
    ) -> Callable[
        [analytics_admin.UpdateDisplayVideo360AdvertiserLinkRequest],
        Union[
            resources.DisplayVideo360AdvertiserLink,
            Awaitable[resources.DisplayVideo360AdvertiserLink],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_display_video360_advertiser_link_proposal(
        self,
    ) -> Callable[
        [analytics_admin.GetDisplayVideo360AdvertiserLinkProposalRequest],
        Union[
            resources.DisplayVideo360AdvertiserLinkProposal,
            Awaitable[resources.DisplayVideo360AdvertiserLinkProposal],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_display_video360_advertiser_link_proposals(
        self,
    ) -> Callable[
        [analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsRequest],
        Union[
            analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsResponse,
            Awaitable[
                analytics_admin.ListDisplayVideo360AdvertiserLinkProposalsResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_display_video360_advertiser_link_proposal(
        self,
    ) -> Callable[
        [analytics_admin.CreateDisplayVideo360AdvertiserLinkProposalRequest],
        Union[
            resources.DisplayVideo360AdvertiserLinkProposal,
            Awaitable[resources.DisplayVideo360AdvertiserLinkProposal],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_display_video360_advertiser_link_proposal(
        self,
    ) -> Callable[
        [analytics_admin.DeleteDisplayVideo360AdvertiserLinkProposalRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def approve_display_video360_advertiser_link_proposal(
        self,
    ) -> Callable[
        [analytics_admin.ApproveDisplayVideo360AdvertiserLinkProposalRequest],
        Union[
            analytics_admin.ApproveDisplayVideo360AdvertiserLinkProposalResponse,
            Awaitable[
                analytics_admin.ApproveDisplayVideo360AdvertiserLinkProposalResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def cancel_display_video360_advertiser_link_proposal(
        self,
    ) -> Callable[
        [analytics_admin.CancelDisplayVideo360AdvertiserLinkProposalRequest],
        Union[
            resources.DisplayVideo360AdvertiserLinkProposal,
            Awaitable[resources.DisplayVideo360AdvertiserLinkProposal],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_custom_dimension(
        self,
    ) -> Callable[
        [analytics_admin.CreateCustomDimensionRequest],
        Union[resources.CustomDimension, Awaitable[resources.CustomDimension]],
    ]:
        raise NotImplementedError()

    @property
    def update_custom_dimension(
        self,
    ) -> Callable[
        [analytics_admin.UpdateCustomDimensionRequest],
        Union[resources.CustomDimension, Awaitable[resources.CustomDimension]],
    ]:
        raise NotImplementedError()

    @property
    def list_custom_dimensions(
        self,
    ) -> Callable[
        [analytics_admin.ListCustomDimensionsRequest],
        Union[
            analytics_admin.ListCustomDimensionsResponse,
            Awaitable[analytics_admin.ListCustomDimensionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def archive_custom_dimension(
        self,
    ) -> Callable[
        [analytics_admin.ArchiveCustomDimensionRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_custom_dimension(
        self,
    ) -> Callable[
        [analytics_admin.GetCustomDimensionRequest],
        Union[resources.CustomDimension, Awaitable[resources.CustomDimension]],
    ]:
        raise NotImplementedError()

    @property
    def create_custom_metric(
        self,
    ) -> Callable[
        [analytics_admin.CreateCustomMetricRequest],
        Union[resources.CustomMetric, Awaitable[resources.CustomMetric]],
    ]:
        raise NotImplementedError()

    @property
    def update_custom_metric(
        self,
    ) -> Callable[
        [analytics_admin.UpdateCustomMetricRequest],
        Union[resources.CustomMetric, Awaitable[resources.CustomMetric]],
    ]:
        raise NotImplementedError()

    @property
    def list_custom_metrics(
        self,
    ) -> Callable[
        [analytics_admin.ListCustomMetricsRequest],
        Union[
            analytics_admin.ListCustomMetricsResponse,
            Awaitable[analytics_admin.ListCustomMetricsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def archive_custom_metric(
        self,
    ) -> Callable[
        [analytics_admin.ArchiveCustomMetricRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_custom_metric(
        self,
    ) -> Callable[
        [analytics_admin.GetCustomMetricRequest],
        Union[resources.CustomMetric, Awaitable[resources.CustomMetric]],
    ]:
        raise NotImplementedError()

    @property
    def get_data_retention_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetDataRetentionSettingsRequest],
        Union[
            resources.DataRetentionSettings, Awaitable[resources.DataRetentionSettings]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_data_retention_settings(
        self,
    ) -> Callable[
        [analytics_admin.UpdateDataRetentionSettingsRequest],
        Union[
            resources.DataRetentionSettings, Awaitable[resources.DataRetentionSettings]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.CreateDataStreamRequest],
        Union[resources.DataStream, Awaitable[resources.DataStream]],
    ]:
        raise NotImplementedError()

    @property
    def delete_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.DeleteDataStreamRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.UpdateDataStreamRequest],
        Union[resources.DataStream, Awaitable[resources.DataStream]],
    ]:
        raise NotImplementedError()

    @property
    def list_data_streams(
        self,
    ) -> Callable[
        [analytics_admin.ListDataStreamsRequest],
        Union[
            analytics_admin.ListDataStreamsResponse,
            Awaitable[analytics_admin.ListDataStreamsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_data_stream(
        self,
    ) -> Callable[
        [analytics_admin.GetDataStreamRequest],
        Union[resources.DataStream, Awaitable[resources.DataStream]],
    ]:
        raise NotImplementedError()

    @property
    def get_audience(
        self,
    ) -> Callable[
        [analytics_admin.GetAudienceRequest],
        Union[audience.Audience, Awaitable[audience.Audience]],
    ]:
        raise NotImplementedError()

    @property
    def list_audiences(
        self,
    ) -> Callable[
        [analytics_admin.ListAudiencesRequest],
        Union[
            analytics_admin.ListAudiencesResponse,
            Awaitable[analytics_admin.ListAudiencesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_audience(
        self,
    ) -> Callable[
        [analytics_admin.CreateAudienceRequest],
        Union[gaa_audience.Audience, Awaitable[gaa_audience.Audience]],
    ]:
        raise NotImplementedError()

    @property
    def update_audience(
        self,
    ) -> Callable[
        [analytics_admin.UpdateAudienceRequest],
        Union[gaa_audience.Audience, Awaitable[gaa_audience.Audience]],
    ]:
        raise NotImplementedError()

    @property
    def archive_audience(
        self,
    ) -> Callable[
        [analytics_admin.ArchiveAudienceRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_search_ads360_link(
        self,
    ) -> Callable[
        [analytics_admin.GetSearchAds360LinkRequest],
        Union[resources.SearchAds360Link, Awaitable[resources.SearchAds360Link]],
    ]:
        raise NotImplementedError()

    @property
    def list_search_ads360_links(
        self,
    ) -> Callable[
        [analytics_admin.ListSearchAds360LinksRequest],
        Union[
            analytics_admin.ListSearchAds360LinksResponse,
            Awaitable[analytics_admin.ListSearchAds360LinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_search_ads360_link(
        self,
    ) -> Callable[
        [analytics_admin.CreateSearchAds360LinkRequest],
        Union[resources.SearchAds360Link, Awaitable[resources.SearchAds360Link]],
    ]:
        raise NotImplementedError()

    @property
    def delete_search_ads360_link(
        self,
    ) -> Callable[
        [analytics_admin.DeleteSearchAds360LinkRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_search_ads360_link(
        self,
    ) -> Callable[
        [analytics_admin.UpdateSearchAds360LinkRequest],
        Union[resources.SearchAds360Link, Awaitable[resources.SearchAds360Link]],
    ]:
        raise NotImplementedError()

    @property
    def get_attribution_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetAttributionSettingsRequest],
        Union[resources.AttributionSettings, Awaitable[resources.AttributionSettings]],
    ]:
        raise NotImplementedError()

    @property
    def update_attribution_settings(
        self,
    ) -> Callable[
        [analytics_admin.UpdateAttributionSettingsRequest],
        Union[resources.AttributionSettings, Awaitable[resources.AttributionSettings]],
    ]:
        raise NotImplementedError()

    @property
    def run_access_report(
        self,
    ) -> Callable[
        [analytics_admin.RunAccessReportRequest],
        Union[
            analytics_admin.RunAccessReportResponse,
            Awaitable[analytics_admin.RunAccessReportResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_access_binding(
        self,
    ) -> Callable[
        [analytics_admin.CreateAccessBindingRequest],
        Union[resources.AccessBinding, Awaitable[resources.AccessBinding]],
    ]:
        raise NotImplementedError()

    @property
    def get_access_binding(
        self,
    ) -> Callable[
        [analytics_admin.GetAccessBindingRequest],
        Union[resources.AccessBinding, Awaitable[resources.AccessBinding]],
    ]:
        raise NotImplementedError()

    @property
    def update_access_binding(
        self,
    ) -> Callable[
        [analytics_admin.UpdateAccessBindingRequest],
        Union[resources.AccessBinding, Awaitable[resources.AccessBinding]],
    ]:
        raise NotImplementedError()

    @property
    def delete_access_binding(
        self,
    ) -> Callable[
        [analytics_admin.DeleteAccessBindingRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_access_bindings(
        self,
    ) -> Callable[
        [analytics_admin.ListAccessBindingsRequest],
        Union[
            analytics_admin.ListAccessBindingsResponse,
            Awaitable[analytics_admin.ListAccessBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_create_access_bindings(
        self,
    ) -> Callable[
        [analytics_admin.BatchCreateAccessBindingsRequest],
        Union[
            analytics_admin.BatchCreateAccessBindingsResponse,
            Awaitable[analytics_admin.BatchCreateAccessBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_get_access_bindings(
        self,
    ) -> Callable[
        [analytics_admin.BatchGetAccessBindingsRequest],
        Union[
            analytics_admin.BatchGetAccessBindingsResponse,
            Awaitable[analytics_admin.BatchGetAccessBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_update_access_bindings(
        self,
    ) -> Callable[
        [analytics_admin.BatchUpdateAccessBindingsRequest],
        Union[
            analytics_admin.BatchUpdateAccessBindingsResponse,
            Awaitable[analytics_admin.BatchUpdateAccessBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_delete_access_bindings(
        self,
    ) -> Callable[
        [analytics_admin.BatchDeleteAccessBindingsRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_expanded_data_set(
        self,
    ) -> Callable[
        [analytics_admin.GetExpandedDataSetRequest],
        Union[
            expanded_data_set.ExpandedDataSet,
            Awaitable[expanded_data_set.ExpandedDataSet],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_expanded_data_sets(
        self,
    ) -> Callable[
        [analytics_admin.ListExpandedDataSetsRequest],
        Union[
            analytics_admin.ListExpandedDataSetsResponse,
            Awaitable[analytics_admin.ListExpandedDataSetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_expanded_data_set(
        self,
    ) -> Callable[
        [analytics_admin.CreateExpandedDataSetRequest],
        Union[
            gaa_expanded_data_set.ExpandedDataSet,
            Awaitable[gaa_expanded_data_set.ExpandedDataSet],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_expanded_data_set(
        self,
    ) -> Callable[
        [analytics_admin.UpdateExpandedDataSetRequest],
        Union[
            gaa_expanded_data_set.ExpandedDataSet,
            Awaitable[gaa_expanded_data_set.ExpandedDataSet],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_expanded_data_set(
        self,
    ) -> Callable[
        [analytics_admin.DeleteExpandedDataSetRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_channel_group(
        self,
    ) -> Callable[
        [analytics_admin.GetChannelGroupRequest],
        Union[channel_group.ChannelGroup, Awaitable[channel_group.ChannelGroup]],
    ]:
        raise NotImplementedError()

    @property
    def list_channel_groups(
        self,
    ) -> Callable[
        [analytics_admin.ListChannelGroupsRequest],
        Union[
            analytics_admin.ListChannelGroupsResponse,
            Awaitable[analytics_admin.ListChannelGroupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_channel_group(
        self,
    ) -> Callable[
        [analytics_admin.CreateChannelGroupRequest],
        Union[
            gaa_channel_group.ChannelGroup, Awaitable[gaa_channel_group.ChannelGroup]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_channel_group(
        self,
    ) -> Callable[
        [analytics_admin.UpdateChannelGroupRequest],
        Union[
            gaa_channel_group.ChannelGroup, Awaitable[gaa_channel_group.ChannelGroup]
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_channel_group(
        self,
    ) -> Callable[
        [analytics_admin.DeleteChannelGroupRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_big_query_link(
        self,
    ) -> Callable[
        [analytics_admin.CreateBigQueryLinkRequest],
        Union[resources.BigQueryLink, Awaitable[resources.BigQueryLink]],
    ]:
        raise NotImplementedError()

    @property
    def get_big_query_link(
        self,
    ) -> Callable[
        [analytics_admin.GetBigQueryLinkRequest],
        Union[resources.BigQueryLink, Awaitable[resources.BigQueryLink]],
    ]:
        raise NotImplementedError()

    @property
    def list_big_query_links(
        self,
    ) -> Callable[
        [analytics_admin.ListBigQueryLinksRequest],
        Union[
            analytics_admin.ListBigQueryLinksResponse,
            Awaitable[analytics_admin.ListBigQueryLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_big_query_link(
        self,
    ) -> Callable[
        [analytics_admin.DeleteBigQueryLinkRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_big_query_link(
        self,
    ) -> Callable[
        [analytics_admin.UpdateBigQueryLinkRequest],
        Union[resources.BigQueryLink, Awaitable[resources.BigQueryLink]],
    ]:
        raise NotImplementedError()

    @property
    def get_enhanced_measurement_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetEnhancedMeasurementSettingsRequest],
        Union[
            resources.EnhancedMeasurementSettings,
            Awaitable[resources.EnhancedMeasurementSettings],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_enhanced_measurement_settings(
        self,
    ) -> Callable[
        [analytics_admin.UpdateEnhancedMeasurementSettingsRequest],
        Union[
            resources.EnhancedMeasurementSettings,
            Awaitable[resources.EnhancedMeasurementSettings],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_ad_sense_link(
        self,
    ) -> Callable[
        [analytics_admin.GetAdSenseLinkRequest],
        Union[resources.AdSenseLink, Awaitable[resources.AdSenseLink]],
    ]:
        raise NotImplementedError()

    @property
    def create_ad_sense_link(
        self,
    ) -> Callable[
        [analytics_admin.CreateAdSenseLinkRequest],
        Union[resources.AdSenseLink, Awaitable[resources.AdSenseLink]],
    ]:
        raise NotImplementedError()

    @property
    def delete_ad_sense_link(
        self,
    ) -> Callable[
        [analytics_admin.DeleteAdSenseLinkRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_ad_sense_links(
        self,
    ) -> Callable[
        [analytics_admin.ListAdSenseLinksRequest],
        Union[
            analytics_admin.ListAdSenseLinksResponse,
            Awaitable[analytics_admin.ListAdSenseLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_event_create_rule(
        self,
    ) -> Callable[
        [analytics_admin.GetEventCreateRuleRequest],
        Union[
            event_create_and_edit.EventCreateRule,
            Awaitable[event_create_and_edit.EventCreateRule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_event_create_rules(
        self,
    ) -> Callable[
        [analytics_admin.ListEventCreateRulesRequest],
        Union[
            analytics_admin.ListEventCreateRulesResponse,
            Awaitable[analytics_admin.ListEventCreateRulesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_event_create_rule(
        self,
    ) -> Callable[
        [analytics_admin.CreateEventCreateRuleRequest],
        Union[
            event_create_and_edit.EventCreateRule,
            Awaitable[event_create_and_edit.EventCreateRule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_event_create_rule(
        self,
    ) -> Callable[
        [analytics_admin.UpdateEventCreateRuleRequest],
        Union[
            event_create_and_edit.EventCreateRule,
            Awaitable[event_create_and_edit.EventCreateRule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_event_create_rule(
        self,
    ) -> Callable[
        [analytics_admin.DeleteEventCreateRuleRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_event_edit_rule(
        self,
    ) -> Callable[
        [analytics_admin.GetEventEditRuleRequest],
        Union[
            event_create_and_edit.EventEditRule,
            Awaitable[event_create_and_edit.EventEditRule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_event_edit_rules(
        self,
    ) -> Callable[
        [analytics_admin.ListEventEditRulesRequest],
        Union[
            analytics_admin.ListEventEditRulesResponse,
            Awaitable[analytics_admin.ListEventEditRulesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_event_edit_rule(
        self,
    ) -> Callable[
        [analytics_admin.CreateEventEditRuleRequest],
        Union[
            event_create_and_edit.EventEditRule,
            Awaitable[event_create_and_edit.EventEditRule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_event_edit_rule(
        self,
    ) -> Callable[
        [analytics_admin.UpdateEventEditRuleRequest],
        Union[
            event_create_and_edit.EventEditRule,
            Awaitable[event_create_and_edit.EventEditRule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_event_edit_rule(
        self,
    ) -> Callable[
        [analytics_admin.DeleteEventEditRuleRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def reorder_event_edit_rules(
        self,
    ) -> Callable[
        [analytics_admin.ReorderEventEditRulesRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_data_redaction_settings(
        self,
    ) -> Callable[
        [analytics_admin.UpdateDataRedactionSettingsRequest],
        Union[
            resources.DataRedactionSettings, Awaitable[resources.DataRedactionSettings]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_data_redaction_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetDataRedactionSettingsRequest],
        Union[
            resources.DataRedactionSettings, Awaitable[resources.DataRedactionSettings]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_calculated_metric(
        self,
    ) -> Callable[
        [analytics_admin.GetCalculatedMetricRequest],
        Union[resources.CalculatedMetric, Awaitable[resources.CalculatedMetric]],
    ]:
        raise NotImplementedError()

    @property
    def create_calculated_metric(
        self,
    ) -> Callable[
        [analytics_admin.CreateCalculatedMetricRequest],
        Union[resources.CalculatedMetric, Awaitable[resources.CalculatedMetric]],
    ]:
        raise NotImplementedError()

    @property
    def list_calculated_metrics(
        self,
    ) -> Callable[
        [analytics_admin.ListCalculatedMetricsRequest],
        Union[
            analytics_admin.ListCalculatedMetricsResponse,
            Awaitable[analytics_admin.ListCalculatedMetricsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_calculated_metric(
        self,
    ) -> Callable[
        [analytics_admin.UpdateCalculatedMetricRequest],
        Union[resources.CalculatedMetric, Awaitable[resources.CalculatedMetric]],
    ]:
        raise NotImplementedError()

    @property
    def delete_calculated_metric(
        self,
    ) -> Callable[
        [analytics_admin.DeleteCalculatedMetricRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_rollup_property(
        self,
    ) -> Callable[
        [analytics_admin.CreateRollupPropertyRequest],
        Union[
            analytics_admin.CreateRollupPropertyResponse,
            Awaitable[analytics_admin.CreateRollupPropertyResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_rollup_property_source_link(
        self,
    ) -> Callable[
        [analytics_admin.GetRollupPropertySourceLinkRequest],
        Union[
            resources.RollupPropertySourceLink,
            Awaitable[resources.RollupPropertySourceLink],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_rollup_property_source_links(
        self,
    ) -> Callable[
        [analytics_admin.ListRollupPropertySourceLinksRequest],
        Union[
            analytics_admin.ListRollupPropertySourceLinksResponse,
            Awaitable[analytics_admin.ListRollupPropertySourceLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_rollup_property_source_link(
        self,
    ) -> Callable[
        [analytics_admin.CreateRollupPropertySourceLinkRequest],
        Union[
            resources.RollupPropertySourceLink,
            Awaitable[resources.RollupPropertySourceLink],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_rollup_property_source_link(
        self,
    ) -> Callable[
        [analytics_admin.DeleteRollupPropertySourceLinkRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def provision_subproperty(
        self,
    ) -> Callable[
        [analytics_admin.ProvisionSubpropertyRequest],
        Union[
            analytics_admin.ProvisionSubpropertyResponse,
            Awaitable[analytics_admin.ProvisionSubpropertyResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_subproperty_event_filter(
        self,
    ) -> Callable[
        [analytics_admin.CreateSubpropertyEventFilterRequest],
        Union[
            gaa_subproperty_event_filter.SubpropertyEventFilter,
            Awaitable[gaa_subproperty_event_filter.SubpropertyEventFilter],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_subproperty_event_filter(
        self,
    ) -> Callable[
        [analytics_admin.GetSubpropertyEventFilterRequest],
        Union[
            subproperty_event_filter.SubpropertyEventFilter,
            Awaitable[subproperty_event_filter.SubpropertyEventFilter],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_subproperty_event_filters(
        self,
    ) -> Callable[
        [analytics_admin.ListSubpropertyEventFiltersRequest],
        Union[
            analytics_admin.ListSubpropertyEventFiltersResponse,
            Awaitable[analytics_admin.ListSubpropertyEventFiltersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_subproperty_event_filter(
        self,
    ) -> Callable[
        [analytics_admin.UpdateSubpropertyEventFilterRequest],
        Union[
            gaa_subproperty_event_filter.SubpropertyEventFilter,
            Awaitable[gaa_subproperty_event_filter.SubpropertyEventFilter],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_subproperty_event_filter(
        self,
    ) -> Callable[
        [analytics_admin.DeleteSubpropertyEventFilterRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_reporting_data_annotation(
        self,
    ) -> Callable[
        [analytics_admin.CreateReportingDataAnnotationRequest],
        Union[
            resources.ReportingDataAnnotation,
            Awaitable[resources.ReportingDataAnnotation],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_reporting_data_annotation(
        self,
    ) -> Callable[
        [analytics_admin.GetReportingDataAnnotationRequest],
        Union[
            resources.ReportingDataAnnotation,
            Awaitable[resources.ReportingDataAnnotation],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_reporting_data_annotations(
        self,
    ) -> Callable[
        [analytics_admin.ListReportingDataAnnotationsRequest],
        Union[
            analytics_admin.ListReportingDataAnnotationsResponse,
            Awaitable[analytics_admin.ListReportingDataAnnotationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_reporting_data_annotation(
        self,
    ) -> Callable[
        [analytics_admin.UpdateReportingDataAnnotationRequest],
        Union[
            resources.ReportingDataAnnotation,
            Awaitable[resources.ReportingDataAnnotation],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_reporting_data_annotation(
        self,
    ) -> Callable[
        [analytics_admin.DeleteReportingDataAnnotationRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def submit_user_deletion(
        self,
    ) -> Callable[
        [analytics_admin.SubmitUserDeletionRequest],
        Union[
            analytics_admin.SubmitUserDeletionResponse,
            Awaitable[analytics_admin.SubmitUserDeletionResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_subproperty_sync_configs(
        self,
    ) -> Callable[
        [analytics_admin.ListSubpropertySyncConfigsRequest],
        Union[
            analytics_admin.ListSubpropertySyncConfigsResponse,
            Awaitable[analytics_admin.ListSubpropertySyncConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_subproperty_sync_config(
        self,
    ) -> Callable[
        [analytics_admin.UpdateSubpropertySyncConfigRequest],
        Union[
            resources.SubpropertySyncConfig, Awaitable[resources.SubpropertySyncConfig]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_subproperty_sync_config(
        self,
    ) -> Callable[
        [analytics_admin.GetSubpropertySyncConfigRequest],
        Union[
            resources.SubpropertySyncConfig, Awaitable[resources.SubpropertySyncConfig]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_reporting_identity_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetReportingIdentitySettingsRequest],
        Union[
            resources.ReportingIdentitySettings,
            Awaitable[resources.ReportingIdentitySettings],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_reporting_identity_settings(
        self,
    ) -> Callable[
        [analytics_admin.UpdateReportingIdentitySettingsRequest],
        Union[
            resources.ReportingIdentitySettings,
            Awaitable[resources.ReportingIdentitySettings],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_user_provided_data_settings(
        self,
    ) -> Callable[
        [analytics_admin.GetUserProvidedDataSettingsRequest],
        Union[
            resources.UserProvidedDataSettings,
            Awaitable[resources.UserProvidedDataSettings],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("AnalyticsAdminServiceTransport",)
