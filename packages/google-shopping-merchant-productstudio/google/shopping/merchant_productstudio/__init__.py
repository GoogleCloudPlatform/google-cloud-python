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
from google.shopping.merchant_productstudio import gapic_version as package_version

__version__ = package_version.__version__


from google.shopping.merchant_productstudio_v1alpha.services.image_service.async_client import (
    ImageServiceAsyncClient,
)
from google.shopping.merchant_productstudio_v1alpha.services.image_service.client import (
    ImageServiceClient,
)
from google.shopping.merchant_productstudio_v1alpha.services.text_suggestions_service.async_client import (
    TextSuggestionsServiceAsyncClient,
)
from google.shopping.merchant_productstudio_v1alpha.services.text_suggestions_service.client import (
    TextSuggestionsServiceClient,
)
from google.shopping.merchant_productstudio_v1alpha.types.image import (
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
from google.shopping.merchant_productstudio_v1alpha.types.productstudio_common import (
    InputImage,
)
from google.shopping.merchant_productstudio_v1alpha.types.textsuggestions import (
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
    "ImageServiceClient",
    "ImageServiceAsyncClient",
    "TextSuggestionsServiceClient",
    "TextSuggestionsServiceAsyncClient",
    "GeneratedImage",
    "GenerateImageBackgroundConfig",
    "GenerateProductImageBackgroundRequest",
    "GenerateProductImageBackgroundResponse",
    "OutputImageConfig",
    "RemoveImageBackgroundConfig",
    "RemoveProductImageBackgroundRequest",
    "RemoveProductImageBackgroundResponse",
    "RgbColor",
    "UpscaleProductImageRequest",
    "UpscaleProductImageResponse",
    "InputImage",
    "GenerateProductTextSuggestionsRequest",
    "GenerateProductTextSuggestionsResponse",
    "Image",
    "OutputSpec",
    "ProductInfo",
    "ProductTextGenerationMetadata",
    "ProductTextGenerationSuggestion",
    "TitleExample",
)
