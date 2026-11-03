> [!WARNING]
> **[DO NOT MERGE] PoC-only mirror.** This directory is a standalone copy of
> `googleapis/google-cloud-rust` `src/storage/grpc-uds` (branch
> `feat/storage-grpc-uds-bidi-shm`, stacked on googleapis/google-cloud-rust#7350) so the
> whole thick/thin PoC (Rust UDS-server + Python `_uds` thin client + benchmarks) can be
> reviewed and run from one branch. It depends on the **unmodified** crates.io
> `google-cloud-storage` 1.21.0. It is removed when the PoC graduates into the
> production PRs; Rust code never lands in `google-cloud-python`.
>
> ```bash
> cd packages/google-cloud-storage/_poc_rust_uds_server
> RUSTFLAGS="--cfg google_cloud_unstable_storage_bidi" cargo test
> (cd python && maturin build --release)     # google-cloud-storage-core wheel
> pip install target/wheels/google_cloud_storage_core-*.whl
> ```

# `storage-grpc-uds` (`gcs-core-server`)

`storage-grpc-uds` exposes the [`google-cloud-storage`](../) Rust core (`Storage` + `StorageControl`) as a local gRPC server over a **Unix Domain Socket (UDS)** (plus an optional Linux `memfd` + `SCM_RIGHTS` shared-memory zero-copy read data plane).

Thin language veneers (Go, Python, Java, C++, Node.js) connect to `gcs-core-server` over UDS and delegate retries, resumable/bidi streaming, CRC32C checksum verification, and gRPC subchannel pooling to a single shared Rust core—without `cgo` or FFI ABI hazards in the caller process.

```text
+-----------------------+       gRPC over UDS (0600, SO_PEERCRED)       +----------------------------------------+
| Thin Language Clients |  ==========================================>  |            gcs-core-server             |
| (Go / Python / Java)  |  -- Control & Streaming: gcscore.v1.GcsCore   |  - google_cloud_storage::Storage       |
|                       |  -- Zero-Copy Reads: <socket>.shm (memfd)     |  - google_cloud_storage::StorageControl|
| - Native TokenSource  |  -- Auth Lending: x-session: <session_id>     |  - Warm gRPC subchannel pool           |
+-----------------------+                                               +-------------------+--------------------+
                                                                                            |
                                                                      JSON/HTTP (reqwest)   |   gRPC v2 / CloudPath (tonic)
                                                                                            v
                                                                          +-----------------------------------+
                                                                          |     Google Cloud Storage (GCS)    |
                                                                          +-----------------------------------+
```

---

## Crate Layout

| File | Responsibility |
| :--- | :--- |
| [`proto/gcscore.proto`](proto/gcscore.proto) | `gcscore.v1.GcsCore` protobuf contract between thin clients and the Rust server. |
| [`src/main.rs`](src/main.rs) | CLI entry point (`gcs-core-server`) with opt-in Linux `PR_SET_PDEATHSIG(SIGTERM)`. |
| [`src/lib.rs`](src/lib.rs) | UDS listener setup (`0600` mode, stale-socket recovery, `@` abstract sockets), `SO_PEERCRED` UID interceptor, `TrackedUnixStream` connection ref-counting, dead-PID session/handle reaper, and `gcs_core_start_inproc` / `gcs_core_stop_inproc` C-FFI entry points. |
| [`include/gcs_core_uds.h`](include/gcs_core_uds.h) | C/C++ header declaring `gcs_core_start_inproc` and `gcs_core_stop_inproc` for linking `libstorage_grpc_uds.{a,so}`. |
| [`src/service.rs`](src/service.rs) | `GcsCore` RPC implementation bridging UDS streams to `Storage` and `StorageControl`. |
| [`src/session.rs`](src/session.rs) | Per-caller OAuth2 token-lending registry (`Sessions`) bound to `(uid, pid)` with dead-PID reaping. |
| [`src/shm.rs`](src/shm.rs) | Linux `memfd_create` + `F_ADD_SEALS` + `SCM_RIGHTS` FD-passing server on `<socket>.shm`. |
| [`tests/uds_integration.rs`](tests/uds_integration.rs) | End-to-end integration tests over real UDS sockets, `httptest`, and `storage-grpc-mock`. |
| [`src/slots.rs`](src/slots.rs) | v2 SHM slot arenas: server-owned read ring (`FREE→SERVER_WRITING→CLIENT_READING→FREE`) and client-owned write slots wrapped in `Bytes::from_owner(SlotLease)` (`FREE→LEASED→FREE`). |
| [`src/bidi_read.rs`](src/bidi_read.rs) | v2 `BidiReadObject` session: one stream == one `ObjectDescriptor`; per-range tasks copy CRC32C-validated chunks into SHM slots. |
| [`src/bidi_write.rs`](src/bidi_write.rs) | v2 `BidiWriteObject` session: one stream == one `AppendableObjectWriter`; zero-copy appends, running CRC32C, `SlotsReleased` forwarding. |
| [`src/object_meta.rs`](src/object_meta.rs) | `model::Object` → `ObjectResource` (typed hot fields + proto3-JSON `object_json`). |
| [`tests/bidi_shm_integration.rs`](tests/bidi_shm_integration.rs) | v2 end-to-end tests: memfd slots, release/cancel, checksum + short-read detection, lease-until-ack, takeover, CRC pre-check. |
| [`python/`](python/) | `maturin` (`bindings = "bin"`) companion wheel / sdist `google-cloud-storage-core` shipping `gcs-core-server` + `binary_path()` locator. |

---

## Supported Deployment Modes

`storage-grpc-uds` supports three deployment topologies from the same binary/library:

| Mode | How to Launch | Process Lifecycle & Use Case |
| :--- | :--- | :--- |
| **1. `N:1` Shared Host Daemon** *(Default)* | `gcs-core-server --socket /run/user/$UID/gcs-core.sock --idle-secs 300` | Multiple thin-client processes share one daemon and one warm GCS gRPC subchannel pool. `TrackedUnixStream` tracks active UDS connections (`active_conns`), and the daemon exits only after `--idle-secs` with `0` active connections. |
| **2. `1:1` Per-Process Child Sidecar** | `gcs-core-server --socket /tmp/gcs-$PID.sock --pdeathsig true --idle-secs 0` | Dedicated child process per application. On Linux, `--pdeathsig true` sets `prctl(PR_SET_PDEATHSIG, SIGTERM)` (with immediate `getppid() == 1` TOCTOU verification) so the sidecar terminates immediately if its parent crashes (`SIGKILL`). |
| **3. Single-Process (In-Process UDS)** | Call `gcs_core_start_inproc(socket_path)` / `gcs_core_stop_inproc(socket_path)` via C-FFI ([`include/gcs_core_uds.h`](include/gcs_core_uds.h)) | Runs the Tonic UDS server on a background Tokio thread inside the host process. All data RPCs still flow over standard UDS sockets (avoiding per-RPC FFI/`cgo` transitions). |

---

## Service Contract (`gcscore.v1.GcsCore`)

Instead of proxying `google.storage.v2.Storage` 1:1 over UDS, [`proto/gcscore.proto`](proto/gcscore.proto) provides a compact surface tailored for thin SDK veneers:

| RPC | Type | Description |
| :--- | :--- | :--- |
| `Ping` | Unary | Echoes `payload`; used for readiness checks (`READY <socket>`) and UDS latency microbenchmarks. |
| `ReadObject` | Server-streaming | Streams object contents in `--chunk-size` slices (`2 MiB` default) over `Transport::JSON` or `Transport::GRPC` (`BidiReadObject`). First `ReadChunk` carries `ObjectMeta`. |
| `OpenObject` / `ReadRange` / `CloseObject` | Unary + Server-streaming | Opens a persistent `BidiReadObject` `ObjectDescriptor` stored under a `(uid, pid)`-bound `uint64` handle in a lock-free `RwLock` table, enabling concurrent multi-range reads (`ReadRange`) over one upstream stream. |
| `ReadObjectShm` | Server-streaming | **Linux Zero-Copy Read:** Clients connect to `<socket>.shm` to receive a 16-byte little-endian header `[region_id: u64, region_size: u64]` + sealed `memfd` via `SCM_RIGHTS`. `ReadObjectShm` writes payload directly into the client's `memfd` and returns a `ShmChunk` `(offset, len, meta)` descriptor. |
| `WriteObject` | Client-streaming | First message carries `WriteHeader` (bucket, object, content-type, optional preconditions/known size, transport); subsequent messages stream `bytes data`. Uses `open_appendable_object` (`BidiWriteObject`) when built with `--cfg google_cloud_unstable_storage_bidi` (falling back to buffered `write_object` if a regional bucket returns `UNIMPLEMENTED`) and reports the actual transport used in `WriteObjectResponse.transport_used`. |
| `ListObjects` / `ListBuckets` | Unary | Single-page control-plane listing via `StorageControl`, matching thin-client page iterators. |
| `CreateSession` / `UpdateToken` / `CloseSession` | Unary | Per-caller OAuth2 bearer token lending bound to kernel-verified `(uid, pid)`. |
| `Stats` / `Shutdown` | Unary | Returns process CPU (`getrusage`) and RSS/VmHWM (`/proc/self/status`) telemetry, or triggers graceful shutdown. |

---

## v2: Zero-Copy Shared-Memory `BidiReadObject` / `BidiWriteObject` Sessions

v2 extends `gcscore.v1.GcsCore` **additively** (no existing RPC, message or field number
changes; old clients stay wire-compatible) and only calls public APIs of the
**unmodified** `google-cloud-storage` crate (built with
`--cfg google_cloud_unstable_storage_bidi`).

| RPC | Type | Description |
| :--- | :--- | :--- |
| `GetServerInfo` | Unary | Versions + capability negotiation (`bidi-read`, `bidi-write`, `bidi-read-shm`, `bidi-write-shm`, `memfd`/`posix-shm`, `inline`), region/slot sizes, `max_ranges_per_request` (1000). |
| `BidiReadObject` | Bidi-streaming | First request `open` (`OpenReadSpec`) opens one `ObjectDescriptor` (`ReadOpened{ObjectResource}`); then `ReadRanges` (≤ 1000, client-chosen `range_id`s), `ReleaseSlots`, `CancelRanges`. Responses: `RangeData{range_id, slot \| inline_data, range_end}` and per-range `RangeError` (the session stays usable). |
| `BidiWriteObject` | Bidi-streaming | First request `open` (`OpenAppendSpec`: create/overwrite, `if_generation_match`, or takeover via `reopen_generation` + `write_handle`/`routing_token`, `ObjectAttrs`); then `Append{slot \| inline_data}`, `Flush`, `Close`, `Finalize{full_object_crc32c}`. Responses: `WriteOpened`, `SlotsReleased`, `Flushed`, `Closed`, `Finalized` (echoing `op_id`). |

`CreateSessionRequest` gains optional `endpoint` / `universe_domain` / `anonymous`
(tags 4–6): anonymous or daemon-ADC sessions share one cached `Storage` per
`(endpoint, universe_domain, anonymous)`.

**Slot protocol.** A `<socket>.shm` region (sealed memfd, 16-byte `(region_id, size)`
header + `SCM_RIGHTS`) is divided into `--shm-slot-size` slots (2 MiB = the SDK's
`MAX_WRITE_CHUNK_SIZE`). Slot state lives only in private Rust memory and is changed with
`compare_exchange(AcqRel)`:

- *Reads (server allocates, client releases):* a per-range task awaits a free slot (fair
  semaphore; back-pressure when the client is slow), `memcpy`s one validated SDK chunk
  piece into it, issues a `Release` fence and sends `RangeData{slot}`. The client copies the
  slot into the user's buffer and sends `ReleaseSlots`. Double release, foreign slots or a
  slot never published to the session abort the session (`FAILED_PRECONDITION`).
  Ranges on finalized objects are validated/clamped against the fixed size (an
  out-of-bounds range yields `RangeError{OUT_OF_RANGE}` without tearing down the shared
  descriptor) and a range that ends short without an SDK error is reported as
  `DATA_LOSS` (never as a silently truncated success).
- *Writes (client allocates, server releases):* `Append{slot}` validates region ownership
  (`(uid, pid)`), bounds and `FREE→LEASED`, then hands the SDK
  `Bytes::from_owner(SlotLease)`. `SlotLease::drop` runs when the **last** clone/slice is
  dropped from the SDK's coalescing / 32 MiB replay buffers (after GCS acks the bytes),
  flips `LEASED→FREE` and queues the slot id; releases are forwarded as `SlotsReleased`
  even while an SDK `append()` is back-pressured. `Close`/`Finalize` drain outstanding
  leases before replying so the client can reuse the region. `--write-copy-mode=copy`
  copies at append time (for untrusted multi-tenant daemons).
- *Finalize CRC32C:* the server keeps a running CRC32C over appended bytes (new objects /
  takeovers at `persisted_size == 0`); on mismatch it `close()`s the writer (object stays
  unfinalized, data persisted) and returns `INVALID_ARGUMENT "... crc32c mismatch ..."`.
  Takeovers with `persisted_size > 0` compare post-hoc with the finalized object.

**Copy count (Linux, per byte).** Reads: GCS → SDK `Bytes` (TLS) → **1 memcpy into SHM** →
1 copy into the user's buffer (required by the Python API); 0 IPC/protobuf payload copies.
Writes: user bytes → **1 copy into SHM** → 0 copies into Rust (`Bytes` view) → HTTP/2 framing.

**New flags:** `--shm-slot-size` (2 MiB), `--write-copy-mode {zero-copy,copy}`,
`--max-regions-per-pid` (16); `MAX_ACTIVE_REGIONS` is 1024. Pages are demand-faulted (no
`MAP_POPULATE`), preserving first-touch cgroup attribution. macOS uses an unlinked,
size-once POSIX `shm_open` object instead of memfd.

**Lifecycle (thin clients).** Attach to `GOOGLE_CLOUD_STORAGE_UDS_SOCKET` if set; otherwise
`<runtime_dir>/gcs-core-<hash>.sock` (0700 dir, hash of binary + endpoint + credential
config), verify the server's uid via `SO_PEERCRED`, and `flock`-spawn one shared N:1 daemon
(`--idle-secs 300`) on the first bidi open. Shared daemons are never killed by clients.

| Platform | Transport | Peer creds | SHM |
| :--- | :--- | :--- | :--- |
| Linux | `unix://` | `SO_PEERCRED` both ways | sealed memfd + `SCM_RIGHTS` |
| macOS (experimental) | `unix://` (≤ 104-byte paths) | `LOCAL_PEERCRED` | unlinked `shm_open` + `SCM_RIGHTS` |
| Windows | — (clients keep their native path) | — | — |

---

## Security & Multi-Process Credential Isolation

When multiple processes on a host share one `gcs-core-server` daemon:

1. **OS-Level Socket Protection (`0600` + `SO_PEERCRED`):**
   - `bind_uds_listener` sets `0600` permissions on both `<socket>` and `<socket>.shm` (and verifies `FileTypeExt::is_socket()` before unlinking stale sockets).
   - Both the Tonic gRPC interceptor and `<socket>.shm` inspect `SO_PEERCRED` on every connection and reject any caller whose effective UID does not match the server's UID (`PERMISSION_DENIED`).
2. **Per-Caller Token, Handle & SHM Isolation (`(uid, pid)` binding):**
   - Thin clients evaluate their native credential source in the host language (e.g. `oauth2.TokenSource`, Workload Identity, impersonation) and lend only the short-lived bearer token + expiry + optional `quota_project` via `CreateSession`.
   - Every `session_id` (`Sessions`), `OpenObject` `handle` (`OpenHandle`), and `ReadObjectShm` `region` (`Region`) is bound to the caller's `(uid, pid)` from `SO_PEERCRED`:
     - Cross-process reuse is rejected with `PERMISSION_DENIED`.
     - Expired tokens are rejected with `UNAUTHENTICATED`.
     - If a client process exits or crashes (`SIGKILL`) without calling `CloseSession` / `CloseObject`, the 1-second background reaper detects `kill(pid, 0) == -1 (ESRCH)` and evicts its sessions and `ObjectDescriptor` handles automatically.

---

## UDS & HTTP/2 Flow-Control Tuning

To prevent HTTP/2 window stalls and kernel socket buffer contention under high concurrency (e.g. 48–256 concurrent streams on `c4-standard-192` with 200 Gbps Tier-1 networking), `serve_with_listener` configures:

| Parameter | Value | Why |
| :--- | :--- | :--- |
| `SO_SNDBUF` / `SO_RCVBUF` | `8 MiB` | Avoids Linux `AF_UNIX` stream buffer backpressure (default is `212 KiB`). |
| `initial_stream_window_size` | `64 MiB` | Allows `64 MiB` in flight per stream without blocking on HTTP/2 `WINDOW_UPDATE`. |
| `initial_connection_window_size` | `256 MiB` | Sustains high aggregate throughput across multiplexed streams on a UDS connection. |
| `max_frame_size` | `4 MiB` | Reduces framing overhead for `2 MiB`–`4 MiB` streaming chunks. |
| `max_decoding/encoding_message_size` | `64 MiB` | Supports large streaming chunks. |

---

## Building, Running & Testing

```bash
# Build release binary (include --cfg google_cloud_unstable_storage_bidi to enable BidiWriteObject appendable uploads)
RUSTFLAGS="--cfg google_cloud_unstable_storage_bidi" \
  cargo build --release -p storage-grpc-uds --bin gcs-core-server

# Run server (prints "READY <socket>" on stdout once listening)
./target/release/gcs-core-server \
  --socket /tmp/gcs-core.sock \
  --default-transport json \
  --grpc-subchannels 16 \
  --idle-secs 300

# Run unit & end-to-end integration tests (v2 bidi tests need the cfg)
RUSTFLAGS="--cfg google_cloud_unstable_storage_bidi" cargo test -p storage-grpc-uds

# Companion Python wheel + sdist (google-cloud-storage-core)
(cd src/storage/grpc-uds/python && maturin build --release && maturin sdist)
```

Regenerating `src/generated/protos/gcscore.v1.rs` (checked in; `build.rs` needs no
`protoc` otherwise):

```bash
PROTOC=/path/to/protoc RUSTFLAGS="--cfg google_cloud_unstable_storage_bidi --cfg google_cloud_generate_protos" \
  cargo build -p storage-grpc-uds
```
