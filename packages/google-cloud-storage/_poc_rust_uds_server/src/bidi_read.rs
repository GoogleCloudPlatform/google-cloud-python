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

//! `BidiReadObject` sessions: one gRPC stream == one `ObjectDescriptor`.
//!
//! Every requested range runs as a task that loops `ReadObjectResponse::next()` on the
//! (unmodified) SDK descriptor; each CRC32C-validated `Bytes` chunk is split into
//! slot-sized pieces, copied once into a server-owned SHM slot and published to the
//! client as a `RangeData{slot}` descriptor. The client copies the slot into the user's
//! buffer and returns it with `ReleaseSlots`. Without a read region the bytes travel
//! inline (`RangeData.inline_data`).

use crate::pb::{self, bidi_read_object_request::Op, bidi_read_object_response::Msg};
use crate::service::{bucket_name, is_checksum_mismatch, to_status};
use crate::shm::Registry;
use crate::slots::{ArenaKind, PublishedSlots, SlotArena};
use google_cloud_storage::client::Storage;
use google_cloud_storage::model_ext::ReadRange;
use google_cloud_storage::object_descriptor::ObjectDescriptor;
use std::collections::HashMap;
use std::sync::Arc;
use tokio::sync::mpsc;
use tokio::task::{AbortHandle, JoinSet};
use tokio_stream::{Stream, StreamExt};
use tonic::Status;

/// Maximum number of ranges accepted in one `ReadRanges` request.
pub const MAX_RANGES_PER_REQUEST: usize = 1000;

type Tx = mpsc::Sender<Result<pb::BidiReadObjectResponse, Status>>;

/// Maps a `RangeSpec` to the SDK `ReadRange`.
///
/// * `offset < 0` -> `ReadRange::tail(-offset)`
/// * `length == 0` (or negative) -> `ReadRange::offset(offset)` (to EOF, unknown size OK)
/// * otherwise -> `ReadRange::segment(offset, length)`
pub fn to_read_range(offset: i64, length: i64) -> ReadRange {
    if offset < 0 {
        ReadRange::tail(offset.unsigned_abs())
    } else if length <= 0 {
        ReadRange::offset(offset as u64)
    } else {
        ReadRange::segment(offset as u64, length as u64)
    }
}

/// Opens the SDK descriptor for an `OpenReadSpec`.
pub async fn open_descriptor(
    storage: &Storage,
    spec: &pb::OpenReadSpec,
) -> Result<ObjectDescriptor, Status> {
    if spec.bucket.is_empty() || spec.object.is_empty() {
        return Err(Status::invalid_argument("bucket and object are required"));
    }
    let mut open = storage
        .open_object(bucket_name(&spec.bucket), spec.object.clone())
        .compute_crc32c(spec.compute_full_crc32c);
    if spec.generation > 0 {
        open = open.set_generation(spec.generation);
    }
    if let Some(v) = spec.if_generation_match {
        open = open.set_if_generation_match(v);
    }
    if let Some(v) = spec.if_generation_not_match {
        open = open.set_if_generation_not_match(v);
    }
    if let Some(v) = spec.if_metageneration_match {
        open = open.set_if_metageneration_match(v);
    }
    if let Some(v) = spec.if_metageneration_not_match {
        open = open.set_if_metageneration_not_match(v);
    }
    if !spec.quota_project.is_empty() {
        open = open.with_quota_project(spec.quota_project.clone());
    }
    if !spec.user_agent.is_empty() {
        open = open.with_user_agent(spec.user_agent.clone());
    }
    open.send().await.map_err(to_status)
}

/// Runs one `BidiReadObject` session until the client half-closes or disconnects.
pub async fn run_read_session<S>(
    storage: Storage,
    regions: Arc<Registry>,
    peer: (u32, i32),
    mut inbound: S,
    tx: Tx,
    slot_size: usize,
) where
    S: Stream<Item = Result<pb::BidiReadObjectRequest, Status>> + Unpin + Send,
{
    let spec = match inbound.next().await {
        Some(Ok(pb::BidiReadObjectRequest {
            op: Some(Op::Open(spec)),
        })) => spec,
        Some(Err(_)) | None => return,
        Some(Ok(_)) => {
            let _ = tx
                .send(Err(Status::invalid_argument(
                    "the first BidiReadObject request must be `open`",
                )))
                .await;
            return;
        }
    };
    let arena = if spec.read_region_id != 0 {
        match regions
            .arena(spec.read_region_id, slot_size, ArenaKind::Read, peer)
            .await
        {
            Ok(a) => Some(a),
            Err(st) => {
                let _ = tx.send(Err(st)).await;
                return;
            }
        }
    } else {
        None
    };
    let desc = match open_descriptor(&storage, &spec).await {
        Ok(d) => d,
        Err(st) => {
            let _ = tx.send(Err(st)).await;
            return;
        }
    };
    let opened = pb::BidiReadObjectResponse {
        msg: Some(Msg::Opened(pb::ReadOpened {
            object: Some(crate::object_meta::object_resource(&desc.object())),
        })),
    };
    if tx.send(Ok(opened)).await.is_err() {
        return;
    }
    if let Err(st) = serve_descriptor(desc, arena, inbound, tx.clone(), slot_size).await {
        let _ = tx.send(Err(st)).await;
    }
}

/// Serves `ReadRanges` / `ReleaseSlots` / `CancelRanges` on an open descriptor.
pub async fn serve_descriptor<S>(
    desc: ObjectDescriptor,
    arena: Option<Arc<SlotArena>>,
    mut inbound: S,
    tx: Tx,
    slot_size: usize,
) -> Result<(), Status>
where
    S: Stream<Item = Result<pb::BidiReadObjectRequest, Status>> + Unpin + Send,
{
    let object = desc.object();
    let object_size = object.size;
    // For finalized objects the size is fixed, so ranges can be validated / clamped locally.
    // This keeps one bad range from tearing down the shared descriptor stream (GCS aborts
    // the whole BidiReadObject stream with OUT_OF_RANGE) and mirrors the Python GAPIC
    // semantics where a segment that runs past EOF is truncated at EOF.
    let fixed_size = object.finalize_time.is_some().then_some(object_size);
    let published = Arc::new(PublishedSlots::default());
    let mut tasks: JoinSet<i64> = JoinSet::new();
    let mut live: HashMap<i64, AbortHandle> = HashMap::new();
    let mut by_task: HashMap<tokio::task::Id, i64> = HashMap::new();

    let result = loop {
        tokio::select! {
            Some(done) = tasks.join_next_with_id(), if !tasks.is_empty() => {
                let task_id = match &done {
                    Ok((id, _)) => *id,
                    Err(e) => e.id(),
                };
                if let Some(range_id) = by_task.remove(&task_id) {
                    // Only forget the range if the entry still belongs to this task (a
                    // cancelled id may have been reused by a newer range).
                    if live.get(&range_id).map(|h| h.id()) == Some(task_id) {
                        live.remove(&range_id);
                    }
                }
            }
            msg = inbound.next() => {
                let req = match msg {
                    None | Some(Err(_)) => break Ok(()),
                    Some(Ok(req)) => req,
                };
                match req.op {
                    Some(Op::Read(r)) => {
                        if r.ranges.len() > MAX_RANGES_PER_REQUEST {
                            break Err(Status::invalid_argument(format!(
                                "at most {MAX_RANGES_PER_REQUEST} ranges per request, got {}",
                                r.ranges.len()
                            )));
                        }
                        let mut dup = None;
                        for rs in &r.ranges {
                            if live.contains_key(&rs.range_id) {
                                dup = Some(rs.range_id);
                                break;
                            }
                        }
                        if let Some(id) = dup {
                            break Err(Status::invalid_argument(format!(
                                "duplicate live range_id {id}"
                            )));
                        }
                        for rs in r.ranges {
                            let range_id = rs.range_id;
                            let rs = match clamp_range(rs, fixed_size) {
                                Clamped::Read(rs) => rs,
                                Clamped::Empty(offset) => {
                                    let _ = tx.send(Ok(range_end(range_id, offset))).await;
                                    continue;
                                }
                                Clamped::OutOfRange(msg) => {
                                    let st = Status::out_of_range(msg);
                                    let _ = tx.send(Ok(range_error(range_id, &st, false))).await;
                                    continue;
                                }
                            };
                            let expected = expected_len(&rs, fixed_size);
                            let h = tasks.spawn(range_task(
                                desc.clone(),
                                rs,
                                object_size,
                                expected,
                                arena.clone(),
                                published.clone(),
                                tx.clone(),
                                slot_size,
                            ));
                            by_task.insert(h.id(), range_id);
                            live.insert(range_id, h);
                        }
                    }
                    Some(Op::Release(r)) => {
                        let Some(a) = arena.as_ref() else {
                            break Err(Status::failed_precondition(
                                "ReleaseSlots on an inline (region-less) session",
                            ));
                        };
                        let mut bad = None;
                        for slot in r.slots {
                            if !published.remove(slot) {
                                bad = Some(Status::failed_precondition(format!(
                                    "slot {slot} was not published to this session"
                                )));
                                break;
                            }
                            if let Err(st) = a.release_from_client(slot) {
                                bad = Some(st);
                                break;
                            }
                        }
                        if let Some(st) = bad {
                            break Err(st);
                        }
                    }
                    Some(Op::Cancel(c)) => {
                        for id in c.range_ids {
                            if let Some(h) = live.remove(&id) {
                                h.abort();
                            }
                        }
                    }
                    Some(Op::Open(_)) => {
                        break Err(Status::invalid_argument("session is already open"));
                    }
                    None => {}
                }
            }
        }
    };

    // Session teardown: stop all range tasks (dropping their `ReadObjectResponse`s), wait
    // for them so no slot is published after this point, then reclaim slots the client
    // still held for this session.
    tasks.abort_all();
    while tasks.join_next().await.is_some() {}
    if let Some(a) = arena.as_ref() {
        for slot in published.drain() {
            let _ = a.release_from_client(slot);
        }
    }
    result
}

/// Exact number of bytes a (clamped) range must produce when the object size is fixed.
fn expected_len(rs: &pb::RangeSpec, fixed_size: Option<i64>) -> Option<i64> {
    let size = fixed_size?;
    if rs.offset < 0 {
        return Some(rs.offset.unsigned_abs().min(size as u64) as i64);
    }
    let remaining = (size - rs.offset).max(0);
    Some(if rs.length > 0 {
        rs.length.min(remaining)
    } else {
        remaining
    })
}

#[allow(clippy::too_many_arguments)]
async fn range_task(
    desc: ObjectDescriptor,
    spec: pb::RangeSpec,
    object_size: i64,
    expected: Option<i64>,
    arena: Option<Arc<SlotArena>>,
    published: Arc<PublishedSlots>,
    tx: Tx,
    slot_size: usize,
) -> i64 {
    let range_id = spec.range_id;
    let mut offset = if spec.offset >= 0 {
        spec.offset
    } else {
        (object_size + spec.offset).max(0)
    };
    let mut received: i64 = 0;
    let mut resp = desc
        .read_range(to_read_range(spec.offset, spec.length))
        .await;
    loop {
        match resp.next().await {
            Some(Ok(chunk)) => {
                let mut start = 0usize;
                while start < chunk.len() {
                    let end = (start + slot_size).min(chunk.len());
                    let piece = chunk.slice(start..end);
                    let len = piece.len();
                    let data = match arena.as_ref() {
                        Some(a) => {
                            let mut slot = match a.acquire().await {
                                Ok(s) => s,
                                Err(st) => {
                                    let _ = tx.send(Ok(range_error(range_id, &st, false))).await;
                                    return range_id;
                                }
                            };
                            if let Err(st) = slot.write(&piece) {
                                let _ = tx.send(Ok(range_error(range_id, &st, false))).await;
                                return range_id;
                            }
                            let s = slot.publish();
                            published.insert(s);
                            pb::RangeData {
                                range_id,
                                range_offset: offset,
                                slot: Some(pb::ShmSlotRef {
                                    region_id: a.region_id(),
                                    slot: s,
                                    length: len as u32,
                                }),
                                inline_data: bytes::Bytes::new(),
                                range_end: false,
                            }
                        }
                        None => pb::RangeData {
                            range_id,
                            range_offset: offset,
                            slot: None,
                            inline_data: piece,
                            range_end: false,
                        },
                    };
                    offset += len as i64;
                    received += len as i64;
                    start = end;
                    let msg = pb::BidiReadObjectResponse {
                        msg: Some(Msg::Data(data)),
                    };
                    if tx.send(Ok(msg)).await.is_err() {
                        return range_id;
                    }
                }
            }
            Some(Err(e)) => {
                let mismatch = is_checksum_mismatch(&e);
                let st = to_status(e);
                let _ = tx.send(Ok(range_error(range_id, &st, mismatch))).await;
                return range_id;
            }
            None => {
                // Defense in depth: the SDK may end a range stream without an error (e.g. a
                // checksum failure on the final chunk of a range drops its reader). Never
                // report a silently truncated range as complete.
                if let Some(want) = expected
                    && received != want
                {
                    let st = Status::data_loss(format!(
                        "range ended after {received} of {want} bytes without an error \
                         (possible checksum failure)"
                    ));
                    let _ = tx.send(Ok(range_error(range_id, &st, false))).await;
                    return range_id;
                }
                let _ = tx.send(Ok(range_end(range_id, offset))).await;
                return range_id;
            }
        }
    }
}

/// Result of validating a range against a fixed (finalized) object size.
#[derive(Debug, PartialEq)]
enum Clamped {
    /// Issue this (possibly truncated) range to the SDK.
    Read(pb::RangeSpec),
    /// Zero bytes to read at this absolute offset (e.g. `offset == size`).
    Empty(i64),
    /// The range starts past the end of the object.
    OutOfRange(String),
}

fn clamp_range(mut rs: pb::RangeSpec, fixed_size: Option<i64>) -> Clamped {
    let Some(size) = fixed_size else {
        return Clamped::Read(rs);
    };
    if rs.offset < 0 {
        // Tail reads larger than the object read the whole object.
        if rs.offset.unsigned_abs() > size as u64 {
            rs.offset = 0;
            rs.length = 0;
        }
        return if size == 0 {
            Clamped::Empty(0)
        } else {
            Clamped::Read(rs)
        };
    }
    if rs.offset > size {
        return Clamped::OutOfRange(format!(
            "read offset {} is past the end of the object (size {size})",
            rs.offset
        ));
    }
    let remaining = size - rs.offset;
    if remaining == 0 {
        return Clamped::Empty(rs.offset);
    }
    if rs.length > remaining {
        rs.length = remaining;
    }
    Clamped::Read(rs)
}

fn range_end(range_id: i64, offset: i64) -> pb::BidiReadObjectResponse {
    pb::BidiReadObjectResponse {
        msg: Some(Msg::Data(pb::RangeData {
            range_id,
            range_offset: offset,
            slot: None,
            inline_data: bytes::Bytes::new(),
            range_end: true,
        })),
    }
}

fn range_error(range_id: i64, st: &Status, checksum_mismatch: bool) -> pb::BidiReadObjectResponse {
    let code = if checksum_mismatch {
        tonic::Code::DataLoss as i32
    } else {
        st.code() as i32
    };
    pb::BidiReadObjectResponse {
        msg: Some(Msg::RangeError(pb::RangeError {
            range_id,
            code,
            message: st.message().to_string(),
            checksum_mismatch,
        })),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn read_range_mapping() {
        assert_eq!(
            format!("{:?}", to_read_range(0, 0)),
            format!("{:?}", ReadRange::offset(0))
        );
        assert_eq!(
            format!("{:?}", to_read_range(100, 0)),
            format!("{:?}", ReadRange::offset(100))
        );
        assert_eq!(
            format!("{:?}", to_read_range(-10, 0)),
            format!("{:?}", ReadRange::tail(10))
        );
        assert_eq!(
            format!("{:?}", to_read_range(5, 7)),
            format!("{:?}", ReadRange::segment(5, 7))
        );
    }

    #[test]
    fn clamp_against_fixed_size() {
        let rs = |offset, length| pb::RangeSpec {
            range_id: 1,
            offset,
            length,
        };
        // Unfinalized objects: pass through untouched.
        assert_eq!(clamp_range(rs(500, 10), None), Clamped::Read(rs(500, 10)));
        assert_eq!(clamp_range(rs(10, 5), Some(100)), Clamped::Read(rs(10, 5)));
        assert_eq!(
            clamp_range(rs(90, 50), Some(100)),
            Clamped::Read(rs(90, 10))
        );
        assert_eq!(clamp_range(rs(0, 0), Some(100)), Clamped::Read(rs(0, 0)));
        assert_eq!(clamp_range(rs(100, 0), Some(100)), Clamped::Empty(100));
        assert_eq!(clamp_range(rs(0, 0), Some(0)), Clamped::Empty(0));
        assert!(matches!(
            clamp_range(rs(1100, 100), Some(100)),
            Clamped::OutOfRange(_)
        ));
        assert_eq!(
            clamp_range(rs(-10, 0), Some(100)),
            Clamped::Read(rs(-10, 0))
        );
        assert_eq!(clamp_range(rs(-200, 0), Some(100)), Clamped::Read(rs(0, 0)));
    }

    #[test]
    fn expected_lengths() {
        let rs = |offset, length| pb::RangeSpec {
            range_id: 1,
            offset,
            length,
        };
        assert_eq!(expected_len(&rs(0, 0), None), None);
        assert_eq!(expected_len(&rs(0, 0), Some(100)), Some(100));
        assert_eq!(expected_len(&rs(10, 5), Some(100)), Some(5));
        assert_eq!(expected_len(&rs(90, 50), Some(100)), Some(10));
        assert_eq!(expected_len(&rs(-10, 0), Some(100)), Some(10));
        assert_eq!(expected_len(&rs(-1000, 0), Some(100)), Some(100));
    }

    #[test]
    fn range_error_codes() {
        let st = Status::out_of_range("past EOF");
        match range_error(3, &st, false).msg {
            Some(Msg::RangeError(e)) => {
                assert_eq!(e.range_id, 3);
                assert_eq!(e.code, tonic::Code::OutOfRange as i32);
                assert!(!e.checksum_mismatch);
            }
            other => panic!("unexpected {other:?}"),
        }
        match range_error(4, &Status::internal("x"), true).msg {
            Some(Msg::RangeError(e)) => {
                assert_eq!(e.code, tonic::Code::DataLoss as i32);
                assert!(e.checksum_mismatch);
            }
            other => panic!("unexpected {other:?}"),
        }
    }
}
