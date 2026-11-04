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

fn main() {
    #[cfg(google_cloud_generate_protos)]
    {
        tonic_prost_build::configure()
            .build_server(true)
            .build_client(true)
            .out_dir("src/generated/protos")
            .bytes(".gcscore.v1.ReadChunk.data")
            .bytes(".gcscore.v1.WriteRequest.data")
            .bytes(".gcscore.v1.PingRequest.payload")
            .bytes(".gcscore.v1.PingResponse.payload")
            .bytes(".gcscore.v1.RangeData.inline_data")
            .bytes(".gcscore.v1.Append.inline_data")
            .compile_protos(&["proto/gcscore.proto"], &["proto"])
            .expect("error compiling protos");
    }
}
