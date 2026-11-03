# -*- coding: utf-8 -*-
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os

import setuptools

name = "gapic-generator"
description = "Google API Client Generator for Python"
url = "https://github.com/googleapis/google-cloud-python/tree/main/packages/gapic-generator"
version = "1.44.1"
release_status = "Development Status :: 5 - Production/Stable"
dependencies = [
    # Ensure that the lower bounds of these dependencies match what we have in the
    # templated setup.py.j2: https://github.com/googleapis/google-cloud-python/blob/main/packages/gapic-generator/gapic/templates/setup.py.j2
    "click >= 6.7",
    "google-api-core[grpc] >= 2.25.0, < 3.0.0",
    "googleapis-common-protos >= 1.69.2, < 2.0.0",
    "grpcio >= 1.59.0, < 2.0.0",
    # 2.11.0 is required which adds the `default` argument to `jinja-filters.map()`
    # https://jinja.palletsprojects.com/en/3.0.x/templates/#jinja-filters.map
    # https://jinja.palletsprojects.com/en/2.11.x/changelog/#version-2-11-0
    "jinja2 >= 2.11",
    "protobuf >= 6.33.5, < 8.0.0",
    "pypandoc >= 1.4",
    "PyYAML >= 5.1.1",
    "grpc-google-iam-v1 >= 0.14.2, < 1.0.0",
    "libcst >= 0.4.9, < 2.0.0",
    "inflection >= 0.5.1, < 1.0.0",
]

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    entry_points="""[console_scripts]
        protoc-gen-dump=gapic.cli.dump:dump
        protoc-gen-python_gapic=gapic.cli.generate:generate
    """,
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    license="Apache-2.0",
    packages=setuptools.find_namespace_packages(
        exclude=["docs*", "tests*", "testing*", ".*", "bazel*", "rules_python_gapic*"]
    ),
    url=url,
    classifiers=[
        release_status,
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3.15",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    platforms="Posix; MacOS X",
    python_requires=">=3.10",
    install_requires=dependencies,
    include_package_data=True,
    zip_safe=False,
)
