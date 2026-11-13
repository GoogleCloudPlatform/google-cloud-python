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

"""OAuth 2.0 credentials with DPoP (RFC 9449) proof-of-possession.

This module provides :class:`DPoPCredentials`, a subclass of
:class:`google.oauth2.credentials.Credentials` that binds OAuth 2.0
refresh and access tokens to a cryptographic key using Demonstrating
Proof-of-Possession (DPoP) as defined in `RFC 9449`_.

In Google's implementation, DPoP proofs are validated by the
authorization server during token refresh and code exchange.  A
stolen refresh token cannot be used without the corresponding
private key.

Usage with an externally-generated PEM key::

    from google.auth.dpop import SoftwareDPoPSigner
    from google.oauth2.dpop_credentials import DPoPCredentials

    signer = SoftwareDPoPSigner.from_pem(
        open("dpop_key.pem", "rb").read()
    )
    creds = DPoPCredentials.from_authorized_user_file(
        "credentials.json", dpop_signer=signer
    )

Usage with a deferred signer (e.g. hardware token)::

    creds = DPoPCredentials.from_authorized_user_file(
        "credentials.json",
        dpop_signer=lambda: MyHardwareSigner(device_id="...")
    )

.. _RFC 9449: https://www.rfc-editor.org/rfc/rfc9449
"""

import io
import json

from google.auth import exceptions, metrics
from google.auth.dpop import DPoPSigner, extract_dpop_nonce
from google.oauth2 import _client, reauth
from google.oauth2 import credentials as _oauth2_credentials

_USE_DPOP_NONCE_ERROR = "use_dpop_nonce"


class DPoPCredentials(_oauth2_credentials.Credentials):
    """OAuth 2.0 credentials with DPoP proof-of-possession.

    This is a subclass of :class:`google.oauth2.credentials.Credentials`
    that adds DPoP proof generation to token refresh requests, binding
    OAuth 2.0 tokens to a cryptographic key per `RFC 9449`_.

    In Google's implementation, DPoP proofs are validated at the
    authorization server (token endpoint) during token refresh and
    code exchange.  This prevents stolen refresh tokens from being
    used without the corresponding private key.

    .. _RFC 9449: https://www.rfc-editor.org/rfc/rfc9449
    """

    def __init__(self, token, dpop_signer=None, dpop_nonce=None, **kwargs):
        """
        Args:
            token (Optional[str]): The OAuth 2.0 access token. Can be
                None if refresh information is provided.
            dpop_signer (Union[google.auth.dpop.DPoPSigner, Callable[[], google.auth.dpop.DPoPSigner], None]):
                A DPoP signer instance, or a zero-argument callable
                that returns one.  When a callable is provided, the
                signer is constructed on first use (i.e. at token
                refresh time), deferring any hardware I/O required by
                TPM, YubiKey, or Secure Enclave signers.
            dpop_nonce (Optional[str]): A server-provided DPoP nonce
                from a previous token response. If available, it will
                be included in the next DPoP proof.
            **kwargs: All remaining keyword arguments are forwarded to
                :class:`google.oauth2.credentials.Credentials`.
        """
        super(DPoPCredentials, self).__init__(token, **kwargs)
        if callable(dpop_signer) and not isinstance(dpop_signer, DPoPSigner):
            self._dpop_signer_factory = dpop_signer
            self._dpop_signer = None
        else:
            self._dpop_signer_factory = None
            self._dpop_signer = dpop_signer
        self._dpop_nonce = dpop_nonce

    @property
    def dpop_signer(self):
        """Optional[google.auth.dpop.DPoPSigner]: The DPoP signer.

        If a callable factory was provided at construction time, it is
        invoked here on first access, and the resulting signer replaces
        the factory (one-shot resolution).
        """
        if self._dpop_signer is None and self._dpop_signer_factory is not None:
            self._dpop_signer = self._dpop_signer_factory()
            self._dpop_signer_factory = None  # one-shot; release the ref
        return self._dpop_signer

    @dpop_signer.setter
    def dpop_signer(self, signer):
        """Sets or replaces the DPoP signer.

        Use this to re-attach a signer after unpickling.

        Args:
            signer (Optional[google.auth.dpop.DPoPSigner]): The DPoP
                signer to bind to these credentials.
        """
        self._dpop_signer = signer

    @property
    def dpop_nonce(self):
        """Optional[str]: The server-provided DPoP nonce."""
        return self._dpop_nonce

    def __getstate__(self):
        """Prepares credentials for pickling.

        The DPoP signer is excluded because it holds private key
        material (cryptography key objects, ctypes handles, or hardware
        device references) that cannot be reliably pickled.  After
        unpickling, the caller must re-attach a signer via the
        ``dpop_signer`` setter before the credentials can refresh.
        """
        state = super(DPoPCredentials, self).__getstate__()
        # _dpop_signer holds unpicklable key material.
        state.pop("_dpop_signer", None)
        # _dpop_signer_factory may hold unpicklable closures/references.
        state.pop("_dpop_signer_factory", None)
        return state

    def __setstate__(self, d):
        """Restores credentials from a pickled state.

        DPoP-specific attributes are restored from the state dict.
        ``_dpop_signer`` is always set to ``None`` — the caller must
        re-attach a signer after unpickling.
        """
        super(DPoPCredentials, self).__setstate__(d)
        self._dpop_nonce = d.get("_dpop_nonce")
        # Signer and factory are never pickled; must be re-attached.
        self._dpop_signer = None
        self._dpop_signer_factory = None

    def _after_refresh(self, request, method, url, headers):
        """Attaches a DPoP proof for the resource server request.

        After credentials are refreshed, this hook creates a DPoP proof
        JWT bound to the target URL and the current access token (via
        the ``ath`` claim) per RFC 9449 §4.3.

        .. note::

            Google resource servers currently ignore the ``DPoP``
            header entirely — the ``Authorization`` header uses the
            ``Bearer`` scheme and the ``DPoP`` proof is not validated.
            This header is included for RFC 9449 compliance and
            forward compatibility with stricter enforcement.

        Args:
            request (google.auth.transport.Request): The object used to
                make HTTP requests.
            method (str): The HTTP method of the request.
            url (str): The target resource server URI.
            headers (Mapping): The request headers to update.
        """
        super(DPoPCredentials, self)._after_refresh(request, method, url, headers)
        if self.dpop_signer is not None and self.token:
            headers["DPoP"] = self.dpop_signer.create_proof(
                method,
                url,
                nonce=self._dpop_nonce,
                access_token=self.token,
            )

    def _call_refresh_grant(self, request, scopes=None):
        """DPoP-aware token refresh grant.

        Creates a DPoP proof for the token endpoint, handles
        ``use_dpop_nonce`` challenges with a single retry, and supports
        the reauth/RAPT flow when ``enable_reauth_refresh`` is set.

        Args:
            request (google.auth.transport.Request): The object used to
                make HTTP requests.
            scopes (Optional[Sequence[str]]): The requested scopes.

        Returns:
            Tuple[str, str, Optional[datetime], Mapping[str, str], str]:
                The access token, new refresh token, expiration, the
                full response data, and the rapt token.

        Raises:
            google.auth.exceptions.RefreshError: If the token endpoint
                returned an error.
            ValueError: If no ``dpop_signer`` has been set on this
                instance.
        """
        if self.dpop_signer is None:
            raise ValueError(
                "DPoPCredentials requires a dpop_signer for token "
                "refresh. Use google.oauth2.credentials.Credentials "
                "for non-DPoP flows."
            )

        token_uri = self._token_uri
        refresh_token = self._refresh_token
        client_id = self._client_id
        client_secret = self._client_secret
        rapt_token = self._rapt_token

        body = {
            "grant_type": _client._REFRESH_GRANT_TYPE,
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
        }
        if scopes:
            body["scope"] = " ".join(scopes)
        if rapt_token:
            body["rapt"] = rapt_token

        headers = {metrics.API_CLIENT_HEADER: metrics.token_request_user()}
        headers["DPoP"] = self.dpop_signer.create_proof(
            "POST", token_uri, nonce=self._dpop_nonce
        )

        (
            response_status_ok,
            response_data,
            retryable_error,
            response_headers,
        ) = _client._token_endpoint_request_no_throw(
            request,
            token_uri,
            body,
            headers=headers,
            return_response_headers=True,
        )

        # Always capture the server-provided nonce from any response.
        self._dpop_nonce = extract_dpop_nonce(response_headers) or self._dpop_nonce

        # Handle use_dpop_nonce challenge — retry once with the new
        # nonce the server just gave us.
        if (
            not response_status_ok
            and isinstance(response_data, dict)
            and response_data.get("error") == _USE_DPOP_NONCE_ERROR
        ):
            headers["DPoP"] = self.dpop_signer.create_proof(
                "POST", token_uri, nonce=self._dpop_nonce
            )
            (
                response_status_ok,
                response_data,
                retryable_error,
                response_headers,
            ) = _client._token_endpoint_request_no_throw(
                request,
                token_uri,
                body,
                headers=headers,
                return_response_headers=True,
            )
            self._dpop_nonce = extract_dpop_nonce(response_headers) or self._dpop_nonce

        # Handle reauth/RAPT challenge.
        if (
            not response_status_ok
            and isinstance(response_data, dict)
            and response_data.get("error") == reauth._REAUTH_NEEDED_ERROR
            and (
                response_data.get("error_subtype")
                == reauth._REAUTH_NEEDED_ERROR_INVALID_RAPT
                or response_data.get("error_subtype")
                == reauth._REAUTH_NEEDED_ERROR_RAPT_REQUIRED
            )
        ):
            if not self._enable_reauth_refresh:
                raise exceptions.RefreshError(
                    "Reauthentication is needed. Please run "
                    "`gcloud auth application-default login` to "
                    "reauthenticate."
                )

            rapt_token = reauth.get_rapt_token(
                request,
                client_id,
                client_secret,
                refresh_token,
                token_uri,
                scopes=scopes,
            )
            body["rapt"] = rapt_token
            headers["DPoP"] = self.dpop_signer.create_proof(
                "POST", token_uri, nonce=self._dpop_nonce
            )
            (
                response_status_ok,
                response_data,
                retryable_error,
                response_headers,
            ) = _client._token_endpoint_request_no_throw(
                request,
                token_uri,
                body,
                headers=headers,
                return_response_headers=True,
            )
            self._dpop_nonce = extract_dpop_nonce(response_headers) or self._dpop_nonce

        if not response_status_ok:
            _client._handle_error_response(response_data, retryable_error)

        return _client._handle_refresh_grant_response(response_data, refresh_token) + (
            rapt_token,
        )

    def _make_copy(self):
        cred = self.__class__(
            self.token,
            dpop_signer=self._dpop_signer or self._dpop_signer_factory,
            dpop_nonce=self._dpop_nonce,
            refresh_token=self.refresh_token,
            id_token=self.id_token,
            token_uri=self.token_uri,
            client_id=self.client_id,
            client_secret=self.client_secret,
            scopes=self.scopes,
            default_scopes=self.default_scopes,
            granted_scopes=self.granted_scopes,
            quota_project_id=self.quota_project_id,
            rapt_token=self.rapt_token,
            enable_reauth_refresh=self._enable_reauth_refresh,
            trust_boundary=self._trust_boundary,
            universe_domain=self._universe_domain,
            account=self._account,
        )
        cred._cred_file_path = self._cred_file_path
        return cred

    def to_json(self, strip=None):
        """Utility function that creates a JSON representation of a
        DPoPCredentials object.

        Args:
            strip (Sequence[str]): Optional list of members to exclude
                from the generated JSON.

        Returns:
            str: A JSON representation of this instance, including
            DPoP metadata (nonce, key ID, thumbprint).  Private key
            material is never included.
        """
        prep = json.loads(super(DPoPCredentials, self).to_json(strip))

        if self._dpop_nonce:
            prep["dpop_nonce"] = self._dpop_nonce
        if self.dpop_signer is not None:
            prep["dpop_thumbprint"] = self.dpop_signer.thumbprint
            if self.dpop_signer.key_id is not None:
                prep["dpop_key_id"] = self.dpop_signer.key_id

        return json.dumps(prep)

    @classmethod
    def from_authorized_user_info(cls, info, scopes=None, dpop_signer=None):
        """Creates a DPoPCredentials instance from parsed authorized
        user info.

        Args:
            info (Mapping[str, str]): The authorized user info in
                Google format.
            scopes (Sequence[str]): Optional list of scopes to include
                in the credentials.
            dpop_signer (Union[google.auth.dpop.DPoPSigner, Callable[[], google.auth.dpop.DPoPSigner], None]):
                A DPoP signer instance or a zero-argument callable
                that returns one.  When a callable is provided, the
                signer is constructed on first use, deferring any
                hardware I/O.

        Returns:
            google.oauth2.dpop_credentials.DPoPCredentials: The
                constructed credentials.

        Raises:
            ValueError: If the info is not in the expected format, or
                if a ``dpop_thumbprint`` is present in the info and
                does not match the provided signer's thumbprint.
        """
        # Let the parent parse and create using cls() — which will be
        # DPoPCredentials with dpop_signer=None initially.
        creds = super(DPoPCredentials, cls).from_authorized_user_info(info, scopes)

        saved_thumbprint = info.get("dpop_thumbprint")

        if callable(dpop_signer) and not isinstance(dpop_signer, DPoPSigner):
            # Factory — defer construction. Wrap with thumbprint
            # validation if a saved thumbprint exists.
            raw_factory = dpop_signer
            if saved_thumbprint:

                def _validating_factory(
                    _factory=raw_factory, _expected=saved_thumbprint
                ):
                    signer = _factory()
                    if signer.thumbprint != _expected:
                        raise ValueError(
                            "DPoP signer thumbprint '{}' does not match the "
                            "thumbprint '{}' saved in the credentials. The "
                            "refresh token is bound to the original key and "
                            "cannot be used with a different signer.".format(
                                signer.thumbprint, _expected
                            )
                        )
                    return signer

                creds._dpop_signer_factory = _validating_factory
            else:
                creds._dpop_signer_factory = raw_factory
            creds._dpop_signer = None
        else:
            # Concrete signer — validate immediately (existing behavior).
            if dpop_signer is not None and saved_thumbprint:
                if dpop_signer.thumbprint != saved_thumbprint:
                    raise ValueError(
                        "DPoP signer thumbprint '{}' does not match the "
                        "thumbprint '{}' saved in the credentials. The "
                        "refresh token is bound to the original key and "
                        "cannot be used with a different signer.".format(
                            dpop_signer.thumbprint, saved_thumbprint
                        )
                    )
            creds._dpop_signer_factory = None
            creds._dpop_signer = dpop_signer

        creds._dpop_nonce = info.get("dpop_nonce")
        return creds

    @classmethod
    def from_authorized_user_file(cls, filename, scopes=None, dpop_signer=None):
        """Creates a DPoPCredentials instance from an authorized user
        json file.

        Args:
            filename (str): The path to the authorized user json file.
            scopes (Sequence[str]): Optional list of scopes to include
                in the credentials.
            dpop_signer (Union[google.auth.dpop.DPoPSigner, Callable[[], google.auth.dpop.DPoPSigner], None]):
                A DPoP signer instance or a zero-argument callable
                that returns one.

        Returns:
            google.oauth2.dpop_credentials.DPoPCredentials: The
                constructed credentials.

        Raises:
            ValueError: If the file is not in the expected format.
        """
        with io.open(filename, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            return cls.from_authorized_user_info(data, scopes, dpop_signer=dpop_signer)
