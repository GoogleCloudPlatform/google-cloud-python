# Copyright 2021 Google LLC
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

import setuptools


# This package has four requirements.
# Each uses a different kind of pin accepted by the function that
# extracts lower bounds.
requirements = [
    "requests>=1.0.0",
    "packaging>=14.0",
    "wheel >=0.41.0",
    "click==7.0.0",
]

extras = {"grpc": "grpcio>=1.0.0"}

setuptools.setup(
    name="valid-package",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    extras_require=extras,
    packages=setuptools.find_packages(),
    python_requires=">=3.9",  # version-scanner: ignore
)
