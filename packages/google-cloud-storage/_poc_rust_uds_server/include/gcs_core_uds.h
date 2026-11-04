// Copyright 2026 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef GOOGLE_CLOUD_RUST_STORAGE_GRPC_UDS_H_
#define GOOGLE_CLOUD_RUST_STORAGE_GRPC_UDS_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

// Starts the `gcscore.v1.GcsCore` gRPC-over-UDS server in-process on a
// background Tokio runtime thread listening on `socket_path` (filesystem path
// or `@abstract` name on Linux).
//
// Blocks until the UDS listener is bound and ready to accept connections.
// Returns `0` on success, or `-1` on error.
int32_t gcs_core_start_inproc(const char* socket_path);

// Triggers graceful shutdown of the in-process server listening on
// `socket_path` and blocks until its background Tokio runtime thread exits.
// Returns `0` on success, or `-1` if no server is registered for `socket_path`.
int32_t gcs_core_stop_inproc(const char* socket_path);

#ifdef __cplusplus
}  // extern "C"
#endif

#endif  // GOOGLE_CLOUD_RUST_STORAGE_GRPC_UDS_H_
