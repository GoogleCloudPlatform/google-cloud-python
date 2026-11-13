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

from google.cloud.vision_v1p1beta1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.vision_v1p1beta1.services.image_annotator",
    "google.cloud.vision_v1p1beta1.types.geometry",
    "google.cloud.vision_v1p1beta1.types.image_annotator",
    "google.cloud.vision_v1p1beta1.types.text_annotation",
    "google.cloud.vision_v1p1beta1.types.web_detection",
}


from google.cloud.vision_helpers import VisionHelpers
from google.cloud.vision_helpers.decorators import add_single_feature_methods

from .services.image_annotator import ImageAnnotatorAsyncClient
from .services.image_annotator import ImageAnnotatorClient as IacImageAnnotatorClient
from .types.geometry import BoundingPoly, Position, Vertex
from .types.image_annotator import (
    AnnotateImageRequest,
    AnnotateImageResponse,
    BatchAnnotateImagesRequest,
    BatchAnnotateImagesResponse,
    ColorInfo,
    CropHint,
    CropHintsAnnotation,
    CropHintsParams,
    DominantColorsAnnotation,
    EntityAnnotation,
    FaceAnnotation,
    Feature,
    Image,
    ImageContext,
    ImageProperties,
    ImageSource,
    LatLongRect,
    Likelihood,
    LocationInfo,
    Property,
    SafeSearchAnnotation,
    TextDetectionParams,
    WebDetectionParams,
)
from .types.text_annotation import Block, Page, Paragraph, Symbol, TextAnnotation, Word
from .types.web_detection import WebDetection


@add_single_feature_methods
class ImageAnnotatorClient(VisionHelpers, IacImageAnnotatorClient):
    __doc__ = IacImageAnnotatorClient.__doc__
    Feature = Feature


__all__ = (
    "ImageAnnotatorAsyncClient",
    "AnnotateImageRequest",
    "AnnotateImageResponse",
    "BatchAnnotateImagesRequest",
    "BatchAnnotateImagesResponse",
    "Block",
    "BoundingPoly",
    "ColorInfo",
    "CropHint",
    "CropHintsAnnotation",
    "CropHintsParams",
    "DominantColorsAnnotation",
    "EntityAnnotation",
    "FaceAnnotation",
    "Feature",
    "Image",
    "ImageAnnotatorClient",
    "ImageContext",
    "ImageProperties",
    "ImageSource",
    "LatLongRect",
    "Likelihood",
    "LocationInfo",
    "Page",
    "Paragraph",
    "Position",
    "Property",
    "SafeSearchAnnotation",
    "Symbol",
    "TextAnnotation",
    "TextDetectionParams",
    "Vertex",
    "WebDetection",
    "WebDetectionParams",
    "Word",
)

api_core.check_python_version("google.cloud.vision_v1p1beta1")
api_core.check_dependency_versions("google.cloud.vision_v1p1beta1")
