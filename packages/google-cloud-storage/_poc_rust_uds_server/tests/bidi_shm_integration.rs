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

//! End-to-end tests for the v2 zero-copy SHM `BidiReadObject` / `BidiWriteObject`
//! sessions: real UDS + sealed memfd regions (SCM_RIGHTS) + unmodified
//! `google-cloud-storage` talking to an in-memory fake `google.storage.v2.Storage`
//! built on `storage-grpc-mock`.

#![cfg(all(target_os = "linux", google_cloud_unstable_storage_bidi))]

use hyper_util::rt::TokioIo;
use std::collections::HashMap;
use std::path::{Path, PathBuf};
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::{Arc, Mutex};
use std::time::Duration;
use storage_grpc_mock::google::storage::v2::{
    self as gcs, BidiWriteHandle, ChecksummedData, Object as ProtoObject, ObjectChecksums,
    ObjectRangeData, ReadRange as ProtoRange, bidi_write_object_request::Data,
    bidi_write_object_request::FirstMessage, bidi_write_object_response::WriteStatus,
};
use storage_grpc_mock::{MockStorage, start as start_grpc_mock};
use storage_grpc_uds::pb::bidi_write_object_response::Msg as WMsg;
use storage_grpc_uds::pb::gcs_core_client::GcsCoreClient;
use storage_grpc_uds::pb::{self, bidi_read_object_response::Msg as RMsg};
use storage_grpc_uds::{Args, Shared, bind_uds_listener, serve_with_listener};
use tokio::net::UnixStream;
use tokio::sync::mpsc;
use tokio_stream::StreamExt;
use tokio_stream::wrappers::ReceiverStream;
use tonic::transport::{Channel, Endpoint, Uri};
use tower::service_fn;

const MIB: usize = 1024 * 1024;
const SLOT: usize = 2 * MIB;
const GENERATION: i64 = 4242;
const HANDLE: &[u8] = b"fake-write-handle";

// ------------------------------------------------------------------ fake GCS

/// `(generation, data, finalized)` per object name.
type StoredObject = (i64, Vec<u8>, bool);

#[derive(Default)]
struct FakeState {
    objects: Mutex<HashMap<String, StoredObject>>,
    corrupt_reads: AtomicBool,
    append_specs: Mutex<Vec<gcs::AppendObjectSpec>>,
}

fn crc(data: &[u8]) -> u32 {
    crc32c::crc32c(data)
}

fn proto_object(name: &str, gen_: i64, data: &[u8], finalized: bool) -> ProtoObject {
    ProtoObject {
        bucket: "projects/_/buckets/bkt".to_string(),
        name: name.to_string(),
        generation: gen_,
        metageneration: 1,
        size: data.len() as i64,
        finalize_time: finalized.then(prost_types::Timestamp::default),
        checksums: finalized.then(|| ObjectChecksums {
            crc32c: Some(crc(data)),
            ..ObjectChecksums::default()
        }),
        ..ProtoObject::default()
    }
}

fn fake_gcs(state: Arc<FakeState>) -> MockStorage {
    let mut mock = MockStorage::new();
    let rs = state.clone();
    mock.expect_bidi_read_object().returning(move |request| {
        let (_, _, mut requests) = request.into_parts();
        let (tx, rx) = mpsc::channel(64);
        let st = rs.clone();
        tokio::spawn(async move {
            let Some(Ok(first)) = requests.recv().await else {
                return;
            };
            let spec = first.read_object_spec.unwrap_or_default();
            let found = st.objects.lock().unwrap().get(&spec.object).cloned();
            let Some((gen_, data, finalized)) = found else {
                let _ = tx
                    .send(Err(tonic::Status::not_found("no such object")))
                    .await;
                return;
            };
            let _ = tx
                .send(Ok(gcs::BidiReadObjectResponse {
                    metadata: Some(proto_object(&spec.object, gen_, &data, finalized)),
                    read_handle: Some(gcs::BidiReadHandle {
                        handle: b"rh".to_vec(),
                    }),
                    ..Default::default()
                }))
                .await;
            let mut pending = first.read_ranges;
            loop {
                for r in std::mem::take(&mut pending) {
                    let size = data.len() as i64;
                    let start = if r.read_offset < 0 {
                        (size + r.read_offset).max(0)
                    } else {
                        r.read_offset.min(size)
                    };
                    let end = if r.read_length == 0 {
                        size
                    } else {
                        (start + r.read_length).min(size)
                    };
                    let mut off = start;
                    loop {
                        let n = ((end - off) as usize).min(SLOT + 12345);
                        let chunk = &data[off as usize..off as usize + n];
                        let mut c = crc(chunk);
                        if st.corrupt_reads.load(Ordering::SeqCst) {
                            c ^= 0xffff_ffff;
                        }
                        let last = off + n as i64 >= end;
                        let _ = tx
                            .send(Ok(gcs::BidiReadObjectResponse {
                                object_data_ranges: vec![ObjectRangeData {
                                    checksummed_data: Some(ChecksummedData {
                                        content: chunk.to_vec(),
                                        crc32c: Some(c),
                                    }),
                                    read_range: Some(ProtoRange {
                                        read_offset: off,
                                        read_length: n as i64,
                                        read_id: r.read_id,
                                    }),
                                    range_end: last,
                                }],
                                ..Default::default()
                            }))
                            .await;
                        off += n as i64;
                        if last {
                            break;
                        }
                    }
                }
                match requests.recv().await {
                    Some(Ok(req)) => pending = req.read_ranges,
                    _ => return,
                }
            }
        });
        Ok(tonic::Response::from(rx))
    });

    let ws = state;
    mock.expect_bidi_write_object().returning(move |request| {
        let (_, _, mut requests) = request.into_parts();
        let (tx, rx) = mpsc::channel(64);
        let st = ws.clone();
        tokio::spawn(async move {
            let Some(Ok(first)) = requests.recv().await else {
                return;
            };
            let (name, mut buf) = match first.first_message.clone() {
                Some(FirstMessage::WriteObjectSpec(spec)) => {
                    let r = spec.resource.unwrap_or_default();
                    if spec.if_generation_match == Some(0)
                        && st.objects.lock().unwrap().contains_key(&r.name)
                    {
                        let _ = tx
                            .send(Err(tonic::Status::failed_precondition("exists")))
                            .await;
                        return;
                    }
                    (r.name, Vec::new())
                }
                Some(FirstMessage::AppendObjectSpec(spec)) => {
                    st.append_specs.lock().unwrap().push(spec.clone());
                    let existing = st.objects.lock().unwrap().get(&spec.object).cloned();
                    match existing {
                        Some((g, d, false)) if g == spec.generation => (spec.object, d),
                        _ => {
                            let _ = tx.send(Err(tonic::Status::not_found("no gen"))).await;
                            return;
                        }
                    }
                }
                _ => return,
            };
            let mut req = first;
            let mut first_msg = true;
            loop {
                if let Some(Data::ChecksummedData(d)) = req.data.take() {
                    if req.write_offset != buf.len() as i64 {
                        let _ = tx.send(Err(tonic::Status::out_of_range("offset"))).await;
                        return;
                    }
                    if let Some(c) = d.crc32c
                        && c != crc(&d.content)
                    {
                        let _ = tx.send(Err(tonic::Status::invalid_argument("crc"))).await;
                        return;
                    }
                    buf.extend_from_slice(&d.content);
                }
                st.objects
                    .lock()
                    .unwrap()
                    .insert(name.clone(), (GENERATION, buf.clone(), false));
                let resp = if req.finish_write {
                    if let Some(c) = req.object_checksums.as_ref().and_then(|c| c.crc32c)
                        && c != crc(&buf)
                    {
                        let _ = tx
                            .send(Err(tonic::Status::invalid_argument("checksum mismatch")))
                            .await;
                        return;
                    }
                    st.objects
                        .lock()
                        .unwrap()
                        .insert(name.clone(), (GENERATION, buf.clone(), true));
                    Some(WriteStatus::Resource(proto_object(
                        &name, GENERATION, &buf, true,
                    )))
                } else if first_msg {
                    Some(WriteStatus::Resource(proto_object(
                        &name, GENERATION, &buf, false,
                    )))
                } else if req.state_lookup {
                    Some(WriteStatus::PersistedSize(buf.len() as i64))
                } else {
                    None
                };
                first_msg = false;
                if let Some(ws) = resp {
                    let _ = tx
                        .send(Ok(gcs::BidiWriteObjectResponse {
                            write_status: Some(ws),
                            write_handle: Some(BidiWriteHandle {
                                handle: HANDLE.to_vec(),
                            }),
                            persisted_data_checksums: Some(ObjectChecksums {
                                crc32c: Some(crc(&buf)),
                                ..ObjectChecksums::default()
                            }),
                        }))
                        .await;
                }
                match requests.recv().await {
                    Some(Ok(r)) => req = r,
                    _ => return,
                }
            }
        });
        Ok(tonic::Response::from(rx))
    });
    mock
}

// ------------------------------------------------------------- UDS harness

struct Harness {
    _dir: tempfile::TempDir,
    sock: PathBuf,
    client: GcsCoreClient<Channel>,
    srv: tokio::task::JoinHandle<()>,
    _mock: tokio::task::JoinHandle<()>,
    state: Arc<FakeState>,
}

async fn connect_uds(sock: PathBuf) -> anyhow::Result<GcsCoreClient<Channel>> {
    let channel = Endpoint::try_from("http://[::]:50051")?
        .connect_with_connector(service_fn(move |_: Uri| {
            let p = sock.clone();
            async move { Ok::<_, std::io::Error>(TokioIo::new(UnixStream::connect(p).await?)) }
        }))
        .await?;
    Ok(GcsCoreClient::new(channel)
        .max_decoding_message_size(64 * MIB)
        .max_encoding_message_size(64 * MIB))
}

async fn harness(shm_size: usize, copy_mode: &str) -> anyhow::Result<Harness> {
    let state = Arc::new(FakeState::default());
    let (endpoint, mock) = start_grpc_mock("127.0.0.1:0", fake_gcs(state.clone())).await?;
    let dir = tempfile::tempdir()?;
    let sock = dir.path().join("bidi.sock");
    let args = Args {
        socket: sock.to_string_lossy().to_string(),
        idle_secs: 0,
        shm_size,
        endpoint: Some(endpoint),
        write_copy_mode: copy_mode.to_string(),
        ..Default::default()
    };
    let listener = bind_uds_listener(&args.socket).map_err(|e| anyhow::anyhow!("{e}"))?;
    let shared = Shared::new();
    let srv = tokio::spawn(async move {
        let _ = serve_with_listener(args, listener, shared).await;
    });
    let shm = PathBuf::from(format!("{}.shm", sock.display()));
    for _ in 0..200 {
        if shm.exists() || shm_size == 0 {
            break;
        }
        tokio::time::sleep(Duration::from_millis(5)).await;
    }
    let mut client = connect_uds(sock.clone()).await?;
    // Anonymous session against the mock endpoint (v2 additive CreateSession fields).
    let sess = client
        .create_session(pb::CreateSessionRequest {
            anonymous: Some(true),
            ..Default::default()
        })
        .await?
        .into_inner();
    assert!(!sess.session_id.is_empty());
    Ok(Harness {
        _dir: dir,
        sock,
        client,
        srv,
        _mock: mock,
        state,
    })
}

impl Harness {
    fn session_request<T>(&self, msg: T, sid: &str) -> tonic::Request<T> {
        let mut r = tonic::Request::new(msg);
        r.metadata_mut().insert("x-session", sid.parse().unwrap());
        r
    }

    async fn sid(&mut self) -> anyhow::Result<String> {
        Ok(self
            .client
            .create_session(pb::CreateSessionRequest {
                anonymous: Some(true),
                ..Default::default()
            })
            .await?
            .into_inner()
            .session_id)
    }

    async fn shutdown(mut self) -> anyhow::Result<()> {
        self.client.shutdown(pb::Empty {}).await?;
        self.srv.await?;
        Ok(())
    }
}

/// A client-side mapping of a server-created memfd region.
struct ClientRegion {
    _stream: std::os::unix::net::UnixStream,
    id: u64,
    size: usize,
    base: *mut u8,
}

impl ClientRegion {
    fn connect(sock: &Path) -> anyhow::Result<Self> {
        use std::os::unix::io::AsRawFd;
        let shm = PathBuf::from(format!("{}.shm", sock.display()));
        let stream = std::os::unix::net::UnixStream::connect(&shm)?;
        let mut hdr = [0u8; 16];
        let mut iov = libc::iovec {
            iov_base: hdr.as_mut_ptr() as *mut libc::c_void,
            iov_len: hdr.len(),
        };
        let mut cmsg = [0u64; 8];
        // SAFETY: zeroed msghdr is a valid initial state; buffers outlive recvmsg.
        let mut msg: libc::msghdr = unsafe { std::mem::zeroed() };
        msg.msg_iov = &mut iov;
        msg.msg_iovlen = 1;
        msg.msg_control = cmsg.as_mut_ptr() as *mut libc::c_void;
        msg.msg_controllen = std::mem::size_of_val(&cmsg);
        // SAFETY: valid socket fd and msghdr.
        let n = unsafe { libc::recvmsg(stream.as_raw_fd(), &mut msg, 0) };
        anyhow::ensure!(n == 16, "short shm header");
        // SAFETY: the server always attaches exactly one SCM_RIGHTS fd.
        let fd = unsafe {
            let c = libc::CMSG_FIRSTHDR(&msg);
            anyhow::ensure!(!c.is_null(), "missing SCM_RIGHTS");
            let mut fd: libc::c_int = -1;
            std::ptr::copy_nonoverlapping(
                libc::CMSG_DATA(c),
                &mut fd as *mut libc::c_int as *mut u8,
                std::mem::size_of::<libc::c_int>(),
            );
            fd
        };
        let id = u64::from_le_bytes(hdr[..8].try_into()?);
        let size = u64::from_le_bytes(hdr[8..].try_into()?) as usize;
        // Sealed: the client can neither shrink nor grow the region.
        // SAFETY: fd is a valid memfd.
        assert_ne!(unsafe { libc::ftruncate(fd, 0) }, 0, "memfd must be sealed");
        // SAFETY: fd is a valid memfd of `size` bytes.
        let base = unsafe {
            libc::mmap(
                std::ptr::null_mut(),
                size,
                libc::PROT_READ | libc::PROT_WRITE,
                libc::MAP_SHARED,
                fd,
                0,
            )
        };
        anyhow::ensure!(base != libc::MAP_FAILED, "mmap failed");
        // SAFETY: fd no longer needed once mapped.
        unsafe { libc::close(fd) };
        Ok(Self {
            _stream: stream,
            id,
            size,
            base: base as *mut u8,
        })
    }

    fn read(&self, slot: u32, len: u32) -> Vec<u8> {
        assert!((slot as usize + 1) * SLOT <= self.size);
        // SAFETY: bounds checked above; the slot is CLIENT_READING (owned by us).
        unsafe {
            std::slice::from_raw_parts(self.base.add(slot as usize * SLOT), len as usize).to_vec()
        }
    }

    fn write(&self, slot: u32, data: &[u8]) {
        assert!(data.len() <= SLOT && (slot as usize + 1) * SLOT <= self.size);
        // SAFETY: bounds checked above; the slot is FREE on the client side.
        unsafe {
            std::ptr::copy_nonoverlapping(
                data.as_ptr(),
                self.base.add(slot as usize * SLOT),
                data.len(),
            )
        };
    }
}

impl Drop for ClientRegion {
    fn drop(&mut self) {
        // SAFETY: base/size come from a successful mmap.
        unsafe { libc::munmap(self.base as *mut libc::c_void, self.size) };
    }
}

fn pattern(n: usize, seed: u8) -> Vec<u8> {
    (0..n)
        .map(|i| (i as u8).wrapping_mul(31).wrapping_add(seed))
        .collect()
}

// --------------------------------------------------------------------- reads

type ReadTx = mpsc::Sender<pb::BidiReadObjectRequest>;

fn open_read(object: &str, region: u64) -> pb::BidiReadObjectRequest {
    pb::BidiReadObjectRequest {
        op: Some(pb::bidi_read_object_request::Op::Open(pb::OpenReadSpec {
            bucket: "bkt".to_string(),
            object: object.to_string(),
            read_region_id: region,
            compute_full_crc32c: true,
            ..Default::default()
        })),
    }
}

fn read_ranges(ranges: &[(i64, i64, i64)]) -> pb::BidiReadObjectRequest {
    pb::BidiReadObjectRequest {
        op: Some(pb::bidi_read_object_request::Op::Read(pb::ReadRanges {
            ranges: ranges
                .iter()
                .map(|&(range_id, offset, length)| pb::RangeSpec {
                    range_id,
                    offset,
                    length,
                })
                .collect(),
        })),
    }
}

fn release(slots: Vec<u32>) -> pb::BidiReadObjectRequest {
    pb::BidiReadObjectRequest {
        op: Some(pb::bidi_read_object_request::Op::Release(
            pb::ReleaseSlots { slots },
        )),
    }
}

async fn drain_ranges(
    resp: &mut tonic::Streaming<pb::BidiReadObjectResponse>,
    tx: &ReadTx,
    region: Option<&ClientRegion>,
    want: usize,
) -> anyhow::Result<(HashMap<i64, Vec<u8>>, HashMap<i64, pb::RangeError>)> {
    let mut data: HashMap<i64, Vec<u8>> = HashMap::new();
    let mut errors = HashMap::new();
    let mut done = 0;
    while done < want {
        let msg = tokio::time::timeout(Duration::from_secs(20), resp.next())
            .await?
            .ok_or_else(|| anyhow::anyhow!("stream ended"))??;
        match msg.msg {
            Some(RMsg::Data(d)) => {
                let buf = data.entry(d.range_id).or_default();
                if let Some(s) = d.slot {
                    let r = region.expect("slot without region");
                    assert_eq!(s.region_id, r.id);
                    assert!(s.length as usize <= SLOT && s.length > 0);
                    buf.extend(r.read(s.slot, s.length));
                    tx.send(release(vec![s.slot])).await?;
                } else {
                    buf.extend_from_slice(&d.inline_data);
                }
                if d.range_end {
                    done += 1;
                }
            }
            Some(RMsg::RangeError(e)) => {
                errors.insert(e.range_id, e);
                done += 1;
            }
            other => anyhow::bail!("unexpected {other:?}"),
        }
    }
    Ok((data, errors))
}

#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn bidi_read_shm_ranges_release_cancel_and_errors() -> anyhow::Result<()> {
    // 8 MiB region = 4 slots: forces the server to wait for releases.
    let mut h = harness(8 * MIB, "zero-copy").await?;
    let object = pattern(11 * MIB + 7, 3);
    h.state
        .objects
        .lock()
        .unwrap()
        .insert("obj".to_string(), (GENERATION, object.clone(), true));
    let region = ClientRegion::connect(&h.sock)?;
    let sid = h.sid().await?;

    let info = h.client.get_server_info(pb::Empty {}).await?.into_inner();
    for f in [
        "bidi-read",
        "bidi-write",
        "bidi-read-shm",
        "bidi-write-shm",
        "memfd",
    ] {
        assert!(
            info.features.iter().any(|x| x == f),
            "missing {f}: {info:?}"
        );
    }
    assert_eq!(info.shm_slot_size as usize, SLOT);
    assert_eq!(info.max_ranges_per_request, 1000);

    let (tx, rx) = mpsc::channel(64);
    tx.send(open_read("obj", region.id)).await?;
    let mut resp = h
        .client
        .bidi_read_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner();
    match resp.next().await.unwrap()?.msg {
        Some(RMsg::Opened(o)) => {
            let o = o.object.unwrap();
            assert_eq!(o.size, object.len() as i64);
            assert_eq!(o.generation, GENERATION);
            assert!(o.finalized);
            assert_eq!(o.crc32c, Some(crc(&object)));
            let v: serde_json::Value = serde_json::from_str(&o.object_json)?;
            assert_eq!(v["generation"], GENERATION.to_string());
        }
        other => anyhow::bail!("expected opened, got {other:?}"),
    }

    // 3 concurrent ranges incl. a to-EOF read larger than the whole region, a tail read
    // and a range past EOF (OUT_OF_RANGE without killing the session).
    tx.send(read_ranges(&[
        (1, 0, 0),
        (2, 100, 5000),
        (3, -10, 0),
        (4, 1 << 40, 10),
        (5, object.len() as i64, 0),
    ]))
    .await?;
    let (data, errors) = drain_ranges(&mut resp, &tx, Some(&region), 5).await?;
    assert_eq!(data[&1], object);
    assert_eq!(data[&2], object[100..5100]);
    assert_eq!(data[&3], object[object.len() - 10..]);
    assert!(data.get(&5).is_none_or(|d| d.is_empty()));
    assert_eq!(errors[&4].code, tonic::Code::OutOfRange as i32);

    // Double release of a slot aborts the session with FAILED_PRECONDITION.
    tx.send(read_ranges(&[(6, 0, 10)])).await?;
    let msg = resp.next().await.unwrap()?;
    let slot = match msg.msg {
        Some(RMsg::Data(d)) => d.slot.unwrap().slot,
        other => anyhow::bail!("unexpected {other:?}"),
    };
    tx.send(release(vec![slot])).await?;
    tx.send(release(vec![slot])).await?;
    let mut saw_err = None;
    while let Some(m) = resp.next().await {
        if let Err(st) = m {
            saw_err = Some(st);
            break;
        }
    }
    assert_eq!(
        saw_err.expect("session must abort").code(),
        tonic::Code::FailedPrecondition
    );
    drop(tx);

    // Cancellation: a new session on the SAME region; cancel a huge to-EOF read while it is
    // blocked on slots, the region must be fully reusable afterwards.
    let (tx, rx) = mpsc::channel(64);
    tx.send(open_read("obj", region.id)).await?;
    let mut resp = h
        .client
        .bidi_read_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner();
    let _ = resp.next().await.unwrap()?;
    tx.send(read_ranges(&[(10, 0, 0)])).await?;
    let first = resp.next().await.unwrap()?;
    let mut held = Vec::new();
    if let Some(RMsg::Data(d)) = first.msg {
        held.push(d.slot.unwrap().slot);
    }
    tx.send(pb::BidiReadObjectRequest {
        op: Some(pb::bidi_read_object_request::Op::Cancel(pb::CancelRanges {
            range_ids: vec![10],
        })),
    })
    .await?;
    // Release what we hold; slots published before the cancel are still delivered.
    tx.send(release(held)).await?;
    tokio::time::sleep(Duration::from_millis(100)).await;
    tx.send(read_ranges(&[(11, 0, 0)])).await?;
    let mut got = Vec::new();
    loop {
        let m = tokio::time::timeout(Duration::from_secs(20), resp.next())
            .await?
            .unwrap()?;
        match m.msg {
            Some(RMsg::Data(d)) => {
                if let Some(s) = d.slot.as_ref() {
                    if d.range_id == 11 {
                        got.extend(region.read(s.slot, s.length));
                    }
                    tx.send(release(vec![s.slot])).await?;
                }
                if d.range_id == 11 && d.range_end {
                    break;
                }
            }
            other => anyhow::bail!("unexpected {other:?}"),
        }
    }
    assert_eq!(got, object);
    drop(tx);

    // Checksum mismatch -> RangeError{checksum_mismatch, DATA_LOSS}; session stays usable.
    h.state.corrupt_reads.store(true, Ordering::SeqCst);
    let (tx, rx) = mpsc::channel(64);
    tx.send(open_read("obj", 0)).await?;
    let mut resp = h
        .client
        .bidi_read_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner();
    let _ = resp.next().await.unwrap()?;
    // A multi-chunk range: the first (corrupted) chunk fails the SDK's per-chunk CRC32C.
    tx.send(read_ranges(&[(20, 0, 3 * MIB as i64)])).await?;
    let (_, errors) = drain_ranges(&mut resp, &tx, None, 1).await?;
    let e = &errors[&20];
    assert!(e.checksum_mismatch, "{e:?}");
    assert_eq!(e.code, tonic::Code::DataLoss as i32);
    drop(tx);

    // A single-chunk range: the SDK drops the reader of a corrupted final chunk without an
    // error; the server must still never report a truncated range as complete.
    let (tx, rx) = mpsc::channel(64);
    tx.send(open_read("obj", 0)).await?;
    let mut resp = h
        .client
        .bidi_read_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner();
    let _ = resp.next().await.unwrap()?;
    tx.send(read_ranges(&[(21, 0, 1000)])).await?;
    let (data, errors) = drain_ranges(&mut resp, &tx, None, 1).await?;
    assert!(data.get(&21).is_none_or(|d| d.len() < 1000));
    assert_eq!(errors[&21].code, tonic::Code::DataLoss as i32, "{errors:?}");
    drop(tx);

    // Unknown object -> NOT_FOUND on the stream.
    h.state.corrupt_reads.store(false, Ordering::SeqCst);
    let (tx, rx) = mpsc::channel(4);
    tx.send(open_read("missing", 0)).await?;
    let err = h
        .client
        .bidi_read_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner()
        .next()
        .await
        .unwrap()
        .expect_err("missing object");
    assert_eq!(err.code(), tonic::Code::NotFound);

    // Unknown region -> NOT_FOUND.
    let (tx, rx) = mpsc::channel(4);
    tx.send(open_read("obj", 999_999)).await?;
    let err = h
        .client
        .bidi_read_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner()
        .next()
        .await
        .unwrap()
        .expect_err("unknown region");
    assert_eq!(err.code(), tonic::Code::NotFound);
    drop(region);
    h.shutdown().await
}

#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn bidi_read_inline_fallback_and_too_many_ranges() -> anyhow::Result<()> {
    let mut h = harness(0, "zero-copy").await?;
    let object = pattern(3 * MIB, 9);
    h.state
        .objects
        .lock()
        .unwrap()
        .insert("o".to_string(), (GENERATION, object.clone(), true));
    let info = h.client.get_server_info(pb::Empty {}).await?.into_inner();
    assert!(!info.features.iter().any(|f| f == "bidi-read-shm"));
    let sid = h.sid().await?;
    let (tx, rx) = mpsc::channel(64);
    tx.send(open_read("o", 0)).await?;
    let mut resp = h
        .client
        .bidi_read_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner();
    let _ = resp.next().await.unwrap()?;
    tx.send(read_ranges(&[(1, 0, 0), (2, MIB as i64, 10)]))
        .await?;
    let (data, _) = drain_ranges(&mut resp, &tx, None, 2).await?;
    assert_eq!(data[&1], object);
    assert_eq!(data[&2], object[MIB..MIB + 10]);
    let too_many: Vec<(i64, i64, i64)> = (0..1001).map(|i| (100 + i, 0, 1)).collect();
    tx.send(read_ranges(&too_many)).await?;
    let mut err = None;
    while let Some(m) = resp.next().await {
        if let Err(st) = m {
            err = Some(st);
            break;
        }
    }
    assert_eq!(err.unwrap().code(), tonic::Code::InvalidArgument);
    h.shutdown().await
}

// -------------------------------------------------------------------- writes

fn wreq(op: pb::bidi_write_object_request::Op, op_id: u64) -> pb::BidiWriteObjectRequest {
    pb::BidiWriteObjectRequest {
        op: Some(op),
        op_id,
    }
}

fn open_write(object: &str, region: u64, reopen: Option<i64>) -> pb::BidiWriteObjectRequest {
    wreq(
        pb::bidi_write_object_request::Op::Open(pb::OpenAppendSpec {
            bucket: "bkt".to_string(),
            object: object.to_string(),
            reopen_generation: reopen,
            write_handle: if reopen.is_some() {
                HANDLE.to_vec()
            } else {
                Vec::new()
            },
            write_region_id: region,
            attrs: Some(pb::ObjectAttrs {
                content_type: "application/octet-stream".to_string(),
                ..Default::default()
            }),
            ..Default::default()
        }),
        1,
    )
}

fn append_slot(region: u64, slot: u32, len: usize) -> pb::BidiWriteObjectRequest {
    wreq(
        pb::bidi_write_object_request::Op::Append(pb::Append {
            slot: Some(pb::ShmSlotRef {
                region_id: region,
                slot,
                length: len as u32,
            }),
            inline_data: bytes::Bytes::new(),
        }),
        0,
    )
}

/// Reads responses until the op-response `op_id` arrives, collecting released slots.
async fn until_op(
    resp: &mut tonic::Streaming<pb::BidiWriteObjectResponse>,
    op_id: u64,
    released: &mut Vec<u32>,
) -> anyhow::Result<pb::BidiWriteObjectResponse> {
    loop {
        let m = tokio::time::timeout(Duration::from_secs(20), resp.next())
            .await?
            .ok_or_else(|| anyhow::anyhow!("stream ended"))??;
        if let Some(WMsg::Released(r)) = &m.msg {
            released.extend(&r.slots);
            continue;
        }
        if m.op_id == op_id {
            return Ok(m);
        }
    }
}

#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn bidi_write_shm_lease_release_flush_close_finalize_and_takeover() -> anyhow::Result<()> {
    // 8 MiB region = 4 x 2 MiB slots.
    let mut h = harness(8 * MIB, "zero-copy").await?;
    let region = ClientRegion::connect(&h.sock)?;
    let sid = h.sid().await?;

    let (tx, rx) = mpsc::channel(64);
    tx.send(open_write("w", region.id, None)).await?;
    let mut resp = h
        .client
        .bidi_write_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner();
    match resp.next().await.unwrap()?.msg {
        Some(WMsg::Opened(o)) => {
            assert_eq!(o.generation, GENERATION);
            assert_eq!(o.persisted_size, 0);
        }
        other => anyhow::bail!("expected opened, got {other:?}"),
    }
    let mut expected = Vec::new();
    for slot in 0..4u32 {
        let d = pattern(SLOT, slot as u8);
        region.write(slot, &d);
        expected.extend_from_slice(&d);
        tx.send(append_slot(region.id, slot, SLOT)).await?;
    }
    // All 4 slots are leased by the SDK's replay buffer until GCS acks them: the client is
    // starved (no SlotsReleased) until it sends a Flush.
    let early = tokio::time::timeout(Duration::from_millis(300), resp.next()).await;
    assert!(early.is_err(), "no release before ack: {early:?}");
    // Duplicate submission of a still-leased slot is rejected... on a fresh session below.
    tx.send(wreq(
        pb::bidi_write_object_request::Op::Flush(pb::Flush {}),
        7,
    ))
    .await?;
    let mut released = Vec::new();
    let flushed = until_op(&mut resp, 7, &mut released).await?;
    match flushed.msg {
        Some(WMsg::Flushed(f)) => assert_eq!(f.persisted_size, 4 * SLOT as i64),
        other => anyhow::bail!("expected flushed, got {other:?}"),
    }
    // Releases may trail the Flushed response slightly.
    for _ in 0..50 {
        if released.len() == 4 {
            break;
        }
        if let Ok(Some(Ok(m))) = tokio::time::timeout(Duration::from_millis(100), resp.next()).await
            && let Some(WMsg::Released(r)) = m.msg
        {
            released.extend(r.slots);
        }
    }
    released.sort();
    assert_eq!(released, vec![0, 1, 2, 3]);

    // Tail (< 2 MiB) then Close -> persisted size, every slot released before Closed.
    let tail = pattern(1000, 77);
    region.write(0, &tail);
    expected.extend_from_slice(&tail);
    tx.send(append_slot(region.id, 0, tail.len())).await?;
    tx.send(wreq(
        pb::bidi_write_object_request::Op::Close(pb::Close {}),
        9,
    ))
    .await?;
    let mut released = Vec::new();
    match until_op(&mut resp, 9, &mut released).await?.msg {
        Some(WMsg::Closed(c)) => assert_eq!(c.persisted_size, expected.len() as i64),
        other => anyhow::bail!("expected closed, got {other:?}"),
    }
    assert_eq!(released, vec![0]);
    drop(tx);
    assert_eq!(h.state.objects.lock().unwrap()["w"].1, expected);

    // Takeover by generation with write_handle, then finalize with the WRONG crc: the
    // server cannot pre-check (persisted_size > 0) so it compares post-hoc.
    let (tx, rx) = mpsc::channel(64);
    tx.send(open_write("w", region.id, Some(GENERATION)))
        .await?;
    let mut resp = h
        .client
        .bidi_write_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner();
    match resp.next().await.unwrap()?.msg {
        Some(WMsg::Opened(o)) => assert_eq!(o.persisted_size, expected.len() as i64),
        other => anyhow::bail!("expected opened, got {other:?}"),
    }
    {
        let specs = h.state.append_specs.lock().unwrap();
        let spec = specs.last().expect("AppendObjectSpec sent");
        assert_eq!(spec.generation, GENERATION);
        assert_eq!(spec.write_handle.as_ref().unwrap().handle, HANDLE);
    }
    let more = pattern(SLOT, 5);
    region.write(1, &more);
    expected.extend_from_slice(&more);
    tx.send(append_slot(region.id, 1, SLOT)).await?;
    // Duplicate submission of the still-leased slot 1 is rejected.
    tx.send(append_slot(region.id, 1, SLOT)).await?;
    let mut err = None;
    while let Some(m) = resp.next().await {
        if let Err(st) = m {
            err = Some(st);
            break;
        }
    }
    assert_eq!(err.unwrap().code(), tonic::Code::FailedPrecondition);
    drop(tx);
    drop(region);
    h.shutdown().await
}

#[tokio::test(flavor = "multi_thread", worker_threads = 4)]
async fn bidi_write_finalize_crc_precheck_inline_and_copy_mode() -> anyhow::Result<()> {
    let mut h = harness(8 * MIB, "copy").await?;
    let region = ClientRegion::connect(&h.sock)?;
    let sid = h.sid().await?;
    let data = pattern(3 * MIB + 5, 1);

    // Matching CRC (copy mode releases immediately after each Append).
    let (tx, rx) = mpsc::channel(64);
    tx.send(open_write("ok", region.id, None)).await?;
    let mut resp = h
        .client
        .bidi_write_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner();
    let _ = resp.next().await.unwrap()?;
    region.write(0, &data[..SLOT]);
    region.write(1, &data[SLOT..]);
    tx.send(append_slot(region.id, 0, SLOT)).await?;
    tx.send(append_slot(region.id, 1, data.len() - SLOT))
        .await?;
    tx.send(wreq(
        pb::bidi_write_object_request::Op::Finalize(pb::Finalize {
            full_object_crc32c: Some(crc(&data)),
        }),
        3,
    ))
    .await?;
    let mut released = Vec::new();
    match until_op(&mut resp, 3, &mut released).await?.msg {
        Some(WMsg::Finalized(f)) => {
            let o = f.object.unwrap();
            assert_eq!(o.size, data.len() as i64);
            assert_eq!(o.crc32c, Some(crc(&data)));
            assert!(o.finalized);
        }
        other => anyhow::bail!("expected finalized, got {other:?}"),
    }
    released.sort();
    assert_eq!(released, vec![0, 1]);
    drop(tx);

    // Mismatching CRC on a new object: pre-checked by the server's running CRC32C; the
    // object stays unfinalized (bytes persisted via close) and INVALID_ARGUMENT is returned.
    let (tx, rx) = mpsc::channel(64);
    tx.send(open_write("bad", 0, None)).await?;
    let mut resp = h
        .client
        .bidi_write_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner();
    let _ = resp.next().await.unwrap()?;
    tx.send(wreq(
        pb::bidi_write_object_request::Op::Append(pb::Append {
            slot: None,
            inline_data: bytes::Bytes::from(data.clone()),
        }),
        0,
    ))
    .await?;
    tx.send(wreq(
        pb::bidi_write_object_request::Op::Finalize(pb::Finalize {
            full_object_crc32c: Some(crc(&data) ^ 1),
        }),
        4,
    ))
    .await?;
    let mut err = None;
    while let Some(m) = resp.next().await {
        if let Err(st) = m {
            err = Some(st);
            break;
        }
    }
    let err = err.expect("crc mismatch must fail");
    assert_eq!(err.code(), tonic::Code::InvalidArgument);
    assert!(err.message().contains("crc32c"), "{err:?}");
    let (_, stored, finalized) = h.state.objects.lock().unwrap()["bad"].clone();
    assert_eq!(stored, data);
    assert!(!finalized, "object must stay unfinalized");
    drop(tx);

    // generation==0 precondition on an existing object -> FAILED_PRECONDITION.
    let (tx, rx) = mpsc::channel(4);
    let mut open = open_write("ok", 0, None);
    if let Some(pb::bidi_write_object_request::Op::Open(spec)) = open.op.as_mut() {
        spec.if_generation_match = Some(0);
    }
    tx.send(open).await?;
    let err = h
        .client
        .bidi_write_object(h.session_request(ReceiverStream::new(rx), &sid))
        .await?
        .into_inner()
        .next()
        .await
        .unwrap()
        .expect_err("precondition");
    assert_eq!(err.code(), tonic::Code::FailedPrecondition);

    // A region cannot be claimed by two writers at once, nor used as a read region.
    let (tx1, rx1) = mpsc::channel(4);
    tx1.send(open_write("a", region.id, None)).await?;
    let mut r1 = h
        .client
        .bidi_write_object(h.session_request(ReceiverStream::new(rx1), &sid))
        .await?
        .into_inner();
    let _ = r1.next().await.unwrap()?;
    let (tx2, rx2) = mpsc::channel(4);
    tx2.send(open_write("b", region.id, None)).await?;
    let err = h
        .client
        .bidi_write_object(h.session_request(ReceiverStream::new(rx2), &sid))
        .await?
        .into_inner()
        .next()
        .await
        .unwrap()
        .expect_err("second writer");
    assert_eq!(err.code(), tonic::Code::FailedPrecondition);
    let (tx3, rx3) = mpsc::channel(4);
    tx3.send(open_read("ok", region.id)).await?;
    let err = h
        .client
        .bidi_read_object(h.session_request(ReceiverStream::new(rx3), &sid))
        .await?
        .into_inner()
        .next()
        .await
        .unwrap()
        .expect_err("write region used for reads");
    assert_eq!(err.code(), tonic::Code::FailedPrecondition);
    drop((tx1, tx2, tx3));
    drop(region);
    h.shutdown().await
}
