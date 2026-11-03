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

//! Binary entry point for `gcs-core-server`.

use clap::Parser;
use storage_grpc_uds::Args;

fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    tracing_subscriber::fmt()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .with_writer(std::io::stderr)
        .init();
    let args = Args::parse();

    #[cfg(target_os = "linux")]
    if args.pdeathsig {
        // Optional 1:1 child mode: request SIGTERM from the kernel if the spawning parent dies.
        // SAFETY: `prctl(PR_SET_PDEATHSIG, SIGTERM)` is a standard Linux syscall taking integer arguments.
        unsafe {
            libc::prctl(libc::PR_SET_PDEATHSIG, libc::SIGTERM);
        }
        // SAFETY: `getppid()` is always safe to call and cannot fail.
        if unsafe { libc::getppid() } == 1 {
            eprintln!("parent already exited; not starting");
            std::process::exit(0);
        }
    }

    let rt = tokio::runtime::Builder::new_multi_thread()
        .enable_all()
        .thread_name("gcs-core")
        .build()?;
    rt.block_on(storage_grpc_uds::run(args))
}
