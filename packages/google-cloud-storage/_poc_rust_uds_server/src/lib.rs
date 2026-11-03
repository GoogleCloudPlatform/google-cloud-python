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

//! Google Cloud Storage Rust core exposed as a gRPC server over a Unix Domain Socket (UDS).
//!
//! Supports all three deployment topologies specified in the GCS SDK Consolidation architecture:
//! 1. **Multi-process shared sidecar daemon (`gcs-core-server`):** A single per-UID daemon process
//!    listening on a `0600` Unix Domain Socket with `SO_PEERCRED` peer-UID authentication,
//!    per-caller OAuth2 token-lending sessions bound to `(uid, pid)`, active-connection reference
//!    counting (`TrackedUnixStream`), dead-PID session/handle reaping, idle timeout eviction,
//!    stale-socket recovery, and an optional Linux `memfd` + `SCM_RIGHTS` shared-memory zero-copy
//!    read data plane.
//! 2. **Per-process `1:1` child sidecar (`--pdeathsig=true`):** Requests `PR_SET_PDEATHSIG(SIGTERM)`
//!    on Linux so the sidecar terminates immediately if its spawning parent process exits.
//! 3. **In-process background server (`gcs_core_start_inproc`):** Spawns the identical `GcsCore`
//!    tonic server inside the caller's OS process on a background Tokio runtime thread.
//!
//! v2 adds zero-copy shared-memory `BidiReadObject` / `BidiWriteObject` sessions
//! ([`bidi_read`], [`bidi_write`]) over slot arenas ([`slots`]) carved out of the same
//! sealed `memfd` regions, plus `GetServerInfo` capability negotiation. All of it uses
//! only public APIs of the unmodified `google-cloud-storage` crate.

pub mod bidi_read;
pub mod bidi_write;
pub mod object_meta;
pub mod service;
pub mod session;
pub mod shm;
pub mod slots;

/// Version of the linked `google-cloud-storage` crate (reported by `GetServerInfo`).
pub const STORAGE_CRATE_VERSION: &str = "1.21.0";

use clap::Parser;
use std::ffi::{CStr, c_char};
use std::path::PathBuf;
use std::pin::Pin;
use std::sync::Arc;
use std::sync::atomic::{AtomicI64, AtomicU64, AtomicUsize, Ordering};
use std::task::{Context, Poll};
use std::time::{Duration, Instant};
use tokio::io::{AsyncRead, AsyncWrite, ReadBuf};
use tokio::net::{UnixListener, UnixStream};
use tokio_stream::StreamExt;
use tokio_stream::wrappers::UnixListenerStream;
use tonic::transport::Server;
use tonic::transport::server::{Connected, UdsConnectInfo};

/// Wrapper around `tokio::net::UnixStream` that decrements `Shared::active_conns`
/// and refreshes `Shared::last_rpc` when a client UDS connection closes (including on `SIGKILL`).
pub struct TrackedUnixStream {
    inner: UnixStream,
    shared: Arc<Shared>,
}

impl Connected for TrackedUnixStream {
    type ConnectInfo = UdsConnectInfo;

    fn connect_info(&self) -> Self::ConnectInfo {
        self.inner.connect_info()
    }
}

impl AsyncRead for TrackedUnixStream {
    fn poll_read(
        mut self: Pin<&mut Self>,
        cx: &mut Context<'_>,
        buf: &mut ReadBuf<'_>,
    ) -> Poll<std::io::Result<()>> {
        Pin::new(&mut self.inner).poll_read(cx, buf)
    }
}

impl AsyncWrite for TrackedUnixStream {
    fn poll_write(
        mut self: Pin<&mut Self>,
        cx: &mut Context<'_>,
        buf: &[u8],
    ) -> Poll<std::io::Result<usize>> {
        Pin::new(&mut self.inner).poll_write(cx, buf)
    }

    fn poll_flush(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<std::io::Result<()>> {
        Pin::new(&mut self.inner).poll_flush(cx)
    }

    fn poll_shutdown(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<std::io::Result<()>> {
        Pin::new(&mut self.inner).poll_shutdown(cx)
    }
}

impl Drop for TrackedUnixStream {
    fn drop(&mut self) {
        self.shared.active_conns.fetch_sub(1, Ordering::Relaxed);
        self.shared.last_rpc.store(now_ms(), Ordering::Relaxed);
    }
}

#[allow(missing_docs, clippy::all)]
pub mod pb {
    include!("generated/protos/gcscore.v1.rs");
}

/// Configuration parameters for the `gcs-core-server` gRPC-over-UDS daemon.
#[derive(Parser, Debug, Clone)]
#[command(version, about = "Google Cloud Storage Rust core gRPC-over-UDS server")]
pub struct Args {
    /// Unix Domain Socket path. Prefix with `@` on Linux to use the abstract socket namespace.
    #[arg(long, default_value = "/tmp/gcs-core.sock")]
    pub socket: String,

    /// Exit after this many seconds with zero active connections and no RPCs (0 = never).
    #[arg(long, default_value_t = 300)]
    pub idle_secs: u64,

    /// Default upstream GCS transport when a request leaves `transport` unspecified (`json` or `grpc`).
    #[arg(long, default_value = "json")]
    pub default_transport: String,

    /// Number of gRPC subchannels to open in the upstream `Storage` pool (0 = available vCPUs, min 4).
    #[arg(long, default_value_t = 0)]
    pub grpc_subchannels: usize,

    /// Linux 1:1 child mode: request `PR_SET_PDEATHSIG(SIGTERM)` when the spawning parent exits.
    /// Defaults to `false` so a shared multi-process daemon survives when the initial spawner exits.
    #[arg(long, default_value_t = false, action = clap::ArgAction::Set)]
    pub pdeathsig: bool,

    /// Enforce `SO_PEERCRED` check rejecting UDS connections from other OS user IDs.
    #[arg(long, default_value_t = true, action = clap::ArgAction::Set)]
    pub peer_uid_check: bool,

    /// Default target bytes per streamed `ReadChunk` message.
    #[arg(long, default_value_t = 2 * 1024 * 1024)]
    pub chunk_size: usize,

    /// Optional explicit GCS endpoint URL (e.g. for `storage-grpc-mock` or local testbench).
    #[arg(long)]
    pub endpoint: Option<String>,

    /// Optional additional TCP listen address (`host:port`) for UDS-vs-TCP microbenchmarks.
    #[arg(long)]
    pub tcp: Option<String>,

    /// Reject data RPCs that do not carry a valid per-caller `x-session` token-lending header.
    #[arg(long, default_value_t = false)]
    pub require_session: bool,

    /// Per-client shared-memory region size served on `<socket>.shm` via `SCM_RIGHTS` (0 = disabled).
    #[arg(long, default_value_t = 256 * 1024 * 1024)]
    pub shm_size: usize,

    /// Slot size used by v2 `BidiReadObject` / `BidiWriteObject` sessions inside SHM regions.
    #[arg(long, default_value_t = slots::DEFAULT_SLOT_SIZE)]
    pub shm_slot_size: usize,

    /// How appended SHM slots are handed to the SDK: `zero-copy` (`Bytes::from_owner`) or
    /// `copy` (memcpy into heap `Bytes`, for untrusted multi-tenant daemons).
    #[arg(long, default_value = "zero-copy")]
    pub write_copy_mode: String,

    /// Maximum number of concurrent SHM regions per client `(uid, pid)` (0 = unlimited).
    #[arg(long, default_value_t = shm::DEFAULT_MAX_REGIONS_PER_PID)]
    pub max_regions_per_pid: usize,
}

impl Default for Args {
    fn default() -> Self {
        Self {
            socket: "/tmp/gcs-core.sock".to_string(),
            idle_secs: 300,
            default_transport: "json".to_string(),
            grpc_subchannels: 0,
            pdeathsig: false,
            peer_uid_check: true,
            chunk_size: 2 * 1024 * 1024,
            endpoint: None,
            tcp: None,
            require_session: false,
            shm_size: 256 * 1024 * 1024,
            shm_slot_size: slots::DEFAULT_SLOT_SIZE,
            write_copy_mode: "zero-copy".to_string(),
            max_regions_per_pid: shm::DEFAULT_MAX_REGIONS_PER_PID,
        }
    }
}

/// Shared server state for activity tracking, connection reference counting, and shutdown coordination.
pub struct Shared {
    pub last_rpc: AtomicI64,
    pub rpcs: AtomicU64,
    pub active_conns: AtomicUsize,
    pub started: Instant,
    shutdown_tx: tokio::sync::watch::Sender<bool>,
}

impl Shared {
    /// Creates a new `Shared` state tracker initialized to the current timestamp.
    pub fn new() -> Arc<Self> {
        let (shutdown_tx, _) = tokio::sync::watch::channel(false);
        Arc::new(Self {
            last_rpc: AtomicI64::new(now_ms()),
            rpcs: AtomicU64::new(0),
            active_conns: AtomicUsize::new(0),
            started: Instant::now(),
            shutdown_tx,
        })
    }

    /// Records an incoming RPC and refreshes the idle timer.
    pub fn touch(&self) {
        self.rpcs.fetch_add(1, Ordering::Relaxed);
        self.last_rpc.store(now_ms(), Ordering::Relaxed);
    }

    /// Signals all server tasks to initiate graceful shutdown.
    pub fn trigger_shutdown(&self) {
        let _ = self.shutdown_tx.send(true);
    }

    /// Waits until graceful shutdown has been triggered.
    pub async fn wait_shutdown(&self) {
        let mut rx = self.shutdown_tx.subscribe();
        let _ = rx.wait_for(|&done| done).await;
    }
}

/// Returns the current Unix epoch timestamp in milliseconds.
pub fn now_ms() -> i64 {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap_or_default()
        .as_millis() as i64
}

/// Binds a Unix Domain Socket listener (supporting both filesystem paths with stale-socket
/// cleanup + `0600` permissions and Linux `@` abstract socket names).
pub fn bind_uds_listener(
    sock: &str,
) -> Result<UnixListener, Box<dyn std::error::Error + Send + Sync>> {
    if let Some(name) = sock.strip_prefix('@') {
        #[cfg(target_os = "linux")]
        {
            use std::os::linux::net::SocketAddrExt;
            let addr = std::os::unix::net::SocketAddr::from_abstract_name(name.as_bytes())?;
            let std_l = std::os::unix::net::UnixListener::bind_addr(&addr)?;
            std_l.set_nonblocking(true)?;
            Ok(UnixListener::from_std(std_l)?)
        }
        #[cfg(not(target_os = "linux"))]
        {
            let _ = name;
            Err("abstract sockets are Linux-only".into())
        }
    } else {
        let p = PathBuf::from(sock);
        if let Ok(meta) = std::fs::symlink_metadata(&p) {
            #[cfg(unix)]
            {
                use std::os::unix::fs::FileTypeExt;
                if !meta.file_type().is_socket() {
                    return Err(format!("refusing to remove non-socket file {sock}").into());
                }
            }
            match std::os::unix::net::UnixStream::connect(&p) {
                Ok(_) => {
                    return Err(format!("another server is already listening on {sock}").into());
                }
                Err(_) => {
                    tracing::warn!("removing stale socket {sock}");
                    std::fs::remove_file(&p)?;
                }
            }
        }
        if let Some(dir) = p.parent()
            && !dir.as_os_str().is_empty()
        {
            std::fs::create_dir_all(dir)?;
        }
        let l = UnixListener::bind(&p)?;
        #[cfg(unix)]
        {
            use std::os::unix::fs::PermissionsExt;
            std::fs::set_permissions(&p, std::fs::Permissions::from_mode(0o600))?;
        }
        Ok(l)
    }
}

/// Runs the `GcsCore` gRPC server until triggered by `Shutdown` RPC, idle timeout, or OS signal.
pub async fn run(args: Args) -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let listener = bind_uds_listener(&args.socket)?;
    let shared = Shared::new();
    #[cfg(unix)]
    {
        let s = shared.clone();
        tokio::spawn(async move {
            if let Ok(mut term) =
                tokio::signal::unix::signal(tokio::signal::unix::SignalKind::terminate())
            {
                tokio::select! {
                    _ = term.recv() => {},
                    _ = tokio::signal::ctrl_c() => {},
                    _ = s.wait_shutdown() => return,
                }
                s.trigger_shutdown();
            }
        });
    }
    eprintln!(
        "gcs-core-server pid={} listening on {}",
        std::process::id(),
        args.socket
    );
    println!("READY {}", args.socket);
    serve_with_listener(args, listener, shared).await
}

/// Serves `GcsCore` on an already-bound `UnixListener`. Used directly by integration tests
/// and in-process server launches.
pub async fn serve_with_listener(
    args: Args,
    listener: UnixListener,
    shared: Arc<Shared>,
) -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let shm = Arc::new(shm::Registry::new());
    if args.shm_size > 0 && !args.socket.starts_with('@') {
        let r = shm.clone();
        let p = format!("{}.shm", args.socket);
        let shm_size = args.shm_size;
        let peer_uid_check = args.peer_uid_check;
        let shm_shared = shared.clone();
        if let Some(dir) = PathBuf::from(&p).parent()
            && !dir.as_os_str().is_empty()
        {
            std::fs::create_dir_all(dir)?;
        }
        tokio::spawn(async move {
            tokio::select! {
                res = r.serve(p, shm_size, peer_uid_check) => {
                    if let Err(e) = res {
                        tracing::error!("shm side channel: {e}");
                    }
                }
                _ = shm_shared.wait_shutdown() => {}
            }
        });
    }

    let svc = service::GcsCoreService::new(&args, shared.clone(), shm).await?;
    let reaper_sessions = svc.sessions();
    let reaper_handles = svc.handles();
    // SAFETY: `getuid()` is always safe to call and cannot fail.
    let my_uid = unsafe { libc::getuid() };
    let peer_check = args.peer_uid_check;

    let auth = move |req: tonic::Request<()>| -> Result<tonic::Request<()>, tonic::Status> {
        if !peer_check {
            return Ok(req);
        }
        match req.extensions().get::<UdsConnectInfo>() {
            Some(info) => match &info.peer_cred {
                Some(c) if c.uid() == my_uid => Ok(req),
                Some(c) => Err(tonic::Status::permission_denied(format!(
                    "peer uid {} != server uid {}",
                    c.uid(),
                    my_uid
                ))),
                None => Err(tonic::Status::permission_denied("no peer credentials")),
            },
            None => Err(tonic::Status::permission_denied(
                "peer uid check requires UDS peer credentials; pass --peer-uid-check=false when using --tcp",
            )),
        }
    };

    let inner = pb::gcs_core_server::GcsCoreServer::new(svc)
        .max_decoding_message_size(64 * 1024 * 1024)
        .max_encoding_message_size(64 * 1024 * 1024);
    let grpc = tonic::service::interceptor::InterceptedService::new(inner, auth);

    {
        let s = shared.clone();
        let idle = (args.idle_secs as i64) * 1000;
        tokio::spawn(async move {
            loop {
                tokio::select! {
                    _ = tokio::time::sleep(Duration::from_secs(1)) => {}
                    _ = s.wait_shutdown() => return,
                }
                let reaped_sessions = reaper_sessions.reap_dead_pids().await;
                let reaped_handles = service::reap_dead_handles(&reaper_handles);
                if reaped_sessions > 0 || reaped_handles > 0 {
                    tracing::info!(
                        reaped_sessions,
                        reaped_handles,
                        "reaped resources from exited client processes"
                    );
                }
                if idle <= 0 {
                    continue;
                }
                if s.active_conns.load(Ordering::Relaxed) > 0 {
                    s.last_rpc.store(now_ms(), Ordering::Relaxed);
                    continue;
                }
                if now_ms() - s.last_rpc.load(Ordering::Relaxed) > idle {
                    tracing::info!(
                        "idle for {}s with 0 active connections, exiting",
                        idle / 1000
                    );
                    s.trigger_shutdown();
                    return;
                }
            }
        });
    }

    let sock = args.socket.clone();
    let uds_shared = shared.clone();
    let conn_shared = shared.clone();
    let uds_grpc = grpc.clone();
    let incoming = UnixListenerStream::new(listener).map(move |res| {
        res.map(|s| {
            conn_shared.active_conns.fetch_add(1, Ordering::Relaxed);
            conn_shared.last_rpc.store(now_ms(), Ordering::Relaxed);
            #[cfg(unix)]
            // SAFETY: `s.as_raw_fd()` is a valid open socket descriptor and `sz` is a properly
            // sized `c_int` buffer for `SO_SNDBUF` / `SO_RCVBUF`.
            unsafe {
                use std::os::unix::io::AsRawFd;
                let fd = s.as_raw_fd();
                let sz: libc::c_int = 8 * 1024 * 1024;
                let _ = libc::setsockopt(
                    fd,
                    libc::SOL_SOCKET,
                    libc::SO_SNDBUF,
                    &sz as *const _ as *const libc::c_void,
                    std::mem::size_of_val(&sz) as libc::socklen_t,
                );
                let _ = libc::setsockopt(
                    fd,
                    libc::SOL_SOCKET,
                    libc::SO_RCVBUF,
                    &sz as *const _ as *const libc::c_void,
                    std::mem::size_of_val(&sz) as libc::socklen_t,
                );
            }
            TrackedUnixStream {
                inner: s,
                shared: conn_shared.clone(),
            }
        })
    });

    let uds = Server::builder()
        .initial_stream_window_size(64 * 1024 * 1024)
        .initial_connection_window_size(256 * 1024 * 1024)
        .max_frame_size(4 * 1024 * 1024)
        .add_service(uds_grpc)
        .serve_with_incoming_shutdown(incoming, async move {
            uds_shared.wait_shutdown().await;
        });

    if let Some(tcp) = args.tcp.clone() {
        let tcp_shared = shared.clone();
        let addr: std::net::SocketAddr = tcp.parse()?;
        let tcp_srv = Server::builder()
            .initial_stream_window_size(64 * 1024 * 1024)
            .initial_connection_window_size(256 * 1024 * 1024)
            .max_frame_size(4 * 1024 * 1024)
            .add_service(grpc)
            .serve_with_shutdown(addr, async move {
                tcp_shared.wait_shutdown().await;
            });
        let (a, b) = tokio::join!(uds, tcp_srv);
        a?;
        b?;
    } else {
        uds.await?;
    }

    if !sock.starts_with('@') {
        let _ = std::fs::remove_file(&sock);
        let _ = std::fs::remove_file(format!("{sock}.shm"));
    }
    Ok(())
}

struct InprocHandle {
    shared: Arc<Shared>,
    join: Option<std::thread::JoinHandle<()>>,
}

static INPROC_SERVERS: std::sync::LazyLock<
    std::sync::Mutex<std::collections::HashMap<String, InprocHandle>>,
> = std::sync::LazyLock::new(|| std::sync::Mutex::new(std::collections::HashMap::new()));

/// C-FFI entry point for launching the gRPC-over-UDS server **in-process** on a background
/// Tokio runtime thread. Returns `0` once the UDS listener is bound and ready to accept connections,
/// or `-1` on error.
///
/// # Safety
/// `socket_path` must be a valid, non-null, NUL-terminated C string pointer.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn gcs_core_start_inproc(socket_path: *const c_char) -> i32 {
    std::panic::catch_unwind(|| {
        if socket_path.is_null() {
            return -1;
        }
        // SAFETY: The caller guarantees `socket_path` is a non-null, NUL-terminated C string.
        let sock = match unsafe { CStr::from_ptr(socket_path) }.to_str() {
            Ok(s) => s.to_owned(),
            Err(_) => return -1,
        };
        let shared = Shared::new();
        let srv_shared = shared.clone();
        let srv_sock = sock.clone();
        let (tx, rx) = std::sync::mpsc::sync_channel::<i32>(1);
        let join = std::thread::spawn(move || {
            let rt = match tokio::runtime::Builder::new_multi_thread()
                .enable_all()
                .thread_name("gcs-core-inproc")
                .build()
            {
                Ok(rt) => rt,
                Err(_) => {
                    let _ = tx.send(-1);
                    return;
                }
            };
            rt.block_on(async move {
                let args = Args {
                    socket: srv_sock,
                    idle_secs: 0,
                    ..Default::default()
                };
                let listener = match bind_uds_listener(&args.socket) {
                    Ok(l) => l,
                    Err(_) => {
                        let _ = tx.send(-1);
                        return;
                    }
                };
                let _ = tx.send(0);
                let _ = serve_with_listener(args, listener, srv_shared).await;
            });
        });
        let rc = rx.recv().unwrap_or(-1);
        if rc == 0 {
            INPROC_SERVERS.lock().unwrap().insert(
                sock,
                InprocHandle {
                    shared,
                    join: Some(join),
                },
            );
        }
        rc
    })
    .unwrap_or(-1)
}

/// C-FFI entry point for stopping an in-process gRPC-over-UDS server previously started via
/// [`gcs_core_start_inproc`] and waiting for its background Tokio runtime thread to exit.
/// Returns `0` on clean shutdown or `-1` if no in-process server was registered for `socket_path`.
///
/// # Safety
/// `socket_path` must be a valid, non-null, NUL-terminated C string pointer.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn gcs_core_stop_inproc(socket_path: *const c_char) -> i32 {
    std::panic::catch_unwind(|| {
        if socket_path.is_null() {
            return -1;
        }
        // SAFETY: The caller guarantees `socket_path` is a non-null, NUL-terminated C string.
        let sock = match unsafe { CStr::from_ptr(socket_path) }.to_str() {
            Ok(s) => s,
            Err(_) => return -1,
        };
        let handle = INPROC_SERVERS.lock().unwrap().remove(sock);
        match handle {
            Some(mut h) => {
                h.shared.trigger_shutdown();
                if let Some(j) = h.join.take() {
                    let _ = j.join();
                }
                0
            }
            None => -1,
        }
    })
    .unwrap_or(-1)
}
