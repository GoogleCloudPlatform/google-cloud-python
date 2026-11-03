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

//! Implementation of the `gcscore.v1.GcsCore` gRPC service over Unix Domain Sockets.

use crate::pb::{self, gcs_core_server::GcsCore};
use crate::session::Sessions;
use crate::{Args, Shared};
use bytes::Bytes;
use google_cloud_storage::client::{Storage, StorageControl};
use google_cloud_storage::model_ext::ReadRange;
use google_cloud_storage::object_descriptor::ObjectDescriptor;
use google_cloud_storage::streaming_source::{SizeHint, StreamingSource};
use std::collections::HashMap;
use std::pin::Pin;
use std::sync::atomic::{AtomicU64, Ordering};
use std::sync::{Arc, RwLock};
use tokio::sync::mpsc;
use tokio_stream::Stream;
use tokio_stream::wrappers::ReceiverStream;
use tonic::transport::server::UdsConnectInfo;
use tonic::{Request, Response, Status, Streaming};

type RespStream<T> = Pin<Box<dyn Stream<Item = Result<T, Status>> + Send + 'static>>;

/// An open `BidiReadObject` descriptor bound to the owning client's `(uid, pid)`.
pub struct OpenHandle {
    pub uid: u32,
    pub pid: i32,
    pub desc: Arc<ObjectDescriptor>,
}

/// Reaps any open `ObjectDescriptor` handles whose owning client process (`pid`) has exited.
pub fn reap_dead_handles(handles: &RwLock<HashMap<u64, OpenHandle>>) -> usize {
    let mut guard = handles.write().unwrap();
    let before = guard.len();
    guard.retain(|_, h| {
        if h.pid <= 0 {
            return true;
        }
        // SAFETY: `kill(pid, 0)` with signal 0 performs an existence check without sending a signal.
        let rc = unsafe { libc::kill(h.pid, 0) };
        if rc == 0 {
            return true;
        }
        std::io::Error::last_os_error().raw_os_error() != Some(libc::ESRCH)
    });
    before - guard.len()
}

/// The `GcsCore` service bridging local gRPC-over-UDS requests to `google-cloud-storage`.
pub struct GcsCoreService {
    shm: Arc<crate::shm::Registry>,
    sessions: Arc<Sessions>,
    require_session: bool,
    storage: Storage,
    control: StorageControl,
    shared: Arc<Shared>,
    default_grpc: bool,
    chunk_size: usize,
    handles: Arc<RwLock<HashMap<u64, OpenHandle>>>,
    next_handle: AtomicU64,
    shm_size: usize,
    slot_size: usize,
    copy_mode: crate::slots::WriteCopyMode,
}

impl GcsCoreService {
    /// Initializes a new `GcsCoreService` with pooled `Storage` and `StorageControl` clients.
    pub async fn new(
        args: &Args,
        shared: Arc<Shared>,
        shm: Arc<crate::shm::Registry>,
    ) -> Result<Self, Box<dyn std::error::Error + Send + Sync>> {
        let subchannels = if args.grpc_subchannels > 0 {
            args.grpc_subchannels
        } else {
            std::thread::available_parallelism()
                .map(|n| n.get().max(4))
                .unwrap_or(16)
        };
        let mut sb = Storage::builder().with_grpc_subchannel_count(subchannels);
        let mut cb = StorageControl::builder();
        if let Some(e) = &args.endpoint {
            sb = sb.with_endpoint(e.clone());
            cb = cb.with_endpoint(e.clone());
        }
        let copy_mode = args
            .write_copy_mode
            .parse::<crate::slots::WriteCopyMode>()
            .map_err(|e| -> Box<dyn std::error::Error + Send + Sync> { e.into() })?;
        if args.shm_slot_size == 0 {
            return Err("--shm-slot-size must be > 0".into());
        }
        shm.set_max_regions_per_pid(args.max_regions_per_pid);
        Ok(Self {
            shm,
            sessions: Arc::new(Sessions::new(args.endpoint.clone(), subchannels)),
            require_session: args.require_session,
            storage: sb.build().await?,
            control: cb.build().await?,
            shared,
            default_grpc: args.default_transport.eq_ignore_ascii_case("grpc"),
            chunk_size: args.chunk_size,
            handles: Arc::new(RwLock::new(HashMap::new())),
            next_handle: AtomicU64::new(1),
            shm_size: args.shm_size,
            slot_size: args.shm_slot_size,
            copy_mode,
        })
    }

    /// Returns a reference to the per-caller `Sessions` registry.
    pub fn sessions(&self) -> Arc<Sessions> {
        self.sessions.clone()
    }

    /// Returns a reference to the open `ObjectDescriptor` handle table.
    pub fn handles(&self) -> Arc<RwLock<HashMap<u64, OpenHandle>>> {
        self.handles.clone()
    }

    fn peer<T>(req: &Request<T>) -> (u32, i32) {
        match req
            .extensions()
            .get::<UdsConnectInfo>()
            .and_then(|i| i.peer_cred)
        {
            Some(c) => (c.uid(), c.pid().unwrap_or(0)),
            None => (u32::MAX, 0),
        }
    }

    async fn pick<T>(&self, req: &Request<T>) -> Result<(Storage, StorageControl), Status> {
        let (uid, pid) = Self::peer(req);
        match req
            .metadata()
            .get("x-session")
            .and_then(|v| v.to_str().ok())
        {
            Some(id) => {
                let s = self.sessions.get(id, uid, pid).await?;
                Ok((s.storage.clone(), s.control.clone()))
            }
            None if self.require_session => Err(Status::unauthenticated("x-session required")),
            None => Ok((self.storage.clone(), self.control.clone())),
        }
    }

    fn use_grpc(&self, t: i32) -> bool {
        match pb::Transport::try_from(t) {
            Ok(pb::Transport::Grpc) => true,
            Ok(pb::Transport::Json) => false,
            _ => self.default_grpc,
        }
    }

    fn chunk(&self, requested: u32) -> usize {
        if requested == 0 {
            self.chunk_size
        } else {
            requested as usize
        }
    }
}

pub(crate) fn bucket_name(b: &str) -> String {
    if b.starts_with("projects/") {
        b.to_string()
    } else {
        format!("projects/_/buckets/{b}")
    }
}

/// Returns `true` if `e` (or any error in its source chain) is a read checksum mismatch.
pub(crate) fn is_checksum_mismatch(e: &google_cloud_storage::Error) -> bool {
    use google_cloud_storage::error::ReadError;
    let mut cur: Option<&(dyn std::error::Error + 'static)> = std::error::Error::source(e);
    while let Some(err) = cur {
        if let Some(ReadError::ChecksumMismatch(_)) = err.downcast_ref::<ReadError>() {
            return true;
        }
        cur = err.source();
    }
    false
}

/// Finds the innermost-first storage/gax error carrying a service status in `e`'s source
/// chain (e.g. a bidi range read wraps the stream's `OUT_OF_RANGE` status inside a
/// `ReadError::UnrecoverableBidiReadInterrupt`).
fn inner_service_error(e: &google_cloud_storage::Error) -> Option<&google_cloud_storage::Error> {
    let has_status =
        |x: &google_cloud_storage::Error| x.status().is_some() || x.http_status_code().is_some();
    let mut cur: Option<&(dyn std::error::Error + 'static)> = std::error::Error::source(e);
    while let Some(err) = cur {
        if let Some(inner) = err.downcast_ref::<google_cloud_storage::Error>()
            && has_status(inner)
        {
            return Some(inner);
        }
        if let Some(inner) = err.downcast_ref::<Arc<google_cloud_storage::Error>>()
            && has_status(inner)
        {
            return Some(inner.as_ref());
        }
        cur = err.source();
    }
    None
}

pub(crate) fn to_status(e: google_cloud_storage::Error) -> Status {
    let msg = format!("{e}");
    if is_checksum_mismatch(&e) {
        return Status::data_loss(msg);
    }
    let target = if e.status().is_none() && e.http_status_code().is_none() {
        inner_service_error(&e).unwrap_or(&e)
    } else {
        &e
    };
    status_from(target, msg)
}

fn status_from(e: &google_cloud_storage::Error, msg: String) -> Status {
    if let Some(s) = e.status() {
        use google_cloud_gax::error::rpc::Code;
        // GCS JSON error envelopes (`{"error": {"code": 404, "message": "..."}}`) often omit a
        // gRPC `status` string, causing `google-cloud-gax` to set `s.code = Code::Unknown` while
        // populating `e.http_status_code()`. Fall through to `http_status_code()` when `s.code`
        // is `Code::Unknown` so 404 (`NotFound`), 412 (`FailedPrecondition`), etc. are preserved.
        match s.code {
            Code::Cancelled => return Status::cancelled(msg),
            Code::Unknown => {}
            Code::InvalidArgument => return Status::invalid_argument(msg),
            Code::DeadlineExceeded => return Status::deadline_exceeded(msg),
            Code::NotFound => return Status::not_found(msg),
            Code::AlreadyExists => return Status::already_exists(msg),
            Code::PermissionDenied => return Status::permission_denied(msg),
            Code::ResourceExhausted => return Status::resource_exhausted(msg),
            Code::FailedPrecondition => return Status::failed_precondition(msg),
            Code::Aborted => return Status::aborted(msg),
            Code::OutOfRange => return Status::out_of_range(msg),
            Code::Unimplemented => return Status::unimplemented(msg),
            Code::Internal => return Status::internal(msg),
            Code::Unavailable => return Status::unavailable(msg),
            Code::DataLoss => return Status::data_loss(msg),
            Code::Unauthenticated => return Status::unauthenticated(msg),
            _ => return Status::unknown(msg),
        }
    }
    match e.http_status_code() {
        Some(400) => return Status::invalid_argument(msg),
        Some(401) => return Status::unauthenticated(msg),
        Some(403) => return Status::permission_denied(msg),
        Some(404) => return Status::not_found(msg),
        Some(408) | Some(504) => return Status::deadline_exceeded(msg),
        Some(409) => return Status::aborted(msg),
        Some(412) => return Status::failed_precondition(msg),
        Some(416) => return Status::out_of_range(msg),
        Some(429) => return Status::resource_exhausted(msg),
        Some(499) => return Status::cancelled(msg),
        Some(501) => return Status::unimplemented(msg),
        Some(502) | Some(503) => return Status::unavailable(msg),
        _ => {}
    }
    if e.is_authentication() {
        return Status::unauthenticated(msg);
    }
    let dbg = format!("{e:?}");
    if dbg.contains("status_code: Some(401)")
        || dbg.contains("Invalid Credentials")
        || dbg.contains("lent token expired")
    {
        return Status::unauthenticated(msg);
    }
    if dbg.contains("status_code: Some(403)") {
        return Status::permission_denied(msg);
    }
    if dbg.contains("status_code: Some(404)") {
        return Status::not_found(msg);
    }
    if dbg.contains("status_code: Some(412)") {
        return Status::failed_precondition(msg);
    }
    if e.status().is_some() {
        return Status::unknown(msg);
    }
    Status::internal(msg)
}

fn read_range(offset: i64, length: i64) -> Option<ReadRange> {
    if offset == 0 && length < 0 {
        None
    } else if offset < 0 {
        Some(ReadRange::tail((-offset) as u64))
    } else if length < 0 {
        Some(ReadRange::offset(offset as u64))
    } else {
        Some(ReadRange::segment(offset as u64, length as u64))
    }
}

fn meta_from_highlights(h: &google_cloud_storage::model_ext::ObjectHighlights) -> pb::ObjectMeta {
    pb::ObjectMeta {
        size: h.size,
        generation: h.generation,
        metageneration: h.metageneration,
        content_type: h.content_type.clone(),
        content_encoding: h.content_encoding.clone(),
        crc32c: h.checksums.as_ref().and_then(|c| c.crc32c).unwrap_or(0),
    }
}

fn meta_from_object(o: &google_cloud_storage::model::Object) -> pb::ObjectMeta {
    pb::ObjectMeta {
        size: o.size,
        generation: o.generation,
        metageneration: o.metageneration,
        content_type: o.content_type.clone(),
        content_encoding: o.content_encoding.clone(),
        crc32c: o.checksums.as_ref().and_then(|c| c.crc32c).unwrap_or(0),
    }
}

async fn pump_reader(
    mut resp: google_cloud_storage::read_object::ReadObjectResponse,
    first_meta: Option<pb::ObjectMeta>,
    chunk: usize,
    tx: mpsc::Sender<Result<pb::ReadChunk, Status>>,
) {
    let mut meta = first_meta;
    let mut parts: Vec<Bytes> = Vec::with_capacity(64);
    let mut buffered = 0usize;
    loop {
        match resp.next().await {
            Some(Ok(b)) => {
                buffered += b.len();
                parts.push(b);
                if buffered >= chunk {
                    let msg = pb::ReadChunk {
                        data: std::mem::take(&mut parts),
                        meta: meta.take(),
                    };
                    buffered = 0;
                    if tx.send(Ok(msg)).await.is_err() {
                        return;
                    }
                }
            }
            Some(Err(e)) => {
                let _ = tx.send(Err(to_status(e))).await;
                return;
            }
            None => {
                if !parts.is_empty() || meta.is_some() {
                    let _ = tx
                        .send(Ok(pb::ReadChunk {
                            data: parts,
                            meta: meta.take(),
                        }))
                        .await;
                }
                return;
            }
        }
    }
}

struct ChanSource {
    rx: mpsc::Receiver<Result<Bytes, std::io::Error>>,
    exact: Option<u64>,
}

impl StreamingSource for ChanSource {
    type Error = std::io::Error;
    async fn next(&mut self) -> Option<Result<Bytes, Self::Error>> {
        self.rx.recv().await
    }
    async fn size_hint(&self) -> Result<SizeHint, Self::Error> {
        let mut h = SizeHint::new();
        if let Some(n) = self.exact {
            h.set_exact(n);
        }
        Ok(h)
    }
}

#[tonic::async_trait]
impl GcsCore for GcsCoreService {
    type ReadObjectStream = RespStream<pb::ReadChunk>;
    type ReadRangeStream = RespStream<pb::ReadChunk>;
    type ReadObjectShmStream = RespStream<pb::ShmChunk>;
    type BidiReadObjectStream = RespStream<pb::BidiReadObjectResponse>;
    type BidiWriteObjectStream = RespStream<pb::BidiWriteObjectResponse>;

    async fn get_server_info(
        &self,
        _req: Request<pb::Empty>,
    ) -> Result<Response<pb::ServerInfo>, Status> {
        self.shared.touch();
        let mut features = vec!["bidi-read".to_string(), "inline".to_string()];
        #[cfg(google_cloud_unstable_storage_bidi)]
        features.push("bidi-write".to_string());
        let shm_capable = cfg!(any(target_os = "linux", target_os = "macos"))
            && self.shm_size > 0
            && self.shm_size >= self.slot_size;
        if shm_capable {
            features.push("bidi-read-shm".to_string());
            #[cfg(google_cloud_unstable_storage_bidi)]
            features.push("bidi-write-shm".to_string());
            features.push(
                if cfg!(target_os = "linux") {
                    "memfd"
                } else {
                    "posix-shm"
                }
                .to_string(),
            );
        }
        // SAFETY: `getuid()` is always safe to call and cannot fail.
        let my_uid = unsafe { libc::getuid() };
        Ok(Response::new(pb::ServerInfo {
            server_version: env!("CARGO_PKG_VERSION").to_string(),
            storage_crate_version: crate::STORAGE_CRATE_VERSION.to_string(),
            features,
            max_ranges_per_request: crate::bidi_read::MAX_RANGES_PER_REQUEST as u32,
            shm_region_size: if shm_capable { self.shm_size as u64 } else { 0 },
            shm_slot_size: self.slot_size as u32,
            pid: std::process::id() as i32,
            uid: my_uid,
        }))
    }

    async fn bidi_read_object(
        &self,
        req: Request<Streaming<pb::BidiReadObjectRequest>>,
    ) -> Result<Response<Self::BidiReadObjectStream>, Status> {
        self.shared.touch();
        let peer = Self::peer(&req);
        let (storage, _) = self.pick(&req).await?;
        let inbound = req.into_inner();
        let (tx, rx) = mpsc::channel(64);
        tokio::spawn(crate::bidi_read::run_read_session(
            storage,
            self.shm.clone(),
            peer,
            inbound,
            tx,
            self.slot_size,
        ));
        Ok(Response::new(Box::pin(ReceiverStream::new(rx))))
    }

    async fn bidi_write_object(
        &self,
        req: Request<Streaming<pb::BidiWriteObjectRequest>>,
    ) -> Result<Response<Self::BidiWriteObjectStream>, Status> {
        self.shared.touch();
        let peer = Self::peer(&req);
        let (storage, _) = self.pick(&req).await?;
        let inbound = req.into_inner();
        let (tx, rx) = mpsc::channel(64);
        tokio::spawn(crate::bidi_write::run_write_session(
            storage,
            self.shm.clone(),
            peer,
            inbound,
            tx,
            crate::bidi_write::WriteSessionConfig {
                slot_size: self.slot_size,
                copy_mode: self.copy_mode,
            },
        ));
        Ok(Response::new(Box::pin(ReceiverStream::new(rx))))
    }

    async fn ping(
        &self,
        req: Request<pb::PingRequest>,
    ) -> Result<Response<pb::PingResponse>, Status> {
        self.shared.touch();
        Ok(Response::new(pb::PingResponse {
            payload: req.into_inner().payload,
        }))
    }

    async fn read_object_shm(
        &self,
        req: Request<pb::ReadObjectShmRequest>,
    ) -> Result<Response<Self::ReadObjectShmStream>, Status> {
        self.shared.touch();
        let (uid, pid) = Self::peer(&req);
        let (storage, _) = self.pick(&req).await?;
        let outer = req.into_inner();
        let r = outer
            .read
            .ok_or_else(|| Status::invalid_argument("missing read"))?;
        let reg = self
            .shm
            .get(outer.region)
            .await
            .ok_or_else(|| Status::not_found("unknown shm region"))?;
        if uid != u32::MAX && (reg.peer_uid != uid || (reg.peer_pid > 0 && reg.peer_pid != pid)) {
            return Err(Status::permission_denied(
                "shm region is bound to another process",
            ));
        }
        let write_guard = reg.try_lock_write().ok_or_else(|| {
            Status::failed_precondition("shm region is already in use by an active read")
        })?;
        let base = outer.base_offset as usize;
        let cap = outer.capacity as usize;
        if base.saturating_add(cap) > reg.size {
            return Err(Status::out_of_range("base_offset+capacity > region size"));
        }
        let range = read_range(r.offset, r.length);
        let bucket = bucket_name(&r.bucket);
        let (tx, rx) = mpsc::channel(16);

        if self.use_grpc(r.transport) {
            let mut open = storage.open_object(bucket, r.object);
            if r.generation > 0 {
                open = open.set_generation(r.generation);
            }
            if let Some(g) = r.if_generation_match.filter(|&g| g >= 0) {
                open = open.set_if_generation_match(g);
            }
            let (desc, mut resp) = open
                .send_and_read(range.unwrap_or_else(|| ReadRange::offset(0)))
                .await
                .map_err(to_status)?;
            let mut meta = Some(meta_from_object(&desc.object()));
            tokio::spawn(async move {
                let mut cur = base;
                while let Some(part) = resp.next().await {
                    match part {
                        Ok(b) => {
                            if cur - base + b.len() > cap {
                                let _ = tx
                                    .send(Err(Status::out_of_range("object > shm capacity")))
                                    .await;
                                return;
                            }
                            if let Err(e) = write_guard.write_at(cur, &b) {
                                let _ = tx.send(Err(Status::internal(e))).await;
                                return;
                            }
                            cur += b.len();
                        }
                        Err(e) => {
                            let _ = tx.send(Err(to_status(e))).await;
                            return;
                        }
                    }
                }
                let _ = tx
                    .send(Ok(pb::ShmChunk {
                        offset: base as u64,
                        len: (cur - base) as u64,
                        meta: meta.take(),
                    }))
                    .await;
            });
        } else {
            let mut rd = storage.read_object(bucket, r.object);
            if let Some(range) = range {
                rd = rd.set_read_range(range);
            }
            if r.generation > 0 {
                rd = rd.set_generation(r.generation);
            }
            if let Some(g) = r.if_generation_match.filter(|&g| g >= 0) {
                rd = rd.set_if_generation_match(g);
            }
            let mut resp = rd.send().await.map_err(to_status)?;
            let mut meta = Some(meta_from_highlights(&resp.object()));
            tokio::spawn(async move {
                let mut cur = base;
                while let Some(part) = resp.next().await {
                    match part {
                        Ok(b) => {
                            if cur - base + b.len() > cap {
                                let _ = tx
                                    .send(Err(Status::out_of_range("object > shm capacity")))
                                    .await;
                                return;
                            }
                            if let Err(e) = write_guard.write_at(cur, &b) {
                                let _ = tx.send(Err(Status::internal(e))).await;
                                return;
                            }
                            cur += b.len();
                        }
                        Err(e) => {
                            let _ = tx.send(Err(to_status(e))).await;
                            return;
                        }
                    }
                }
                let _ = tx
                    .send(Ok(pb::ShmChunk {
                        offset: base as u64,
                        len: (cur - base) as u64,
                        meta: meta.take(),
                    }))
                    .await;
            });
        }
        Ok(Response::new(Box::pin(ReceiverStream::new(rx))))
    }

    async fn read_object(
        &self,
        req: Request<pb::ReadObjectRequest>,
    ) -> Result<Response<Self::ReadObjectStream>, Status> {
        self.shared.touch();
        let (storage, _) = self.pick(&req).await?;
        let r = req.into_inner();
        let chunk = self.chunk(r.chunk_size);
        let range = read_range(r.offset, r.length);
        let bucket = bucket_name(&r.bucket);
        let (tx, rx) = mpsc::channel(16);

        if self.use_grpc(r.transport) {
            let mut open = storage.open_object(bucket, r.object);
            if r.generation > 0 {
                open = open.set_generation(r.generation);
            }
            if let Some(g) = r.if_generation_match.filter(|&g| g >= 0) {
                open = open.set_if_generation_match(g);
            }
            let (desc, resp) = open
                .send_and_read(range.unwrap_or_else(|| ReadRange::offset(0)))
                .await
                .map_err(to_status)?;
            let meta = meta_from_object(&desc.object());
            tokio::spawn(pump_reader(resp, Some(meta), chunk, tx));
        } else {
            let mut rd = storage.read_object(bucket, r.object);
            if let Some(range) = range {
                rd = rd.set_read_range(range);
            }
            if r.generation > 0 {
                rd = rd.set_generation(r.generation);
            }
            if let Some(g) = r.if_generation_match.filter(|&g| g >= 0) {
                rd = rd.set_if_generation_match(g);
            }
            let resp = rd.send().await.map_err(to_status)?;
            let meta = meta_from_highlights(&resp.object());
            tokio::spawn(pump_reader(resp, Some(meta), chunk, tx));
        }
        Ok(Response::new(Box::pin(ReceiverStream::new(rx))))
    }

    async fn open_object(
        &self,
        req: Request<pb::OpenObjectRequest>,
    ) -> Result<Response<pb::OpenObjectResponse>, Status> {
        self.shared.touch();
        let (uid, pid) = Self::peer(&req);
        let (storage, _) = self.pick(&req).await?;
        let r = req.into_inner();
        let mut open = storage.open_object(bucket_name(&r.bucket), r.object);
        if r.generation > 0 {
            open = open.set_generation(r.generation);
        }
        let desc = open.send().await.map_err(to_status)?;
        let meta = meta_from_object(&desc.object());
        let h = self.next_handle.fetch_add(1, Ordering::Relaxed);
        self.handles.write().unwrap().insert(
            h,
            OpenHandle {
                uid,
                pid,
                desc: Arc::new(desc),
            },
        );
        Ok(Response::new(pb::OpenObjectResponse {
            handle: h,
            meta: Some(meta),
        }))
    }

    async fn read_range(
        &self,
        req: Request<pb::ReadRangeRequest>,
    ) -> Result<Response<Self::ReadRangeStream>, Status> {
        self.shared.touch();
        let (uid, pid) = Self::peer(&req);
        let r = req.into_inner();
        let desc = {
            let guard = self.handles.read().unwrap();
            let entry = guard
                .get(&r.handle)
                .ok_or_else(|| Status::not_found("unknown handle"))?;
            if entry.uid != uid || entry.pid != pid {
                return Err(Status::permission_denied(
                    "handle is bound to another process",
                ));
            }
            entry.desc.clone()
        };
        let chunk = self.chunk(r.chunk_size);
        let (tx, rx) = mpsc::channel(16);
        let range = read_range(r.offset, r.length).unwrap_or_else(|| ReadRange::offset(0));
        tokio::spawn(async move {
            let resp = desc.read_range(range).await;
            pump_reader(resp, None, chunk, tx).await;
        });
        Ok(Response::new(Box::pin(ReceiverStream::new(rx))))
    }

    async fn close_object(
        &self,
        req: Request<pb::CloseObjectRequest>,
    ) -> Result<Response<pb::Empty>, Status> {
        self.shared.touch();
        let (uid, pid) = Self::peer(&req);
        let handle = req.into_inner().handle;
        {
            let mut guard = self.handles.write().unwrap();
            if let Some(entry) = guard.get(&handle)
                && (entry.uid != uid || entry.pid != pid)
            {
                return Err(Status::permission_denied(
                    "handle is bound to another process",
                ));
            }
            guard.remove(&handle);
        }
        Ok(Response::new(pb::Empty {}))
    }

    async fn write_object(
        &self,
        req: Request<Streaming<pb::WriteRequest>>,
    ) -> Result<Response<pb::WriteObjectResponse>, Status> {
        self.shared.touch();
        let (storage, _) = self.pick(&req).await?;
        let mut inbound = req.into_inner();
        let header = match inbound.message().await? {
            Some(pb::WriteRequest {
                msg: Some(pb::write_request::Msg::Header(h)),
            }) => h,
            _ => return Err(Status::invalid_argument("first message must be header")),
        };
        let bucket = bucket_name(&header.bucket);
        let object = header.object.clone();

        #[cfg(google_cloud_unstable_storage_bidi)]
        if self.use_grpc(header.transport) {
            let mut open = storage.open_appendable_object(bucket.clone(), object.clone());
            if !header.content_type.is_empty() {
                open = open.set_content_type(header.content_type.clone());
            }
            if let Some(g) = header.if_generation_match.filter(|&g| g >= 0) {
                open = open.set_if_generation_match(g);
            }
            match open.send().await {
                Ok(mut w) => {
                    while let Some(m) = inbound.message().await? {
                        if let Some(pb::write_request::Msg::Data(d)) = m.msg {
                            w.append(d).await.map_err(to_status)?;
                        }
                    }
                    let obj = w.finalize().await.map_err(to_status)?;
                    return Ok(Response::new(pb::WriteObjectResponse {
                        size: obj.size,
                        generation: obj.generation,
                        crc32c: obj.checksums.as_ref().and_then(|c| c.crc32c).unwrap_or(0),
                        transport_used: pb::Transport::Grpc as i32,
                    }));
                }
                Err(e) => {
                    let st = to_status(e);
                    if st.code() != tonic::Code::Unimplemented {
                        return Err(st);
                    }
                    // Standard regional buckets reject appendable objects with UNIMPLEMENTED;
                    // fall back transparently to write_object.
                }
            }
        }

        let (tx, rx) = mpsc::channel::<Result<Bytes, std::io::Error>>(16);
        let exact = header.known_size.filter(|&n| n >= 0).map(|n| n as u64);
        let mut wo =
            storage.write_object::<_, _, _, ChanSource>(bucket, object, ChanSource { rx, exact });
        if !header.content_type.is_empty() {
            wo = wo.set_content_type(header.content_type.clone());
        }
        if let Some(g) = header.if_generation_match.filter(|&g| g >= 0) {
            wo = wo.set_if_generation_match(g);
        }
        if header.chunk_size > 0 {
            wo = wo.with_resumable_upload_buffer_size(header.chunk_size as usize);
        }
        let upload = tokio::spawn(async move { wo.send_buffered().await });
        let mut pump_err: Option<Status> = None;
        loop {
            match inbound.message().await {
                Ok(Some(m)) => {
                    if let Some(pb::write_request::Msg::Data(d)) = m.msg
                        && tx.send(Ok(d)).await.is_err()
                    {
                        pump_err = Some(Status::aborted("upload aborted"));
                        break;
                    }
                }
                Ok(None) => break,
                Err(status) => {
                    let _ = tx
                        .send(Err(std::io::Error::new(
                            std::io::ErrorKind::BrokenPipe,
                            status.to_string(),
                        )))
                        .await;
                    upload.abort();
                    return Err(status);
                }
            }
        }
        drop(tx);
        let obj = upload
            .await
            .map_err(|e| Status::internal(format!("upload task: {e}")))?
            .map_err(to_status)?;
        if let Some(e) = pump_err {
            return Err(e);
        }
        Ok(Response::new(pb::WriteObjectResponse {
            size: obj.size,
            generation: obj.generation,
            crc32c: obj.checksums.as_ref().and_then(|c| c.crc32c).unwrap_or(0),
            transport_used: pb::Transport::Json as i32,
        }))
    }

    async fn list_objects(
        &self,
        req: Request<pb::ListObjectsRequest>,
    ) -> Result<Response<pb::ListObjectsResponse>, Status> {
        self.shared.touch();
        let (_, control) = self.pick(&req).await?;
        let r = req.into_inner();
        let mut q = control
            .list_objects()
            .set_parent(bucket_name(&r.bucket))
            .set_prefix(r.prefix)
            .set_delimiter(r.delimiter)
            .set_page_token(r.page_token)
            .set_versions(r.versions);
        if !r.start_offset.is_empty() {
            q = q.set_lexicographic_start(r.start_offset);
        }
        if !r.end_offset.is_empty() {
            q = q.set_lexicographic_end(r.end_offset);
        }
        if r.page_size > 0 {
            q = q.set_page_size(r.page_size);
        }
        let resp = q.send().await.map_err(to_status)?;
        Ok(Response::new(pb::ListObjectsResponse {
            items: resp
                .objects
                .iter()
                .map(|o| pb::ListedObject {
                    name: o.name.clone(),
                    size: o.size,
                    generation: o.generation,
                    metageneration: o.metageneration,
                    content_type: o.content_type.clone(),
                    storage_class: o.storage_class.clone(),
                    updated_unix_secs: o.update_time.as_ref().map(|t| t.seconds()).unwrap_or(0),
                    crc32c: o.checksums.as_ref().and_then(|c| c.crc32c).unwrap_or(0),
                })
                .collect(),
            prefixes: resp.prefixes,
            next_page_token: resp.next_page_token,
        }))
    }

    async fn list_buckets(
        &self,
        req: Request<pb::ListBucketsRequest>,
    ) -> Result<Response<pb::ListBucketsResponse>, Status> {
        self.shared.touch();
        let (_, control) = self.pick(&req).await?;
        let r = req.into_inner();
        let parent = if r.project.starts_with("projects/") {
            r.project
        } else {
            format!("projects/{}", r.project)
        };
        let mut q = control
            .list_buckets()
            .set_parent(parent)
            .set_prefix(r.prefix)
            .set_page_token(r.page_token);
        if r.page_size > 0 {
            q = q.set_page_size(r.page_size);
        }
        let resp = q.send().await.map_err(to_status)?;
        Ok(Response::new(pb::ListBucketsResponse {
            items: resp
                .buckets
                .iter()
                .map(|b| pb::ListedBucket {
                    name: b
                        .name
                        .strip_prefix("projects/_/buckets/")
                        .unwrap_or(&b.name)
                        .to_string(),
                    location: b.location.clone(),
                    storage_class: b.storage_class.clone(),
                    metageneration: b.metageneration,
                    created_unix_secs: b.create_time.as_ref().map(|t| t.seconds()).unwrap_or(0),
                })
                .collect(),
            next_page_token: resp.next_page_token,
        }))
    }

    async fn stats(
        &self,
        req: Request<pb::StatsRequest>,
    ) -> Result<Response<pb::StatsResponse>, Status> {
        if req.into_inner().reset_peak_rss {
            let _ = std::fs::write("/proc/self/clear_refs", b"5");
        }
        // SAFETY: `rusage` is a plain-old-data C struct and `getrusage(RUSAGE_SELF, &mut ru)`
        // writes process resource statistics into `ru`.
        let mut ru: libc::rusage = unsafe { std::mem::zeroed() };
        unsafe { libc::getrusage(libc::RUSAGE_SELF, &mut ru) };
        let tv = |t: libc::timeval| t.tv_sec as f64 + t.tv_usec as f64 / 1e6;
        let status = std::fs::read_to_string("/proc/self/status").unwrap_or_default();
        let kb = |key: &str| -> i64 {
            status
                .lines()
                .find(|l| l.starts_with(key))
                .and_then(|l| l.split_whitespace().nth(1))
                .and_then(|v| v.parse::<i64>().ok())
                .unwrap_or(0)
        };
        Ok(Response::new(pb::StatsResponse {
            pid: std::process::id() as i32,
            cpu_user_secs: tv(ru.ru_utime),
            cpu_sys_secs: tv(ru.ru_stime),
            rss_bytes: kb("VmRSS") * 1024,
            peak_rss_bytes: kb("VmHWM") * 1024,
            threads: kb("Threads") as i32,
            uptime_ms: self.shared.started.elapsed().as_millis() as i64,
            rpcs_served: self.shared.rpcs.load(Ordering::Relaxed) as i64,
        }))
    }

    async fn create_session(
        &self,
        req: Request<pb::CreateSessionRequest>,
    ) -> Result<Response<pb::CreateSessionResponse>, Status> {
        self.shared.touch();
        let (uid, pid) = Self::peer(&req);
        if uid == u32::MAX {
            return Err(Status::permission_denied(
                "sessions require a UDS connection with peer credentials",
            ));
        }
        let r = req.into_inner();
        let endpoint = r.endpoint.filter(|e| !e.is_empty());
        let universe = r.universe_domain.filter(|u| !u.is_empty());
        let anonymous = r.anonymous.unwrap_or(false);
        let v2_fields = endpoint.is_some() || universe.is_some() || r.anonymous.is_some();
        let s = if anonymous || (r.access_token.is_empty() && v2_fields) {
            // v2: anonymous or daemon-ADC session sharing one cached client per key.
            self.sessions
                .create_shared((endpoint, universe, anonymous), uid, pid)
                .await
                .map_err(|e| Status::internal(format!("session client: {e}")))?
        } else {
            if r.access_token.is_empty() {
                return Err(Status::invalid_argument("access_token required"));
            }
            let qp = if r.quota_project.is_empty() {
                None
            } else {
                Some(r.quota_project)
            };
            self.sessions
                .create_with_endpoint(
                    r.access_token,
                    r.expiry_unix_secs,
                    qp,
                    endpoint,
                    universe,
                    uid,
                    pid,
                )
                .await
                .map_err(|e| Status::internal(format!("session client: {e}")))?
        };
        let n = self.sessions.len().await;
        tracing::info!(sessions = n, pid, "session created");
        Ok(Response::new(pb::CreateSessionResponse {
            session_id: s.id.clone(),
        }))
    }

    async fn update_token(
        &self,
        req: Request<pb::UpdateTokenRequest>,
    ) -> Result<Response<pb::Empty>, Status> {
        self.shared.touch();
        let (uid, pid) = Self::peer(&req);
        let r = req.into_inner();
        if r.access_token.is_empty() {
            return Err(Status::invalid_argument("access_token required"));
        }
        let s = self.sessions.get(&r.session_id, uid, pid).await?;
        s.token.set(r.access_token, r.expiry_unix_secs);
        Ok(Response::new(pb::Empty {}))
    }

    async fn close_session(
        &self,
        req: Request<pb::SessionRef>,
    ) -> Result<Response<pb::Empty>, Status> {
        self.shared.touch();
        let (uid, pid) = Self::peer(&req);
        let r = req.into_inner();
        self.sessions.close(&r.session_id, uid, pid).await?;
        Ok(Response::new(pb::Empty {}))
    }

    async fn shutdown(&self, _req: Request<pb::Empty>) -> Result<Response<pb::Empty>, Status> {
        self.shared.trigger_shutdown();
        Ok(Response::new(pb::Empty {}))
    }
}
