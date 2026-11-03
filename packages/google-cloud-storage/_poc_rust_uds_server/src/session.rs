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

//! Per-caller credential sessions.
//!
//! Host applications lend short-lived OAuth2 access tokens (never private key files)
//! over the Unix Domain Socket. The server constructs a dedicated `Storage` and
//! `StorageControl` client per session backed by a dynamic `CredentialsProvider`
//! (`LentToken`) and binds the session ID to the caller's kernel-verified `(uid, pid)`
//! obtained via `SO_PEERCRED`.
//!
//! v2 adds (additively) shared sessions: when a caller asks for anonymous access or for
//! the daemon's own Application Default Credentials against a specific endpoint /
//! universe domain, all such sessions share ONE cached `Storage` per
//! `(endpoint, universe_domain, anonymous)` key (one warm gRPC subchannel pool).

use google_cloud_auth::credentials::{
    CacheableResource, Credentials, CredentialsProvider, EntityTag,
};
use google_cloud_storage::client::{Storage, StorageControl};
use http::{HeaderMap, HeaderValue};
use std::collections::HashMap;
use std::sync::{Arc, RwLock};
use tokio::sync::Mutex;

/// Serves `Authorization: Bearer <token>` (and optional `x-goog-user-project`)
/// from an in-memory cell refreshed by the host application via `UpdateToken`.
#[derive(Debug)]
pub struct LentToken {
    inner: RwLock<(String, i64, EntityTag)>,
    quota_project: Option<String>,
}

impl LentToken {
    /// Creates a new `LentToken` with the initial bearer token, expiry timestamp, and optional quota project.
    pub fn new(token: String, expiry: i64, quota_project: Option<String>) -> Self {
        Self {
            inner: RwLock::new((token, expiry, EntityTag::new())),
            quota_project,
        }
    }

    /// Atomically updates the bearer token and expiry timestamp, generating a new `EntityTag`.
    pub fn set(&self, token: String, expiry: i64) {
        *self.inner.write().unwrap() = (token, expiry, EntityTag::new());
    }

    /// Returns the Unix epoch expiry timestamp (in seconds) of the current token.
    pub fn expiry(&self) -> i64 {
        self.inner.read().unwrap().1
    }
}

impl CredentialsProvider for LentToken {
    async fn headers(
        &self,
        extensions: http::Extensions,
    ) -> std::result::Result<
        CacheableResource<HeaderMap>,
        google_cloud_auth::errors::CredentialsError,
    > {
        let (tok, exp, tag) = {
            let g = self.inner.read().unwrap();
            (g.0.clone(), g.1, g.2.clone())
        };
        if exp > 0 && exp < crate::now_ms() / 1000 {
            return Err(google_cloud_auth::errors::CredentialsError::from_msg(
                false,
                "lent token expired; caller must invoke UpdateToken",
            ));
        }
        if let Some(t) = extensions.get::<EntityTag>()
            && *t == tag
        {
            return Ok(CacheableResource::NotModified);
        }
        let mut h = HeaderMap::new();
        let mut v = HeaderValue::from_str(&format!("Bearer {tok}"))
            .map_err(|e| google_cloud_auth::errors::CredentialsError::from_source(false, e))?;
        v.set_sensitive(true);
        h.insert(http::header::AUTHORIZATION, v);
        if let Some(qp) = &self.quota_project {
            let qv = HeaderValue::from_str(qp)
                .map_err(|e| google_cloud_auth::errors::CredentialsError::from_source(false, e))?;
            h.insert(
                http::header::HeaderName::from_static("x-goog-user-project"),
                qv,
            );
        }
        Ok(CacheableResource::New {
            entity_tag: tag,
            data: h,
        })
    }

    async fn universe_domain(&self) -> Option<String> {
        None
    }
}

/// An authenticated caller session bound to `(peer_uid, peer_pid)`.
pub struct Session {
    pub id: String,
    pub peer_uid: u32,
    pub peer_pid: i32,
    pub token: Arc<LentToken>,
    pub storage: Storage,
    pub control: StorageControl,
}

/// Cache key for shared (non-token-lending) clients: `(endpoint, universe_domain, anonymous)`.
pub type SharedKey = (Option<String>, Option<String>, bool);

/// Registry of active caller sessions.
pub struct Sessions {
    map: Mutex<HashMap<String, Arc<Session>>>,
    endpoint: Option<String>,
    subchannels: usize,
    shared: Mutex<HashMap<SharedKey, (Storage, StorageControl)>>,
}

fn random_id() -> Result<String, String> {
    let mut b = [0u8; 32];
    #[cfg(target_os = "linux")]
    {
        // SAFETY: `b` is a valid mutable stack buffer of `b.len()` bytes.
        let rc = unsafe { libc::getrandom(b.as_mut_ptr() as *mut libc::c_void, b.len(), 0) };
        if rc != b.len() as isize {
            return Err(std::io::Error::last_os_error().to_string());
        }
    }
    #[cfg(not(target_os = "linux"))]
    {
        std::fs::File::open("/dev/urandom")
            .and_then(|mut f| std::io::Read::read_exact(&mut f, &mut b))
            .map_err(|e| e.to_string())?;
    }
    Ok(b.iter().map(|x| format!("{x:02x}")).collect())
}

impl Sessions {
    /// Creates a new session registry.
    pub fn new(endpoint: Option<String>, subchannels: usize) -> Self {
        Self {
            map: Mutex::new(HashMap::new()),
            endpoint,
            subchannels,
            shared: Mutex::new(HashMap::new()),
        }
    }

    /// Returns (building on first use) the shared clients for `key`.
    pub async fn shared_clients(
        &self,
        key: &SharedKey,
    ) -> Result<(Storage, StorageControl), String> {
        let mut cache = self.shared.lock().await;
        if let Some(c) = cache.get(key) {
            return Ok(c.clone());
        }
        let (endpoint, universe, anonymous) = key;
        let mut sb = Storage::builder().with_grpc_subchannel_count(self.subchannels);
        let mut cb = StorageControl::builder();
        if *anonymous {
            let creds = google_cloud_auth::credentials::anonymous::Builder::new().build();
            sb = sb.with_credentials(creds.clone());
            cb = cb.with_credentials(creds);
        }
        if let Some(e) = endpoint.as_ref().or(self.endpoint.as_ref()) {
            sb = sb.with_endpoint(e.clone());
            cb = cb.with_endpoint(e.clone());
        }
        if let Some(u) = universe {
            sb = sb.with_universe_domain(u.clone());
        }
        let storage = sb.build().await.map_err(|e| e.to_string())?;
        let control = cb.build().await.map_err(|e| e.to_string())?;
        cache.insert(key.clone(), (storage.clone(), control.clone()));
        Ok((storage, control))
    }

    /// Registers a shared session (anonymous or daemon ADC for a given endpoint/universe)
    /// bound to `(uid, pid)`; the underlying clients are shared via [`Self::shared_clients`].
    pub async fn create_shared(
        &self,
        key: SharedKey,
        uid: u32,
        pid: i32,
    ) -> Result<Arc<Session>, String> {
        let (storage, control) = self.shared_clients(&key).await?;
        let s = Arc::new(Session {
            id: random_id()?,
            peer_uid: uid,
            peer_pid: pid,
            token: Arc::new(LentToken::new(String::new(), 0, None)),
            storage,
            control,
        });
        self.map.lock().await.insert(s.id.clone(), s.clone());
        Ok(s)
    }

    /// Registers a new session bound to `(uid, pid)` and initializes its GCS clients.
    pub async fn create(
        &self,
        token: String,
        expiry: i64,
        quota_project: Option<String>,
        uid: u32,
        pid: i32,
    ) -> Result<Arc<Session>, String> {
        self.create_with_endpoint(token, expiry, quota_project, None, None, uid, pid)
            .await
    }

    /// Like [`Self::create`], optionally overriding the endpoint / universe domain.
    #[allow(clippy::too_many_arguments)]
    pub async fn create_with_endpoint(
        &self,
        token: String,
        expiry: i64,
        quota_project: Option<String>,
        endpoint: Option<String>,
        universe_domain: Option<String>,
        uid: u32,
        pid: i32,
    ) -> Result<Arc<Session>, String> {
        let lent = Arc::new(LentToken::new(token, expiry, quota_project));
        let creds: Credentials = SharedProvider(lent.clone()).into();
        let mut sb = Storage::builder()
            .with_credentials(creds.clone())
            .with_grpc_subchannel_count(self.subchannels);
        let mut cb = StorageControl::builder().with_credentials(creds);
        if let Some(e) = endpoint.as_ref().or(self.endpoint.as_ref()) {
            sb = sb.with_endpoint(e.clone());
            cb = cb.with_endpoint(e.clone());
        }
        if let Some(u) = universe_domain {
            sb = sb.with_universe_domain(u);
        }
        let storage = sb.build().await.map_err(|e| e.to_string())?;
        let control = cb.build().await.map_err(|e| e.to_string())?;
        let s = Arc::new(Session {
            id: random_id()?,
            peer_uid: uid,
            peer_pid: pid,
            token: lent,
            storage,
            control,
        });
        self.map.lock().await.insert(s.id.clone(), s.clone());
        Ok(s)
    }

    /// Looks up a session by ID and verifies that the caller's `(uid, pid)` matches the owner.
    pub async fn get(&self, id: &str, uid: u32, pid: i32) -> Result<Arc<Session>, tonic::Status> {
        let s = self
            .map
            .lock()
            .await
            .get(id)
            .cloned()
            .ok_or_else(|| tonic::Status::unauthenticated("unknown session"))?;
        if s.peer_uid != uid || s.peer_pid != pid {
            return Err(tonic::Status::permission_denied(
                "session is bound to another process",
            ));
        }
        Ok(s)
    }

    /// Removes a session by ID after verifying that the caller's `(uid, pid)` matches the owner.
    pub async fn close(&self, id: &str, uid: u32, pid: i32) -> Result<(), tonic::Status> {
        let mut guard = self.map.lock().await;
        let s = guard
            .get(id)
            .ok_or_else(|| tonic::Status::unauthenticated("unknown session"))?;
        if s.peer_uid != uid || s.peer_pid != pid {
            return Err(tonic::Status::permission_denied(
                "session is bound to another process",
            ));
        }
        guard.remove(id);
        Ok(())
    }

    /// Removes a session by ID.
    pub async fn remove(&self, id: &str) {
        self.map.lock().await.remove(id);
    }

    /// Returns the number of active sessions.
    pub async fn len(&self) -> usize {
        self.map.lock().await.len()
    }

    /// Returns `true` if no sessions are currently registered.
    pub async fn is_empty(&self) -> bool {
        self.map.lock().await.is_empty()
    }

    /// Reaps any registered sessions whose owning client process (`peer_pid`) has exited
    /// (`kill(pid, 0) == -1 && errno == ESRCH`), freeing its pooled `Storage` / `StorageControl`
    /// instances even if the client crashed (`SIGKILL`) without calling `CloseSession`.
    pub async fn reap_dead_pids(&self) -> usize {
        let mut guard = self.map.lock().await;
        let before = guard.len();
        guard.retain(|_, s| {
            if s.peer_pid <= 0 {
                return true;
            }
            // SAFETY: `kill(pid, 0)` with signal 0 performs an existence check without sending a signal.
            let rc = unsafe { libc::kill(s.peer_pid, 0) };
            if rc == 0 {
                return true;
            }
            std::io::Error::last_os_error().raw_os_error() != Some(libc::ESRCH)
        });
        before - guard.len()
    }
}

#[derive(Debug)]
struct SharedProvider(Arc<LentToken>);

impl CredentialsProvider for SharedProvider {
    async fn headers(
        &self,
        extensions: http::Extensions,
    ) -> std::result::Result<
        CacheableResource<HeaderMap>,
        google_cloud_auth::errors::CredentialsError,
    > {
        self.0.headers(extensions).await
    }

    async fn universe_domain(&self) -> Option<String> {
        None
    }
}
