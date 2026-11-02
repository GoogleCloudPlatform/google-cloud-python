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
from google.maps.addressvalidation import gapic_version as package_version

__version__ = package_version.__version__


from google.maps.addressvalidation_v1.services.address_validation.async_client import (
    AddressValidationAsyncClient,
)
from google.maps.addressvalidation_v1.services.address_validation.client import (
    AddressValidationClient,
)
from google.maps.addressvalidation_v1.types.address import (
    Address,
    AddressComponent,
    ComponentName,
)
from google.maps.addressvalidation_v1.types.address_validation_service import (
    ProvideValidationFeedbackRequest,
    ProvideValidationFeedbackResponse,
    ValidateAddressRequest,
    ValidateAddressResponse,
    ValidationResult,
    Verdict,
)
from google.maps.addressvalidation_v1.types.geocode import Geocode, PlusCode
from google.maps.addressvalidation_v1.types.metadata_ import AddressMetadata
from google.maps.addressvalidation_v1.types.usps_data import UspsAddress, UspsData

__all__ = (
    "AddressValidationClient",
    "AddressValidationAsyncClient",
    "Address",
    "AddressComponent",
    "ComponentName",
    "ProvideValidationFeedbackRequest",
    "ProvideValidationFeedbackResponse",
    "ValidateAddressRequest",
    "ValidateAddressResponse",
    "ValidationResult",
    "Verdict",
    "Geocode",
    "PlusCode",
    "AddressMetadata",
    "UspsAddress",
    "UspsData",
)
