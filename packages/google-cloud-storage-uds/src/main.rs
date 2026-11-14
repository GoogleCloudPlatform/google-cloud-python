// Copyright 2026 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

//! Standalone Rust gRPC-over-UDS sidecar server (`gcs-accelerator-server`).
//!
//! Listens on a Unix Domain Socket (`unix:///...`) and bridges the local
//! `google.cloud.storage.accelerator.v1.StorageAccelerator` gRPC service to the
//! official `google-cloud-storage` Rust SDK (`Storage` and `StorageControl`).

use std::convert::Infallible;
use std::future::Future;
use std::io::Write as _;
use std::path::{Path, PathBuf};
use std::pin::Pin;
use std::sync::Arc;
use std::task::{Context, Poll};

use bytes::{Bytes, BytesMut};
use futures_util::future::try_join_all;
use google_cloud_gax::paginator::Paginator as _;
use google_cloud_storage::client::{Storage, StorageControl};
use google_cloud_storage::model::Object;
use google_cloud_storage::model_ext::ReadRange;
use tokio::net::UnixListener;
use tokio::sync::{mpsc, OnceCell};
use tokio_stream::wrappers::{ReceiverStream, UnixListenerStream};
use tonic::body::Body;
use tonic::server::{Grpc, ServerStreamingService, UnaryService};
use tonic::transport::Server;
use tonic::{Request, Response, Status};
use tonic_prost::ProstCodec;
use tower_service::Service;

const DEFAULT_WORKER_THREADS: usize = 4;
const MAX_GRPC_MESSAGE_BYTES: usize = 512 * 1024 * 1024; // 512 MiB
const VERSION: &str = env!("CARGO_PKG_VERSION");

// ============================================================================
// Protobuf Wire Messages (`google.cloud.storage.accelerator.v1`)
// ============================================================================

#[derive(Clone, PartialEq, ::prost::Message)]
pub struct PingRequest {}

#[derive(Clone, PartialEq, ::prost::Message)]
pub struct PingResponse {
    #[prost(uint32, tag = "1")]
    pub pid: u32,
    #[prost(uint32, tag = "2")]
    pub worker_threads: u32,
    #[prost(string, tag = "3")]
    pub version: String,
}

#[derive(Clone, Copy, PartialEq, ::prost::Message)]
pub struct ByteRange {
    #[prost(uint64, tag = "1")]
    pub offset: u64,
    #[prost(uint64, tag = "2")]
    pub length: u64,
}

#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ReadRangesRequest {
    #[prost(string, tag = "1")]
    pub bucket: String,
    #[prost(string, tag = "2")]
    pub object: String,
    #[prost(message, repeated, tag = "3")]
    pub ranges: Vec<ByteRange>,
    #[prost(string, tag = "4")]
    pub endpoint: String,
    #[prost(bool, tag = "5")]
    pub simulated: bool,
    #[prost(string, tag = "6")]
    pub shm_path: String,
}

#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ReadRangesResponse {
    #[prost(bytes = "bytes", repeated, tag = "1")]
    pub chunks: Vec<Bytes>,
    #[prost(uint64, repeated, tag = "2")]
    pub actual_lengths: Vec<u64>,
}

#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ReadRangeChunk {
    #[prost(uint32, tag = "1")]
    pub range_index: u32,
    #[prost(bytes = "bytes", tag = "2")]
    pub data: Bytes,
}

#[derive(Clone, PartialEq, ::prost::Message)]
pub struct WriteObjectRequest {
    #[prost(string, tag = "1")]
    pub bucket: String,
    #[prost(string, tag = "2")]
    pub object: String,
    #[prost(bytes = "bytes", tag = "3")]
    pub data: Bytes,
    #[prost(string, tag = "4")]
    pub endpoint: String,
    #[prost(bool, tag = "5")]
    pub simulated: bool,
    #[prost(string, tag = "6")]
    pub shm_path: String,
    #[prost(uint64, tag = "7")]
    pub shm_length: u64,
}

#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ObjectMetadata {
    #[prost(string, tag = "1")]
    pub name: String,
    #[prost(string, tag = "2")]
    pub bucket: String,
    #[prost(int64, tag = "3")]
    pub generation: i64,
    #[prost(int64, tag = "4")]
    pub metageneration: i64,
    #[prost(int64, tag = "5")]
    pub size: i64,
    #[prost(string, tag = "6")]
    pub storage_class: String,
    #[prost(string, tag = "7")]
    pub etag: String,
    #[prost(uint32, tag = "8")]
    pub crc32c: u32,
    #[prost(bool, tag = "9")]
    pub has_crc32c: bool,
}

#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ListObjectsRequest {
    #[prost(string, tag = "1")]
    pub bucket: String,
    #[prost(string, tag = "2")]
    pub prefix: String,
    #[prost(string, tag = "3")]
    pub delimiter: String,
    #[prost(bool, tag = "4")]
    pub versions: bool,
    #[prost(bool, tag = "5")]
    pub include_folders_as_prefixes: bool,
    #[prost(uint32, tag = "6")]
    pub max_results: u32,
    #[prost(string, tag = "7")]
    pub endpoint: String,
    #[prost(uint32, tag = "8")]
    pub simulated_count: u32,
}

#[derive(Clone, PartialEq, ::prost::Message)]
pub struct ListObjectsResponse {
    #[prost(message, repeated, tag = "1")]
    pub objects: Vec<ObjectMetadata>,
    #[prost(string, repeated, tag = "2")]
    pub prefixes: Vec<String>,
}

// ============================================================================
// POSIX Shared Memory (`mmap`) Zero-Copy Wrapper
// ============================================================================

struct ShmMapping {
    ptr: *mut u8,
    len: usize,
}

unsafe impl Send for ShmMapping {}
unsafe impl Sync for ShmMapping {}

impl ShmMapping {
    fn open_map(path: &str, len: usize, writable: bool) -> Result<Self, Status> {
        use std::os::unix::io::AsRawFd as _;
        if len == 0 {
            return Err(Status::invalid_argument("shm_length must be > 0"));
        }
        let file = std::fs::OpenOptions::new()
            .read(true)
            .write(writable)
            .open(path)
            .map_err(|e| Status::internal(format!("Failed to open shm {path}: {e}")))?;

        let meta_len = file
            .metadata()
            .map_err(|e| Status::internal(format!("Failed to stat shm {path}: {e}")))?
            .len() as usize;
        if meta_len < len {
            if writable {
                file.set_len(len as u64)
                    .map_err(|e| Status::internal(format!("Failed to resize shm {path}: {e}")))?;
            } else {
                return Err(Status::invalid_argument(format!(
                    "shm file {path} length ({meta_len}) is smaller than requested ({len})"
                )));
            }
        }

        let prot = if writable {
            libc::PROT_READ | libc::PROT_WRITE
        } else {
            libc::PROT_READ
        };
        let raw_ptr = unsafe {
            libc::mmap(
                std::ptr::null_mut(),
                len,
                prot,
                libc::MAP_SHARED,
                file.as_raw_fd(),
                0,
            )
        };
        if raw_ptr == libc::MAP_FAILED {
            return Err(Status::internal(format!(
                "mmap failed for {path}: {}",
                std::io::Error::last_os_error()
            )));
        }
        Ok(Self {
            ptr: raw_ptr as *mut u8,
            len,
        })
    }

    #[inline]
    fn raw_ptr(&self) -> usize {
        self.ptr as usize
    }
}

impl AsRef<[u8]> for ShmMapping {
    fn as_ref(&self) -> &[u8] {
        unsafe { std::slice::from_raw_parts(self.ptr as *const u8, self.len) }
    }
}

impl Drop for ShmMapping {
    fn drop(&mut self) {
        if !self.ptr.is_null() && self.len > 0 {
            unsafe {
                let _ = libc::munmap(self.ptr as *mut libc::c_void, self.len);
            }
        }
    }
}

struct ShmSliceOwner {
    shm: Arc<ShmMapping>,
    len: usize,
}

impl AsRef<[u8]> for ShmSliceOwner {
    fn as_ref(&self) -> &[u8] {
        &(*self.shm).as_ref()[..self.len]
    }
}

struct CachedShm {
    path: String,
    len: usize,
    mapping: Arc<ShmMapping>,
}

static SHM_CACHE: std::sync::Mutex<Option<CachedShm>> = std::sync::Mutex::new(None);

fn get_or_map_shm(path: &str, min_len: usize) -> Result<Arc<ShmMapping>, Status> {
    let mut guard = SHM_CACHE
        .lock()
        .map_err(|_| Status::internal("SHM_CACHE lock poisoned"))?;
    if let Some(ref cached) = *guard {
        if cached.path == path && cached.len >= min_len {
            return Ok(cached.mapping.clone());
        }
    }
    let meta_len = std::fs::metadata(path)
        .map(|m| m.len() as usize)
        .unwrap_or(min_len)
        .max(min_len);
    let mapping = Arc::new(ShmMapping::open_map(path, meta_len, true)?);
    *guard = Some(CachedShm {
        path: path.to_owned(),
        len: meta_len,
        mapping: mapping.clone(),
    });
    Ok(mapping)
}

// ============================================================================
// Shared GCS Rust SDK Clients
// ============================================================================

struct SharedClients {
    storage: Storage,
    control: StorageControl,
}

static DEFAULT_CLIENTS: OnceCell<SharedClients> = OnceCell::const_new();

fn bucket_resource(bucket: &str) -> String {
    if bucket.starts_with("projects/") {
        bucket.to_owned()
    } else {
        format!("projects/_/buckets/{bucket}")
    }
}

fn object_to_proto(obj: &Object) -> ObjectMetadata {
    let (crc32c, has_crc32c) = match &obj.checksums {
        Some(cs) => match cs.crc32c {
            Some(v) => (v, true),
            None => (0, false),
        },
        None => (0, false),
    };
    ObjectMetadata {
        name: obj.name.clone(),
        bucket: obj.bucket.clone(),
        generation: obj.generation,
        metageneration: obj.metageneration,
        size: obj.size,
        storage_class: obj.storage_class.clone(),
        etag: obj.etag.clone(),
        crc32c,
        has_crc32c,
    }
}

async fn get_default_clients() -> Result<&'static SharedClients, Status> {
    DEFAULT_CLIENTS
        .get_or_try_init(|| async move {
            let (storage, control) = tokio::try_join!(
                async {
                    Storage::builder()
                        .build()
                        .await
                        .map_err(|e| Status::internal(format!("Storage init failed: {e}")))
                },
                async {
                    StorageControl::builder()
                        .build()
                        .await
                        .map_err(|e| Status::internal(format!("StorageControl init failed: {e}")))
                }
            )?;
            Ok(SharedClients { storage, control })
        })
        .await
}

async fn resolve_storage_client(endpoint: &str) -> Result<Storage, Status> {
    if endpoint.is_empty() {
        Ok(get_default_clients().await?.storage.clone())
    } else {
        Storage::builder()
            .with_endpoint(endpoint.to_owned())
            .build()
            .await
            .map_err(|e| Status::internal(format!("Storage init failed for {endpoint}: {e}")))
    }
}

async fn resolve_control_client(endpoint: &str) -> Result<StorageControl, Status> {
    if endpoint.is_empty() {
        Ok(get_default_clients().await?.control.clone())
    } else {
        StorageControl::builder()
            .with_endpoint(endpoint.to_owned())
            .build()
            .await
            .map_err(|e| Status::internal(format!("StorageControl init failed for {endpoint}: {e}")))
    }
}

// ============================================================================
// Core Business Logic (Rust SDK HTTP/JSON + gRPC Control Operations)
// ============================================================================

#[derive(Clone)]
struct AcceleratorHandler {
    worker_threads: u32,
}

impl AcceleratorHandler {
    async fn handle_ping(&self, _req: PingRequest) -> Result<Response<PingResponse>, Status> {
        Ok(Response::new(PingResponse {
            pid: std::process::id(),
            worker_threads: self.worker_threads,
            version: VERSION.to_owned(),
        }))
    }

    async fn read_single_range(
        storage: Storage,
        bucket_res: String,
        object_name: String,
        range: ByteRange,
    ) -> Result<Bytes, Status> {
        let mut req = storage.read_object(&bucket_res, &object_name);
        if range.length > 0 {
            req = req.set_read_range(ReadRange::segment(range.offset, range.length));
        } else if range.offset > 0 {
            req = req.set_read_range(ReadRange::offset(range.offset));
        }
        let mut reader = req.send().await.map_err(|e| {
            Status::internal(format!("read_object failed for {object_name}: {e}"))
        })?;

        let capacity = usize::try_from(range.length).unwrap_or(0);
        let mut buf = BytesMut::with_capacity(capacity);
        while let Some(chunk) = reader.next().await.transpose().map_err(|e| {
            Status::internal(format!("read_object stream failed for {object_name}: {e}"))
        })? {
            buf.extend_from_slice(&chunk);
        }
        Ok(buf.freeze())
    }

    async fn read_single_range_into_shm(
        storage: Storage,
        bucket_res: String,
        object_name: String,
        range: ByteRange,
        shm: Arc<ShmMapping>,
        shm_offset: usize,
        cap: usize,
    ) -> Result<u64, Status> {
        let mut req = storage.read_object(&bucket_res, &object_name);
        if range.length > 0 {
            req = req.set_read_range(ReadRange::segment(range.offset, range.length));
        } else if range.offset > 0 {
            req = req.set_read_range(ReadRange::offset(range.offset));
        }
        let mut reader = req.send().await.map_err(|e| {
            Status::internal(format!("read_object failed for {object_name}: {e}"))
        })?;

        let base_addr = shm.raw_ptr();
        let mut written = 0usize;
        while let Some(chunk) = reader.next().await.transpose().map_err(|e| {
            Status::internal(format!("read_object stream failed for {object_name}: {e}"))
        })? {
            let copy_len = chunk.len().min(cap.saturating_sub(written));
            if copy_len > 0 {
                unsafe {
                    std::ptr::copy_nonoverlapping(
                        chunk.as_ptr(),
                        (base_addr as *mut u8).add(shm_offset + written),
                        copy_len,
                    );
                }
                written += copy_len;
            }
        }
        Ok(written as u64)
    }

    async fn handle_read_ranges(
        &self,
        req: ReadRangesRequest,
    ) -> Result<Response<ReadRangesResponse>, Status> {
        if req.bucket.is_empty() || req.object.is_empty() {
            return Err(Status::invalid_argument(
                "bucket and object must be non-empty",
            ));
        }

        let ranges = if req.ranges.is_empty() {
            vec![ByteRange {
                offset: 0,
                length: 0,
            }]
        } else {
            req.ranges
        };

        // Zero-copy shared-memory (`mmap`) path: write directly into `/dev/shm`
        // and return only `actual_lengths` over the UDS socket.
        if !req.shm_path.is_empty() {
            let mut offsets_and_caps = Vec::with_capacity(ranges.len());
            let mut cursor = 0usize;
            for r in &ranges {
                let cap = if r.length > 0 {
                    usize::try_from(r.length).unwrap_or(1024)
                } else {
                    1024
                };
                offsets_and_caps.push((*r, cursor, cap));
                cursor += cap;
            }

            let shm = get_or_map_shm(&req.shm_path, cursor.max(1))?;

            if req.simulated {
                let base_ptr = shm.raw_ptr() as *mut u8;
                let mut actual_lengths = Vec::with_capacity(offsets_and_caps.len());
                for (r, shm_offset, cap) in offsets_and_caps {
                    unsafe {
                        let dst = std::slice::from_raw_parts_mut(base_ptr.add(shm_offset), cap);
                        if !dst.is_empty() {
                            dst[0] = (r.offset & 0xFF) as u8;
                            if dst.len() > 1 {
                                dst[dst.len() - 1] = ((r.offset as usize + dst.len() - 1) & 0xFF) as u8;
                            }
                        }
                    }
                    actual_lengths.push(cap as u64);
                }
                return Ok(Response::new(ReadRangesResponse {
                    chunks: Vec::new(),
                    actual_lengths,
                }));
            }

            let storage = resolve_storage_client(&req.endpoint).await?;
            let bucket_res = bucket_resource(&req.bucket);
            let object_name = req.object;

            let tasks = offsets_and_caps
                .into_iter()
                .map(|(r, shm_offset, cap)| {
                    Self::read_single_range_into_shm(
                        storage.clone(),
                        bucket_res.clone(),
                        object_name.clone(),
                        r,
                        shm.clone(),
                        shm_offset,
                        cap,
                    )
                });

            let actual_lengths = try_join_all(tasks).await?;
            return Ok(Response::new(ReadRangesResponse {
                chunks: Vec::new(),
                actual_lengths,
            }));
        }

        if req.simulated {
            let chunks = ranges
                .into_iter()
                .map(|r| {
                    let len = if r.length > 0 {
                        usize::try_from(r.length).unwrap_or(1024)
                    } else {
                        1024
                    };
                    let mut buf = vec![0u8; len];
                    for (i, b) in buf.iter_mut().enumerate() {
                        *b = ((r.offset as usize + i) & 0xFF) as u8;
                    }
                    Bytes::from(buf)
                })
                .collect();
            return Ok(Response::new(ReadRangesResponse {
                chunks,
                actual_lengths: Vec::new(),
            }));
        }

        let storage = resolve_storage_client(&req.endpoint).await?;
        let bucket_res = bucket_resource(&req.bucket);
        let object_name = req.object;

        let tasks = ranges.into_iter().map(|r| {
            Self::read_single_range(
                storage.clone(),
                bucket_res.clone(),
                object_name.clone(),
                r,
            )
        });

        let chunks = try_join_all(tasks).await?;
        Ok(Response::new(ReadRangesResponse {
            chunks,
            actual_lengths: Vec::new(),
        }))
    }

    async fn handle_read_object_stream(
        &self,
        req: ReadRangesRequest,
    ) -> Result<Response<ReceiverStream<Result<ReadRangeChunk, Status>>>, Status> {
        if req.bucket.is_empty() || req.object.is_empty() {
            return Err(Status::invalid_argument(
                "bucket and object must be non-empty",
            ));
        }

        let ranges = if req.ranges.is_empty() {
            vec![ByteRange {
                offset: 0,
                length: 0,
            }]
        } else {
            req.ranges
        };

        let (tx, rx) = mpsc::channel(ranges.len().max(1));

        if req.simulated {
            tokio::spawn(async move {
                for (idx, r) in ranges.into_iter().enumerate() {
                    let len = if r.length > 0 {
                        usize::try_from(r.length).unwrap_or(1024)
                    } else {
                        1024
                    };
                    let mut buf = vec![0u8; len];
                    for (i, b) in buf.iter_mut().enumerate() {
                        *b = ((r.offset as usize + i) & 0xFF) as u8;
                    }
                    if tx
                        .send(Ok(ReadRangeChunk {
                            range_index: idx as u32,
                            data: Bytes::from(buf),
                        }))
                        .await
                        .is_err()
                    {
                        break;
                    }
                }
            });
            return Ok(Response::new(ReceiverStream::new(rx)));
        }

        let storage = resolve_storage_client(&req.endpoint).await?;
        let bucket_res = bucket_resource(&req.bucket);
        let object_name = req.object;

        const STREAM_CHUNK_TARGET: usize = 4 * 1024 * 1024; // 4 MiB pipelined UDS chunk

        for (idx, r) in ranges.into_iter().enumerate() {
            let tx_clone = tx.clone();
            let st = storage.clone();
            let b_res = bucket_res.clone();
            let obj = object_name.clone();
            tokio::spawn(async move {
                let mut req_builder = st.read_object(&b_res, &obj);
                if r.length > 0 {
                    req_builder = req_builder.set_read_range(ReadRange::segment(r.offset, r.length));
                } else if r.offset > 0 {
                    req_builder = req_builder.set_read_range(ReadRange::offset(r.offset));
                }
                let mut reader = match req_builder.send().await {
                    Ok(rdr) => rdr,
                    Err(e) => {
                        let _ = tx_clone
                            .send(Err(Status::internal(format!(
                                "read_object failed for {obj}: {e}"
                            ))))
                            .await;
                        return;
                    }
                };

                let cap = usize::try_from(r.length)
                    .unwrap_or(STREAM_CHUNK_TARGET)
                    .min(STREAM_CHUNK_TARGET);
                let mut buf = BytesMut::with_capacity(cap);

                loop {
                    match reader.next().await.transpose() {
                        Ok(Some(chunk)) => {
                            buf.extend_from_slice(&chunk);
                            if buf.len() >= STREAM_CHUNK_TARGET {
                                let data = buf.split().freeze();
                                buf.reserve(cap);
                                if tx_clone
                                    .send(Ok(ReadRangeChunk {
                                        range_index: idx as u32,
                                        data,
                                    }))
                                    .await
                                    .is_err()
                                {
                                    return;
                                }
                            }
                        }
                        Ok(None) => {
                            if !buf.is_empty() || r.length == 0 {
                                let _ = tx_clone
                                    .send(Ok(ReadRangeChunk {
                                        range_index: idx as u32,
                                        data: buf.freeze(),
                                    }))
                                    .await;
                            }
                            break;
                        }
                        Err(e) => {
                            let _ = tx_clone
                                .send(Err(Status::internal(format!(
                                    "read_object stream failed for {obj}: {e}"
                                ))))
                                .await;
                            break;
                        }
                    }
                }
            });
        }

        Ok(Response::new(ReceiverStream::new(rx)))
    }

    async fn handle_write_object(
        &self,
        req: WriteObjectRequest,
    ) -> Result<Response<ObjectMetadata>, Status> {
        if req.bucket.is_empty() || req.object.is_empty() {
            return Err(Status::invalid_argument(
                "bucket and object must be non-empty",
            ));
        }

        let payload: Bytes = if !req.shm_path.is_empty() && req.shm_length > 0 {
            let len = req.shm_length as usize;
            let shm = get_or_map_shm(&req.shm_path, len)?;
            Bytes::from_owner(ShmSliceOwner { shm, len })
        } else {
            req.data
        };

        if req.simulated {
            return Ok(Response::new(ObjectMetadata {
                name: req.object,
                bucket: bucket_resource(&req.bucket),
                generation: 1_700_000_000_000_000,
                metageneration: 1,
                size: payload.len() as i64,
                storage_class: "STANDARD".to_owned(),
                etag: "simulated-etag".to_owned(),
                crc32c: 0,
                has_crc32c: false,
            }));
        }

        let storage = resolve_storage_client(&req.endpoint).await?;
        let obj = storage
            .write_object(bucket_resource(&req.bucket), &req.object, payload)
            .send_unbuffered()
            .await
            .map_err(|e| {
                Status::internal(format!(
                    "write_object failed for {}/{}: {e}",
                    req.bucket, req.object
                ))
            })?;

        Ok(Response::new(object_to_proto(&obj)))
    }

    async fn handle_list_objects(
        &self,
        req: ListObjectsRequest,
    ) -> Result<Response<ListObjectsResponse>, Status> {
        if req.bucket.is_empty() {
            return Err(Status::invalid_argument("bucket must be non-empty"));
        }

        if req.simulated_count > 0 {
            let count = req.simulated_count as usize;
            let b_res = bucket_resource(&req.bucket);
            let objects = (0..count)
                .map(|i| ObjectMetadata {
                    name: format!("{}object_{i:06}.bin", req.prefix),
                    bucket: b_res.clone(),
                    generation: 1_700_000_000_000_000 + i as i64,
                    metageneration: 1,
                    size: 16 * 1024 * 1024,
                    storage_class: "STANDARD".to_owned(),
                    etag: format!("etag-{i:06}"),
                    crc32c: 0,
                    has_crc32c: false,
                })
                .collect();
            return Ok(Response::new(ListObjectsResponse {
                objects,
                prefixes: Vec::new(),
            }));
        }

        let control = resolve_control_client(&req.endpoint).await?;
        let mut builder = control
            .list_objects()
            .set_parent(bucket_resource(&req.bucket))
            .set_prefix(&req.prefix)
            .set_versions(req.versions);

        if !req.delimiter.is_empty() {
            builder = builder
                .set_delimiter(&req.delimiter)
                .set_include_folders_as_prefixes(req.include_folders_as_prefixes);
        }
        let max_results = if req.max_results > 0 {
            Some(req.max_results as usize)
        } else {
            None
        };
        if let Some(limit) = max_results {
            builder = builder.set_page_size(i32::try_from(limit.min(1000)).unwrap_or(1000));
        }

        let mut objects: Vec<ObjectMetadata> = Vec::new();
        let mut prefixes: Vec<String> = Vec::new();
        let mut pages = builder.by_page();
        while let Some(page) = pages.next().await {
            let page = page.map_err(|e| {
                Status::internal(format!(
                    "ListObjects failed for {}/{}: {e}",
                    req.bucket, req.prefix
                ))
            })?;
            objects.extend(page.objects.iter().map(object_to_proto));
            prefixes.extend(page.prefixes);
            if max_results.is_some_and(|limit| objects.len() + prefixes.len() >= limit) {
                if let Some(limit) = max_results {
                    objects.truncate(limit);
                }
                break;
            }
        }

        Ok(Response::new(ListObjectsResponse { objects, prefixes }))
    }
}

// ============================================================================
// Tonic gRPC Service Dispatcher
// ============================================================================

#[derive(Clone)]
struct StorageAcceleratorServer {
    inner: Arc<AcceleratorHandler>,
}

impl StorageAcceleratorServer {
    fn new(worker_threads: u32) -> Self {
        Self {
            inner: Arc::new(AcceleratorHandler { worker_threads }),
        }
    }
}

impl Service<http::Request<Body>> for StorageAcceleratorServer {
    type Response = http::Response<Body>;
    type Error = Infallible;
    type Future = Pin<Box<dyn Future<Output = Result<Self::Response, Self::Error>> + Send>>;

    fn poll_ready(&mut self, _cx: &mut Context<'_>) -> Poll<Result<(), Self::Error>> {
        Poll::Ready(Ok(()))
    }

    fn call(&mut self, req: http::Request<Body>) -> Self::Future {
        let inner = self.inner.clone();

        match req.uri().path() {
            "/google.cloud.storage.accelerator.v1.StorageAccelerator/Ping" => {
                struct PingSvc(Arc<AcceleratorHandler>);
                impl UnaryService<PingRequest> for PingSvc {
                    type Response = PingResponse;
                    type Future =
                        Pin<Box<dyn Future<Output = Result<Response<Self::Response>, Status>> + Send>>;
                    fn call(&mut self, request: Request<PingRequest>) -> Self::Future {
                        let h = self.0.clone();
                        Box::pin(async move { h.handle_ping(request.into_inner()).await })
                    }
                }
                Box::pin(async move {
                    let mut grpc = Grpc::new(ProstCodec::<PingResponse, PingRequest>::default())
                        .max_decoding_message_size(MAX_GRPC_MESSAGE_BYTES)
                        .max_encoding_message_size(MAX_GRPC_MESSAGE_BYTES);
                    Ok(grpc.unary(PingSvc(inner), req).await)
                })
            }
            "/google.cloud.storage.accelerator.v1.StorageAccelerator/ReadRanges" => {
                struct ReadRangesSvc(Arc<AcceleratorHandler>);
                impl UnaryService<ReadRangesRequest> for ReadRangesSvc {
                    type Response = ReadRangesResponse;
                    type Future =
                        Pin<Box<dyn Future<Output = Result<Response<Self::Response>, Status>> + Send>>;
                    fn call(&mut self, request: Request<ReadRangesRequest>) -> Self::Future {
                        let h = self.0.clone();
                        Box::pin(async move { h.handle_read_ranges(request.into_inner()).await })
                    }
                }
                Box::pin(async move {
                    let mut grpc =
                        Grpc::new(ProstCodec::<ReadRangesResponse, ReadRangesRequest>::default())
                            .max_decoding_message_size(MAX_GRPC_MESSAGE_BYTES)
                            .max_encoding_message_size(MAX_GRPC_MESSAGE_BYTES);
                    Ok(grpc.unary(ReadRangesSvc(inner), req).await)
                })
            }
            "/google.cloud.storage.accelerator.v1.StorageAccelerator/ReadObjectStream" => {
                struct ReadStreamSvc(Arc<AcceleratorHandler>);
                impl ServerStreamingService<ReadRangesRequest> for ReadStreamSvc {
                    type Response = ReadRangeChunk;
                    type ResponseStream = ReceiverStream<Result<ReadRangeChunk, Status>>;
                    type Future = Pin<
                        Box<
                            dyn Future<Output = Result<Response<Self::ResponseStream>, Status>>
                                + Send,
                        >,
                    >;
                    fn call(&mut self, request: Request<ReadRangesRequest>) -> Self::Future {
                        let h = self.0.clone();
                        Box::pin(
                            async move { h.handle_read_object_stream(request.into_inner()).await },
                        )
                    }
                }
                Box::pin(async move {
                    let mut grpc =
                        Grpc::new(ProstCodec::<ReadRangeChunk, ReadRangesRequest>::default())
                            .max_decoding_message_size(MAX_GRPC_MESSAGE_BYTES)
                            .max_encoding_message_size(MAX_GRPC_MESSAGE_BYTES);
                    Ok(grpc.server_streaming(ReadStreamSvc(inner), req).await)
                })
            }
            "/google.cloud.storage.accelerator.v1.StorageAccelerator/WriteObject" => {
                struct WriteObjectSvc(Arc<AcceleratorHandler>);
                impl UnaryService<WriteObjectRequest> for WriteObjectSvc {
                    type Response = ObjectMetadata;
                    type Future =
                        Pin<Box<dyn Future<Output = Result<Response<Self::Response>, Status>> + Send>>;
                    fn call(&mut self, request: Request<WriteObjectRequest>) -> Self::Future {
                        let h = self.0.clone();
                        Box::pin(async move { h.handle_write_object(request.into_inner()).await })
                    }
                }
                Box::pin(async move {
                    let mut grpc =
                        Grpc::new(ProstCodec::<ObjectMetadata, WriteObjectRequest>::default())
                            .max_decoding_message_size(MAX_GRPC_MESSAGE_BYTES)
                            .max_encoding_message_size(MAX_GRPC_MESSAGE_BYTES);
                    Ok(grpc.unary(WriteObjectSvc(inner), req).await)
                })
            }
            "/google.cloud.storage.accelerator.v1.StorageAccelerator/ListObjects" => {
                struct ListObjectsSvc(Arc<AcceleratorHandler>);
                impl UnaryService<ListObjectsRequest> for ListObjectsSvc {
                    type Response = ListObjectsResponse;
                    type Future =
                        Pin<Box<dyn Future<Output = Result<Response<Self::Response>, Status>> + Send>>;
                    fn call(&mut self, request: Request<ListObjectsRequest>) -> Self::Future {
                        let h = self.0.clone();
                        Box::pin(async move { h.handle_list_objects(request.into_inner()).await })
                    }
                }
                Box::pin(async move {
                    let mut grpc =
                        Grpc::new(ProstCodec::<ListObjectsResponse, ListObjectsRequest>::default())
                            .max_decoding_message_size(MAX_GRPC_MESSAGE_BYTES)
                            .max_encoding_message_size(MAX_GRPC_MESSAGE_BYTES);
                    Ok(grpc.unary(ListObjectsSvc(inner), req).await)
                })
            }
            _ => Box::pin(async move {
                Ok(Status::unimplemented(format!(
                    "Unknown method: {}",
                    req.uri().path()
                ))
                .into_http())
            }),
        }
    }
}

// ============================================================================
// Server Lifecycle & Entrypoint
// ============================================================================

struct ServerConfig {
    uds_path: PathBuf,
    pid_file: Option<PathBuf>,
    worker_threads: usize,
    prewarm_clients: bool,
}

fn parse_args() -> ServerConfig {
    let mut uds_path = std::env::var("GCS_ACCELERATOR_UDS_PATH")
        .map(PathBuf::from)
        .unwrap_or_else(|_| PathBuf::from("/tmp/gcs_accelerator.sock"));
    let mut pid_file = std::env::var("GCS_ACCELERATOR_PID_FILE")
        .ok()
        .map(PathBuf::from);
    let mut worker_threads = std::env::var("GCS_RUST_WORKER_THREADS")
        .ok()
        .and_then(|v| v.parse().ok())
        .filter(|&n| n > 0)
        .unwrap_or(DEFAULT_WORKER_THREADS);
    let mut prewarm_clients = false;

    let mut args = std::env::args().skip(1);
    while let Some(arg) = args.next() {
        match arg.as_str() {
            "--uds-path" => {
                if let Some(p) = args.next() {
                    uds_path = PathBuf::from(p);
                }
            }
            "--pid-file" => {
                if let Some(p) = args.next() {
                    pid_file = Some(PathBuf::from(p));
                }
            }
            "--worker-threads" => {
                if let Some(n) = args.next().and_then(|v| v.parse().ok()) {
                    if n > 0 {
                        worker_threads = n;
                    }
                }
            }
            "--prewarm" => {
                prewarm_clients = true;
            }
            _ => {}
        }
    }

    ServerConfig {
        uds_path,
        pid_file,
        worker_threads,
        prewarm_clients,
    }
}

fn cleanup_files(uds_path: &Path, pid_file: Option<&Path>) {
    let _ = std::fs::remove_file(uds_path);
    if let Some(pf) = pid_file {
        let _ = std::fs::remove_file(pf);
    }
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let cfg = parse_args();

    let runtime = tokio::runtime::Builder::new_multi_thread()
        .worker_threads(cfg.worker_threads)
        .enable_all()
        .build()?;

    runtime.block_on(async move {
        if let Some(parent) = cfg.uds_path.parent() {
            std::fs::create_dir_all(parent)?;
        }
        // Remove stale UDS socket file before binding
        if cfg.uds_path.exists() {
            let _ = std::fs::remove_file(&cfg.uds_path);
        }

        let listener = UnixListener::bind(&cfg.uds_path)?;
        let incoming = UnixListenerStream::new(listener);

        let pid = std::process::id();
        if let Some(ref pf) = cfg.pid_file {
            if let Some(parent) = pf.parent() {
                std::fs::create_dir_all(parent)?;
            }
            std::fs::write(pf, format!("{pid}\n"))?;
        }

        if cfg.prewarm_clients {
            let _ = get_default_clients().await;
        }

        // Notify parent process that UDS server is listening
        println!("READY {} pid={}", cfg.uds_path.display(), pid);
        let _ = std::io::stdout().flush();

        let uds_cleanup = cfg.uds_path.clone();
        let pid_cleanup = cfg.pid_file.clone();

        let shutdown_signal = async move {
            let mut sigterm =
                tokio::signal::unix::signal(tokio::signal::unix::SignalKind::terminate())
                    .expect("failed to install SIGTERM handler");
            tokio::select! {
                _ = tokio::signal::ctrl_c() => {},
                _ = sigterm.recv() => {},
            }
        };

        let svc = StorageAcceleratorServer::new(cfg.worker_threads as u32);

        let res = Server::builder()
            .initial_stream_window_size(64 * 1024 * 1024)
            .initial_connection_window_size(256 * 1024 * 1024)
            .max_frame_size(16 * 1024 * 1024 - 1)
            .http2_adaptive_window(Some(true))
            .serve_with_incoming_shutdown(svc, incoming, shutdown_signal)
            .await;

        cleanup_files(&uds_cleanup, pid_cleanup.as_deref());
        res?;
        Ok(())
    })
}
