# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import json
import os
import pickle

import pytest  # type: ignore
from cryptography.hazmat.primitives.asymmetric import ec

from google.auth import _helpers
from google.auth.crypt import base, es

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

# To generate es384_privatekey.pem, es384_privatekey.pub, and
# es384_public_cert.pem:
#   $ openssl ecparam -genkey -name secp384r1 -noout -out es384_privatekey.pem
#   $ openssl ec -in es384_privatekey.pem -pubout -out es384_publickey.pem
#   $ openssl req -new -x509 -key es384_privatekey.pem -out \
#   >     es384_public_cert.pem

with open(os.path.join(DATA_DIR, "es384_privatekey.pem"), "rb") as fh:
    PRIVATE_KEY_BYTES = fh.read()
    PKCS1_KEY_BYTES = PRIVATE_KEY_BYTES

with open(os.path.join(DATA_DIR, "es384_publickey.pem"), "rb") as fh:
    PUBLIC_KEY_BYTES = fh.read()

with open(os.path.join(DATA_DIR, "es384_public_cert.pem"), "rb") as fh:
    PUBLIC_CERT_BYTES = fh.read()

# RSA keys used to test for type errors in EsVerifier and EsSigner.
with open(os.path.join(DATA_DIR, "privatekey.pem"), "rb") as fh:
    RSA_PRIVATE_KEY_BYTES = fh.read()
    RSA_PKCS1_KEY_BYTES = RSA_PRIVATE_KEY_BYTES

with open(os.path.join(DATA_DIR, "privatekey.pub"), "rb") as fh:
    RSA_PUBLIC_KEY_BYTES = fh.read()

SERVICE_ACCOUNT_JSON_FILE = os.path.join(DATA_DIR, "es384_service_account.json")

with open(SERVICE_ACCOUNT_JSON_FILE, "rb") as fh:
    SERVICE_ACCOUNT_INFO = json.load(fh)


class TestEsVerifier(object):
    def test_verify_success(self):
        to_sign = b"foo"
        signer = es.EsSigner.from_string(PRIVATE_KEY_BYTES)
        actual_signature = signer.sign(to_sign)

        verifier = es.EsVerifier.from_string(PUBLIC_KEY_BYTES)
        assert verifier.verify(to_sign, actual_signature)

    def test_verify_unicode_success(self):
        to_sign = "foo"
        signer = es.EsSigner.from_string(PRIVATE_KEY_BYTES)
        actual_signature = signer.sign(to_sign)

        verifier = es.EsVerifier.from_string(PUBLIC_KEY_BYTES)
        assert verifier.verify(to_sign, actual_signature)

    def test_verify_failure(self):
        verifier = es.EsVerifier.from_string(PUBLIC_KEY_BYTES)
        bad_signature1 = b""
        assert not verifier.verify(b"foo", bad_signature1)
        bad_signature2 = b"a"
        assert not verifier.verify(b"foo", bad_signature2)

    def test_verify_failure_with_wrong_raw_signature(self):
        to_sign = b"foo"

        # This signature has a wrong "r" value in the "(r,s)" raw signature.
        wrong_signature = base64.urlsafe_b64decode(
            b"m7oaRxUDeYqjZ8qiMwo0PZLTMZWKJLFQREpqce1StMIa_yXQQ-C5WgeIRHW7OqlYSDL0XbUrj_uAw9i-QhfOJQ=="
        )

        verifier = es.EsVerifier.from_string(PUBLIC_KEY_BYTES)
        assert not verifier.verify(to_sign, wrong_signature)

    def test_from_string_pub_key(self):
        verifier = es.EsVerifier.from_string(PUBLIC_KEY_BYTES)
        assert isinstance(verifier, es.EsVerifier)
        assert isinstance(verifier._pubkey, ec.EllipticCurvePublicKey)

    def test_from_string_pub_key_unicode(self):
        public_key = _helpers.from_bytes(PUBLIC_KEY_BYTES)
        verifier = es.EsVerifier.from_string(public_key)
        assert isinstance(verifier, es.EsVerifier)
        assert isinstance(verifier._pubkey, ec.EllipticCurvePublicKey)

    def test_from_string_pub_cert(self):
        verifier = es.EsVerifier.from_string(PUBLIC_CERT_BYTES)
        assert isinstance(verifier, es.EsVerifier)
        assert isinstance(verifier._pubkey, ec.EllipticCurvePublicKey)

    def test_from_string_pub_cert_unicode(self):
        public_cert = _helpers.from_bytes(PUBLIC_CERT_BYTES)
        verifier = es.EsVerifier.from_string(public_cert)
        assert isinstance(verifier, es.EsVerifier)
        assert isinstance(verifier._pubkey, ec.EllipticCurvePublicKey)

    def test_from_string_type_error(self):
        with pytest.raises(TypeError):
            es.EsVerifier.from_string(RSA_PUBLIC_KEY_BYTES)


class TestEsSigner(object):
    def test_from_string_pkcs1(self):
        signer = es.EsSigner.from_string(PKCS1_KEY_BYTES)
        assert isinstance(signer, es.EsSigner)
        assert isinstance(signer._key, ec.EllipticCurvePrivateKey)

    def test_from_string_pkcs1_unicode(self):
        key_bytes = _helpers.from_bytes(PKCS1_KEY_BYTES)
        signer = es.EsSigner.from_string(key_bytes)
        assert isinstance(signer, es.EsSigner)
        assert isinstance(signer._key, ec.EllipticCurvePrivateKey)

    def test_from_string_bogus_key(self):
        key_bytes = "bogus-key"
        with pytest.raises(ValueError):
            es.EsSigner.from_string(key_bytes)

    def test_from_string_type_error(self):
        key_bytes = _helpers.from_bytes(RSA_PKCS1_KEY_BYTES)
        with pytest.raises(TypeError):
            es.EsSigner.from_string(key_bytes)

    def test_from_service_account_info(self):
        signer = es.EsSigner.from_service_account_info(SERVICE_ACCOUNT_INFO)

        assert signer.key_id == SERVICE_ACCOUNT_INFO[base._JSON_FILE_PRIVATE_KEY_ID]
        assert isinstance(signer._key, ec.EllipticCurvePrivateKey)

    def test_from_service_account_info_missing_key(self):
        with pytest.raises(ValueError) as excinfo:
            es.EsSigner.from_service_account_info({})

        assert excinfo.match(base._JSON_FILE_PRIVATE_KEY)

    def test_from_service_account_file(self):
        signer = es.EsSigner.from_service_account_file(SERVICE_ACCOUNT_JSON_FILE)

        assert signer.key_id == SERVICE_ACCOUNT_INFO[base._JSON_FILE_PRIVATE_KEY_ID]
        assert isinstance(signer._key, ec.EllipticCurvePrivateKey)

    def test_pickle(self):
        signer = es.EsSigner.from_service_account_file(SERVICE_ACCOUNT_JSON_FILE)

        assert signer.key_id == SERVICE_ACCOUNT_INFO[base._JSON_FILE_PRIVATE_KEY_ID]
        assert isinstance(signer._key, ec.EllipticCurvePrivateKey)

        pickled_signer = pickle.dumps(signer)
        signer = pickle.loads(pickled_signer)

        assert signer.key_id == SERVICE_ACCOUNT_INFO[base._JSON_FILE_PRIVATE_KEY_ID]
        assert isinstance(signer._key, ec.EllipticCurvePrivateKey)
