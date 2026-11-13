
set -euxo pipefail
echo '--- Extracting source code tarball on VM ---'
sudo apt-get update && sudo apt-get install -y python3-pip python3-venv
tar -xzf google-cloud-storage.tar.gz
cd google-cloud-storage

echo '--- Installing Python and dependencies on VM ---'
python3 -m venv env
source env/bin/activate

echo 'Install testing libraries explicitly, as they are not in setup.py'
pip install --upgrade pip
pip install pytest pytest-timeout pytest-subtests pytest-asyncio
pip install google-cloud-testutils google-cloud-kms
pip install -e .

echo '--- Setting up environment variables on VM ---'
export RAPID_BUCKET=${_RAPID_BUCKET}
export CROSS_REGION_BUCKET=${CROSS_REGION_BUCKET:-}
export RUN_RAPID_SYSTEM_TESTS=True
export GCE_METADATA_MTLS_MODE=None
CURRENT_ULIMIT=$(ulimit -n)
echo '--- Running Rapid tests on VM with ulimit set to ---' $CURRENT_ULIMIT
pytest -vv -s --log-format='%(asctime)s %(levelname)s %(message)s' --log-date-format='%H:%M:%S' tests/system/test_rapid.py
