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

//! Conversion of `google_cloud_storage::model::Object` into the UDS `ObjectResource`.
//!
//! The prost `google.storage.v2.Object` types inside `google-cloud-storage` are
//! `pub(crate)`, so the full resource travels as proto3 JSON produced by the public
//! `serde::Serialize` impl of `model::Object` (`object_json`), alongside a handful of
//! typed "hot" fields that thin clients need without parsing JSON.

use crate::pb;
use google_cloud_storage::model::Object;

/// Converts a `model::Object` into an `ObjectResource` (typed hot fields + proto3 JSON).
pub fn object_resource(o: &Object) -> pb::ObjectResource {
    let checksums = o.checksums.as_ref();
    pb::ObjectResource {
        bucket: o.bucket.clone(),
        name: o.name.clone(),
        generation: o.generation,
        metageneration: o.metageneration,
        size: o.size,
        storage_class: o.storage_class.clone(),
        etag: o.etag.clone(),
        content_type: o.content_type.clone(),
        content_encoding: o.content_encoding.clone(),
        finalized: o.finalize_time.is_some(),
        crc32c: checksums.and_then(|c| c.crc32c),
        md5_hash: checksums.map(|c| c.md5_hash.to_vec()).unwrap_or_default(),
        metadata: o
            .metadata
            .iter()
            .map(|(k, v)| (k.clone(), v.clone()))
            .collect(),
        kms_key: o.kms_key.clone(),
        object_json: serde_json::to_string(o).unwrap_or_default(),
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use google_cloud_storage::model::ObjectChecksums;

    #[test]
    fn hot_fields_and_json_round_trip() {
        let o = Object::new()
            .set_bucket("projects/_/buckets/b")
            .set_name("o")
            .set_generation(123)
            .set_metageneration(4)
            .set_size(1_048_576)
            .set_storage_class("RAPID")
            .set_content_type("text/plain")
            .set_finalize_time(google_cloud_wkt::Timestamp::clamp(1_700_000_000, 5))
            .set_checksums(ObjectChecksums::new().set_crc32c(0xdead_beef_u32))
            .set_metadata([("k", "v")])
            .set_kms_key("projects/p/locations/l/keyRings/r/cryptoKeys/k");
        let r = object_resource(&o);
        assert_eq!(r.bucket, "projects/_/buckets/b");
        assert_eq!(r.generation, 123);
        assert_eq!(r.size, 1_048_576);
        assert!(r.finalized);
        assert_eq!(r.crc32c, Some(0xdead_beef));
        assert_eq!(r.metadata.get("k").map(String::as_str), Some("v"));
        let v: serde_json::Value = serde_json::from_str(&r.object_json).unwrap();
        // proto3 JSON: camelCase names, int64 as strings, fixed32 as numbers.
        assert_eq!(v["generation"], "123");
        assert_eq!(v["size"], "1048576");
        assert_eq!(v["checksums"]["crc32c"], 0xdead_beef_u32);
        assert_eq!(v["storageClass"], "RAPID");
        assert!(v["finalizeTime"].is_string());
        let back: Object = serde_json::from_str(&r.object_json).unwrap();
        assert_eq!(back, o);
    }

    #[test]
    fn unfinalized_object_has_no_crc() {
        let o = Object::new().set_generation(7).set_size(10);
        let r = object_resource(&o);
        assert!(!r.finalized);
        assert_eq!(r.crc32c, None);
        assert!(r.md5_hash.is_empty());
    }
}
