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

from typing import Union

from google.cloud.documentai import Document

USER_AGENT_PRODUCT = "documentai-toolbox"

JSON_EXTENSION = ".json"
JSON_MIMETYPE = "application/json"

PDF_EXTENSION = ".pdf"
PDF_MIMETYPE = "application/pdf"

FILE_CHECK_REGEX = r"(.*[.].*$)"

# https://cloud.google.com/document-ai/quotas#content_limits
BATCH_MAX_FILES = 1000
# 1GB in Bytes
BATCH_MAX_FILE_SIZE = 1073741824
BATCH_MAX_REQUESTS = 5

# https://cloud.google.com/document-ai/docs/file-types
VALID_MIME_TYPES = {
    PDF_MIMETYPE,
    "image/bmp",
    "image/gif",
    "image/jpeg",
    "image/png",
    "image/tiff",
    "image/webp",
}

IMAGE_ENTITIES = {"Portrait"}

ElementWithLayout = Union[
    Document.Page.Paragraph,
    Document.Page,
    Document.Page.Token,
    Document.Page.Block,
    Document.Page.Symbol,
]
