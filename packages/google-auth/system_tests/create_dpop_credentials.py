# Copyright 2026 Google LLC
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

"""Create system_tests/data/dpop_authorized_user.json using system_tests/data/dpop_key.pem.

Usage:
    python system_tests/create_dpop_credentials.py
"""

import hashlib
import http.server
import json
import os
import secrets
import urllib.parse
import webbrowser

import requests

from google.auth import _helpers, dpop
from google.oauth2 import dpop_credentials

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
CLIENT_SECRETS_FILE = os.path.join(DATA_DIR, "dpop_client_secrets.json")
KEY_FILE = os.path.join(DATA_DIR, "dpop_key.pem")
CREDS_FILE = os.path.join(DATA_DIR, "dpop_authorized_user.json")
AUTH_URI = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URI = "https://oauth2.googleapis.com/token"
SCOPES = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/cloud-platform",
    "openid",
]


def _capture_auth_code(auth_uri, client_id, state, code_challenge):
    result = {}

    class _Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urllib.parse.urlsplit(self.path)
            if parsed.path not in ("", "/"):
                self.send_response(404)
                self.end_headers()
                return
            params = urllib.parse.parse_qs(parsed.query)
            result["state"] = params.get("state", [None])[0]
            result["code"] = params.get("code", [None])[0]
            result["error"] = params.get("error", [None])[0]
            self.send_response(400 if result["error"] else 200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"DPoP authorization complete. You may close this tab.")

        def log_message(self, format, *args):
            return

    server = http.server.HTTPServer(("127.0.0.1", 0), _Handler)
    try:
        redirect_uri = "http://127.0.0.1:{}".format(server.server_port)
        url = "{}?{}".format(
            auth_uri,
            urllib.parse.urlencode(
                {
                    "client_id": client_id,
                    "redirect_uri": redirect_uri,
                    "response_type": "code",
                    "scope": " ".join(SCOPES),
                    "state": state,
                    "code_challenge": code_challenge,
                    "code_challenge_method": "S256",
                    "access_type": "offline",
                    "prompt": "consent",
                }
            ),
        )
        print("Open this URL to authorize:\n{}".format(url))
        webbrowser.open(url)
        while "state" not in result:
            server.handle_request()
    finally:
        server.server_close()

    if result.get("error") or result.get("state") != state or not result.get("code"):
        raise SystemExit("Authorization failed: {}".format(result))
    return result["code"], redirect_uri


def main():
    if not os.path.isfile(KEY_FILE):
        raise SystemExit(
            "Key not found at {p}. Generate one first with:\n"
            "  openssl ecparam -name prime256v1 -genkey -noout -out {p}".format(
                p=KEY_FILE
            )
        )
    if not os.path.isfile(CLIENT_SECRETS_FILE):
        raise SystemExit(
            "OAuth client secrets not found at {p}.\n"
            "Download a Desktop OAuth client JSON from Cloud Console and save it there.".format(
                p=CLIENT_SECRETS_FILE
            )
        )

    with open(KEY_FILE, "rb") as fh:
        signer = dpop.SoftwareDPoPSigner.from_pem(fh.read())
    with open(CLIENT_SECRETS_FILE, "r", encoding="utf-8") as fh:
        raw = json.load(fh)
    cfg = raw.get("installed") or raw.get("web") or raw
    client_id, client_secret = cfg["client_id"], cfg["client_secret"]
    auth_uri = cfg.get("auth_uri", AUTH_URI)
    token_uri = cfg.get("token_uri", TOKEN_URI)

    state = secrets.token_urlsafe(24)
    verifier = _helpers.unpadded_urlsafe_b64encode(secrets.token_bytes(32)).decode(
        "ascii"
    )
    challenge = _helpers.unpadded_urlsafe_b64encode(
        hashlib.sha256(verifier.encode("ascii")).digest()
    ).decode("ascii")

    code, redirect_uri = _capture_auth_code(auth_uri, client_id, state, challenge)

    jti = dpop.compute_auth_code_jti(code)
    body = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret,
        "code_verifier": verifier,
    }
    nonce = None
    for attempt in range(2):
        proof = signer.create_proof("POST", token_uri, nonce=nonce, jti=jti)
        resp = requests.post(token_uri, data=body, headers={"dpop": proof}, timeout=30)
        nonce = dpop._extract_dpop_nonce(resp.headers) or nonce
        data = resp.json() if resp.text else {}
        if resp.status_code == 200:
            break
        if (
            attempt == 0
            and resp.status_code == 400
            and data.get("error") == "use_dpop_nonce"
            and nonce
        ):
            continue
        raise SystemExit(
            "Token exchange failed ({}): {}".format(resp.status_code, resp.text)
        )

    creds = dpop_credentials.DPoPCredentials(
        token=data.get("access_token"),
        refresh_token=data["refresh_token"],
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret,
        scopes=SCOPES,
        dpop_signer=signer,
        dpop_nonce=nonce,
    )
    os.makedirs(DATA_DIR, exist_ok=True)
    fd = os.open(CREDS_FILE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(json.loads(creds.to_json()), indent=2) + "\n")
    print("Saved DPoP credentials to {}".format(CREDS_FILE))


if __name__ == "__main__":
    main()
