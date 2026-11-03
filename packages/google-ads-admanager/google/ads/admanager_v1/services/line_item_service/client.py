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
import json
import logging as std_logging
import os
import re
import warnings
from collections import OrderedDict
from http import HTTPStatus
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
    cast,
)

import google.protobuf
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.ads.admanager_v1 import gapic_version as package_version
from google.ads.admanager_v1._compat import (
    get_api_endpoint,
    get_default_mtls_endpoint,
    get_universe_domain,
    read_environment_variables,
    should_use_client_cert,
)

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.ads.admanager_v1.services.line_item_service import pagers
from google.ads.admanager_v1.types import (
    applied_label,
    child_content_eligibility_enum,
    creative_placeholder,
    creative_targeting,
    custom_field_value,
    custom_pacing_curve,
    delivery_enums,
    delivery_indicator,
    environment_type_enum,
    exclusion_scope_enum,
    frequency_cap,
    goal,
    grp_settings,
    line_item_allowed_format_enum,
    line_item_deal_info,
    line_item_delivery_forecast_source_enum,
    line_item_discount,
    line_item_enums,
    line_item_messages,
    line_item_service,
    line_item_stats,
    skippable_ad_type_enum,
    targeting,
    third_party_measurement_settings,
)

from .transports.base import DEFAULT_CLIENT_INFO, LineItemServiceTransport
from .transports.rest import LineItemServiceRestTransport


class LineItemServiceClientMeta(type):
    """Metaclass for the LineItemService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[LineItemServiceTransport]]
    _transport_registry["rest"] = LineItemServiceRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[LineItemServiceTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class LineItemServiceClient(metaclass=LineItemServiceClientMeta):
    """Provides methods for handling ``LineItem`` objects."""

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "admanager.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "admanager.{UNIVERSE_DOMAIN}"
    _DEFAULT_UNIVERSE = "googleapis.com"

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            LineItemServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

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
            LineItemServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> LineItemServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            LineItemServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def ad_unit_path(
        network_code: str,
        ad_unit: str,
    ) -> str:
        """Returns a fully-qualified ad_unit string."""
        return "networks/{network_code}/adUnits/{ad_unit}".format(
            network_code=network_code,
            ad_unit=ad_unit,
        )

    @staticmethod
    def parse_ad_unit_path(path: str) -> Dict[str, str]:
        """Parses a ad_unit path into its component segments."""
        m = re.match(r"^networks/(?P<network_code>.+?)/adUnits/(?P<ad_unit>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def application_path(
        network_code: str,
        application: str,
    ) -> str:
        """Returns a fully-qualified application string."""
        return "networks/{network_code}/applications/{application}".format(
            network_code=network_code,
            application=application,
        )

    @staticmethod
    def parse_application_path(path: str) -> Dict[str, str]:
        """Parses a application path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/applications/(?P<application>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def audience_segment_path(
        network_code: str,
        audience_segment: str,
    ) -> str:
        """Returns a fully-qualified audience_segment string."""
        return "networks/{network_code}/audienceSegments/{audience_segment}".format(
            network_code=network_code,
            audience_segment=audience_segment,
        )

    @staticmethod
    def parse_audience_segment_path(path: str) -> Dict[str, str]:
        """Parses a audience_segment path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/audienceSegments/(?P<audience_segment>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def bandwidth_group_path(
        network_code: str,
        bandwidth_group: str,
    ) -> str:
        """Returns a fully-qualified bandwidth_group string."""
        return "networks/{network_code}/bandwidthGroups/{bandwidth_group}".format(
            network_code=network_code,
            bandwidth_group=bandwidth_group,
        )

    @staticmethod
    def parse_bandwidth_group_path(path: str) -> Dict[str, str]:
        """Parses a bandwidth_group path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/bandwidthGroups/(?P<bandwidth_group>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def browser_path(
        network_code: str,
        browser: str,
    ) -> str:
        """Returns a fully-qualified browser string."""
        return "networks/{network_code}/browsers/{browser}".format(
            network_code=network_code,
            browser=browser,
        )

    @staticmethod
    def parse_browser_path(path: str) -> Dict[str, str]:
        """Parses a browser path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/browsers/(?P<browser>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def browser_language_path(
        network_code: str,
        browser_language: str,
    ) -> str:
        """Returns a fully-qualified browser_language string."""
        return "networks/{network_code}/browserLanguages/{browser_language}".format(
            network_code=network_code,
            browser_language=browser_language,
        )

    @staticmethod
    def parse_browser_language_path(path: str) -> Dict[str, str]:
        """Parses a browser_language path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/browserLanguages/(?P<browser_language>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def cms_metadata_value_path(
        network_code: str,
        cms_metadata_value: str,
    ) -> str:
        """Returns a fully-qualified cms_metadata_value string."""
        return "networks/{network_code}/cmsMetadataValues/{cms_metadata_value}".format(
            network_code=network_code,
            cms_metadata_value=cms_metadata_value,
        )

    @staticmethod
    def parse_cms_metadata_value_path(path: str) -> Dict[str, str]:
        """Parses a cms_metadata_value path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/cmsMetadataValues/(?P<cms_metadata_value>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def company_path(
        network_code: str,
        company: str,
    ) -> str:
        """Returns a fully-qualified company string."""
        return "networks/{network_code}/companies/{company}".format(
            network_code=network_code,
            company=company,
        )

    @staticmethod
    def parse_company_path(path: str) -> Dict[str, str]:
        """Parses a company path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/companies/(?P<company>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def content_path(
        network_code: str,
        content: str,
    ) -> str:
        """Returns a fully-qualified content string."""
        return "networks/{network_code}/content/{content}".format(
            network_code=network_code,
            content=content,
        )

    @staticmethod
    def parse_content_path(path: str) -> Dict[str, str]:
        """Parses a content path into its component segments."""
        m = re.match(r"^networks/(?P<network_code>.+?)/content/(?P<content>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def content_bundle_path(
        network_code: str,
        content_bundle: str,
    ) -> str:
        """Returns a fully-qualified content_bundle string."""
        return "networks/{network_code}/contentBundles/{content_bundle}".format(
            network_code=network_code,
            content_bundle=content_bundle,
        )

    @staticmethod
    def parse_content_bundle_path(path: str) -> Dict[str, str]:
        """Parses a content_bundle path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/contentBundles/(?P<content_bundle>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def custom_field_path(
        network_code: str,
        custom_field: str,
    ) -> str:
        """Returns a fully-qualified custom_field string."""
        return "networks/{network_code}/customFields/{custom_field}".format(
            network_code=network_code,
            custom_field=custom_field,
        )

    @staticmethod
    def parse_custom_field_path(path: str) -> Dict[str, str]:
        """Parses a custom_field path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/customFields/(?P<custom_field>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def custom_targeting_key_path(
        network_code: str,
        custom_targeting_key: str,
    ) -> str:
        """Returns a fully-qualified custom_targeting_key string."""
        return (
            "networks/{network_code}/customTargetingKeys/{custom_targeting_key}".format(
                network_code=network_code,
                custom_targeting_key=custom_targeting_key,
            )
        )

    @staticmethod
    def parse_custom_targeting_key_path(path: str) -> Dict[str, str]:
        """Parses a custom_targeting_key path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/customTargetingKeys/(?P<custom_targeting_key>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def custom_targeting_value_path(
        network_code: str,
        custom_targeting_value: str,
    ) -> str:
        """Returns a fully-qualified custom_targeting_value string."""
        return "networks/{network_code}/customTargetingValues/{custom_targeting_value}".format(
            network_code=network_code,
            custom_targeting_value=custom_targeting_value,
        )

    @staticmethod
    def parse_custom_targeting_value_path(path: str) -> Dict[str, str]:
        """Parses a custom_targeting_value path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/customTargetingValues/(?P<custom_targeting_value>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def device_capability_path(
        network_code: str,
        device_capability: str,
    ) -> str:
        """Returns a fully-qualified device_capability string."""
        return "networks/{network_code}/deviceCapabilities/{device_capability}".format(
            network_code=network_code,
            device_capability=device_capability,
        )

    @staticmethod
    def parse_device_capability_path(path: str) -> Dict[str, str]:
        """Parses a device_capability path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/deviceCapabilities/(?P<device_capability>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def device_category_path(
        network_code: str,
        device_category: str,
    ) -> str:
        """Returns a fully-qualified device_category string."""
        return "networks/{network_code}/deviceCategories/{device_category}".format(
            network_code=network_code,
            device_category=device_category,
        )

    @staticmethod
    def parse_device_category_path(path: str) -> Dict[str, str]:
        """Parses a device_category path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/deviceCategories/(?P<device_category>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def device_manufacturer_path(
        network_code: str,
        device_manufacturer: str,
    ) -> str:
        """Returns a fully-qualified device_manufacturer string."""
        return (
            "networks/{network_code}/deviceManufacturers/{device_manufacturer}".format(
                network_code=network_code,
                device_manufacturer=device_manufacturer,
            )
        )

    @staticmethod
    def parse_device_manufacturer_path(path: str) -> Dict[str, str]:
        """Parses a device_manufacturer path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/deviceManufacturers/(?P<device_manufacturer>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def geo_target_path(
        network_code: str,
        geo_target: str,
    ) -> str:
        """Returns a fully-qualified geo_target string."""
        return "networks/{network_code}/geoTargets/{geo_target}".format(
            network_code=network_code,
            geo_target=geo_target,
        )

    @staticmethod
    def parse_geo_target_path(path: str) -> Dict[str, str]:
        """Parses a geo_target path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/geoTargets/(?P<geo_target>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def label_path(
        network_code: str,
        label: str,
    ) -> str:
        """Returns a fully-qualified label string."""
        return "networks/{network_code}/labels/{label}".format(
            network_code=network_code,
            label=label,
        )

    @staticmethod
    def parse_label_path(path: str) -> Dict[str, str]:
        """Parses a label path into its component segments."""
        m = re.match(r"^networks/(?P<network_code>.+?)/labels/(?P<label>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def line_item_path(
        network_code: str,
        line_item: str,
    ) -> str:
        """Returns a fully-qualified line_item string."""
        return "networks/{network_code}/lineItems/{line_item}".format(
            network_code=network_code,
            line_item=line_item,
        )

    @staticmethod
    def parse_line_item_path(path: str) -> Dict[str, str]:
        """Parses a line_item path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/lineItems/(?P<line_item>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def mobile_carrier_path(
        network_code: str,
        mobile_carrier: str,
    ) -> str:
        """Returns a fully-qualified mobile_carrier string."""
        return "networks/{network_code}/mobileCarriers/{mobile_carrier}".format(
            network_code=network_code,
            mobile_carrier=mobile_carrier,
        )

    @staticmethod
    def parse_mobile_carrier_path(path: str) -> Dict[str, str]:
        """Parses a mobile_carrier path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/mobileCarriers/(?P<mobile_carrier>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def mobile_device_path(
        network_code: str,
        mobile_device: str,
    ) -> str:
        """Returns a fully-qualified mobile_device string."""
        return "networks/{network_code}/mobileDevices/{mobile_device}".format(
            network_code=network_code,
            mobile_device=mobile_device,
        )

    @staticmethod
    def parse_mobile_device_path(path: str) -> Dict[str, str]:
        """Parses a mobile_device path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/mobileDevices/(?P<mobile_device>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def mobile_device_submodel_path(
        network_code: str,
        mobile_device_submodel: str,
    ) -> str:
        """Returns a fully-qualified mobile_device_submodel string."""
        return "networks/{network_code}/mobileDeviceSubmodels/{mobile_device_submodel}".format(
            network_code=network_code,
            mobile_device_submodel=mobile_device_submodel,
        )

    @staticmethod
    def parse_mobile_device_submodel_path(path: str) -> Dict[str, str]:
        """Parses a mobile_device_submodel path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/mobileDeviceSubmodels/(?P<mobile_device_submodel>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def network_path(
        network_code: str,
    ) -> str:
        """Returns a fully-qualified network string."""
        return "networks/{network_code}".format(
            network_code=network_code,
        )

    @staticmethod
    def parse_network_path(path: str) -> Dict[str, str]:
        """Parses a network path into its component segments."""
        m = re.match(r"^networks/(?P<network_code>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def operating_system_path(
        network_code: str,
        operating_system: str,
    ) -> str:
        """Returns a fully-qualified operating_system string."""
        return "networks/{network_code}/operatingSystems/{operating_system}".format(
            network_code=network_code,
            operating_system=operating_system,
        )

    @staticmethod
    def parse_operating_system_path(path: str) -> Dict[str, str]:
        """Parses a operating_system path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/operatingSystems/(?P<operating_system>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def operating_system_version_path(
        network_code: str,
        operating_system_version: str,
    ) -> str:
        """Returns a fully-qualified operating_system_version string."""
        return "networks/{network_code}/operatingSystemVersions/{operating_system_version}".format(
            network_code=network_code,
            operating_system_version=operating_system_version,
        )

    @staticmethod
    def parse_operating_system_version_path(path: str) -> Dict[str, str]:
        """Parses a operating_system_version path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/operatingSystemVersions/(?P<operating_system_version>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def order_path(
        network_code: str,
        order: str,
    ) -> str:
        """Returns a fully-qualified order string."""
        return "networks/{network_code}/orders/{order}".format(
            network_code=network_code,
            order=order,
        )

    @staticmethod
    def parse_order_path(path: str) -> Dict[str, str]:
        """Parses a order path into its component segments."""
        m = re.match(r"^networks/(?P<network_code>.+?)/orders/(?P<order>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def placement_path(
        network_code: str,
        placement: str,
    ) -> str:
        """Returns a fully-qualified placement string."""
        return "networks/{network_code}/placements/{placement}".format(
            network_code=network_code,
            placement=placement,
        )

    @staticmethod
    def parse_placement_path(path: str) -> Dict[str, str]:
        """Parses a placement path into its component segments."""
        m = re.match(
            r"^networks/(?P<network_code>.+?)/placements/(?P<placement>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(
        billing_account: str,
    ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(
        folder: str,
    ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(
            folder=folder,
        )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(
        organization: str,
    ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(
            organization=organization,
        )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(
        project: str,
    ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(
            project=project,
        )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
    ):
        """Deprecated. Return the API endpoint and client cert source for mutual TLS.

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

        warnings.warn(
            "get_mtls_endpoint_and_cert_source is deprecated. Use the api_endpoint property instead.",
            DeprecationWarning,
        )
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = should_use_client_cert()
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert:
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT  # type: ignore
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    @staticmethod
    def _get_client_cert_source(provided_cert_source, use_cert_flag):
        """Return the client cert source to be used by the client.

        Args:
            provided_cert_source (bytes): The client certificate source provided.
            use_cert_flag (bool): A flag indicating whether to use the client certificate.

        Returns:
            bytes or None: The client cert source to be used by the client.
        """
        client_cert_source = None
        if use_cert_flag:
            if provided_cert_source:
                client_cert_source = provided_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()
        return client_cert_source

    def _validate_universe_domain(self):
        """Validates client's and credentials' universe domains are consistent.

        Returns:
            bool: True iff the configured universe domain is valid.

        Raises:
            ValueError: If the configured universe domain is not valid.
        """

        # NOTE (b/349488459): universe validation is disabled until further notice.
        return True

    def _add_cred_info_for_auth_errors(
        self, error: core_exceptions.GoogleAPICallError
    ) -> None:
        """Adds credential info string to error details for 401/403/404 errors.

        Args:
            error (google.api_core.exceptions.GoogleAPICallError): The error to add the cred info.
        """
        if error.code not in [
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
            HTTPStatus.NOT_FOUND,
        ]:
            return

        cred = self._transport._credentials

        # get_cred_info is only available in google-auth>=2.35.0
        if not hasattr(cred, "get_cred_info"):
            return

        # ignore the type check since pypy test fails when get_cred_info
        # is not available
        cred_info = cred.get_cred_info()  # type: ignore
        if cred_info and hasattr(error._details, "append"):
            error._details.append(json.dumps(cred_info))

    @property
    def api_endpoint(self) -> str:
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used by the client instance.
        """
        return self._universe_domain

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str, LineItemServiceTransport, Callable[..., LineItemServiceTransport]
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the line item service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,LineItemServiceTransport,Callable[..., LineItemServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the LineItemServiceTransport constructor.
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
                default "googleapis.com" universe. Note that the ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client_options = client_options
        if isinstance(self._client_options, dict):
            self._client_options = client_options_lib.from_dict(self._client_options)
        if self._client_options is None:
            self._client_options = client_options_lib.ClientOptions()
        self._client_options = cast(
            client_options_lib.ClientOptions, self._client_options
        )

        universe_domain_opt = getattr(self._client_options, "universe_domain", None)

        self._use_client_cert, self._use_mtls_endpoint, self._universe_domain_env = (
            read_environment_variables()
        )
        self._client_cert_source = LineItemServiceClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=LineItemServiceClient._DEFAULT_UNIVERSE,
        )
        self._api_endpoint: str = ""  # updated below, depending on `transport`

        # Initialize the universe domain validation.
        self._is_universe_domain_valid = False

        if CLIENT_LOGGING_SUPPORTED:  # pragma: NO COVER
            # Setup logging.
            client_logging.initialize_logging()

        api_key_value = getattr(self._client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        transport_provided = isinstance(transport, LineItemServiceTransport)
        if transport_provided:
            # transport is a LineItemServiceTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(LineItemServiceTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=LineItemServiceClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=LineItemServiceClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=LineItemServiceClient._DEFAULT_ENDPOINT_TEMPLATE,
            use_mtls=self._use_mtls_endpoint == "always"
            or (self._use_mtls_endpoint == "auto" and self._client_cert_source),
        )

        if not transport_provided:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            transport_init: Union[
                Type[LineItemServiceTransport], Callable[..., LineItemServiceTransport]
            ] = (
                LineItemServiceClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., LineItemServiceTransport], transport)
            )
            # initialize with the provided callable or the passed in class
            self._transport = transport_init(
                credentials=credentials,
                credentials_file=self._client_options.credentials_file,
                host=self._api_endpoint,
                scopes=self._client_options.scopes,
                client_cert_source_for_mtls=self._client_cert_source,
                quota_project_id=self._client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
                api_audience=self._client_options.api_audience,
            )

        if "async" not in str(self._transport):
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                std_logging.DEBUG
            ):  # pragma: NO COVER
                _LOGGER.debug(
                    "Created client `google.ads.admanager_v1.LineItemServiceClient`.",
                    extra={
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "universeDomain": getattr(
                            self._transport._credentials, "universe_domain", ""
                        ),
                        "credentialsType": f"{type(self._transport._credentials).__module__}.{type(self._transport._credentials).__qualname__}",
                        "credentialsInfo": getattr(
                            self.transport._credentials, "get_cred_info", lambda: None
                        )(),
                    }
                    if hasattr(self._transport, "_credentials")
                    else {
                        "serviceName": "google.ads.admanager.v1.LineItemService",
                        "credentialsType": None,
                    },
                )

    def get_line_item(
        self,
        request: Optional[Union[line_item_service.GetLineItemRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_messages.LineItem:
        r"""Retrieves a ``LineItem`` object.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_get_line_item():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.GetLineItemRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_line_item(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.GetLineItemRequest, dict]):
                The request object. Request object for ``GetLineItem`` method.
            name (str):
                Required. The resource name of the LineItem. Format:
                ``networks/{network_code}/lineItems/{line_item_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.LineItem:
                A LineItem contains information about
                how specific ad creatives are intended
                to serve to your website or app along
                with pricing and other delivery details.

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
        if not isinstance(request, line_item_service.GetLineItemRequest):
            request = line_item_service.GetLineItemRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_line_item]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_line_items(
        self,
        request: Optional[Union[line_item_service.ListLineItemsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListLineItemsPager:
        r"""Lists ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_list_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.ListLineItemsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_line_items(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.ListLineItemsRequest, dict]):
                The request object. Request object for ``ListLineItems`` method.
            parent (str):
                Required. The parent, which owns this collection of
                LineItems. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.services.line_item_service.pagers.ListLineItemsPager:
                Response object for ListLineItemsRequest containing matching LineItem
                   objects.

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
        if not isinstance(request, line_item_service.ListLineItemsRequest):
            request = line_item_service.ListLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_line_items]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListLineItemsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_line_item(
        self,
        request: Optional[Union[line_item_service.CreateLineItemRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        line_item: Optional[line_item_messages.LineItem] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_messages.LineItem:
        r"""Creates a ``LineItem`` object.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_create_line_item():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                line_item = admanager_v1.LineItem()
                line_item.creative_placeholders.size.width = 544
                line_item.creative_placeholders.size.height = 633
                line_item.creative_placeholders.size.size_type = "AUDIO"

                request = admanager_v1.CreateLineItemRequest(
                    parent="parent_value",
                    line_item=line_item,
                )

                # Make the request
                response = client.create_line_item(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.CreateLineItemRequest, dict]):
                The request object. Request object for ``CreateLineItem`` method.
            parent (str):
                Required. The parent resource where this ``LineItem``
                will be created. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            line_item (google.ads.admanager_v1.types.LineItem):
                Required. The ``LineItem`` to create.
                This corresponds to the ``line_item`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.LineItem:
                A LineItem contains information about
                how specific ad creatives are intended
                to serve to your website or app along
                with pricing and other delivery details.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, line_item]
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
        if not isinstance(request, line_item_service.CreateLineItemRequest):
            request = line_item_service.CreateLineItemRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if line_item is not None:
                request.line_item = line_item

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_line_item]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_create_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchCreateLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        requests: Optional[
            MutableSequence[line_item_service.CreateLineItemRequest]
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_service.BatchCreateLineItemsResponse:
        r"""Creates ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_create_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                requests = admanager_v1.CreateLineItemRequest()
                requests.parent = "parent_value"
                requests.line_item.creative_placeholders.size.width = 544
                requests.line_item.creative_placeholders.size.height = 633
                requests.line_item.creative_placeholders.size.size_type = "AUDIO"

                request = admanager_v1.BatchCreateLineItemsRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = client.batch_create_line_items(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchCreateLineItemsRequest, dict]):
                The request object. Request object for ``BatchCreateLineItems`` method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be created. Format: ``networks/{network_code}`` The
                parent field in the CreateLineItemRequest must match
                this field.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            requests (MutableSequence[google.ads.admanager_v1.types.CreateLineItemRequest]):
                Required. The ``LineItem`` objects to create. A maximum
                of 100 objects can be created in a batch.

                This corresponds to the ``requests`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.BatchCreateLineItemsResponse:
                Response object for BatchCreateLineItems method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, requests]
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
        if not isinstance(request, line_item_service.BatchCreateLineItemsRequest):
            request = line_item_service.BatchCreateLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if requests is not None:
                request.requests = requests

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_create_line_items]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_line_item(
        self,
        request: Optional[Union[line_item_service.UpdateLineItemRequest, dict]] = None,
        *,
        line_item: Optional[line_item_messages.LineItem] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_messages.LineItem:
        r"""Updates a ``LineItem`` object.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_update_line_item():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                line_item = admanager_v1.LineItem()
                line_item.creative_placeholders.size.width = 544
                line_item.creative_placeholders.size.height = 633
                line_item.creative_placeholders.size.size_type = "AUDIO"

                request = admanager_v1.UpdateLineItemRequest(
                    line_item=line_item,
                )

                # Make the request
                response = client.update_line_item(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.UpdateLineItemRequest, dict]):
                The request object. Request object for ``UpdateLineItem`` method.
            line_item (google.ads.admanager_v1.types.LineItem):
                Required. The ``LineItem`` to update.

                The ``LineItem``'s ``name`` is used to identify the
                ``LineItem`` to update.

                This corresponds to the ``line_item`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The list of fields to
                update.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.LineItem:
                A LineItem contains information about
                how specific ad creatives are intended
                to serve to your website or app along
                with pricing and other delivery details.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [line_item, update_mask]
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
        if not isinstance(request, line_item_service.UpdateLineItemRequest):
            request = line_item_service.UpdateLineItemRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if line_item is not None:
                request.line_item = line_item
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_line_item]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("line_item.name", request.line_item.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_update_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchUpdateLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        requests: Optional[
            MutableSequence[line_item_service.UpdateLineItemRequest]
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_service.BatchUpdateLineItemsResponse:
        r"""Batch updates ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_update_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                requests = admanager_v1.UpdateLineItemRequest()
                requests.line_item.creative_placeholders.size.width = 544
                requests.line_item.creative_placeholders.size.height = 633
                requests.line_item.creative_placeholders.size.size_type = "AUDIO"

                request = admanager_v1.BatchUpdateLineItemsRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = client.batch_update_line_items(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchUpdateLineItemsRequest, dict]):
                The request object. Request object for ``BatchUpdateLineItems`` method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be updated. Format: ``networks/{network_code}`` The
                parent segment of the ``line_item.name`` in each
                ``UpdateLineItemRequest`` must match this field.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            requests (MutableSequence[google.ads.admanager_v1.types.UpdateLineItemRequest]):
                Required. The ``LineItem`` objects to update. A maximum
                of 100 objects can be updated in a batch.

                This corresponds to the ``requests`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.BatchUpdateLineItemsResponse:
                Response object for BatchUpdateLineItems method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, requests]
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
        if not isinstance(request, line_item_service.BatchUpdateLineItemsRequest):
            request = line_item_service.BatchUpdateLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if requests is not None:
                request.requests = requests

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_update_line_items]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_activate_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchActivateLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_service.BatchActivateLineItemsResponse:
        r"""Batch activates ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_activate_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchActivateLineItemsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = client.batch_activate_line_items(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchActivateLineItemsRequest, dict]):
                The request object. Request object for ``BatchActivateLineItems`` method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be updated. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. The names of the ``LineItem`` objects to
                activate. Format:
                ``networks/{network_code}/lineItems/{line_item}``

                This corresponds to the ``names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.BatchActivateLineItemsResponse:
                Response object for BatchActivateLineItems method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(request, line_item_service.BatchActivateLineItemsRequest):
            request = line_item_service.BatchActivateLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.batch_activate_line_items
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_pause_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchPauseLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_service.BatchPauseLineItemsResponse:
        r"""Batch pauses ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_pause_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchPauseLineItemsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = client.batch_pause_line_items(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchPauseLineItemsRequest, dict]):
                The request object. Request object for ``BatchPauseLineItems`` method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be updated. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. The names of the ``LineItem`` objects to
                pause. Format:
                ``networks/{network_code}/lineItems/{line_item}``

                This corresponds to the ``names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.BatchPauseLineItemsResponse:
                Response object for BatchPauseLineItems method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(request, line_item_service.BatchPauseLineItemsRequest):
            request = line_item_service.BatchPauseLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_pause_line_items]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_resume_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchResumeLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_service.BatchResumeLineItemsResponse:
        r"""Batch resumes ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_resume_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchResumeLineItemsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = client.batch_resume_line_items(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchResumeLineItemsRequest, dict]):
                The request object. Request object for ``BatchResumeLineItems`` method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be updated. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. The names of the ``LineItem`` objects to
                resume. Format:
                ``networks/{network_code}/lineItems/{line_item}``

                This corresponds to the ``names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.BatchResumeLineItemsResponse:
                Response object for BatchResumeLineItems method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(request, line_item_service.BatchResumeLineItemsRequest):
            request = line_item_service.BatchResumeLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_resume_line_items]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_resume_and_overbook_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchResumeAndOverbookLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_service.BatchResumeAndOverbookLineItemsResponse:
        r"""Batch resumes and overbooks ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_resume_and_overbook_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchResumeAndOverbookLineItemsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = client.batch_resume_and_overbook_line_items(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchResumeAndOverbookLineItemsRequest, dict]):
                The request object. Request object for ``BatchResumeAndOverbookLineItems``
                method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be updated. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. The names of the ``LineItem`` objects to
                resume and overbook. Format:
                ``networks/{network_code}/lineItems/{line_item}``

                This corresponds to the ``names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.BatchResumeAndOverbookLineItemsResponse:
                Response object for BatchResumeAndOverbookLineItems
                method.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(
            request, line_item_service.BatchResumeAndOverbookLineItemsRequest
        ):
            request = line_item_service.BatchResumeAndOverbookLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.batch_resume_and_overbook_line_items
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_delete_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchDeleteLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Batch deletes ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_delete_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchDeleteLineItemsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                client.batch_delete_line_items(request=request)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchDeleteLineItemsRequest, dict]):
                The request object. Request object for ``BatchDeleteLineItems`` method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be updated. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. The names of the ``LineItem`` objects to
                delete. Format:
                ``networks/{network_code}/lineItems/{line_item}``

                This corresponds to the ``names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(request, line_item_service.BatchDeleteLineItemsRequest):
            request = line_item_service.BatchDeleteLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_delete_line_items]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def batch_reserve_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchReserveLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_service.BatchReserveLineItemsResponse:
        r"""Batch reserves ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_reserve_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchReserveLineItemsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = client.batch_reserve_line_items(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchReserveLineItemsRequest, dict]):
                The request object. Request object for ``BatchReserveLineItems`` method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be updated. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. The names of the ``LineItem`` objects to
                reserve. Format:
                ``networks/{network_code}/lineItems/{line_item}``

                This corresponds to the ``names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.BatchReserveLineItemsResponse:
                Response object for BatchReserveLineItems method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(request, line_item_service.BatchReserveLineItemsRequest):
            request = line_item_service.BatchReserveLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_reserve_line_items]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_reserve_and_overbook_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchReserveAndOverbookLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_service.BatchReserveAndOverbookLineItemsResponse:
        r"""Batch reserves and overbooks ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_reserve_and_overbook_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchReserveAndOverbookLineItemsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = client.batch_reserve_and_overbook_line_items(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchReserveAndOverbookLineItemsRequest, dict]):
                The request object. Request object for ``BatchReserveAndOverbookLineItems``
                method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be updated. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. The names of the ``LineItem`` objects to
                reserve and overbook. Format:
                ``networks/{network_code}/lineItems/{line_item}``

                This corresponds to the ``names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.BatchReserveAndOverbookLineItemsResponse:
                Response object for BatchReserveAndOverbookLineItems
                method.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(
            request, line_item_service.BatchReserveAndOverbookLineItemsRequest
        ):
            request = line_item_service.BatchReserveAndOverbookLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.batch_reserve_and_overbook_line_items
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_release_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchReleaseLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_service.BatchReleaseLineItemsResponse:
        r"""Batch releases ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_release_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchReleaseLineItemsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = client.batch_release_line_items(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchReleaseLineItemsRequest, dict]):
                The request object. Request object for ``BatchReleaseLineItems`` method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be updated. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. The names of the ``LineItem`` objects to
                release. Format:
                ``networks/{network_code}/lineItems/{line_item}``

                This corresponds to the ``names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.BatchReleaseLineItemsResponse:
                Response object for BatchReleaseLineItems method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(request, line_item_service.BatchReleaseLineItemsRequest):
            request = line_item_service.BatchReleaseLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_release_line_items]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_archive_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchArchiveLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_service.BatchArchiveLineItemsResponse:
        r"""Batch archives ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_archive_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchArchiveLineItemsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = client.batch_archive_line_items(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchArchiveLineItemsRequest, dict]):
                The request object. Request object for ``BatchArchiveLineItems`` method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be updated. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. The names of the ``LineItem`` objects to
                archive. Format:
                ``networks/{network_code}/lineItems/{line_item}``

                This corresponds to the ``names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.BatchArchiveLineItemsResponse:
                Response object for BatchArchiveLineItems method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(request, line_item_service.BatchArchiveLineItemsRequest):
            request = line_item_service.BatchArchiveLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_archive_line_items]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def batch_unarchive_line_items(
        self,
        request: Optional[
            Union[line_item_service.BatchUnarchiveLineItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> line_item_service.BatchUnarchiveLineItemsResponse:
        r"""Batch unarchives ``LineItem`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_unarchive_line_items():
                # Create a client
                client = admanager_v1.LineItemServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchUnarchiveLineItemsRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = client.batch_unarchive_line_items(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchUnarchiveLineItemsRequest, dict]):
                The request object. Request object for ``BatchUnarchiveLineItems`` method.
            parent (str):
                Required. The parent resource where ``LineItems`` will
                be unarchived. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. The names of the ``LineItem`` objects to
                extract. Format:
                ``networks/{network_code}/lineItems/{line_item}``

                This corresponds to the ``names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.ads.admanager_v1.types.BatchUnarchiveLineItemsResponse:
                Response object for BatchUnarchiveLineItems method.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, names]
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
        if not isinstance(request, line_item_service.BatchUnarchiveLineItemsRequest):
            request = line_item_service.BatchUnarchiveLineItemsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.batch_unarchive_line_items
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "LineItemServiceClient":
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()

    def get_operation(
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
            retry (google.api_core.retry.Retry): Designation of what errors,
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
        rpc = self._transport._wrapped_methods[self._transport.get_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        try:
            # Send the request.
            response = rpc(
                request_pb,
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            )

            # Done; return the response.
            return response
        except core_exceptions.GoogleAPICallError as e:
            self._add_cred_info_for_auth_errors(e)
            raise e

    def cancel_operation(
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
            retry (google.api_core.retry.Retry): Designation of what errors,
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
        rpc = self._transport._wrapped_methods[self._transport.cancel_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__

__all__ = ("LineItemServiceClient",)
