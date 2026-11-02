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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.ads.admanager_v1.services.ad_rule_service import pagers
from google.ads.admanager_v1.types import (
    ad_rule_enums,
    ad_rule_messages,
    ad_rule_service,
    targeting,
)

from .transports.base import DEFAULT_CLIENT_INFO, AdRuleServiceTransport
from .transports.rest import AdRuleServiceRestTransport


class AdRuleServiceClientMeta(type):
    """Metaclass for the AdRuleService client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[AdRuleServiceTransport]]
    _transport_registry["rest"] = AdRuleServiceRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[AdRuleServiceTransport]:
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


class AdRuleServiceClient(metaclass=AdRuleServiceClientMeta):
    """Provides methods for handling ``AdRule`` objects."""

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
            AdRuleServiceClient: The constructed client.
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
            AdRuleServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> AdRuleServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            AdRuleServiceTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def ad_rule_path(
        network_code: str,
        ad_rule: str,
    ) -> str:
        """Returns a fully-qualified ad_rule string."""
        return "networks/{network_code}/adRules/{ad_rule}".format(
            network_code=network_code,
            ad_rule=ad_rule,
        )

    @staticmethod
    def parse_ad_rule_path(path: str) -> Dict[str, str]:
        """Parses a ad_rule path into its component segments."""
        m = re.match(r"^networks/(?P<network_code>.+?)/adRules/(?P<ad_rule>.+?)$", path)
        return m.groupdict() if m else {}

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
            Union[str, AdRuleServiceTransport, Callable[..., AdRuleServiceTransport]]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the ad rule service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,AdRuleServiceTransport,Callable[..., AdRuleServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the AdRuleServiceTransport constructor.
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
        self._client_cert_source = AdRuleServiceClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=AdRuleServiceClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, AdRuleServiceTransport)
        if transport_provided:
            # transport is a AdRuleServiceTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(AdRuleServiceTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=AdRuleServiceClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=AdRuleServiceClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=AdRuleServiceClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[AdRuleServiceTransport], Callable[..., AdRuleServiceTransport]
            ] = (
                AdRuleServiceClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., AdRuleServiceTransport], transport)
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
                    "Created client `google.ads.admanager_v1.AdRuleServiceClient`.",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
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
                        "serviceName": "google.ads.admanager.v1.AdRuleService",
                        "credentialsType": None,
                    },
                )

    def get_ad_rule(
        self,
        request: Optional[Union[ad_rule_service.GetAdRuleRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ad_rule_messages.AdRule:
        r"""Retrieves an ``AdRule`` object.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_get_ad_rule():
                # Create a client
                client = admanager_v1.AdRuleServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.GetAdRuleRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_ad_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.GetAdRuleRequest, dict]):
                The request object. Request object for ``GetAdRule`` method.
            name (str):
                Required. The resource name of the AdRule. Format:
                ``networks/{network_code}/adRules/{ad_rule_id}``

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
            google.ads.admanager_v1.types.AdRule:
                An AdRule contains data that the ad
                server will use to generate a playlist
                of video ads.

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
        if not isinstance(request, ad_rule_service.GetAdRuleRequest):
            request = ad_rule_service.GetAdRuleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_ad_rule]

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

    def list_ad_rules(
        self,
        request: Optional[Union[ad_rule_service.ListAdRulesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAdRulesPager:
        r"""Lists ``AdRule`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_list_ad_rules():
                # Create a client
                client = admanager_v1.AdRuleServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.ListAdRulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_ad_rules(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.ListAdRulesRequest, dict]):
                The request object. Request object for ``ListAdRules`` method.
            parent (str):
                Required. The parent, which owns this collection of
                AdRules. Format: ``networks/{network_code}``

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
            google.ads.admanager_v1.services.ad_rule_service.pagers.ListAdRulesPager:
                Response object for ListAdRulesRequest containing matching AdRule
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
        if not isinstance(request, ad_rule_service.ListAdRulesRequest):
            request = ad_rule_service.ListAdRulesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_ad_rules]

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
        response = pagers.ListAdRulesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_ad_rule(
        self,
        request: Optional[Union[ad_rule_service.CreateAdRuleRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        ad_rule: Optional[ad_rule_messages.AdRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ad_rule_messages.AdRule:
        r"""Creates a ``AdRule`` object.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_create_ad_rule():
                # Create a client
                client = admanager_v1.AdRuleServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.CreateAdRuleRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_ad_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.CreateAdRuleRequest, dict]):
                The request object. Request object for ``CreateAdRule`` method.
            parent (str):
                Required. The parent resource where this ``AdRule`` will
                be created. Format: ``networks/{network_code}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ad_rule (google.ads.admanager_v1.types.AdRule):
                Required. The ``AdRule`` to create.
                This corresponds to the ``ad_rule`` field
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
            google.ads.admanager_v1.types.AdRule:
                An AdRule contains data that the ad
                server will use to generate a playlist
                of video ads.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, ad_rule]
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
        if not isinstance(request, ad_rule_service.CreateAdRuleRequest):
            request = ad_rule_service.CreateAdRuleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if ad_rule is not None:
                request.ad_rule = ad_rule

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_ad_rule]

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

    def batch_create_ad_rules(
        self,
        request: Optional[
            Union[ad_rule_service.BatchCreateAdRulesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        requests: Optional[MutableSequence[ad_rule_service.CreateAdRuleRequest]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ad_rule_service.BatchCreateAdRulesResponse:
        r"""Batch creates ``AdRule`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_create_ad_rules():
                # Create a client
                client = admanager_v1.AdRuleServiceClient()

                # Initialize request argument(s)
                requests = admanager_v1.CreateAdRuleRequest()
                requests.parent = "parent_value"

                request = admanager_v1.BatchCreateAdRulesRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = client.batch_create_ad_rules(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchCreateAdRulesRequest, dict]):
                The request object. Request object for ``BatchCreateAdRules`` method.
            parent (str):
                Required. The parent resource where ``AdRules`` will be
                created. Format: ``networks/{network_code}`` The parent
                field in the CreateAdRuleRequest must match this field.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            requests (MutableSequence[google.ads.admanager_v1.types.CreateAdRuleRequest]):
                Required. The ``AdRule`` objects to create. A maximum of
                100 objects can be created in a batch.

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
            google.ads.admanager_v1.types.BatchCreateAdRulesResponse:
                Response object for BatchCreateAdRules method.
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
        if not isinstance(request, ad_rule_service.BatchCreateAdRulesRequest):
            request = ad_rule_service.BatchCreateAdRulesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if requests is not None:
                request.requests = requests

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_create_ad_rules]

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

    def update_ad_rule(
        self,
        request: Optional[Union[ad_rule_service.UpdateAdRuleRequest, dict]] = None,
        *,
        ad_rule: Optional[ad_rule_messages.AdRule] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ad_rule_messages.AdRule:
        r"""Updates a ``AdRule`` object.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_update_ad_rule():
                # Create a client
                client = admanager_v1.AdRuleServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.UpdateAdRuleRequest(
                )

                # Make the request
                response = client.update_ad_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.UpdateAdRuleRequest, dict]):
                The request object. Request object for ``UpdateAdRule`` method.
            ad_rule (google.ads.admanager_v1.types.AdRule):
                Required. The ``AdRule`` to update.

                The ``AdRule``'s ``name`` is used to identify the
                ``AdRule`` to update.

                This corresponds to the ``ad_rule`` field
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
            google.ads.admanager_v1.types.AdRule:
                An AdRule contains data that the ad
                server will use to generate a playlist
                of video ads.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [ad_rule, update_mask]
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
        if not isinstance(request, ad_rule_service.UpdateAdRuleRequest):
            request = ad_rule_service.UpdateAdRuleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if ad_rule is not None:
                request.ad_rule = ad_rule
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_ad_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("ad_rule.name", request.ad_rule.name),)
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

    def batch_update_ad_rules(
        self,
        request: Optional[
            Union[ad_rule_service.BatchUpdateAdRulesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        requests: Optional[MutableSequence[ad_rule_service.UpdateAdRuleRequest]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ad_rule_service.BatchUpdateAdRulesResponse:
        r"""Batch updates ``AdRule`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_update_ad_rules():
                # Create a client
                client = admanager_v1.AdRuleServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchUpdateAdRulesRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.batch_update_ad_rules(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchUpdateAdRulesRequest, dict]):
                The request object. Request object for ``BatchUpdateAdRules`` method.
            parent (str):
                Required. The parent resource where ``AdRules`` will be
                updated. Format: ``networks/{network_code}`` The parent
                field in the UpdateAdRuleRequest must match this field.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            requests (MutableSequence[google.ads.admanager_v1.types.UpdateAdRuleRequest]):
                Required. The ``AdRule`` objects to update. A maximum of
                100 objects can be updated in a batch.

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
            google.ads.admanager_v1.types.BatchUpdateAdRulesResponse:
                Response object for BatchUpdateAdRules method.
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
        if not isinstance(request, ad_rule_service.BatchUpdateAdRulesRequest):
            request = ad_rule_service.BatchUpdateAdRulesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if requests is not None:
                request.requests = requests

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_update_ad_rules]

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

    def batch_activate_ad_rules(
        self,
        request: Optional[
            Union[ad_rule_service.BatchActivateAdRulesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ad_rule_service.BatchActivateAdRulesResponse:
        r"""Activates a list of ``AdRule`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_activate_ad_rules():
                # Create a client
                client = admanager_v1.AdRuleServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchActivateAdRulesRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = client.batch_activate_ad_rules(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchActivateAdRulesRequest, dict]):
                The request object. Request object for ``BatchActivateAdRules`` method.
            parent (str):
                Required. Format: ``networks/{network_code}``
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. Resource names for the AdRule. Format:
                ``networks/{network_code}/adRules/{ad_rule}``

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
            google.ads.admanager_v1.types.BatchActivateAdRulesResponse:
                Response object for BatchActivateAdRules method.
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
        if not isinstance(request, ad_rule_service.BatchActivateAdRulesRequest):
            request = ad_rule_service.BatchActivateAdRulesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_activate_ad_rules]

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

    def batch_deactivate_ad_rules(
        self,
        request: Optional[
            Union[ad_rule_service.BatchDeactivateAdRulesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> ad_rule_service.BatchDeactivateAdRulesResponse:
        r"""Deactivates a list of ``AdRule`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_deactivate_ad_rules():
                # Create a client
                client = admanager_v1.AdRuleServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchDeactivateAdRulesRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                response = client.batch_deactivate_ad_rules(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchDeactivateAdRulesRequest, dict]):
                The request object. Request object for ``BatchDeactivateAdRules`` method.
            parent (str):
                Required. Format: ``networks/{network_code}``
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. Resource names for the AdRule. Format:
                ``networks/{network_code}/adRules/{ad_rule}``

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
            google.ads.admanager_v1.types.BatchDeactivateAdRulesResponse:
                Response object for BatchDeactivateAdRules method.
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
        if not isinstance(request, ad_rule_service.BatchDeactivateAdRulesRequest):
            request = ad_rule_service.BatchDeactivateAdRulesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.batch_deactivate_ad_rules
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

    def batch_delete_ad_rules(
        self,
        request: Optional[
            Union[ad_rule_service.BatchDeleteAdRulesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        names: Optional[MutableSequence[str]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a list of ``AdRule`` objects.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ads import admanager_v1

            def sample_batch_delete_ad_rules():
                # Create a client
                client = admanager_v1.AdRuleServiceClient()

                # Initialize request argument(s)
                request = admanager_v1.BatchDeleteAdRulesRequest(
                    parent="parent_value",
                    names=['names_value1', 'names_value2'],
                )

                # Make the request
                client.batch_delete_ad_rules(request=request)

        Args:
            request (Union[google.ads.admanager_v1.types.BatchDeleteAdRulesRequest, dict]):
                The request object. Request object for ``BatchDeleteAdRules`` method.
            parent (str):
                Required. Format: ``networks/{network_code}``
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            names (MutableSequence[str]):
                Required. Resource names for the AdRule. Format:
                ``networks/{network_code}/adRules/{ad_rule}``

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
        if not isinstance(request, ad_rule_service.BatchDeleteAdRulesRequest):
            request = ad_rule_service.BatchDeleteAdRulesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if names is not None:
                request.names = names

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_delete_ad_rules]

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

    def __enter__(self) -> "AdRuleServiceClient":
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

__all__ = ("AdRuleServiceClient",)
