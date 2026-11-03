#!/usr/bin/env bash
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
# Vendors `gcscore.proto` (owned by google-cloud-rust `src/storage/grpc-uds`) into the
# private `_uds` package and regenerates `gcscore_pb2.py` / `gcscore_pb2.pyi`.
#
# Usage:
#   scripts/regen_gcscore.sh [--check]
#
# Environment:
#   GOOGLE_CLOUD_RUST_DIR   google-cloud-rust checkout (default: ../../../google-cloud-rust)
#   GCS_CORE_COMMIT         optional commit/branch to read the proto from (`git show`);
#                           defaults to the working tree.
#   PYTHON                  interpreter with grpcio-tools installed (default: python3)
#
# `--check` verifies that the vendored proto body still matches PINNED_PROTO_SHA256 and
# that the generated module is up to date; it exits non-zero on drift (CI guard).
set -euo pipefail

# Pinned to google-cloud-rust branch `feat/storage-grpc-uds-bidi-shm`
# (stacked on googleapis/google-cloud-rust#7350 @ bb8c400).
PINNED_PROTO_SHA256="50c8ff8a73ac8263d156bd427ce4256b9f0ab6ed87bb59fcdd706681e9c911cc"
# Oldest protobuf runtime supported by google-cloud-storage[grpc] (setup.py floor).
PROTOBUF_FLOOR_MAJOR=6
PROTOBUF_FLOOR_MINOR=33
PROTOBUF_FLOOR_PATCH=5

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
pkg_root="$(cd "${here}/.." && pwd)"
uds_dir="${pkg_root}/google/cloud/storage/asyncio/_uds"
vendored="${uds_dir}/proto/gcscore.proto"
rust_dir="${GOOGLE_CLOUD_RUST_DIR:-${pkg_root}/../../../google-cloud-rust}"
rel_proto="src/storage/grpc-uds/proto/gcscore.proto"
python="${PYTHON:-python3}"

body_sha() {
  # SHA-256 of the proto body (everything after the vendoring header).
  sed '1,/^\/\/ END VENDORED HEADER$/d' "$1" | sha256sum | cut -d' ' -f1
}

generate() {
  local src="$1" out="$2"
  local tmp
  tmp="$(mktemp -d)"
  trap 'rm -rf "${tmp}"' RETURN
  cp "${src}" "${tmp}/gcscore.proto"
  "${python}" -m grpc_tools.protoc -I"${tmp}" --python_out="${tmp}" --pyi_out="${tmp}" \
    "${tmp}/gcscore.proto"
  # grpcio-tools stamps the gencode with its own (newer) protobuf version; lower the
  # runtime check to the setup.py floor. The builder APIs used by the gencode
  # (AddSerializedFile + BuildMessageAndEnumDescriptors) are stable across 5.x-7.x.
  "${python}" - "${tmp}/gcscore_pb2.py" <<EOF
import re, sys
p = sys.argv[1]
s = open(p).read()
s = re.sub(
    r"_runtime_version\.Domain\.PUBLIC,\n\s+\d+,\n\s+\d+,\n\s+\d+,",
    "_runtime_version.Domain.PUBLIC,\n    ${PROTOBUF_FLOOR_MAJOR},\n    ${PROTOBUF_FLOOR_MINOR},\n    ${PROTOBUF_FLOOR_PATCH},",
    s,
    count=1,
)
s = re.sub(r"# Protobuf Python Version: .*", "# Protobuf Python Version: ${PROTOBUF_FLOOR_MAJOR}.${PROTOBUF_FLOOR_MINOR}.${PROTOBUF_FLOOR_PATCH} (floor; see scripts/regen_gcscore.sh)", s, count=1)
open(p, "w").write(s)
EOF
  cp "${tmp}/gcscore_pb2.py" "${out}/gcscore_pb2.py"
  cp "${tmp}/gcscore_pb2.pyi" "${out}/gcscore_pb2.pyi"
}

if [[ "${1:-}" == "--check" ]]; then
  got="$(body_sha "${vendored}")"
  if [[ "${got}" != "${PINNED_PROTO_SHA256}" ]]; then
    echo "vendored gcscore.proto drifted: ${got} != pinned ${PINNED_PROTO_SHA256}" >&2
    exit 1
  fi
  tmp_out="$(mktemp -d)"
  sed '1,/^\/\/ END VENDORED HEADER$/d' "${vendored}" > "${tmp_out}/gcscore.proto"
  generate "${tmp_out}/gcscore.proto" "${tmp_out}"
  for f in gcscore_pb2.py gcscore_pb2.pyi; do
    if ! cmp -s "${tmp_out}/${f}" "${uds_dir}/${f}"; then
      echo "${f} is stale; run scripts/regen_gcscore.sh" >&2
      rm -rf "${tmp_out}"
      exit 1
    fi
  done
  rm -rf "${tmp_out}"
  echo "gcscore.proto and generated modules are up to date (${got})."
  exit 0
fi

src="$(mktemp)"
if [[ -n "${GCS_CORE_COMMIT:-}" ]]; then
  git -C "${rust_dir}" show "${GCS_CORE_COMMIT}:${rel_proto}" > "${src}"
  rev="$(git -C "${rust_dir}" rev-parse "${GCS_CORE_COMMIT}")"
else
  cp "${rust_dir}/${rel_proto}" "${src}"
  rev="$(git -C "${rust_dir}" rev-parse HEAD 2>/dev/null || echo unknown)+worktree"
fi
mkdir -p "${uds_dir}/proto"
{
  echo "// VENDORED from googleapis/google-cloud-rust ${rel_proto}"
  echo "// at ${rev}. DO NOT EDIT: regenerate with scripts/regen_gcscore.sh."
  echo "// END VENDORED HEADER"
  cat "${src}"
} > "${vendored}"
generate "${src}" "${uds_dir}"
rm -f "${src}"
echo "Vendored proto body sha256: $(body_sha "${vendored}")"
echo "Update PINNED_PROTO_SHA256 in scripts/regen_gcscore.sh if this is an intended change."
