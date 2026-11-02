# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import io
import os
import re

from setuptools import find_packages, setup

# Package metadata.
name = "django-google-spanner"
description = "Bridge to enable using Django with Spanner."
# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 5 - Production/Stable"
# (django_spanner/__init__.py currently enforces SUPPORTED_DJANGO_VERSIONS = [(6, 0), (5, 2)])
dependencies = [
    "sqlparse >= 0.3.0",
    "google-cloud-spanner >= 3.70.0",
    "django >= 5.2, < 6.1",
]
extras = {
    "tracing": [
        "opentelemetry-api >= 1.1.0",
        "opentelemetry-sdk >= 1.1.0",
        "opentelemetry-instrumentation >= 0.20b0",
    ]
}

BASE_DIR = os.path.dirname(__file__)

package_root = os.path.abspath(BASE_DIR)

version = None

with open(os.path.join(package_root, "django_spanner/version.py")) as fp:
    version_candidates = re.findall(r"(?<=\")\d+.\d+.\d+(?=\")", fp.read())
    assert len(version_candidates) == 1
    version = version_candidates[0]

# Setup boilerplate below this line.

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    license="BSD",
    packages=find_packages(exclude=["tests"]),
    install_requires=dependencies,
    url="https://github.com/googleapis/google-cloud-python/tree/main/packages/django-google-spanner",
    classifiers=[
        release_status,
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3.15",
        "Topic :: Utilities",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Framework :: Django :: 6.0",
    ],
    extras_require=extras,
    python_requires=">=3.10",
)
