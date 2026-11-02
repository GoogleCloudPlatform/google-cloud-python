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
# Generated code. DO NOT EDIT!
#
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-speech

# [START speech_v1_config_Adaptation_CreateCustomClass_Basic_async]
from google.cloud import speech_v1


async def sample_create_custom_class_Basic(
    parent: str = "projects/[PROJECT]/locations/us",
    custom_class_id: str = "passengerships",
) -> speech_v1.CustomClass:
    """Custom Class Creation.

    Shows how to create a custom class.

    Args:
      parent: The custom class parent element
      custom_class_id: The id for the custom class

    Returns:
      a CustomClass
    """
    client = speech_v1.AdaptationAsyncClient(
        client_options={"api_endpoint": "us-speech.googleapis.com"}
    )

    request = speech_v1.CreateCustomClassRequest(
        parent=parent,
        custom_class_id=custom_class_id,
        custom_class=speech_v1.CustomClass(
            items=[
                speech_v1.CustomClass.ClassItem(value="Titanic"),
                speech_v1.CustomClass.ClassItem(value="RMS Queen Mary"),
            ]
        ),
    )

    print("Calling the CreateCustomClass operation.")
    response = await client.create_custom_class(request=request)
    created_custom_class = response.result()

    print("A Custom Class with the following name has been created.")
    print(created_custom_class.name)

    print("The Custom class contains the following items.")
    items_list = created_custom_class.items
    for item in items_list:
        print(item)

    return created_custom_class


# [END speech_v1_config_Adaptation_CreateCustomClass_Basic_async]
