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

//! Shared-memory zero-copy data plane (Linux `memfd_create` + `SCM_RIGHTS` + `mmap`).
//!
//! For each client connection on `<socket>.shm`, the server verifies `SO_PEERCRED`,
//! allocates a sealed anonymous memory file (`memfd_create` with
//! `F_SEAL_SHRINK | F_SEAL_GROW | F_SEAL_SEAL`), `mmap`s it into the server's address
//! space, and sends the file descriptor over the Unix socket via `SCM_RIGHTS` alongside
//! a 16-byte little-endian header `(region_id: u64, size: u64)`. During `ReadObjectShm`,
//! object bytes are written directly into the shared mapping and only `(offset, len)`
//! descriptors travel over gRPC.
//!
//! The v2 `BidiReadObject` / `BidiWriteObject` sessions reuse the same regions but
//! address them as fixed-size slots (see [`crate::slots`]): [`Region::slot_ptr`] gives
//! bounds-checked slot addressing and [`Registry::arena`] lazily binds one
//! [`crate::slots::SlotArena`] per region. Pages are demand-faulted (no `MAP_POPULATE`)
//! so first-touch cgroup attribution holds (read-region pages are charged to the daemon,
//! write-region pages to the client that fills them).

use std::collections::HashMap;
use std::os::fd::{AsRawFd, FromRawFd, OwnedFd};
use std::sync::Arc;
use std::sync::atomic::{AtomicBool, AtomicU64, Ordering, fence};
use tokio::io::AsyncReadExt;
use tokio::net::UnixListener;
use tokio::sync::Mutex;

/// Maximum number of concurrent shared-memory regions retained by the server.
pub const MAX_ACTIVE_REGIONS: usize = 1024;

/// Default maximum number of concurrent regions bound to one `(uid, pid)`.
pub const DEFAULT_MAX_REGIONS_PER_PID: usize = 16;

/// A shared-memory region mapped in both the sidecar and the client process.
pub struct Region {
    pub id: u64,
    pub size: usize,
    pub peer_uid: u32,
    pub peer_pid: i32,
    base: *mut u8,
    in_flight: AtomicBool,
    _fd: OwnedFd,
}

// SAFETY: `Region` owns a kernel-sealed `memfd` mapping (`base..base+size`) that remains valid
// for the lifetime of `Region` until `Drop` calls `munmap`. Concurrent writes are serialized via
// `RegionWriteGuard` (`in_flight` atomic lock) and separated from reads by Acquire/Release fences.
unsafe impl Send for Region {}
// SAFETY: Shared references to `Region` synchronize concurrent access via `in_flight` (`Acquire`/`Release`).
unsafe impl Sync for Region {}

/// RAII guard ensuring at most one concurrent writer operates on a `Region` at a time.
pub struct RegionWriteGuard(Arc<Region>);

impl RegionWriteGuard {
    /// Copies `data` into the shared-memory region at `offset` and issues a release fence
    /// so the written bytes are visible to the client process before the `ShmChunk` descriptor arrives.
    pub fn write_at(&self, offset: usize, data: &[u8]) -> Result<(), String> {
        self.0.write_at(offset, data)
    }
}

impl Drop for RegionWriteGuard {
    fn drop(&mut self) {
        self.0.in_flight.store(false, Ordering::Release);
    }
}

impl Region {
    /// Acquires exclusive write access to this region for an in-flight `ReadObjectShm` stream,
    /// preventing concurrent overlapping writes (data races) on the same region.
    pub fn try_lock_write(self: &Arc<Self>) -> Option<RegionWriteGuard> {
        if self
            .in_flight
            .compare_exchange(false, true, Ordering::Acquire, Ordering::Relaxed)
            .is_ok()
        {
            Some(RegionWriteGuard(self.clone()))
        } else {
            None
        }
    }

    /// Copies `data` into the shared-memory region at `offset`.
    pub fn write_at(&self, offset: usize, data: &[u8]) -> Result<(), String> {
        if offset.saturating_add(data.len()) > self.size {
            return Err(format!(
                "shm region overflow: {}+{} > {}",
                offset,
                data.len(),
                self.size
            ));
        }
        // SAFETY: `offset + data.len() <= self.size` is verified above, `self.base` points to a
        // valid `MAP_SHARED` mapping of `self.size` bytes, and `data` is a separate heap/stack slice
        // that does not overlap with the `memfd` region.
        unsafe {
            std::ptr::copy_nonoverlapping(data.as_ptr(), self.base.add(offset), data.len());
        }
        fence(Ordering::Release);
        Ok(())
    }

    /// Reads a slice copy from `[offset, offset + len)` (used in unit/integration tests).
    pub fn read_at(&self, offset: usize, len: usize) -> Result<Vec<u8>, String> {
        if offset.saturating_add(len) > self.size {
            return Err(format!(
                "shm read out of bounds: {}+{} > {}",
                offset, len, self.size
            ));
        }
        fence(Ordering::Acquire);
        let mut out = vec![0u8; len];
        // SAFETY: `offset + len <= self.size` is verified above, `self.base` points to a valid
        // `MAP_SHARED` mapping of `self.size` bytes, and `out` is a freshly allocated `Vec<u8>`.
        unsafe {
            std::ptr::copy_nonoverlapping(self.base.add(offset), out.as_mut_ptr(), len);
        }
        Ok(out)
    }

    /// Returns a raw pointer to the start of `slot` for `slot_size`-byte slots.
    ///
    /// # Panics
    /// Panics if `(slot + 1) * slot_size` exceeds the region size; callers validate slot
    /// indices against `size / slot_size` before calling.
    pub fn slot_ptr(&self, slot: usize, slot_size: usize) -> *mut u8 {
        let end = slot
            .checked_add(1)
            .and_then(|s| s.checked_mul(slot_size))
            .expect("slot offset overflow");
        assert!(end <= self.size, "slot {slot} out of bounds");
        // SAFETY: `slot * slot_size + slot_size <= self.size` was asserted above, so the
        // resulting pointer stays within the `MAP_SHARED` mapping of `self.size` bytes.
        unsafe { self.base.add(slot * slot_size) }
    }
}

impl Drop for Region {
    fn drop(&mut self) {
        // SAFETY: `self.base` and `self.size` were returned by a successful `libc::mmap` in
        // `Registry::create` and are unmapped exactly once when `Region` is dropped.
        unsafe {
            libc::munmap(self.base as *mut libc::c_void, self.size);
        }
    }
}

/// Registry of active client shared-memory regions.
pub struct Registry {
    regions: Mutex<HashMap<u64, Arc<Region>>>,
    arenas: std::sync::Mutex<HashMap<u64, Arc<crate::slots::SlotArena>>>,
    next: AtomicU64,
    max_per_pid: std::sync::atomic::AtomicUsize,
}

impl Default for Registry {
    fn default() -> Self {
        Self::new()
    }
}

impl Registry {
    /// Creates an empty shared-memory region registry.
    pub fn new() -> Self {
        Self {
            regions: Mutex::new(HashMap::new()),
            arenas: std::sync::Mutex::new(HashMap::new()),
            next: AtomicU64::new(1),
            max_per_pid: std::sync::atomic::AtomicUsize::new(DEFAULT_MAX_REGIONS_PER_PID),
        }
    }

    /// Sets the per-`(uid, pid)` region cap (`0` = unlimited).
    pub fn set_max_regions_per_pid(&self, n: usize) {
        self.max_per_pid.store(n, Ordering::Relaxed);
    }

    /// Number of active regions.
    pub async fn len(&self) -> usize {
        self.regions.lock().await.len()
    }

    /// Returns `true` if no regions are active.
    pub async fn is_empty(&self) -> bool {
        self.regions.lock().await.is_empty()
    }

    /// Returns the slot arena bound to region `id`, creating it with `kind` on first use.
    ///
    /// Verifies that the region is bound to `(uid, pid)` (when `uid != u32::MAX`, i.e. the
    /// caller has kernel-verified peer credentials) and that an existing arena has the same
    /// kind and slot size.
    pub async fn arena(
        &self,
        id: u64,
        slot_size: usize,
        kind: crate::slots::ArenaKind,
        peer: (u32, i32),
    ) -> Result<Arc<crate::slots::SlotArena>, tonic::Status> {
        let reg = self
            .get(id)
            .await
            .ok_or_else(|| tonic::Status::not_found(format!("unknown shm region {id}")))?;
        let (uid, pid) = peer;
        if uid != u32::MAX && (reg.peer_uid != uid || (reg.peer_pid > 0 && reg.peer_pid != pid)) {
            return Err(tonic::Status::permission_denied(
                "shm region is bound to another process",
            ));
        }
        let mut arenas = self.arenas.lock().unwrap();
        if let Some(a) = arenas.get(&id) {
            if a.kind() != kind || a.slot_size() != slot_size {
                return Err(tonic::Status::failed_precondition(format!(
                    "shm region {id} is already bound as a {:?} region",
                    a.kind()
                )));
            }
            return Ok(a.clone());
        }
        let a = Arc::new(crate::slots::SlotArena::new(reg, slot_size, kind)?);
        arenas.insert(id, a.clone());
        Ok(a)
    }

    async fn remove_region(&self, id: u64) {
        self.regions.lock().await.remove(&id);
        self.arenas.lock().unwrap().remove(&id);
    }

    /// Looks up an active shared-memory region by ID.
    pub async fn get(&self, id: u64) -> Option<Arc<Region>> {
        self.regions.lock().await.get(&id).cloned()
    }

    /// Allocates and registers a new sealed `memfd` region of `size` bytes bound to `(peer_uid, peer_pid)`.
    #[cfg(target_os = "linux")]
    pub fn create(
        &self,
        size: usize,
        peer_uid: u32,
        peer_pid: i32,
    ) -> std::io::Result<Arc<Region>> {
        if size == 0 || size > isize::MAX as usize {
            return Err(std::io::Error::new(
                std::io::ErrorKind::InvalidInput,
                "invalid shm region size",
            ));
        }
        let name = std::ffi::CString::new("gcs-core-shm").unwrap();
        // SAFETY: `name.as_ptr()` is a valid NUL-terminated C string.
        let fd = unsafe {
            libc::memfd_create(name.as_ptr(), libc::MFD_CLOEXEC | libc::MFD_ALLOW_SEALING)
        };
        if fd < 0 {
            return Err(std::io::Error::last_os_error());
        }
        // SAFETY: `fd` is a newly created valid file descriptor returned by `memfd_create`.
        let fd = unsafe { OwnedFd::from_raw_fd(fd) };
        // SAFETY: `fd` is a valid open `memfd` and `size <= isize::MAX`.
        if unsafe { libc::ftruncate(fd.as_raw_fd(), size as libc::off_t) } != 0 {
            return Err(std::io::Error::last_os_error());
        }
        // SAFETY: `fd` is a valid `memfd` truncated to `size` bytes; kernel chooses the mapping address.
        let base = unsafe {
            libc::mmap(
                std::ptr::null_mut(),
                size,
                libc::PROT_READ | libc::PROT_WRITE,
                libc::MAP_SHARED,
                fd.as_raw_fd(),
                0,
            )
        };
        if base == libc::MAP_FAILED {
            return Err(std::io::Error::last_os_error());
        }
        // SAFETY: `fd` is a valid `memfd` created with `MFD_ALLOW_SEALING`.
        if unsafe {
            libc::fcntl(
                fd.as_raw_fd(),
                libc::F_ADD_SEALS,
                libc::F_SEAL_SHRINK | libc::F_SEAL_GROW | libc::F_SEAL_SEAL,
            )
        } < 0
        {
            let err = std::io::Error::last_os_error();
            // SAFETY: `base` and `size` came from the successful `mmap` above.
            unsafe {
                libc::munmap(base, size);
            }
            return Err(err);
        }
        let id = self.next.fetch_add(1, Ordering::Relaxed);
        Ok(Arc::new(Region {
            id,
            size,
            peer_uid,
            peer_pid,
            base: base as *mut u8,
            in_flight: AtomicBool::new(false),
            _fd: fd,
        }))
    }

    /// macOS fallback (no `memfd`): `shm_open` a random name with `O_CREAT|O_EXCL`, unlink it
    /// immediately (no filesystem name remains), size it once with `ftruncate` (Darwin
    /// forbids re-truncation, a de-facto seal) and `mmap` it. The fd is still passed via
    /// `SCM_RIGHTS`.
    #[cfg(target_os = "macos")]
    pub fn create(
        &self,
        size: usize,
        peer_uid: u32,
        peer_pid: i32,
    ) -> std::io::Result<Arc<Region>> {
        if size == 0 || size > isize::MAX as usize {
            return Err(std::io::Error::new(
                std::io::ErrorKind::InvalidInput,
                "invalid shm region size",
            ));
        }
        let mut rnd = [0u8; 12];
        std::io::Read::read_exact(&mut std::fs::File::open("/dev/urandom")?, &mut rnd)?;
        let suffix: String = rnd.iter().map(|b| format!("{b:02x}")).collect();
        // 31-character limit on Darwin: "/gcs" + 24 hex chars = 28 chars.
        let name = std::ffi::CString::new(format!("/gcs{suffix}"))
            .map_err(|e| std::io::Error::new(std::io::ErrorKind::InvalidInput, e))?;
        // SAFETY: `name` is a valid NUL-terminated C string; mode is passed as the variadic arg.
        let fd = unsafe {
            libc::shm_open(
                name.as_ptr(),
                libc::O_CREAT | libc::O_EXCL | libc::O_RDWR,
                0o600 as libc::c_uint,
            )
        };
        if fd < 0 {
            return Err(std::io::Error::last_os_error());
        }
        // SAFETY: `fd` is a newly created valid descriptor; `name` is valid.
        let fd = unsafe {
            libc::shm_unlink(name.as_ptr());
            OwnedFd::from_raw_fd(fd)
        };
        // SAFETY: `fd` is a valid open shm object and `size <= isize::MAX`.
        if unsafe { libc::ftruncate(fd.as_raw_fd(), size as libc::off_t) } != 0 {
            return Err(std::io::Error::last_os_error());
        }
        // SAFETY: `fd` is a valid shm object sized to `size` bytes.
        let base = unsafe {
            libc::mmap(
                std::ptr::null_mut(),
                size,
                libc::PROT_READ | libc::PROT_WRITE,
                libc::MAP_SHARED,
                fd.as_raw_fd(),
                0,
            )
        };
        if base == libc::MAP_FAILED {
            return Err(std::io::Error::last_os_error());
        }
        let id = self.next.fetch_add(1, Ordering::Relaxed);
        Ok(Arc::new(Region {
            id,
            size,
            peer_uid,
            peer_pid,
            base: base as *mut u8,
            in_flight: AtomicBool::new(false),
            _fd: fd,
        }))
    }

    #[cfg(not(any(target_os = "linux", target_os = "macos")))]
    pub fn create(
        &self,
        _size: usize,
        _peer_uid: u32,
        _peer_pid: i32,
    ) -> std::io::Result<Arc<Region>> {
        Err(std::io::Error::new(
            std::io::ErrorKind::Unsupported,
            "memfd_create is Linux-only",
        ))
    }

    /// Accepts connections on `path` (`<socket>.shm`), verifies `SO_PEERCRED`, creates a sealed
    /// `memfd` region per connection, sends `(fd, id: u64, size: u64)` via `SCM_RIGHTS`, and
    /// retains the region until the client closes the companion socket.
    pub async fn serve(
        self: Arc<Self>,
        path: String,
        size: usize,
        peer_uid_check: bool,
    ) -> std::io::Result<()> {
        if let Ok(meta) = std::fs::symlink_metadata(&path) {
            #[cfg(unix)]
            {
                use std::os::unix::fs::FileTypeExt;
                if !meta.file_type().is_socket() {
                    return Err(std::io::Error::new(
                        std::io::ErrorKind::AlreadyExists,
                        format!("refusing to remove non-socket file {path}"),
                    ));
                }
            }
            let _ = std::fs::remove_file(&path);
        }
        let listener = UnixListener::bind(&path)?;
        #[cfg(unix)]
        {
            use std::os::unix::fs::PermissionsExt;
            let _ = std::fs::set_permissions(&path, std::fs::Permissions::from_mode(0o600));
        }
        // SAFETY: `getuid()` is always safe to call and cannot fail.
        let my_uid = unsafe { libc::getuid() };
        loop {
            let (stream, _) = listener.accept().await?;
            let (peer_uid, peer_pid) = match stream.peer_cred() {
                Ok(c) => {
                    if peer_uid_check && c.uid() != my_uid {
                        tracing::warn!(
                            "rejecting .shm connection from foreign uid {} != {}",
                            c.uid(),
                            my_uid
                        );
                        continue;
                    }
                    (c.uid(), c.pid().unwrap_or(0))
                }
                Err(e) => {
                    tracing::warn!("rejecting .shm connection without peer_cred: {e}");
                    continue;
                }
            };
            {
                let regions = self.regions.lock().await;
                if regions.len() >= MAX_ACTIVE_REGIONS {
                    tracing::warn!("rejecting .shm connection: MAX_ACTIVE_REGIONS reached");
                    continue;
                }
                let cap = self.max_per_pid.load(Ordering::Relaxed);
                if cap > 0
                    && regions
                        .values()
                        .filter(|r| r.peer_uid == peer_uid && r.peer_pid == peer_pid)
                        .count()
                        >= cap
                {
                    tracing::warn!(
                        peer_pid,
                        cap,
                        "rejecting .shm connection: per-process region cap reached"
                    );
                    continue;
                }
            }
            let reg = match self.create(size, peer_uid, peer_pid) {
                Ok(r) => r,
                Err(e) => {
                    tracing::error!("memfd: {e}");
                    continue;
                }
            };
            let mut payload = [0u8; 16];
            payload[..8].copy_from_slice(&reg.id.to_le_bytes());
            payload[8..].copy_from_slice(&(reg.size as u64).to_le_bytes());
            if let Err(e) = send_fd(stream.as_raw_fd(), reg._fd.as_raw_fd(), &payload) {
                tracing::error!("sendmsg SCM_RIGHTS: {e}");
                continue;
            }
            self.regions.lock().await.insert(reg.id, reg.clone());
            let me = self.clone();
            let mut stream = stream;
            tokio::spawn(async move {
                let mut b = [0u8; 1];
                let _ = stream.read(&mut b).await;
                let id = reg.id;
                drop(reg);
                me.remove_region(id).await;
            });
        }
    }
}

fn send_fd(sock: i32, fd: i32, payload: &[u8]) -> std::io::Result<()> {
    // SAFETY: `iov` references `payload` for the duration of `sendmsg`; `buf` is `u64`-aligned
    // and sized via `CMSG_SPACE` to hold one `i32` file descriptor in `SCM_RIGHTS`.
    unsafe {
        let mut iov = libc::iovec {
            iov_base: payload.as_ptr() as *mut libc::c_void,
            iov_len: payload.len(),
        };
        let space = libc::CMSG_SPACE(std::mem::size_of::<i32>() as u32) as usize;
        let mut buf = vec![0u64; space.div_ceil(std::mem::size_of::<u64>())];
        let mut msg: libc::msghdr = std::mem::zeroed();
        msg.msg_iov = &mut iov;
        msg.msg_iovlen = 1;
        msg.msg_control = buf.as_mut_ptr() as *mut libc::c_void;
        msg.msg_controllen = space as _;
        let cmsg = libc::CMSG_FIRSTHDR(&msg);
        (*cmsg).cmsg_level = libc::SOL_SOCKET;
        (*cmsg).cmsg_type = libc::SCM_RIGHTS;
        (*cmsg).cmsg_len = libc::CMSG_LEN(std::mem::size_of::<i32>() as u32) as _;
        std::ptr::copy_nonoverlapping(
            &fd as *const i32 as *const u8,
            libc::CMSG_DATA(cmsg),
            std::mem::size_of::<i32>(),
        );
        loop {
            let n = libc::sendmsg(sock, &msg, libc::MSG_NOSIGNAL);
            if n >= 0 {
                break;
            }
            let err = std::io::Error::last_os_error();
            if err.kind() != std::io::ErrorKind::Interrupted {
                return Err(err);
            }
        }
    }
    Ok(())
}

#[cfg(all(test, target_os = "linux"))]
mod tests {
    use super::*;
    use crate::slots::ArenaKind;

    #[tokio::test]
    async fn arena_binding_is_per_process_and_per_kind() {
        let reg = Registry::new();
        let r = reg.create(8 * 1024, 1000, 42).unwrap();
        let id = r.id;
        reg.regions.lock().await.insert(id, r.clone());
        // Foreign pid / uid -> PERMISSION_DENIED.
        let err = reg
            .arena(id, 1024, ArenaKind::Read, (1000, 43))
            .await
            .unwrap_err();
        assert_eq!(err.code(), tonic::Code::PermissionDenied);
        let err = reg
            .arena(id, 1024, ArenaKind::Read, (1001, 42))
            .await
            .unwrap_err();
        assert_eq!(err.code(), tonic::Code::PermissionDenied);
        // Owner gets the same arena on every call; a different kind is rejected.
        let a = reg
            .arena(id, 1024, ArenaKind::Read, (1000, 42))
            .await
            .unwrap();
        let b = reg
            .arena(id, 1024, ArenaKind::Read, (1000, 42))
            .await
            .unwrap();
        assert!(Arc::ptr_eq(&a, &b));
        assert_eq!(a.len(), 8);
        let err = reg
            .arena(id, 1024, ArenaKind::Write, (1000, 42))
            .await
            .unwrap_err();
        assert_eq!(err.code(), tonic::Code::FailedPrecondition);
        // Unknown region -> NOT_FOUND; removal drops the arena too.
        assert_eq!(
            reg.arena(id + 1, 1024, ArenaKind::Read, (1000, 42))
                .await
                .unwrap_err()
                .code(),
            tonic::Code::NotFound
        );
        reg.remove_region(id).await;
        assert!(reg.is_empty().await);
        assert!(reg.arenas.lock().unwrap().is_empty());
        // The mapping outlives the registry entry while an arena/lease still holds it.
        assert_eq!(a.slot_size(), 1024);
    }

    #[test]
    fn slot_ptr_bounds() {
        let reg = Registry::new();
        let r = reg.create(4096, 1, 1).unwrap();
        let p0 = r.slot_ptr(0, 1024);
        let p3 = r.slot_ptr(3, 1024);
        assert_eq!(p3 as usize - p0 as usize, 3 * 1024);
        let res = std::panic::catch_unwind(std::panic::AssertUnwindSafe(|| r.slot_ptr(4, 1024)));
        assert!(res.is_err(), "out-of-bounds slot must panic");
    }
}
