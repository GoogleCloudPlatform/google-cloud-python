# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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

import sys
import warnings

from google.cloud.documentai_toolbox import version as package_version

__version__ = package_version.__version__

from .converters import converter
from .utilities import docai_utilities, gcs_utilities
from .wrappers import document, entity, page

__all__ = (
    "document",
    "page",
    "entity",
    "converter",
    "docai_utilities",
    "gcs_utilities",
)


# Checks if the current runtime is Python < 3.10.
if sys.version_info < (3, 10):  # pragma: NO COVER
    message = (
        "The google-cloud-documentai-toolbox library no longer supports Python 3.7, 3.8, and 3.9. "
        "We recommend that you update soon to ensure ongoing support. For "
        "more details, see: [Google Cloud Client Libraries Supported Python Versions policy](https://cloud.google.com/python/docs/supported-python-versions)"
    )
    warnings.warn(message, FutureWarning)
