#!/bin/bash
# ==============================================================================
# Automated Google Cloud Storage Read Microbenchmark Runner
# Intended for GitHub CI/CD & GCE High-Bandwidth Tier-1 VMs (C4/N2/C3 series)
# Location: packages/google-cloud-storage/cloudbuild/run_benchmark_tests.sh
# ==============================================================================

set -eo pipefail

# Configurable defaults
PROCESSES="${PROCESSES:-48}"
COROS="${COROS:-1}"
FILE_SIZE_MIB="${FILE_SIZE_MIB:-10240}"      # 10 GiB files by default
CHUNK_SIZE_KIB="${CHUNK_SIZE_KIB:-102400}"   # ~100 MiB read chunks by default
ROUNDS="${ROUNDS:-3}"                        # Run benchmark 3 rounds by default
BUCKET_TYPE="${BUCKET_TYPE:-rapid}"          # "rapid" uses BidiReadObject gRPC DirectPath, "regional" uses REST/gRPC standard
RAPID_BUCKET="${RAPID_BUCKET:-${DEFAULT_RAPID_BUCKET:-gcs-read-bench-zb-us-west4-a}}"
REGIONAL_BUCKET="${REGIONAL_BUCKET:-${DEFAULT_STANDARD_BUCKET:-gcs-read-bench-rb-us-west4}}"
# Limit concurrent ALTS handshakes per worker process to 2 so that 48 worker
# processes never exceed 96 total concurrent streams against the local GCE
# metadata server (169.254.169.254:8080, ~100 stream buffer limit), preventing
# GOAWAY [11] "Buffers full" errors while still handshaking multiple subchannels.
GRPC_ALTS_MAX_CONCURRENT_HANDSHAKES="${GRPC_ALTS_MAX_CONCURRENT_HANDSHAKES:-2}"
if [ -n "${TARGET_BUCKET:-}" ]; then
  if [ "${BUCKET_TYPE}" = "regional" ]; then
    REGIONAL_BUCKET="${TARGET_BUCKET}"
  else
    RAPID_BUCKET="${TARGET_BUCKET}"
  fi
fi
# Ensure HOME is exported for gRPC / ALTS Application Default Credentials
export HOME="${HOME:-/root}"
OUTPUT_JSON_PATH="${OUTPUT_JSON_PATH:-${OUT_JSON:-${HOME}/bench_result.json}}"
rm -f "${OUTPUT_JSON_PATH}" 2>/dev/null || true
UPLOAD_GCS_PREFIX="${UPLOAD_GCS_PREFIX:-}"

echo "========================================================================"
echo " GCS Read Microbenchmark Runner (gRPC BidiReadObject / REST)"
echo " Processes:        ${PROCESSES}"
echo " Coroutines/proc:  ${COROS}"
echo " File Size:        ${FILE_SIZE_MIB} MiB"
echo " Chunk Size:       ${CHUNK_SIZE_KIB} KiB"
echo " Rounds:           ${ROUNDS}"
echo " Bucket Type:      ${BUCKET_TYPE}"
echo " Rapid Bucket:     gs://${RAPID_BUCKET}"
echo " Regional Bucket:  gs://${REGIONAL_BUCKET}"
echo " ALTS Handshakes:  ${GRPC_ALTS_MAX_CONCURRENT_HANDSHAKES}"
echo " Output JSON Path: ${OUTPUT_JSON_PATH}"
echo " Upload GCS Path:  ${UPLOAD_GCS_PREFIX:-None}"
echo "========================================================================"

export DEFAULT_RAPID_BUCKET="${RAPID_BUCKET}"
export DEFAULT_STANDARD_BUCKET="${REGIONAL_BUCKET}"
export PROCESSES="${PROCESSES}"
export COROS="${COROS}"
export FILE_SIZE_MIB="${FILE_SIZE_MIB}"
export CHUNK_SIZE_KIB="${CHUNK_SIZE_KIB}"
export ROUNDS="${ROUNDS}"
export BUCKET_TYPE="${BUCKET_TYPE}"
export GRPC_ALTS_MAX_CONCURRENT_HANDSHAKES="${GRPC_ALTS_MAX_CONCURRENT_HANDSHAKES}"

# Navigate to package directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}/.."

echo "--- 1. Setting up Python environment ---"
# Ensure python3-pip and python3-venv are present on the VM
if ! command -v pip3 &>/dev/null || ! python3 -c "import venv" 2>/dev/null; then
  echo "Installing python3-pip and python3-venv on VM..."
  sudo apt-get update && sudo apt-get install -y python3-pip python3-venv
fi

# Ensure persistent virtual environment exists and is activated
BENCH_VENV="${HOME}/bench_env"
if [ ! -d "${BENCH_VENV}" ]; then
  echo "Creating virtual environment at ${BENCH_VENV}..."
  python3 -m venv "${BENCH_VENV}"
fi
source "${BENCH_VENV}/bin/activate"

# Check and install all dependencies into virtual environment
if ! python3 -c "import pytest, psutil, yaml, google.cloud.storage" 2>/dev/null; then
  echo "Installing dependencies into virtual environment..."
  pip install --upgrade pip
  pip install -e ".[grpc,testing]"
fi

echo "--- 2. Executing pytest benchmark suite (${ROUNDS} rounds) ---"
set +e
python3 -m pytest --benchmark-json="${OUTPUT_JSON_PATH}" \
  -rA \
  tests/perf/microbenchmarks/time_based/reads/test_reads.py
TEST_EXIT_CODE=$?
set -e

if [ -s "${OUTPUT_JSON_PATH}" ]; then
  DISPLAY_SCRIPT="${SCRIPT_DIR}/display_benchmark_results.py"
  if [ ! -f "${DISPLAY_SCRIPT}" ]; then
    DISPLAY_SCRIPT="cloudbuild/display_benchmark_results.py"
  fi
  python3 "${DISPLAY_SCRIPT}" "${OUTPUT_JSON_PATH}"

  if [ -n "${UPLOAD_GCS_PREFIX}" ]; then
    GCS_DEST="${UPLOAD_GCS_PREFIX}/test_result_$(hostname)_$(date +%s).json"
    echo "Uploading JSON report to ${GCS_DEST}..."
    gcloud storage cp "${OUTPUT_JSON_PATH}" "${GCS_DEST}"
  fi
fi

echo "--- Benchmark Run Complete ---"
exit $TEST_EXIT_CODE
