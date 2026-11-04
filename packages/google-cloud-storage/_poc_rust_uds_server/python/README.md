# google-cloud-storage-core

Companion platform wheel for `google-cloud-storage[uds]`. It bundles the
`gcs-core-server` executable built from
[`google-cloud-rust/src/storage/grpc-uds`](../README.md): the unmodified Rust
`google-cloud-storage` client exposed as a gRPC server over a Unix domain socket,
with zero-copy shared-memory `BidiReadObject` / `BidiWriteObject` sessions.

```python
import google_cloud_storage_core
print(google_cloud_storage_core.binary_path())
```

The Python SDK finds the binary automatically; `GOOGLE_CLOUD_STORAGE_UDS_BINARY`
overrides it.
