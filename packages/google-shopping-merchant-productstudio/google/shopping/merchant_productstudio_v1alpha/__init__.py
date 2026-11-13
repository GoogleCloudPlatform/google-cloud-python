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
import google.api_core as api_core

from google.shopping.merchant_productstudio_v1alpha import (
    gapic_version as package_version,
)

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.shopping.merchant_productstudio_v1alpha.services.image_service",
    "google.shopping.merchant_productstudio_v1alpha.services.text_suggestions_service",
    "google.shopping.merchant_productstudio_v1alpha.types.image",
    "google.shopping.merchant_productstudio_v1alpha.types.productstudio_common",
    "google.shopping.merchant_productstudio_v1alpha.types.textsuggestions",
}


from .services.image_service import ImageServiceAsyncClient, ImageServiceClient
from .services.text_suggestions_service import (
    TextSuggestionsServiceAsyncClient,
    TextSuggestionsServiceClient,
)
from .types.image import (
    GeneratedImage,
    GenerateImageBackgroundConfig,
    GenerateProductImageBackgroundRequest,
    GenerateProductImageBackgroundResponse,
    OutputImageConfig,
    RemoveImageBackgroundConfig,
    RemoveProductImageBackgroundRequest,
    RemoveProductImageBackgroundResponse,
    RgbColor,
    UpscaleProductImageRequest,
    UpscaleProductImageResponse,
)
from .types.productstudio_common import InputImage
from .types.textsuggestions import (
    GenerateProductTextSuggestionsRequest,
    GenerateProductTextSuggestionsResponse,
    Image,
    OutputSpec,
    ProductInfo,
    ProductTextGenerationMetadata,
    ProductTextGenerationSuggestion,
    TitleExample,
)

__all__ = (
    "ImageServiceAsyncClient",
    "TextSuggestionsServiceAsyncClient",
    "GenerateImageBackgroundConfig",
    "GenerateProductImageBackgroundRequest",
    "GenerateProductImageBackgroundResponse",
    "GenerateProductTextSuggestionsRequest",
    "GenerateProductTextSuggestionsResponse",
    "GeneratedImage",
    "Image",
    "ImageServiceClient",
    "InputImage",
    "OutputImageConfig",
    "OutputSpec",
    "ProductInfo",
    "ProductTextGenerationMetadata",
    "ProductTextGenerationSuggestion",
    "RemoveImageBackgroundConfig",
    "RemoveProductImageBackgroundRequest",
    "RemoveProductImageBackgroundResponse",
    "RgbColor",
    "TextSuggestionsServiceClient",
    "TitleExample",
    "UpscaleProductImageRequest",
    "UpscaleProductImageResponse",
)

api_core.check_python_version("google.shopping.merchant_productstudio_v1alpha")
api_core.check_dependency_versions("google.shopping.merchant_productstudio_v1alpha")
