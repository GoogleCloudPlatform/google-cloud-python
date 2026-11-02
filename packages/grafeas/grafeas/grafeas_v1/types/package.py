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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from grafeas.grafeas_v1.types import common

__protobuf__ = proto.module(
    package="grafeas.v1",
    manifest={
        "Architecture",
        "Distribution",
        "Location",
        "PackageNote",
        "PackageOccurrence",
        "Version",
    },
)


class Architecture(proto.Enum):
    r"""Instruction set architectures supported by various package
    managers.

    Values:
        ARCHITECTURE_UNSPECIFIED (0):
            Unknown architecture.
        X86 (1):
            X86 architecture.
        X64 (2):
            X64 architecture.
    """

    ARCHITECTURE_UNSPECIFIED = 0
    X86 = 1
    X64 = 2


class Distribution(proto.Message):
    r"""This represents a particular channel of distribution for a
    given package. E.g., Debian's jessie-backports dpkg mirror.

    Attributes:
        cpe_uri (str):
            The cpe_uri in `CPE
            format <https://cpe.mitre.org/specification/>`__ denoting
            the package manager version distributing a package.
        architecture (grafeas.grafeas_v1.types.Architecture):
            The CPU architecture for which packages in
            this distribution channel were built.
        latest_version (grafeas.grafeas_v1.types.Version):
            The latest available version of this package
            in this distribution channel.
        maintainer (str):
            A freeform string denoting the maintainer of
            this package.
        url (str):
            The distribution channel-specific homepage
            for this package.
        description (str):
            The distribution channel-specific description
            of this package.
    """

    cpe_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    architecture: "Architecture" = proto.Field(
        proto.ENUM,
        number=2,
        enum="Architecture",
    )
    latest_version: "Version" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Version",
    )
    maintainer: str = proto.Field(
        proto.STRING,
        number=4,
    )
    url: str = proto.Field(
        proto.STRING,
        number=5,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )


class Location(proto.Message):
    r"""An occurrence of a particular package installation found within a
    system's filesystem. E.g., glibc was found in
    ``/var/lib/dpkg/status``.

    Attributes:
        cpe_uri (str):
            Deprecated. The CPE URI in `CPE
            format <https://cpe.mitre.org/specification/>`__
        version (grafeas.grafeas_v1.types.Version):
            Deprecated.
            The version installed at this location.
        path (str):
            The path from which we gathered that this
            package/version is installed.
    """

    cpe_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: "Version" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Version",
    )
    path: str = proto.Field(
        proto.STRING,
        number=3,
    )


class PackageNote(proto.Message):
    r"""PackageNote represents a particular package version.

    Attributes:
        name (str):
            The name of the package.
        distribution (MutableSequence[grafeas.grafeas_v1.types.Distribution]):
            Deprecated.
            The various channels by which a package is
            distributed.
        package_type (str):
            The type of package; whether native or non
            native (e.g., ruby gems, node.js packages,
            etc.).
        cpe_uri (str):
            The cpe_uri in `CPE
            format <https://cpe.mitre.org/specification/>`__ denoting
            the package manager version distributing a package. The
            cpe_uri will be blank for language packages.
        architecture (grafeas.grafeas_v1.types.Architecture):
            The CPU architecture for which packages in
            this distribution channel were built.
            Architecture will be blank for language
            packages.
        version (grafeas.grafeas_v1.types.Version):
            The version of the package.
        maintainer (str):
            A freeform text denoting the maintainer of
            this package.
        url (str):
            The homepage for this package.
        description (str):
            The description of this package.
        license_ (grafeas.grafeas_v1.types.License):
            Licenses that have been declared by the
            authors of the package.
        digest (MutableSequence[grafeas.grafeas_v1.types.Digest]):
            Hash value, typically a file digest, that
            allows unique identification a specific package.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    distribution: MutableSequence["Distribution"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="Distribution",
    )
    package_type: str = proto.Field(
        proto.STRING,
        number=11,
    )
    cpe_uri: str = proto.Field(
        proto.STRING,
        number=12,
    )
    architecture: "Architecture" = proto.Field(
        proto.ENUM,
        number=13,
        enum="Architecture",
    )
    version: "Version" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="Version",
    )
    maintainer: str = proto.Field(
        proto.STRING,
        number=15,
    )
    url: str = proto.Field(
        proto.STRING,
        number=16,
    )
    description: str = proto.Field(
        proto.STRING,
        number=17,
    )
    license_: common.License = proto.Field(
        proto.MESSAGE,
        number=18,
        message=common.License,
    )
    digest: MutableSequence[common.Digest] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message=common.Digest,
    )


class PackageOccurrence(proto.Message):
    r"""Details on how a particular software package was installed on
    a system.

    Attributes:
        name (str):
            The name of the installed package.
        location (MutableSequence[grafeas.grafeas_v1.types.Location]):
            All of the places within the filesystem
            versions of this package have been found.
        package_type (str):
            The type of package; whether native or non
            native (e.g., ruby gems, node.js packages,
            etc.).
        cpe_uri (str):
            The cpe_uri in `CPE
            format <https://cpe.mitre.org/specification/>`__ denoting
            the package manager version distributing a package. The
            cpe_uri will be blank for language packages.
        architecture (grafeas.grafeas_v1.types.Architecture):
            The CPU architecture for which packages in
            this distribution channel were built.
            Architecture will be blank for language
            packages.
        license_ (grafeas.grafeas_v1.types.License):
            Licenses that have been declared by the
            authors of the package.
        version (grafeas.grafeas_v1.types.Version):
            The version of the package.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: MutableSequence["Location"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Location",
    )
    package_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cpe_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    architecture: "Architecture" = proto.Field(
        proto.ENUM,
        number=5,
        enum="Architecture",
    )
    license_: common.License = proto.Field(
        proto.MESSAGE,
        number=6,
        message=common.License,
    )
    version: "Version" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Version",
    )


class Version(proto.Message):
    r"""Version contains structured information about the version of
    a package.

    Attributes:
        epoch (int):
            Used to correct mistakes in the version
            numbering scheme.
        name (str):
            Required only when version kind is NORMAL.
            The main part of the version name.
        revision (str):
            The iteration of the package build from the
            above version.
        inclusive (bool):
            Whether this version is specifying part of an
            inclusive range. Grafeas does not have the
            capability to specify version ranges; instead we
            have fields that specify start version and end
            versions. At times this is insufficient - we
            also need to specify whether the version is
            included in the range or is excluded from the
            range. This boolean is expected to be set to
            true when the version is included in a range.
        kind (grafeas.grafeas_v1.types.Version.VersionKind):
            Required. Distinguishes between sentinel
            MIN/MAX versions and normal versions.
        full_name (str):
            Human readable version string. This string is
            of the form <epoch>:<name>-<revision> and is
            only set when kind is NORMAL.
    """

    class VersionKind(proto.Enum):
        r"""Whether this is an ordinary package version or a sentinel
        MIN/MAX version.

        Values:
            VERSION_KIND_UNSPECIFIED (0):
                Unknown.
            NORMAL (1):
                A standard package version.
            MINIMUM (2):
                A special version representing negative
                infinity.
            MAXIMUM (3):
                A special version representing positive
                infinity.
        """

        VERSION_KIND_UNSPECIFIED = 0
        NORMAL = 1
        MINIMUM = 2
        MAXIMUM = 3

    epoch: int = proto.Field(
        proto.INT32,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    revision: str = proto.Field(
        proto.STRING,
        number=3,
    )
    inclusive: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    kind: VersionKind = proto.Field(
        proto.ENUM,
        number=4,
        enum=VersionKind,
    )
    full_name: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
