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

//! `BidiWriteObject` sessions: one gRPC stream == one `AppendableObjectWriter`.
//!
//! Operations are processed strictly in order by a single task. `Append{slot}` wraps the
//! client's SHM slot in `Bytes::from_owner(SlotLease)` and hands it to the unmodified
//! SDK writer; the slot is reported back in `SlotsReleased` only when the SDK drops the
//! last clone of those bytes (after the replay buffer is acknowledged, or immediately
//! for coalescing copies). Releases are forwarded while an SDK call is in flight so a
//! back-pressured `append()` never starves the client of slots.

use crate::pb::{self, bidi_write_object_request::Op, bidi_write_object_response::Msg};
#[cfg(google_cloud_unstable_storage_bidi)]
use crate::service::{bucket_name, to_status};
use crate::shm::Registry;
use crate::slots::{ArenaKind, WriteCopyMode};
use std::sync::Arc;
use tokio::sync::mpsc;
use tokio_stream::Stream;
use tonic::Status;

type Tx = mpsc::Sender<Result<pb::BidiWriteObjectResponse, Status>>;

/// How long `Close`/`Finalize` wait for the SDK to drop leased slots before replying.
#[cfg(google_cloud_unstable_storage_bidi)]
const RELEASE_DRAIN_TIMEOUT: std::time::Duration = std::time::Duration::from_secs(5);

/// Static configuration of write sessions.
#[derive(Clone, Copy, Debug)]
pub struct WriteSessionConfig {
    /// Slot size of write regions.
    pub slot_size: usize,
    /// Zero-copy or copy hand-off of SHM slots to the SDK.
    pub copy_mode: WriteCopyMode,
}

/// Runs one `BidiWriteObject` session.
#[cfg(not(google_cloud_unstable_storage_bidi))]
pub async fn run_write_session<S>(
    _storage: google_cloud_storage::client::Storage,
    _regions: Arc<Registry>,
    _peer: (u32, i32),
    _inbound: S,
    tx: Tx,
    _cfg: WriteSessionConfig,
) where
    S: Stream<Item = Result<pb::BidiWriteObjectRequest, Status>> + Unpin + Send,
{
    let _ = tx
        .send(Err(Status::unimplemented(
            "BidiWriteObject requires --cfg google_cloud_unstable_storage_bidi",
        )))
        .await;
}

/// Runs one `BidiWriteObject` session.
#[cfg(google_cloud_unstable_storage_bidi)]
pub async fn run_write_session<S>(
    storage: google_cloud_storage::client::Storage,
    regions: Arc<Registry>,
    peer: (u32, i32),
    inbound: S,
    tx: Tx,
    cfg: WriteSessionConfig,
) where
    S: Stream<Item = Result<pb::BidiWriteObjectRequest, Status>> + Unpin + Send,
{
    if let Err(st) = imp::session(storage, regions, peer, inbound, tx.clone(), cfg).await {
        let _ = tx.send(Err(st)).await;
    }
}

#[cfg(google_cloud_unstable_storage_bidi)]
mod imp {
    use super::*;
    use google_cloud_storage::appendable_object_writer::AppendableObjectWriter;
    use google_cloud_storage::client::Storage;
    use std::sync::atomic::{AtomicUsize, Ordering};
    use tokio_stream::StreamExt;

    fn resp(op_id: u64, msg: Msg) -> pb::BidiWriteObjectResponse {
        pb::BidiWriteObjectResponse {
            msg: Some(msg),
            op_id,
        }
    }

    /// Builds the SDK writer for an `OpenAppendSpec` (create/overwrite or takeover).
    pub(super) async fn open_writer(
        storage: &Storage,
        spec: &pb::OpenAppendSpec,
    ) -> Result<AppendableObjectWriter, Status> {
        if spec.bucket.is_empty() || spec.object.is_empty() {
            return Err(Status::invalid_argument("bucket and object are required"));
        }
        let bucket = bucket_name(&spec.bucket);
        if let Some(g) = spec.reopen_generation {
            let mut b = storage.reopen_appendable_object(bucket, spec.object.clone(), g);
            if !spec.write_handle.is_empty() {
                b = b.set_write_handle(bytes::Bytes::from(spec.write_handle.clone()));
            }
            if !spec.routing_token.is_empty() {
                b = b.set_routing_token(spec.routing_token.clone());
            }
            if let Some(v) = spec.if_metageneration_match {
                b = b.set_if_metageneration_match(v);
            }
            if let Some(v) = spec.if_metageneration_not_match {
                b = b.set_if_metageneration_not_match(v);
            }
            if !spec.quota_project.is_empty() {
                b = b.with_quota_project(spec.quota_project.clone());
            }
            if !spec.user_agent.is_empty() {
                b = b.with_user_agent(spec.user_agent.clone());
            }
            return b.send().await.map_err(to_status);
        }
        let mut b = storage.open_appendable_object(bucket, spec.object.clone());
        if let Some(v) = spec.if_generation_match {
            b = b.set_if_generation_match(v);
        }
        if let Some(v) = spec.if_generation_not_match {
            b = b.set_if_generation_not_match(v);
        }
        if let Some(v) = spec.if_metageneration_match {
            b = b.set_if_metageneration_match(v);
        }
        if let Some(v) = spec.if_metageneration_not_match {
            b = b.set_if_metageneration_not_match(v);
        }
        if !spec.quota_project.is_empty() {
            b = b.with_quota_project(spec.quota_project.clone());
        }
        if !spec.user_agent.is_empty() {
            b = b.with_user_agent(spec.user_agent.clone());
        }
        if let Some(a) = spec.attrs.as_ref() {
            if !a.storage_class.is_empty() {
                b = b.set_storage_class(a.storage_class.clone());
            }
            if !a.content_type.is_empty() {
                b = b.set_content_type(a.content_type.clone());
            }
            if !a.content_encoding.is_empty() {
                b = b.set_content_encoding(a.content_encoding.clone());
            }
            if !a.content_language.is_empty() {
                b = b.set_content_language(a.content_language.clone());
            }
            if !a.content_disposition.is_empty() {
                b = b.set_content_disposition(a.content_disposition.clone());
            }
            if !a.cache_control.is_empty() {
                b = b.set_cache_control(a.cache_control.clone());
            }
            if !a.metadata.is_empty() {
                b = b.set_metadata(a.metadata.clone());
            }
            if !a.kms_key.is_empty() {
                b = b.set_kms_key(a.kms_key.clone());
            }
            if a.custom_time_secs.is_some() || a.custom_time_nanos.is_some() {
                b = b.set_custom_time(google_cloud_wkt::Timestamp::clamp(
                    a.custom_time_secs.unwrap_or(0),
                    a.custom_time_nanos.unwrap_or(0),
                ));
            }
            if !a.contexts_json.is_empty() {
                let ctx: google_cloud_storage::model::ObjectContexts =
                    serde_json::from_slice(&a.contexts_json).map_err(|e| {
                        Status::invalid_argument(format!("invalid contexts_json: {e}"))
                    })?;
                b = b.set_contexts(ctx);
            }
        }
        b.send().await.map_err(to_status)
    }

    /// Forwards released slots (batched) to the client.
    async fn forward_released(
        first: u32,
        rel_rx: &mut mpsc::UnboundedReceiver<u32>,
        tx: &Tx,
    ) -> Result<(), Status> {
        let mut slots = vec![first];
        while slots.len() < 64 {
            match rel_rx.try_recv() {
                Ok(s) => slots.push(s),
                Err(_) => break,
            }
        }
        tx.send(Ok(resp(0, Msg::Released(pb::SlotsReleased { slots }))))
            .await
            .map_err(|_| Status::cancelled("client went away"))
    }

    /// Awaits `fut` while forwarding slot releases to the client.
    async fn drive<F: std::future::Future>(
        fut: F,
        rel_rx: &mut mpsc::UnboundedReceiver<u32>,
        tx: &Tx,
    ) -> Result<F::Output, Status> {
        tokio::pin!(fut);
        loop {
            tokio::select! {
                biased;
                out = &mut fut => return Ok(out),
                Some(s) = rel_rx.recv() => forward_released(s, rel_rx, tx).await?,
            }
        }
    }

    /// Waits (bounded) until every leased slot was dropped by the SDK and flushes the
    /// corresponding `SlotsReleased`, so the client can reuse the region for another writer.
    async fn drain_releases(
        outstanding: &AtomicUsize,
        rel_rx: &mut mpsc::UnboundedReceiver<u32>,
        tx: &Tx,
    ) -> Result<(), Status> {
        let deadline = tokio::time::Instant::now() + RELEASE_DRAIN_TIMEOUT;
        let mut slots = Vec::new();
        loop {
            while let Ok(s) = rel_rx.try_recv() {
                slots.push(s);
            }
            if outstanding.load(Ordering::Acquire) == 0 {
                while let Ok(s) = rel_rx.try_recv() {
                    slots.push(s);
                }
                break;
            }
            if tokio::time::Instant::now() >= deadline {
                tracing::warn!(
                    outstanding = outstanding.load(Ordering::Acquire),
                    "write slots still leased after close; client will discard the region"
                );
                break;
            }
            tokio::select! {
                Some(s) = rel_rx.recv() => slots.push(s),
                _ = tokio::time::sleep(std::time::Duration::from_millis(5)) => {}
            }
        }
        if !slots.is_empty() {
            tx.send(Ok(resp(0, Msg::Released(pb::SlotsReleased { slots }))))
                .await
                .map_err(|_| Status::cancelled("client went away"))?;
        }
        Ok(())
    }

    pub(super) async fn session<S>(
        storage: Storage,
        regions: Arc<Registry>,
        peer: (u32, i32),
        mut inbound: S,
        tx: Tx,
        cfg: WriteSessionConfig,
    ) -> Result<(), Status>
    where
        S: Stream<Item = Result<pb::BidiWriteObjectRequest, Status>> + Unpin + Send,
    {
        let (spec, open_op) = match inbound.next().await {
            Some(Ok(pb::BidiWriteObjectRequest {
                op: Some(Op::Open(spec)),
                op_id,
            })) => (spec, op_id),
            Some(Err(_)) | None => return Ok(()),
            Some(Ok(_)) => {
                return Err(Status::invalid_argument(
                    "the first BidiWriteObject request must be `open`",
                ));
            }
        };
        let claim = if spec.write_region_id != 0 {
            let arena = regions
                .arena(spec.write_region_id, cfg.slot_size, ArenaKind::Write, peer)
                .await?;
            Some(arena.claim_for_writer()?)
        } else {
            None
        };
        let mut writer = open_writer(&storage, &spec).await?;
        // The running CRC32C is authoritative only when the server saw every byte.
        let base_known = spec.reopen_generation.is_none() || writer.persisted_size() == 0;
        let mut crc: u32 = 0;
        tx.send(Ok(resp(
            open_op,
            Msg::Opened(pb::WriteOpened {
                generation: writer.generation(),
                persisted_size: writer.persisted_size(),
            }),
        )))
        .await
        .map_err(|_| Status::cancelled("client went away"))?;

        let (rel_tx, mut rel_rx) = mpsc::unbounded_channel::<u32>();
        let outstanding = Arc::new(AtomicUsize::new(0));

        loop {
            let next = tokio::select! {
                biased;
                Some(s) = rel_rx.recv() => {
                    forward_released(s, &mut rel_rx, &tx).await?;
                    continue;
                }
                m = inbound.next() => m,
            };
            let req = match next {
                // Client half-closed or vanished without Close/Finalize: drop the writer
                // (same as the process exiting with an unclosed GAPIC stream).
                None | Some(Err(_)) => return Ok(()),
                Some(Ok(r)) => r,
            };
            let op_id = req.op_id;
            match req.op {
                Some(Op::Append(a)) => {
                    let data = match (a.slot.as_ref(), claim.as_ref()) {
                        (Some(r), Some(c)) => {
                            c.arena()
                                .lease_for_append(r, cfg.copy_mode, &outstanding, &rel_tx)?
                        }
                        (Some(_), None) => {
                            return Err(Status::failed_precondition(
                                "Append references a slot but the writer has no write region",
                            ));
                        }
                        (None, _) => a.inline_data,
                    };
                    if data.is_empty() {
                        continue;
                    }
                    if base_known {
                        crc = crc32c::crc32c_append(crc, &data);
                    }
                    drive(writer.append(data), &mut rel_rx, &tx)
                        .await?
                        .map_err(to_status)?;
                }
                Some(Op::Flush(_)) => {
                    let ps = drive(writer.flush(), &mut rel_rx, &tx)
                        .await?
                        .map_err(to_status)?;
                    tx.send(Ok(resp(
                        op_id,
                        Msg::Flushed(pb::Flushed { persisted_size: ps }),
                    )))
                    .await
                    .map_err(|_| Status::cancelled("client went away"))?;
                }
                Some(Op::Close(_)) => {
                    let ps = drive(writer.close(), &mut rel_rx, &tx)
                        .await?
                        .map_err(to_status)?;
                    drain_releases(&outstanding, &mut rel_rx, &tx).await?;
                    tx.send(Ok(resp(
                        op_id,
                        Msg::Closed(pb::Closed { persisted_size: ps }),
                    )))
                    .await
                    .map_err(|_| Status::cancelled("client went away"))?;
                    return Ok(());
                }
                Some(Op::Finalize(f)) => {
                    if let (Some(want), true) = (f.full_object_crc32c, base_known)
                        && want != crc
                    {
                        // Keep the object unfinalized (all queued bytes persisted), then fail
                        // exactly like GCS does for a mismatching `object_checksums`.
                        let _ = drive(writer.close(), &mut rel_rx, &tx).await?;
                        drain_releases(&outstanding, &mut rel_rx, &tx).await?;
                        return Err(Status::invalid_argument(format!(
                            "full_object_checksum crc32c mismatch: provided {want:#010x}, \
                             computed {crc:#010x} over the appended bytes"
                        )));
                    }
                    let obj = drive(writer.finalize(), &mut rel_rx, &tx)
                        .await?
                        .map_err(to_status)?;
                    drain_releases(&outstanding, &mut rel_rx, &tx).await?;
                    if let Some(want) = f.full_object_crc32c
                        && !base_known
                    {
                        let got = obj.checksums.as_ref().and_then(|c| c.crc32c);
                        if got != Some(want) {
                            return Err(Status::invalid_argument(format!(
                                "full_object_checksum crc32c mismatch: provided {want:#010x}, \
                                 object finalized with {got:?}"
                            )));
                        }
                    }
                    tx.send(Ok(resp(
                        op_id,
                        Msg::Finalized(pb::Finalized {
                            object: Some(crate::object_meta::object_resource(&obj)),
                        }),
                    )))
                    .await
                    .map_err(|_| Status::cancelled("client went away"))?;
                    return Ok(());
                }
                Some(Op::Open(_)) => {
                    return Err(Status::invalid_argument("writer is already open"));
                }
                None => {}
            }
        }
    }
}
