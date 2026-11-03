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

//! Shared-memory slot arenas for the v2 `BidiReadObject` / `BidiWriteObject` sessions.
//!
//! A sealed `memfd` region (see [`crate::shm`]) is divided into fixed-size slots
//! (2 MiB by default, matching the Rust SDK's `MAX_WRITE_CHUNK_SIZE`). All slot
//! ownership state lives in private Rust heap memory (never in the client-writable
//! shared mapping), and every transition is a `compare_exchange(AcqRel)`:
//!
//! * **Reads** (server allocates, client releases):
//!   `FREE -> SERVER_WRITING -> CLIENT_READING -> FREE` (the last edge on `ReleaseSlots`).
//! * **Writes** (client allocates, server releases):
//!   `FREE -> LEASED -> FREE`. A leased slot is wrapped with
//!   [`bytes::Bytes::from_owner`] around a [`SlotLease`]; the slot only returns to
//!   `FREE` (and is reported back to the client in `SlotsReleased`) when the LAST
//!   `Bytes` clone/slice held by the SDK's coalescing / replay buffers is dropped.

use crate::pb;
use crate::shm::Region;
use bytes::Bytes;
use std::collections::HashSet;
use std::sync::atomic::{AtomicBool, AtomicU8, AtomicUsize, Ordering, fence};
use std::sync::{Arc, Mutex};
use tokio::sync::{Semaphore, mpsc};
use tonic::Status;

/// Slot is unused and owned by the allocator.
pub const FREE: u8 = 0;
/// Read path: the server is copying object bytes into the slot.
pub const SERVER_WRITING: u8 = 1;
/// Read path: the slot was published to the client and awaits `ReleaseSlots`.
pub const CLIENT_READING: u8 = 2;
/// Write path: the slot is owned by the SDK (via `Bytes::from_owner(SlotLease)`).
pub const LEASED: u8 = 3;

/// Default slot size (2 MiB == google-cloud-storage `MAX_WRITE_CHUNK_SIZE`).
pub const DEFAULT_SLOT_SIZE: usize = 2 * 1024 * 1024;

/// How appended SHM slots are handed to the SDK.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Default)]
pub enum WriteCopyMode {
    /// `Bytes::from_owner(SlotLease)`: zero copies between SHM and the SDK.
    #[default]
    ZeroCopy,
    /// `Bytes::copy_from_slice`: one memcpy SHM -> heap; the slot is released immediately.
    /// Recommended for untrusted multi-tenant daemons.
    Copy,
}

impl std::str::FromStr for WriteCopyMode {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "zero-copy" | "zerocopy" => Ok(Self::ZeroCopy),
            "copy" => Ok(Self::Copy),
            other => Err(format!("unknown write copy mode {other:?}")),
        }
    }
}

/// What an arena is used for. A region is bound to exactly one use for its lifetime.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum ArenaKind {
    /// Server-allocated read slot ring (shared by all read sessions of one client process).
    Read,
    /// Client-allocated write slots (owned by exactly one writer session at a time).
    Write,
}

/// Channel used by [`SlotLease::drop`] to report released write slots.
pub type ReleaseTx = mpsc::UnboundedSender<u32>;

/// A fixed-size slot allocator over one shared-memory region.
pub struct SlotArena {
    region: Arc<Region>,
    slot_size: usize,
    n: u32,
    kind: ArenaKind,
    sem: Arc<Semaphore>,
    state: Box<[AtomicU8]>,
    write_claimed: AtomicBool,
}

impl std::fmt::Debug for SlotArena {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("SlotArena")
            .field("region", &self.region.id)
            .field("slot_size", &self.slot_size)
            .field("n", &self.n)
            .field("kind", &self.kind)
            .finish()
    }
}

impl SlotArena {
    /// Creates an arena over `region` with `slot_size`-byte slots.
    pub fn new(region: Arc<Region>, slot_size: usize, kind: ArenaKind) -> Result<Self, Status> {
        if slot_size == 0 {
            return Err(Status::invalid_argument("slot size must be > 0"));
        }
        let n = region.size / slot_size;
        if n == 0 {
            return Err(Status::failed_precondition(format!(
                "shm region of {} bytes is smaller than one {slot_size}-byte slot",
                region.size
            )));
        }
        let n = u32::try_from(n).map_err(|_| Status::invalid_argument("too many slots"))?;
        let state = (0..n).map(|_| AtomicU8::new(FREE)).collect::<Vec<_>>();
        Ok(Self {
            region,
            slot_size,
            n,
            kind,
            sem: Arc::new(Semaphore::new(n as usize)),
            state: state.into_boxed_slice(),
            write_claimed: AtomicBool::new(false),
        })
    }

    /// The id of the underlying region.
    pub fn region_id(&self) -> u64 {
        self.region.id
    }

    /// The `(uid, pid)` the underlying region is bound to.
    pub fn owner(&self) -> (u32, i32) {
        (self.region.peer_uid, self.region.peer_pid)
    }

    /// Number of slots.
    pub fn len(&self) -> u32 {
        self.n
    }

    /// Returns `true` if the arena has no slots (never true for a constructed arena).
    pub fn is_empty(&self) -> bool {
        self.n == 0
    }

    /// Slot size in bytes.
    pub fn slot_size(&self) -> usize {
        self.slot_size
    }

    /// The arena kind.
    pub fn kind(&self) -> ArenaKind {
        self.kind
    }

    /// Returns the current state of `slot` (test/diagnostic helper).
    pub fn slot_state(&self, slot: u32) -> Option<u8> {
        self.state
            .get(slot as usize)
            .map(|s| s.load(Ordering::Acquire))
    }

    /// Number of slots currently `FREE`.
    pub fn free_slots(&self) -> usize {
        self.state
            .iter()
            .filter(|s| s.load(Ordering::Acquire) == FREE)
            .count()
    }

    fn cas(&self, slot: u32, from: u8, to: u8) -> bool {
        self.state[slot as usize]
            .compare_exchange(from, to, Ordering::AcqRel, Ordering::Acquire)
            .is_ok()
    }

    fn slot_ptr(&self, slot: u32) -> *mut u8 {
        debug_assert!(slot < self.n);
        // `slot < n` and `n * slot_size <= region.size` (by construction).
        self.region.slot_ptr(slot as usize, self.slot_size)
    }

    // ------------------------------------------------------------------ reads

    /// Acquires a free slot for the server to write into (read path). Waits (fairly)
    /// for the client to release slots when the ring is exhausted.
    pub async fn acquire(self: &Arc<Self>) -> Result<ReadSlot, Status> {
        if self.kind != ArenaKind::Read {
            return Err(Status::failed_precondition("not a read arena"));
        }
        let permit = self
            .sem
            .clone()
            .acquire_owned()
            .await
            .map_err(|_| Status::cancelled("read arena closed"))?;
        for i in 0..self.n {
            if self.cas(i, FREE, SERVER_WRITING) {
                // Ownership of the permit moves into the slot state machine; it is
                // returned by `release_from_client` or `ReadSlot::drop`.
                permit.forget();
                return Ok(ReadSlot {
                    arena: self.clone(),
                    slot: i,
                    published: false,
                });
            }
        }
        // Unreachable when the semaphore and state are consistent.
        Err(Status::internal("slot semaphore/state mismatch"))
    }

    /// Client returned a published read slot (`CLIENT_READING -> FREE`).
    pub fn release_from_client(&self, slot: u32) -> Result<(), Status> {
        if self.kind != ArenaKind::Read {
            return Err(Status::failed_precondition("not a read arena"));
        }
        if slot >= self.n {
            return Err(Status::invalid_argument(format!(
                "slot {slot} out of range"
            )));
        }
        if !self.cas(slot, CLIENT_READING, FREE) {
            return Err(Status::failed_precondition(format!(
                "slot {slot} released twice or never published"
            )));
        }
        self.sem.add_permits(1);
        Ok(())
    }

    // ----------------------------------------------------------------- writes

    /// Claims exclusive use of a write arena for one writer session.
    pub fn claim_for_writer(self: &Arc<Self>) -> Result<WriterClaim, Status> {
        if self.kind != ArenaKind::Write {
            return Err(Status::failed_precondition(
                "shm region is already used as a read region",
            ));
        }
        if self
            .write_claimed
            .compare_exchange(false, true, Ordering::AcqRel, Ordering::Acquire)
            .is_err()
        {
            return Err(Status::failed_precondition(
                "shm write region is already in use by another writer",
            ));
        }
        Ok(WriterClaim {
            arena: self.clone(),
        })
    }

    /// Validates a client `ShmSlotRef` and wraps the slot in a `Bytes` (write path).
    ///
    /// In [`WriteCopyMode::ZeroCopy`] the returned `Bytes` borrows the SHM slot through a
    /// [`SlotLease`] (`FREE -> LEASED`); the slot is released when the last clone drops.
    /// In [`WriteCopyMode::Copy`] the bytes are copied and the slot is released immediately.
    pub fn lease_for_append(
        self: &Arc<Self>,
        r: &pb::ShmSlotRef,
        mode: WriteCopyMode,
        outstanding: &Arc<AtomicUsize>,
        tx: &ReleaseTx,
    ) -> Result<Bytes, Status> {
        if self.kind != ArenaKind::Write {
            return Err(Status::failed_precondition("not a write arena"));
        }
        if r.region_id != self.region.id {
            return Err(Status::permission_denied(
                "slot references a region not bound to this writer",
            ));
        }
        if r.slot >= self.n {
            return Err(Status::invalid_argument(format!(
                "slot {} out of range (n={})",
                r.slot, self.n
            )));
        }
        let len = r.length as usize;
        if len == 0 || len > self.slot_size {
            return Err(Status::invalid_argument(format!(
                "slot length {len} must be in 1..={}",
                self.slot_size
            )));
        }
        if !self.cas(r.slot, FREE, LEASED) {
            return Err(Status::failed_precondition(format!(
                "slot {} submitted while still leased",
                r.slot
            )));
        }
        // Pair with the client's writes into the slot (published before the UDS message).
        fence(Ordering::Acquire);
        match mode {
            WriteCopyMode::Copy => {
                // SAFETY: `slot < n`, `len <= slot_size`, so `[ptr, ptr+len)` is inside the
                // live `MAP_SHARED` mapping owned by `self.region` (kept alive by `self`).
                let data = unsafe { std::slice::from_raw_parts(self.slot_ptr(r.slot), len) };
                let b = Bytes::copy_from_slice(data);
                let _ = self.cas(r.slot, LEASED, FREE);
                let _ = tx.send(r.slot);
                Ok(b)
            }
            WriteCopyMode::ZeroCopy => {
                outstanding.fetch_add(1, Ordering::AcqRel);
                Ok(Bytes::from_owner(SlotLease {
                    arena: self.clone(),
                    slot: r.slot,
                    len,
                    outstanding: outstanding.clone(),
                    release_tx: tx.clone(),
                }))
            }
        }
    }
}

/// A read slot being filled by the server.
pub struct ReadSlot {
    arena: Arc<SlotArena>,
    slot: u32,
    published: bool,
}

impl ReadSlot {
    /// The slot index.
    pub fn slot(&self) -> u32 {
        self.slot
    }

    /// Copies `data` into the slot and issues a release fence so the bytes are visible
    /// to the client before the `RangeData` descriptor is sent.
    pub fn write(&mut self, data: &[u8]) -> Result<(), Status> {
        if data.len() > self.arena.slot_size {
            return Err(Status::internal("chunk larger than slot"));
        }
        // SAFETY: `slot < n` and `data.len() <= slot_size`, so the destination lies inside the
        // live mapping; `data` is a heap buffer that never overlaps the memfd mapping. The slot
        // is in `SERVER_WRITING`, so the client never reads it concurrently (well-behaved peer).
        unsafe {
            std::ptr::copy_nonoverlapping(
                data.as_ptr(),
                self.arena.slot_ptr(self.slot),
                data.len(),
            );
        }
        fence(Ordering::Release);
        Ok(())
    }

    /// Publishes the slot to the client (`SERVER_WRITING -> CLIENT_READING`).
    pub fn publish(mut self) -> u32 {
        let ok = self.arena.cas(self.slot, SERVER_WRITING, CLIENT_READING);
        debug_assert!(ok);
        self.published = true;
        self.slot
    }
}

impl Drop for ReadSlot {
    fn drop(&mut self) {
        if !self.published && self.arena.cas(self.slot, SERVER_WRITING, FREE) {
            self.arena.sem.add_permits(1);
        }
    }
}

/// Exclusive claim of a write arena by one writer session (released on drop).
pub struct WriterClaim {
    arena: Arc<SlotArena>,
}

impl WriterClaim {
    /// The claimed arena.
    pub fn arena(&self) -> &Arc<SlotArena> {
        &self.arena
    }
}

impl Drop for WriterClaim {
    fn drop(&mut self) {
        self.arena.write_claimed.store(false, Ordering::Release);
    }
}

/// `Bytes` owner for a leased write slot; releases the slot when the last clone drops.
pub struct SlotLease {
    arena: Arc<SlotArena>,
    slot: u32,
    len: usize,
    outstanding: Arc<AtomicUsize>,
    release_tx: ReleaseTx,
}

impl AsRef<[u8]> for SlotLease {
    fn as_ref(&self) -> &[u8] {
        // SAFETY: the slot is `LEASED`, `len <= slot_size` and `slot < n` were validated in
        // `lease_for_append`, and `self.arena` keeps the `Region` (and thus the mapping) alive.
        // A well-behaved client never writes a leased slot (it waits for `SlotsReleased`); a
        // misbehaving same-UID client can only corrupt its own upload bytes (plain `u8`).
        unsafe { std::slice::from_raw_parts(self.arena.slot_ptr(self.slot), self.len) }
    }
}

impl Drop for SlotLease {
    fn drop(&mut self) {
        if self.arena.cas(self.slot, LEASED, FREE) {
            let _ = self.release_tx.send(self.slot);
        }
        self.outstanding.fetch_sub(1, Ordering::AcqRel);
    }
}

/// Tracks read slots published to one session so they can be validated on release
/// and reclaimed when the session ends.
#[derive(Default)]
pub struct PublishedSlots {
    inner: Mutex<HashSet<u32>>,
}

impl PublishedSlots {
    /// Records a published slot.
    pub fn insert(&self, slot: u32) {
        self.inner.lock().unwrap().insert(slot);
    }

    /// Removes a slot; returns `false` if the slot was not published to this session.
    pub fn remove(&self, slot: u32) -> bool {
        self.inner.lock().unwrap().remove(&slot)
    }

    /// Drains all outstanding slots.
    pub fn drain(&self) -> Vec<u32> {
        self.inner.lock().unwrap().drain().collect()
    }

    /// Number of outstanding slots.
    pub fn len(&self) -> usize {
        self.inner.lock().unwrap().len()
    }

    /// Returns `true` if no slots are outstanding.
    pub fn is_empty(&self) -> bool {
        self.len() == 0
    }
}

#[cfg(all(test, target_os = "linux"))]
mod tests {
    use super::*;
    use crate::shm::Registry;

    fn region(size: usize) -> Arc<Region> {
        let reg = Registry::new();
        reg.create(size, 1000, 42).expect("memfd region")
    }

    #[tokio::test]
    async fn read_slot_state_machine() {
        let arena = Arc::new(SlotArena::new(region(4 * 1024), 1024, ArenaKind::Read).unwrap());
        assert_eq!(arena.len(), 4);
        let mut s = arena.acquire().await.unwrap();
        s.write(b"hello").unwrap();
        let slot = s.publish();
        assert_eq!(arena.slot_state(slot), Some(CLIENT_READING));
        arena.release_from_client(slot).unwrap();
        assert_eq!(arena.slot_state(slot), Some(FREE));
        // Double release is rejected.
        assert_eq!(
            arena.release_from_client(slot).unwrap_err().code(),
            tonic::Code::FailedPrecondition
        );
        assert_eq!(
            arena.release_from_client(99).unwrap_err().code(),
            tonic::Code::InvalidArgument
        );
        // Dropping an unpublished slot returns it to the pool.
        {
            let _s = arena.acquire().await.unwrap();
            assert_eq!(arena.free_slots(), 3);
        }
        assert_eq!(arena.free_slots(), 4);
    }

    #[tokio::test]
    async fn read_acquire_waits_for_release() {
        let arena = Arc::new(SlotArena::new(region(2 * 1024), 1024, ArenaKind::Read).unwrap());
        let a = arena.acquire().await.unwrap().publish();
        let _b = arena.acquire().await.unwrap().publish();
        let a2 = arena.clone();
        let waiter = tokio::spawn(async move { a2.acquire().await.map(|s| s.slot()) });
        tokio::time::sleep(std::time::Duration::from_millis(20)).await;
        assert!(!waiter.is_finished());
        arena.release_from_client(a).unwrap();
        assert_eq!(waiter.await.unwrap().unwrap(), a);
    }

    #[test]
    fn write_lease_released_only_after_last_clone() {
        let reg = region(4 * 1024);
        let rid = reg.id;
        let arena = Arc::new(SlotArena::new(reg, 1024, ArenaKind::Write).unwrap());
        let _claim = arena.claim_for_writer().unwrap();
        assert!(arena.claim_for_writer().is_err(), "second writer rejected");
        let (tx, mut rx) = mpsc::unbounded_channel();
        let outstanding = Arc::new(AtomicUsize::new(0));
        let r = pb::ShmSlotRef {
            region_id: rid,
            slot: 1,
            length: 10,
        };
        let b = arena
            .lease_for_append(&r, WriteCopyMode::ZeroCopy, &outstanding, &tx)
            .unwrap();
        assert_eq!(b.len(), 10);
        assert_eq!(arena.slot_state(1), Some(LEASED));
        // Duplicate submission of a leased slot is rejected.
        assert_eq!(
            arena
                .lease_for_append(&r, WriteCopyMode::ZeroCopy, &outstanding, &tx)
                .unwrap_err()
                .code(),
            tonic::Code::FailedPrecondition
        );
        let slice = b.slice(2..5);
        let clone = b.clone();
        drop(b);
        drop(clone);
        assert_eq!(arena.slot_state(1), Some(LEASED), "slice still alive");
        assert!(rx.try_recv().is_err());
        drop(slice);
        assert_eq!(arena.slot_state(1), Some(FREE));
        assert_eq!(rx.try_recv().unwrap(), 1);
        assert_eq!(outstanding.load(Ordering::Acquire), 0);
    }

    #[test]
    fn write_lease_validation_and_copy_mode() {
        let reg = region(4 * 1024);
        let rid = reg.id;
        let arena = Arc::new(SlotArena::new(reg, 1024, ArenaKind::Write).unwrap());
        let (tx, mut rx) = mpsc::unbounded_channel();
        let outstanding = Arc::new(AtomicUsize::new(0));
        let bad = |slot, length, region_id| pb::ShmSlotRef {
            region_id,
            slot,
            length,
        };
        let code = |r: pb::ShmSlotRef| {
            arena
                .lease_for_append(&r, WriteCopyMode::ZeroCopy, &outstanding, &tx)
                .unwrap_err()
                .code()
        };
        assert_eq!(code(bad(9, 1, rid)), tonic::Code::InvalidArgument);
        assert_eq!(code(bad(0, 0, rid)), tonic::Code::InvalidArgument);
        assert_eq!(code(bad(0, 1025, rid)), tonic::Code::InvalidArgument);
        assert_eq!(code(bad(0, 1, rid + 100)), tonic::Code::PermissionDenied);
        let b = arena
            .lease_for_append(&bad(2, 7, rid), WriteCopyMode::Copy, &outstanding, &tx)
            .unwrap();
        assert_eq!(b.len(), 7);
        assert_eq!(
            arena.slot_state(2),
            Some(FREE),
            "copy mode releases at once"
        );
        assert_eq!(rx.try_recv().unwrap(), 2);
        // A read arena cannot be used for writes and vice versa.
        let ra = Arc::new(SlotArena::new(region(2048), 1024, ArenaKind::Read).unwrap());
        assert!(ra.claim_for_writer().is_err());
        assert!(arena.release_from_client(0).is_err());
    }
}
