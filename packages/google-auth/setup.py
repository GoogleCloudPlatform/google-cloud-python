# Copyright 2014 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os

from setuptools import find_namespace_packages, setup

cryptography_base_require = [
    "cryptography >= 38.0.3; python_version < '3.14'",
    "cryptography >= 41.0.5; python_version >= '3.14'",
]

DEPENDENCIES = (
    "pyasn1-modules>=0.2.1",
    # rsa==4.5 is the last version to support 2.7
    # https://github.com/sybrenstuvel/python-rsa/issues/152#issuecomment-643470233
    "rsa>=3.1.4,<5",
)

requests_extra_require = ["requests >= 2.30.0, < 3.0.0"]

aiohttp_extra_require = [
    "aiohttp >= 3.8.0, < 4.0.0; python_version < '3.14'",
    "aiohttp >= 3.9.0, < 4.0.0; python_version >= '3.14'",
    *requests_extra_require,
]

pyjwt_extra_require = ["pyjwt>=2.0", *cryptography_base_require]

reauth_extra_require = ["pyu2f>=0.1.5"]

enterprise_cert_extra_require = cryptography_base_require

urllib3_extra_require = [
    "urllib3 >= 1.26.15, < 3.0.0",
    "packaging >= 20.0",
]

grpc_extra_require = [
    "grpcio >= 1.59.0, < 2.0.0; python_version < '3.14'",
    "grpcio >= 1.75.1, < 2.0.0; python_version >= '3.14'",
]

# Unit test requirements.
testing_extra_require = [
    *grpc_extra_require,
    "flask",
    "freezegun",
    # TODO(https://github.com/googleapis/google-auth-library-python/issues/1736): Remove `oauth2client` from testing requirements once an extra is added for `oauth2client` dependency.
    "oauth2client",
    *pyjwt_extra_require,
    "pytest",
    "pytest-cov",
    "pytest-localserver",
    *reauth_extra_require,
    "responses",
    *urllib3_extra_require,
    # Async Dependencies
    *aiohttp_extra_require,
    "aioresponses",
    "pytest-asyncio",
]

extras = {
    "cryptography": cryptography_base_require,
    # pyopenssl is deprecated, kept for backwards compatibility
    "pyopenssl": cryptography_base_require,
    "aiohttp": aiohttp_extra_require,
    "enterprise_cert": enterprise_cert_extra_require,
    "pyjwt": pyjwt_extra_require,
    "reauth": reauth_extra_require,
    "requests": requests_extra_require,
    "testing": testing_extra_require,
    "urllib3": urllib3_extra_require,
    "grpc": grpc_extra_require,
    # TODO(https://github.com/googleapis/google-auth-library-python/issues/1735): Add an extra for `grpcio` dependency.
    # TODO(https://github.com/googleapis/google-auth-library-python/issues/1736): Add an extra for `oauth2client` dependency.
}

with io.open("README.rst", "r") as fh:
    long_description = fh.read()

package_root = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(package_root, "google/auth/version.py")) as fp:
    exec(fp.read(), version)
version = version["__version__"]

setup(
    name="google-auth",
    version=version,
    author="Google Cloud Platform",
    author_email="googleapis-packages@google.com",
    description="Google Authentication Library",
    long_description=long_description,
    url="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth",
    packages=find_namespace_packages(
        exclude=("tests*", "system_tests*", "docs*", "samples*", "build*")
    ),
    package_data={"google.auth": ["py.typed"], "google.oauth2": ["py.typed"]},
    install_requires=DEPENDENCIES,
    extras_require=extras,
    python_requires=">=3.10",
    license="Apache 2.0",
    keywords="google auth oauth client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3.15",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
