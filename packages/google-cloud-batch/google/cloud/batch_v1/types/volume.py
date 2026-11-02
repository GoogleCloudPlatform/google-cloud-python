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

__protobuf__ = proto.module(
    package="google.cloud.batch.v1",
    manifest={
        "Volume",
        "NFS",
        "GCS",
    },
)


class Volume(proto.Message):
    r"""Volume describes a volume and parameters for it to be mounted
    to a VM.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        nfs (google.cloud.batch_v1.types.NFS):
            A Network File System (NFS) volume. For
            example, a Filestore file share.

            This field is a member of `oneof`_ ``source``.
        gcs (google.cloud.batch_v1.types.GCS):
            A Google Cloud Storage (GCS) volume.

            This field is a member of `oneof`_ ``source``.
        device_name (str):
            Device name of an attached disk volume, which should align
            with a device_name specified by
            job.allocation_policy.instances[0].policy.disks[i].device_name
            or defined by the given instance template in
            job.allocation_policy.instances[0].instance_template.

            This field is a member of `oneof`_ ``source``.
        mount_path (str):
            The mount path for the volume, e.g.
            /mnt/disks/share.
        mount_options (MutableSequence[str]):
            Mount options vary based on the type of storage volume:

            - For a Cloud Storage bucket, all the mount options provided
              by the ```gcsfuse``
              tool <https://cloud.google.com/storage/docs/gcsfuse-cli>`__
              are supported.
            - For an existing persistent disk, all mount options
              provided by the ```mount``
              command <https://man7.org/linux/man-pages/man8/mount.8.html>`__
              except writing are supported. This is due to restrictions
              of `multi-writer
              mode <https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms>`__.
            - For any other disk or a Network File System (NFS), all the
              mount options provided by the ``mount`` command are
              supported.
    """

    nfs: "NFS" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="NFS",
    )
    gcs: "GCS" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message="GCS",
    )
    device_name: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="source",
    )
    mount_path: str = proto.Field(
        proto.STRING,
        number=4,
    )
    mount_options: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class NFS(proto.Message):
    r"""Represents an NFS volume.

    Attributes:
        server (str):
            The IP address of the NFS.
        remote_path (str):
            Remote source path exported from the NFS,
            e.g., "/share".
    """

    server: str = proto.Field(
        proto.STRING,
        number=1,
    )
    remote_path: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GCS(proto.Message):
    r"""Represents a Google Cloud Storage volume.

    Attributes:
        remote_path (str):
            Remote path, either a bucket name or a subdirectory of a
            bucket, e.g.: bucket_name, bucket_name/subdirectory/
    """

    remote_path: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
