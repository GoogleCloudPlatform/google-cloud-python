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

//! End-to-end integration tests for `storage-grpc-uds` (`gcs-core-server`).

use bytes::Bytes;
use httptest::{Expectation, Server as HttpServer, matchers::*, responders::*};
use hyper_util::rt::TokioIo;
use std::path::PathBuf;
use std::sync::atomic::Ordering;
use storage_grpc_mock::google::storage::v2::{
    BidiReadObjectResponse, ChecksummedData, Object as ProtoObject, ObjectRangeData,
    ReadRange as ProtoRange,
};
use storage_grpc_mock::{MockStorage, start as start_grpc_mock};
use storage_grpc_uds::pb::gcs_core_client::GcsCoreClient;
use storage_grpc_uds::pb::*;
use storage_grpc_uds::{Args, Shared, bind_uds_listener, serve_with_listener};
use tokio::net::UnixStream;
use tokio_stream::StreamExt;
use tonic::transport::{Channel, Endpoint, Uri};
use tower::service_fn;

async fn connect_uds(sock: PathBuf) -> anyhow::Result<GcsCoreClient<Channel>> {
    let channel = Endpoint::try_from("http://[::]:50051")?
        .connect_with_connector(service_fn(move |_: Uri| {
            let p = sock.clone();
            async move { Ok::<_, std::io::Error>(TokioIo::new(UnixStream::connect(p).await?)) }
        }))
        .await?;
    Ok(GcsCoreClient::new(channel)
        .max_decoding_message_size(64 * 1024 * 1024)
        .max_encoding_message_size(64 * 1024 * 1024))
}

#[tokio::test(flavor = "multi_thread", worker_threads = 2)]
async fn ping_stats_active_conns_and_stale_socket_recovery() -> anyhow::Result<()> {
    let dir = tempfile::tempdir()?;
    let sock_path = dir.path().join("gcs-core.sock");
    let sock_str = sock_path.to_string_lossy().to_string();

    // Verify bind_uds_listener refuses to remove a regular non-socket file.
    let regular_file = dir.path().join("not-a-socket.txt");
    std::fs::write(&regular_file, b"keep-me")?;
    assert!(
        bind_uds_listener(&regular_file.to_string_lossy()).is_err(),
        "bind_uds_listener must refuse to delete a regular file"
    );
    assert!(regular_file.exists());

    // Create a stale socket file by binding and immediately dropping a raw UnixListener.
    {
        let _stale = std::os::unix::net::UnixListener::bind(&sock_path)?;
    }
    assert!(
        sock_path.exists(),
        "stale socket file should exist before bind_uds_listener"
    );

    let args = Args {
        socket: sock_str.clone(),
        idle_secs: 0,
        shm_size: 0,
        endpoint: Some("http://127.0.0.1:1".to_string()),
        ..Default::default()
    };

    let listener = bind_uds_listener(&args.socket)
        .map_err(|e| anyhow::anyhow!("bind_uds_listener failed: {e}"))?;

    #[cfg(unix)]
    {
        use std::os::unix::fs::PermissionsExt;
        let mode = std::fs::metadata(&sock_path)?.permissions().mode() & 0o777;
        assert_eq!(mode, 0o600, "UDS socket must have 0600 permissions");
    }

    let shared = Shared::new();
    let srv_shared = shared.clone();
    let srv_handle = tokio::spawn(async move {
        let _ = serve_with_listener(args, listener, srv_shared).await;
    });

    {
        let mut client = connect_uds(sock_path.clone()).await?;
        let payload = Bytes::from_static(b"hello-uds-core");
        let resp = client
            .ping(PingRequest {
                payload: payload.clone(),
            })
            .await?
            .into_inner();
        assert_eq!(resp.payload, payload);
        assert!(
            shared.active_conns.load(Ordering::Relaxed) >= 1,
            "TrackedUnixStream must increment active_conns while connected"
        );

        let stats = client
            .stats(StatsRequest {
                reset_peak_rss: false,
            })
            .await?
            .into_inner();
        assert!(stats.rpcs_served >= 1);
        assert_eq!(stats.pid as u32, std::process::id());
    }

    // Wait briefly for the dropped client connection to close and decrement active_conns.
    for _ in 0..50 {
        if shared.active_conns.load(Ordering::Relaxed) == 0 {
            break;
        }
        tokio::time::sleep(std::time::Duration::from_millis(10)).await;
    }
    assert_eq!(
        shared.active_conns.load(Ordering::Relaxed),
        0,
        "TrackedUnixStream Drop must decrement active_conns to 0"
    );

    let mut client = connect_uds(sock_path.clone()).await?;
    client.shutdown(Empty {}).await?;
    srv_handle.await?;
    assert!(
        !sock_path.exists(),
        "socket file should be removed after shutdown"
    );
    Ok(())
}

#[tokio::test(flavor = "multi_thread", worker_threads = 2)]
async fn session_lifecycle_expiry_and_peer_isolation() -> anyhow::Result<()> {
    let dir = tempfile::tempdir()?;
    let sock_path = dir.path().join("session.sock");

    let args = Args {
        socket: sock_path.to_string_lossy().to_string(),
        idle_secs: 0,
        shm_size: 0,
        require_session: true,
        endpoint: Some("http://127.0.0.1:1".to_string()),
        ..Default::default()
    };

    let listener = bind_uds_listener(&args.socket)
        .map_err(|e| anyhow::anyhow!("bind_uds_listener failed: {e}"))?;
    let shared = Shared::new();
    let srv_shared = shared.clone();
    let srv_handle = tokio::spawn(async move {
        let _ = serve_with_listener(args, listener, srv_shared).await;
    });

    let mut client = connect_uds(sock_path.clone()).await?;

    // Data RPC without x-session when --require-session is enabled must return UNAUTHENTICATED.
    let err = client
        .list_objects(ListObjectsRequest {
            bucket: "b".to_string(),
            ..Default::default()
        })
        .await
        .expect_err("expected UNAUTHENTICATED without x-session");
    assert_eq!(err.code(), tonic::Code::Unauthenticated);

    let now_secs = storage_grpc_uds::now_ms() / 1000;
    // Create a valid session via UDS (peer_cred carries our current UID & PID).
    let sess = client
        .create_session(CreateSessionRequest {
            access_token: "test-bearer-initial-token".to_string(),
            expiry_unix_secs: now_secs + 60,
            quota_project: "test-quota-proj".to_string(),
            ..Default::default()
        })
        .await?
        .into_inner();
    assert_eq!(sess.session_id.len(), 64);

    // Reject empty access_token on UpdateToken with INVALID_ARGUMENT.
    let empty_err = client
        .update_token(UpdateTokenRequest {
            session_id: sess.session_id.clone(),
            access_token: String::new(),
            expiry_unix_secs: now_secs + 120,
        })
        .await
        .expect_err("empty access_token should be rejected");
    assert_eq!(empty_err.code(), tonic::Code::InvalidArgument);

    // Rotate to an already-expired token and verify a data RPC returns UNAUTHENTICATED.
    client
        .update_token(UpdateTokenRequest {
            session_id: sess.session_id.clone(),
            access_token: "test-bearer-expired-token".to_string(),
            expiry_unix_secs: 1, // expired in 1970
        })
        .await?;
    let mut expired_req = tonic::Request::new(ListObjectsRequest {
        bucket: "b".to_string(),
        ..Default::default()
    });
    expired_req
        .metadata_mut()
        .insert("x-session", sess.session_id.parse()?);
    let expired_err = client
        .list_objects(expired_req)
        .await
        .expect_err("expired lent token must fail with UNAUTHENTICATED");
    assert_eq!(expired_err.code(), tonic::Code::Unauthenticated);

    // Close session and confirm subsequent UpdateToken returns UNAUTHENTICATED.
    client
        .close_session(SessionRef {
            session_id: sess.session_id.clone(),
        })
        .await?;
    let err = client
        .update_token(UpdateTokenRequest {
            session_id: sess.session_id,
            access_token: "test-bearer-after-close".to_string(),
            expiry_unix_secs: 0,
        })
        .await
        .expect_err("closed session should not exist");
    assert_eq!(err.code(), tonic::Code::Unauthenticated);

    // Direct cross-PID rejection unit check on `Sessions` registry.
    let sessions =
        storage_grpc_uds::session::Sessions::new(Some("http://127.0.0.1:1".to_string()), 4);
    let created = sessions
        .create("tok".to_string(), 0, None, 1000, 4242)
        .await
        .map_err(|e| anyhow::anyhow!(e))?;
    let cross_pid = sessions
        .get(&created.id, 1000, 9999)
        .await
        .err()
        .expect("mismatched PID must be rejected");
    assert_eq!(cross_pid.code(), tonic::Code::PermissionDenied);

    client.shutdown(Empty {}).await?;
    srv_handle.await?;
    Ok(())
}

#[cfg(target_os = "linux")]
#[tokio::test(flavor = "multi_thread", worker_threads = 2)]
async fn shm_memfd_scm_rights_and_zero_copy_read() -> anyhow::Result<()> {
    let payload = b"zero-copy-memfd-scm-rights-payload-0123456789";
    let http_srv = HttpServer::run();
    http_srv.expect(
        Expectation::matching(all_of![
            request::method_path("GET", "/storage/v1/b/test-bucket/o/test-obj"),
            request::query(url_decoded(contains(("alt", "media")))),
        ])
        .respond_with(
            status_code(200)
                .append_header("x-goog-generation", "77")
                .body(payload.as_slice()),
        ),
    );

    let dir = tempfile::tempdir()?;
    let sock_path = dir.path().join("shm-test.sock");
    let shm_sock_path = dir.path().join("shm-test.sock.shm");

    let args = Args {
        socket: sock_path.to_string_lossy().to_string(),
        idle_secs: 0,
        shm_size: 4 * 1024 * 1024,
        endpoint: Some(format!("http://{}", http_srv.addr())),
        ..Default::default()
    };

    let listener = bind_uds_listener(&args.socket)
        .map_err(|e| anyhow::anyhow!("bind_uds_listener failed: {e}"))?;
    let shared = Shared::new();
    let srv_shared = shared.clone();
    let srv_handle = tokio::spawn(async move {
        let _ = serve_with_listener(args, listener, srv_shared).await;
    });

    // Wait briefly for the `.shm` side listener task to bind.
    for _ in 0..50 {
        if shm_sock_path.exists() {
            break;
        }
        tokio::time::sleep(std::time::Duration::from_millis(10)).await;
    }
    assert!(shm_sock_path.exists(), ".shm socket should be bound");

    // Connect to `<socket>.shm` and receive the 16-byte (region_id, region_size) header + memfd via SCM_RIGHTS.
    // Keep `_shm_stream` alive while using the region so the server retains the mapping.
    let (_shm_stream, region_id, fd, mapped_len) = {
        use std::os::unix::io::AsRawFd;
        let stream = std::os::unix::net::UnixStream::connect(&shm_sock_path)?;
        let mut hdr_buf = [0u8; 16];
        let mut iov = libc::iovec {
            iov_base: hdr_buf.as_mut_ptr() as *mut libc::c_void,
            iov_len: hdr_buf.len(),
        };
        let mut cmsg_space =
            [0u8; unsafe { libc::CMSG_SPACE(std::mem::size_of::<libc::c_int>() as u32) as usize }];
        let mut msg: libc::msghdr = unsafe { std::mem::zeroed() };
        msg.msg_iov = &mut iov;
        msg.msg_iovlen = 1;
        msg.msg_control = cmsg_space.as_mut_ptr() as *mut libc::c_void;
        msg.msg_controllen = cmsg_space.len();

        let n = unsafe { libc::recvmsg(stream.as_raw_fd(), &mut msg, 0) };
        assert_eq!(n, 16, "expected 16-byte (region_id, size) header from .shm");
        let cmsg = unsafe { libc::CMSG_FIRSTHDR(&msg) };
        assert!(!cmsg.is_null(), "expected SCM_RIGHTS control message");
        let mut recv_fd: libc::c_int = -1;
        unsafe {
            std::ptr::copy_nonoverlapping(
                libc::CMSG_DATA(cmsg),
                &mut recv_fd as *mut libc::c_int as *mut u8,
                std::mem::size_of::<libc::c_int>(),
            );
        }
        assert!(recv_fd >= 0, "valid memfd expected");
        let rid = u64::from_le_bytes(hdr_buf[..8].try_into().unwrap());
        let rsize = u64::from_le_bytes(hdr_buf[8..16].try_into().unwrap()) as usize;
        assert_eq!(rsize, 4 * 1024 * 1024);
        (stream, rid, recv_fd, rsize)
    };

    let mut client = connect_uds(sock_path.clone()).await?;
    let sess = client
        .create_session(CreateSessionRequest {
            access_token: "test-bearer-shm-test".to_string(),
            expiry_unix_secs: 0,
            quota_project: String::new(),
            ..Default::default()
        })
        .await?
        .into_inner();

    // Verify out-of-bounds base_offset + capacity > region_size returns OUT_OF_RANGE.
    let mut oob_req = tonic::Request::new(ReadObjectShmRequest {
        read: Some(ReadObjectRequest {
            bucket: "test-bucket".to_string(),
            object: "test-obj".to_string(),
            offset: 0,
            length: -1,
            generation: 0,
            if_generation_match: None,
            transport: Transport::Json as i32,
            chunk_size: 0,
        }),
        region: region_id,
        base_offset: mapped_len as u64,
        capacity: 1024,
    });
    oob_req
        .metadata_mut()
        .insert("x-session", sess.session_id.parse()?);
    let oob_err = client
        .read_object_shm(oob_req)
        .await
        .expect_err("out-of-bounds shm capacity must fail");
    assert_eq!(oob_err.code(), tonic::Code::OutOfRange);

    let mut req = tonic::Request::new(ReadObjectShmRequest {
        read: Some(ReadObjectRequest {
            bucket: "test-bucket".to_string(),
            object: "test-obj".to_string(),
            offset: 0,
            length: -1,
            generation: 0,
            if_generation_match: None,
            transport: Transport::Json as i32,
            chunk_size: 0,
        }),
        region: region_id,
        base_offset: 128,
        capacity: 1024 * 1024,
    });
    req.metadata_mut()
        .insert("x-session", sess.session_id.parse()?);

    let mut stream = client.read_object_shm(req).await?.into_inner();
    let mut total_written = 0usize;
    let mut first_gen = 0i64;
    while let Some(chunk) = stream.next().await {
        let chunk = chunk?;
        if let Some(ref m) = chunk.meta
            && first_gen == 0
        {
            first_gen = m.generation;
        }
        total_written += chunk.len as usize;
    }
    assert_eq!(total_written, payload.len());
    assert_eq!(first_gen, 77);

    // Read directly from the received memfd at offset 128 and verify zero-copy contents.
    let slice = unsafe {
        let base = libc::mmap(
            std::ptr::null_mut(),
            mapped_len,
            libc::PROT_READ,
            libc::MAP_SHARED,
            fd,
            0,
        );
        assert_ne!(base, libc::MAP_FAILED);
        let bytes =
            std::slice::from_raw_parts((base as *const u8).add(128), total_written).to_vec();
        libc::munmap(base, mapped_len);
        libc::close(fd);
        bytes
    };
    assert_eq!(slice.as_slice(), payload);

    client.shutdown(Empty {}).await?;
    srv_handle.await?;
    Ok(())
}

#[tokio::test(flavor = "multi_thread", worker_threads = 2)]
async fn read_write_and_list_over_uds_via_httptest() -> anyhow::Result<()> {
    let body_bytes = vec![b'R'; 256 * 1024];
    let http_srv = HttpServer::run();
    // 1. Non-empty object read
    http_srv.expect(
        Expectation::matching(all_of![
            request::method_path("GET", "/storage/v1/b/my-bucket/o/my-object"),
            request::query(url_decoded(contains(("alt", "media")))),
        ])
        .respond_with(
            status_code(200)
                .append_header("x-goog-generation", "12345")
                .append_header("content-type", "application/octet-stream")
                .body(body_bytes.clone()),
        ),
    );
    // 2. 0-byte empty object read (must still deliver ObjectMeta on first chunk)
    http_srv.expect(
        Expectation::matching(all_of![
            request::method_path("GET", "/storage/v1/b/my-bucket/o/empty-object"),
            request::query(url_decoded(contains(("alt", "media")))),
        ])
        .respond_with(
            status_code(200)
                .append_header("x-goog-generation", "42")
                .append_header("content-type", "text/plain")
                .body(Vec::<u8>::new()),
        ),
    );
    // 3. WriteObject multipart upload (known_size >= 0)
    http_srv.expect(
        Expectation::matching(all_of![
            request::method_path("POST", "/upload/storage/v1/b/my-bucket/o"),
            request::query(url_decoded(contains(("uploadType", "multipart")))),
        ])
        .respond_with(
            status_code(200)
                .append_header("content-type", "application/json")
                .body(
                    serde_json::json!({
                        "name": "uploaded.bin",
                        "bucket": "my-bucket",
                        "size": "11",
                        "generation": "999"
                    })
                    .to_string(),
                ),
        ),
    );

    let dir = tempfile::tempdir()?;
    let sock_path = dir.path().join("read-write-test.sock");
    let endpoint_url = format!("http://{}", http_srv.addr());

    let args = Args {
        socket: sock_path.to_string_lossy().to_string(),
        idle_secs: 0,
        shm_size: 0,
        chunk_size: 64 * 1024,
        endpoint: Some(endpoint_url),
        ..Default::default()
    };

    let listener = bind_uds_listener(&args.socket)
        .map_err(|e| anyhow::anyhow!("bind_uds_listener failed: {e}"))?;
    let shared = Shared::new();
    let srv_shared = shared.clone();
    let srv_handle = tokio::spawn(async move {
        let _ = serve_with_listener(args, listener, srv_shared).await;
    });

    let mut client = connect_uds(sock_path.clone()).await?;
    let sess = client
        .create_session(CreateSessionRequest {
            access_token: "test-bearer-read-test".to_string(),
            expiry_unix_secs: 0,
            quota_project: String::new(),
            ..Default::default()
        })
        .await?
        .into_inner();

    // Test 1: 256 KiB streamed read
    let mut req = tonic::Request::new(ReadObjectRequest {
        bucket: "my-bucket".to_string(),
        object: "my-object".to_string(),
        offset: 0,
        length: -1,
        generation: 0,
        if_generation_match: None,
        transport: Transport::Json as i32,
        chunk_size: 64 * 1024,
    });
    req.metadata_mut()
        .insert("x-session", sess.session_id.parse()?);

    let mut stream = client.read_object(req).await?.into_inner();
    let mut received = Vec::new();
    let mut first_gen = 0i64;
    while let Some(chunk) = stream.next().await {
        let chunk = chunk?;
        if let Some(ref m) = chunk.meta
            && first_gen == 0
        {
            first_gen = m.generation;
        }
        for slice in &chunk.data {
            received.extend_from_slice(slice);
        }
    }
    assert_eq!(first_gen, 12345);
    assert_eq!(received.len(), body_bytes.len());
    assert_eq!(received, body_bytes);

    // Test 2: 0-byte empty object read still emits 1 ReadChunk carrying ObjectMeta
    let mut empty_req = tonic::Request::new(ReadObjectRequest {
        bucket: "my-bucket".to_string(),
        object: "empty-object".to_string(),
        offset: 0,
        length: -1,
        generation: 0,
        if_generation_match: None,
        transport: Transport::Json as i32,
        chunk_size: 64 * 1024,
    });
    empty_req
        .metadata_mut()
        .insert("x-session", sess.session_id.parse()?);
    let mut empty_stream = client.read_object(empty_req).await?.into_inner();
    let first_chunk = empty_stream
        .next()
        .await
        .expect("0-byte object must emit metadata chunk")?;
    assert!(first_chunk.data.is_empty());
    assert_eq!(first_chunk.meta.unwrap().generation, 42);
    assert!(empty_stream.next().await.is_none());

    // Test 3: WriteObject streaming upload (Header + 2 Data frames)
    let frames = vec![
        WriteRequest {
            msg: Some(write_request::Msg::Header(WriteHeader {
                bucket: "my-bucket".to_string(),
                object: "uploaded.bin".to_string(),
                content_type: "application/octet-stream".to_string(),
                if_generation_match: None,
                known_size: Some(11),
                chunk_size: 0,
                transport: Transport::Json as i32,
            })),
        },
        WriteRequest {
            msg: Some(write_request::Msg::Data(Bytes::from_static(b"hello "))),
        },
        WriteRequest {
            msg: Some(write_request::Msg::Data(Bytes::from_static(b"world"))),
        },
    ];
    let mut write_req = tonic::Request::new(tokio_stream::iter(frames));
    write_req
        .metadata_mut()
        .insert("x-session", sess.session_id.parse()?);
    let write_resp = client.write_object(write_req).await?.into_inner();
    assert_eq!(write_resp.size, 11);
    assert_eq!(write_resp.generation, 999);
    assert_eq!(write_resp.transport_used, Transport::Json as i32);

    // Test 4: WriteObject without initial WriteHeader returns INVALID_ARGUMENT
    let bad_frames = vec![WriteRequest {
        msg: Some(write_request::Msg::Data(Bytes::from_static(b"no-header"))),
    }];
    let mut bad_req = tonic::Request::new(tokio_stream::iter(bad_frames));
    bad_req
        .metadata_mut()
        .insert("x-session", sess.session_id.parse()?);
    let bad_err = client
        .write_object(bad_req)
        .await
        .expect_err("WriteObject without header must fail");
    assert_eq!(bad_err.code(), tonic::Code::InvalidArgument);

    client.shutdown(Empty {}).await?;
    srv_handle.await?;
    Ok(())
}

#[tokio::test(flavor = "multi_thread", worker_threads = 2)]
async fn open_object_read_range_and_close_via_grpc_mock() -> anyhow::Result<()> {
    let mut mock = MockStorage::new();
    mock.expect_bidi_read_object().return_once(move |request| {
        let (_, _, mut requests) = request.into_parts();
        let (tx, rx) = tokio::sync::mpsc::channel(4);
        tokio::spawn(async move {
            // First message opens the object
            if let Some(Ok(_first)) = requests.recv().await {
                let _ = tx
                    .send(Ok(BidiReadObjectResponse {
                        metadata: Some(ProtoObject {
                            name: "bidi-obj".to_string(),
                            bucket: "projects/_/buckets/bidi-bucket".to_string(),
                            generation: 555,
                            size: 16,
                            ..ProtoObject::default()
                        }),
                        ..BidiReadObjectResponse::default()
                    }))
                    .await;
            }
            // Subsequent message requests a byte range
            while let Some(Ok(req)) = requests.recv().await {
                for r in req.read_ranges {
                    let _ = tx
                        .send(Ok(BidiReadObjectResponse {
                            object_data_ranges: vec![ObjectRangeData {
                                checksummed_data: Some(ChecksummedData {
                                    content: b"0123456789abcdef".to_vec(),
                                    crc32c: None,
                                }),
                                read_range: Some(ProtoRange {
                                    read_offset: r.read_offset,
                                    read_length: 16,
                                    read_id: r.read_id,
                                }),
                                range_end: true,
                            }],
                            ..BidiReadObjectResponse::default()
                        }))
                        .await;
                }
            }
        });
        Ok(tonic::Response::from(rx))
    });

    let (mock_endpoint, _mock_srv) = start_grpc_mock("127.0.0.1:0", mock).await?;
    let dir = tempfile::tempdir()?;
    let sock_path = dir.path().join("grpc-mock.sock");

    let args = Args {
        socket: sock_path.to_string_lossy().to_string(),
        idle_secs: 0,
        shm_size: 0,
        endpoint: Some(mock_endpoint),
        ..Default::default()
    };

    let listener = bind_uds_listener(&args.socket)
        .map_err(|e| anyhow::anyhow!("bind_uds_listener failed: {e}"))?;
    let shared = Shared::new();
    let srv_shared = shared.clone();
    let srv_handle = tokio::spawn(async move {
        let _ = serve_with_listener(args, listener, srv_shared).await;
    });

    let mut client = connect_uds(sock_path.clone()).await?;
    let sess = client
        .create_session(CreateSessionRequest {
            access_token: "test-bearer-grpc-mock".to_string(),
            expiry_unix_secs: 0,
            quota_project: String::new(),
            ..Default::default()
        })
        .await?
        .into_inner();

    let mut open_req = tonic::Request::new(OpenObjectRequest {
        bucket: "bidi-bucket".to_string(),
        object: "bidi-obj".to_string(),
        generation: 0,
    });
    open_req
        .metadata_mut()
        .insert("x-session", sess.session_id.parse()?);
    let opened = client.open_object(open_req).await?.into_inner();
    assert!(opened.handle >= 1);
    assert_eq!(opened.meta.unwrap().generation, 555);

    let mut range_stream = client
        .read_range(ReadRangeRequest {
            handle: opened.handle,
            offset: 0,
            length: 16,
            chunk_size: 64 * 1024,
        })
        .await?
        .into_inner();
    let mut range_bytes = Vec::new();
    while let Some(chunk) = range_stream.next().await {
        let chunk = chunk?;
        assert!(
            chunk.meta.is_none(),
            "ReadRange chunks must not repeat ObjectMeta"
        );
        for slice in &chunk.data {
            range_bytes.extend_from_slice(slice);
        }
    }
    assert_eq!(range_bytes, b"0123456789abcdef");

    client
        .close_object(CloseObjectRequest {
            handle: opened.handle,
        })
        .await?;

    // Subsequent ReadRange on closed handle must return NOT_FOUND.
    let closed_err = client
        .read_range(ReadRangeRequest {
            handle: opened.handle,
            offset: 0,
            length: 16,
            chunk_size: 0,
        })
        .await
        .expect_err("closed handle should return NOT_FOUND");
    assert_eq!(closed_err.code(), tonic::Code::NotFound);

    client.shutdown(Empty {}).await?;
    srv_handle.await?;
    Ok(())
}

#[tokio::test(flavor = "multi_thread", worker_threads = 2)]
async fn json_404_and_412_status_mapping_and_inproc_lifecycle() -> anyhow::Result<()> {
    let http_srv = HttpServer::run();
    // 1. GCS JSON 404 error envelope (without gRPC `status` string field)
    http_srv.expect(
        Expectation::matching(all_of![
            request::method_path("GET", "/storage/v1/b/my-bucket/o/missing-object"),
            request::query(url_decoded(contains(("alt", "media")))),
        ])
        .respond_with(
            status_code(404)
                .append_header("content-type", "application/json")
                .body(
                    serde_json::json!({
                        "error": {
                            "code": 404,
                            "message": "No such object: my-bucket/missing-object"
                        }
                    })
                    .to_string(),
                ),
        ),
    );
    // 2. GCS JSON 412 precondition failed envelope
    http_srv.expect(
        Expectation::matching(all_of![
            request::method_path("GET", "/storage/v1/b/my-bucket/o/precond-object"),
            request::query(url_decoded(contains(("alt", "media")))),
            request::query(url_decoded(contains(("ifGenerationMatch", "0")))),
        ])
        .respond_with(
            status_code(412)
                .append_header("content-type", "application/json")
                .body(
                    serde_json::json!({
                        "error": {
                            "code": 412,
                            "message": "At least one of the pre-conditions you specified did not hold."
                        }
                    })
                    .to_string(),
                ),
        ),
    );

    let dir = tempfile::tempdir()?;
    let sock_path = dir.path().join("json-err-test.sock");
    let tcp_listener = std::net::TcpListener::bind("127.0.0.1:0")?;
    let tcp_addr = tcp_listener.local_addr()?;
    drop(tcp_listener);

    let args = Args {
        socket: sock_path.to_string_lossy().to_string(),
        idle_secs: 0,
        shm_size: 0,
        tcp: Some(tcp_addr.to_string()),
        peer_uid_check: true,
        endpoint: Some(format!("http://{}", http_srv.addr())),
        ..Default::default()
    };

    let listener = bind_uds_listener(&args.socket)
        .map_err(|e| anyhow::anyhow!("bind_uds_listener failed: {e}"))?;
    let shared = Shared::new();
    let srv_shared = shared.clone();
    let srv_handle = tokio::spawn(async move {
        let _ = serve_with_listener(args, listener, srv_shared).await;
    });

    let mut client = connect_uds(sock_path.clone()).await?;
    let sess = client
        .create_session(CreateSessionRequest {
            access_token: "test-bearer-err-test".to_string(),
            expiry_unix_secs: 0,
            quota_project: String::new(),
            ..Default::default()
        })
        .await?
        .into_inner();

    // Verify JSON 404 maps to tonic::Code::NotFound (not Code::Unknown)
    let mut req_404 = tonic::Request::new(ReadObjectRequest {
        bucket: "my-bucket".to_string(),
        object: "missing-object".to_string(),
        offset: 0,
        length: -1,
        generation: 0,
        if_generation_match: None,
        transport: Transport::Json as i32,
        chunk_size: 0,
    });
    req_404
        .metadata_mut()
        .insert("x-session", sess.session_id.parse()?);
    let err_404 = client
        .read_object(req_404)
        .await
        .expect_err("404 JSON response must fail with NOT_FOUND");
    assert_eq!(err_404.code(), tonic::Code::NotFound);

    // Verify JSON 412 with optional if_generation_match = Some(0) maps to FailedPrecondition
    let mut req_412 = tonic::Request::new(ReadObjectRequest {
        bucket: "my-bucket".to_string(),
        object: "precond-object".to_string(),
        offset: 0,
        length: -1,
        generation: 0,
        if_generation_match: Some(0),
        transport: Transport::Json as i32,
        chunk_size: 0,
    });
    req_412
        .metadata_mut()
        .insert("x-session", sess.session_id.parse()?);
    let err_412 = client
        .read_object(req_412)
        .await
        .expect_err("412 JSON response must fail with FAILED_PRECONDITION");
    assert_eq!(err_412.code(), tonic::Code::FailedPrecondition);

    // Verify TCP connection is rejected when --peer-uid-check=true
    let tcp_channel = Endpoint::try_from(format!("http://{tcp_addr}"))?
        .connect()
        .await?;
    let mut tcp_client = GcsCoreClient::new(tcp_channel);
    let tcp_err = tcp_client
        .ping(PingRequest {
            payload: Bytes::from_static(b"tcp-ping"),
        })
        .await
        .expect_err("TCP call must be rejected when --peer-uid-check=true");
    assert_eq!(tcp_err.code(), tonic::Code::PermissionDenied);

    client.shutdown(Empty {}).await?;
    srv_handle.await?;

    // Verify gcs_core_start_inproc and gcs_core_stop_inproc C-FFI lifecycle
    let inproc_sock = dir.path().join("inproc.sock");
    let c_sock = std::ffi::CString::new(inproc_sock.to_string_lossy().as_bytes())?;
    let start_rc = unsafe { storage_grpc_uds::gcs_core_start_inproc(c_sock.as_ptr()) };
    assert_eq!(start_rc, 0, "gcs_core_start_inproc must return 0");
    {
        let mut inproc_client = connect_uds(inproc_sock.clone()).await?;
        let pong = inproc_client
            .ping(PingRequest {
                payload: Bytes::from_static(b"inproc-ok"),
            })
            .await?
            .into_inner();
        assert_eq!(pong.payload, Bytes::from_static(b"inproc-ok"));
    }
    let stop_rc = unsafe { storage_grpc_uds::gcs_core_stop_inproc(c_sock.as_ptr()) };
    assert_eq!(stop_rc, 0, "gcs_core_stop_inproc must return 0");
    assert!(
        !inproc_sock.exists(),
        "inproc socket should be removed after gcs_core_stop_inproc"
    );
    Ok(())
}
