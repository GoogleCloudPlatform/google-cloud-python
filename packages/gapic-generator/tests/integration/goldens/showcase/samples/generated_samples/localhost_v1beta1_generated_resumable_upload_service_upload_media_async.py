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
# Generated code. DO NOT EDIT!
#
# Snippet for UploadMedia
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-showcase[async_rest]


# [START localhost_v1beta1_generated_ResumableUploadService_UploadMedia_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google import showcase_v1beta1
from google.api_core.resumable_transfer import ResumableUploadConfig
import io


async def sample_upload_media():
    # Create a client
    client = showcase_v1beta1.ResumableUploadServiceAsyncClient()

    # Initialize request argument(s)
    request = showcase_v1beta1.UploadMediaRequest(
    )

    # Configure optional transfer settings such as chunk size and stall detection
    config = ResumableUploadConfig(
        chunk_size=8 * 1024 * 1024,  # 8 MB
        stall_minimum_rate=64 * 1024,
        stall_timeout=120,
    )

    # Make the request
    upload_session = await client.upload_media(request=request, config=config)

    # Option 1: Upload the entire stream directly and await the final response
    stream = io.BytesIO(b"Example upload data")
    response = await upload_session.upload(stream)

    # Option 2: Alternatively, iterate over the upload to receive progress updates per chunk
    # async for progress in upload_session.upload(stream):
    #     print(f"Uploaded {progress.bytes_uploaded} bytes | State: {progress.state.name}")
    #     print(f"Session URL: {progress.upload_url}")
    # response = upload_session.response

    # Option 3: Alternatively, resume an interrupted upload from a saved session URL
    # response = await upload_session.resume(upload_url, stream, chunk_size=config.chunk_size)

    # Option 4: Alternatively, resume an interrupted upload while receiving progress updates
    # async for progress in upload_session.resume(upload_url, stream, chunk_size=config.chunk_size):
    #     print(f"Resumed {progress.bytes_uploaded} bytes | State: {progress.state.name}")
    # response = upload_session.response

    # Handle the response
    print(response)


# [END localhost_v1beta1_generated_ResumableUploadService_UploadMedia_async]
