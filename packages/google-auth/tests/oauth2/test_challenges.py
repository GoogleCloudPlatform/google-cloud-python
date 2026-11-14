# Copyright 2021 Google LLC
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

"""Tests for the reauth module."""

import base64
import hashlib
import json
import types
from typing import Any
from unittest import mock

import pytest  # type: ignore

from google.auth import exceptions
from google.oauth2 import challenges
from google.oauth2.webauthn_types import (
    AuthenticationExtensionsClientInputs,
    AuthenticatorAssertionResponse,
    GetRequest,
    GetResponse,
    PublicKeyCredentialDescriptor,
)


class FakeAPDU:
    WRONG_DATA = "wrong data"
    USE_NOT_SATISFIED = "use not satisfied"


class FakeApduError(Exception):
    def __init__(self, code):
        self.code = code


class FakeCtapError(Exception):
    class ERR:
        TIMEOUT = "timeout"
        ACTION_TIMEOUT = "action timeout"
        KEEPALIVE_CANCEL = "keepalive cancel"
        OPERATION_DENIED = "operation denied"

    def __init__(self, code):
        self.code = code


class FakeCtapHidDevice:
    devices: list[Any] = []

    @classmethod
    def list_devices(cls):
        return iter(cls.devices)


class FakeCtap1:
    calls: list[Any] = []
    side_effects: list[Any] = []

    def __init__(self, device):
        self.device = device

    def authenticate(self, client_param, app_param, key_handle):
        self.calls.append((self.device, client_param, app_param, key_handle))
        effect = self.side_effects.pop(0)
        if isinstance(effect, Exception):
            raise effect
        return effect


class FakeRegisteredKey:
    def __init__(self, key):
        self.key = key


class FakeU2FError(Exception):
    DEVICE_INELIGIBLE = "device ineligible"
    TIMEOUT = "timeout"
    BAD_REQUEST = "bad request"

    def __init__(self, code):
        self.code = code


class FakePluginError(Exception):
    pass


class FakeNoDeviceFoundError(Exception):
    pass


class FakeCompositeAuthenticator:
    origins: list[str] = []
    calls: list[Any] = []
    side_effects: list[Any] = []

    def Authenticate(self, app_id, challenge_data, print_callback=None):
        self.calls.append((app_id, challenge_data, print_callback))
        effect = self.side_effects.pop(0)
        if isinstance(effect, Exception):
            raise effect
        return effect


def use_fake_fido2(challenge, devices=None, side_effects=None):
    FakeCtapHidDevice.devices = devices if devices is not None else ["security-key"]
    FakeCtap1.calls = []
    FakeCtap1.side_effects = (
        side_effects if side_effects is not None else [b"signature data"]
    )
    return mock.patch.object(
        challenge,
        "_get_fido2_classes",
        return_value=(
            FakeCtapHidDevice,
            FakeCtap1,
            FakeAPDU,
            FakeApduError,
            FakeCtapError,
        ),
    )


def create_composite_authenticator(origin):
    FakeCompositeAuthenticator.origins.append(origin)
    return FakeCompositeAuthenticator()


def use_fake_pyu2f(side_effects=None):
    FakeCompositeAuthenticator.origins = []
    FakeCompositeAuthenticator.calls = []
    FakeCompositeAuthenticator.side_effects = (
        side_effects if side_effects is not None else ["security key response"]
    )

    pyu2f = types.ModuleType("pyu2f")
    convenience = types.ModuleType("pyu2f.convenience")
    authenticator = types.ModuleType("pyu2f.convenience.authenticator")
    errors = types.ModuleType("pyu2f.errors")
    model = types.ModuleType("pyu2f.model")

    authenticator.CreateCompositeAuthenticator = create_composite_authenticator
    convenience.authenticator = authenticator
    errors.U2FError = FakeU2FError
    errors.PluginError = FakePluginError
    errors.NoDeviceFoundError = FakeNoDeviceFoundError
    model.RegisteredKey = FakeRegisteredKey
    pyu2f.convenience = convenience
    pyu2f.errors = errors
    pyu2f.model = model

    return mock.patch.dict(
        "sys.modules",
        {
            "pyu2f": pyu2f,
            "pyu2f.convenience": convenience,
            "pyu2f.convenience.authenticator": authenticator,
            "pyu2f.errors": errors,
            "pyu2f.model": model,
        },
    )


def expected_client_data(challenge):
    challenge_b64 = base64.urlsafe_b64encode(challenge).decode().rstrip("=")
    return json.dumps(
        {
            "challenge": challenge_b64,
            "origin": challenges.REAUTH_ORIGIN,
            "typ": challenges.U2F_AUTHENTICATION_TYPE,
        },
        sort_keys=True,
    ).encode()


def test_get_user_password():
    with mock.patch("getpass.getpass", return_value="foo"):
        assert challenges.get_user_password("") == "foo"


def test_security_key():
    metadata = {
        "status": "READY",
        "challengeId": 2,
        "challengeType": "SECURITY_KEY",
        "securityKey": {
            "applicationId": "security_key_application_id",
            "challenges": [
                {
                    "keyHandle": "some_key",
                    "challenge": base64.urlsafe_b64encode(
                        "some_challenge".encode("ascii")
                    ).decode("ascii"),
                }
            ],
            "relyingPartyId": "security_key_application_id",
        },
    }
    challenge = challenges.SecurityKeyChallenge()
    assert challenge._get_fido2_classes()

    # Test the case that security key challenge is passed with applicationId and
    # relyingPartyId the same.
    with use_fake_fido2(challenge):
        assert challenge.name == "SECURITY_KEY"
        assert challenge.is_locally_eligible
        assert challenge.obtain_challenge_input(metadata) == {
            "securityKey": {
                "clientData": base64.urlsafe_b64encode(
                    expected_client_data(b"some_challenge")
                )
                .decode()
                .rstrip("="),
                "signatureData": "c2lnbmF0dXJlIGRhdGE",
                "applicationId": "security_key_application_id",
                "keyHandle": "some_key",
            }
        }
        assert FakeCtap1.calls == [
            (
                "security-key",
                hashlib.sha256(expected_client_data(b"some_challenge")).digest(),
                hashlib.sha256(b"security_key_application_id").digest(),
                base64.urlsafe_b64decode("some_key"),
            )
        ]

    # Test the case that webauthn plugin is available
    with (
        mock.patch(
            "google.oauth2.challenges.SecurityKeyChallenge._obtain_challenge_input_webauthn",
            return_value={"securityKey": "security key response"},
        ),
        mock.patch(
            "google.oauth2.webauthn_handler.PluginHandler.is_available",
            return_value=True,
        ),
    ):
        assert challenge.obtain_challenge_input(metadata) == {
            "securityKey": "security key response"
        }

    with (
        mock.patch(
            "google.oauth2.challenges.webauthn_handler_factory.WebauthnHandlerFactory",
            side_effect=Exception(),
        ),
        use_fake_fido2(challenge),
    ):
        assert (
            challenge.obtain_challenge_input(metadata)["securityKey"]["applicationId"]
            == "security_key_application_id"
        )

    # Test the case that security key challenge is passed with applicationId and
    # relyingPartyId different, first call works.
    metadata["securityKey"]["relyingPartyId"] = "security_key_relying_party_id"
    with use_fake_fido2(challenge):
        assert challenge.name == "SECURITY_KEY"
        assert challenge.is_locally_eligible
        assert challenge.obtain_challenge_input(metadata) == {
            "securityKey": {
                "clientData": base64.urlsafe_b64encode(
                    expected_client_data(b"some_challenge")
                )
                .decode()
                .rstrip("="),
                "signatureData": "c2lnbmF0dXJlIGRhdGE",
                "applicationId": "security_key_relying_party_id",
                "keyHandle": "some_key",
            }
        }
        assert FakeCtap1.calls == [
            (
                "security-key",
                hashlib.sha256(expected_client_data(b"some_challenge")).digest(),
                hashlib.sha256(b"security_key_relying_party_id").digest(),
                base64.urlsafe_b64decode("some_key"),
            )
        ]

    # Test the case that security key challenge is passed with applicationId and
    # relyingPartyId different, first call fails, requires retry.
    metadata["securityKey"]["relyingPartyId"] = "security_key_relying_party_id"
    with use_fake_fido2(
        challenge,
        side_effects=[
            FakeApduError(FakeAPDU.WRONG_DATA),
            b"security key response",
        ],
    ):
        assert challenge.name == "SECURITY_KEY"
        assert challenge.is_locally_eligible
        assert (
            challenge.obtain_challenge_input(metadata)["securityKey"]["applicationId"]
            == "security_key_application_id"
        )
        assert [call[2] for call in FakeCtap1.calls] == [
            hashlib.sha256(b"security_key_relying_party_id").digest(),
            hashlib.sha256(b"security_key_application_id").digest(),
        ]

    # Test various types of exceptions.
    metadata["securityKey"]["relyingPartyId"] = "security_key_application_id"
    with use_fake_fido2(challenge, side_effects=[FakeApduError(FakeAPDU.WRONG_DATA)]):
        with pytest.raises(exceptions.ReauthFailError) as excinfo:
            challenge.obtain_challenge_input(metadata)
        assert excinfo.match("Ineligible security key.")

    with use_fake_fido2(
        challenge,
        side_effects=[FakeApduError(FakeAPDU.USE_NOT_SATISFIED)],
    ):
        with pytest.raises(exceptions.ReauthFailError) as excinfo:
            challenge.obtain_challenge_input(metadata)
        assert excinfo.match("Timed out waiting for security key touch.")

    with use_fake_fido2(
        challenge,
        side_effects=[FakeCtapError(FakeCtapError.ERR.TIMEOUT)],
    ):
        with pytest.raises(exceptions.ReauthFailError) as excinfo:
            challenge.obtain_challenge_input(metadata)
        assert excinfo.match("Timed out waiting for security key touch.")

    with use_fake_fido2(challenge, side_effects=[FakeApduError("bad request")]):
        with pytest.raises(FakeApduError):
            challenge.obtain_challenge_input(metadata)

    with use_fake_fido2(challenge, side_effects=[FakeCtapError("bad request")]):
        with pytest.raises(FakeCtapError):
            challenge.obtain_challenge_input(metadata)

    with use_fake_fido2(challenge, devices=[]):
        with pytest.raises(exceptions.ReauthFailError) as excinfo:
            challenge.obtain_challenge_input(metadata)
        assert excinfo.match("No security key found.")

    with (
        use_fake_fido2(challenge),
        mock.patch.object(
            FakeCtapHidDevice,
            "list_devices",
            side_effect=OSError("permission denied"),
        ),
    ):
        with pytest.raises(exceptions.ReauthFailError) as excinfo:
            challenge.obtain_challenge_input(metadata)
        assert excinfo.match("Failed to list security keys.")
        assert isinstance(excinfo.value.__cause__, OSError)

    with use_fake_fido2(
        challenge,
        devices=["first-key", "second-key"],
        side_effects=[
            OSError("permission denied"),
            b"security key response",
        ],
    ):
        assert (
            challenge.obtain_challenge_input(metadata)["securityKey"]["applicationId"]
            == "security_key_application_id"
        )
        assert [call[0] for call in FakeCtap1.calls] == ["first-key", "second-key"]

    with (
        mock.patch.object(
            challenge,
            "_get_fido2_classes",
            side_effect=ImportError("fido2"),
        ),
        use_fake_pyu2f(),
        pytest.warns(DeprecationWarning, match="pyu2f is deprecated"),
    ):
        assert challenge.obtain_challenge_input(metadata) == {
            "securityKey": "security key response"
        }
        assert FakeCompositeAuthenticator.origins == [challenges.REAUTH_ORIGIN]
        assert FakeCompositeAuthenticator.calls[0][0] == "security_key_application_id"

    metadata["securityKey"]["relyingPartyId"] = "security_key_relying_party_id"
    with (
        mock.patch.object(
            challenge,
            "_get_fido2_classes",
            side_effect=ImportError("fido2"),
        ),
        use_fake_pyu2f(
            side_effects=[
                FakeU2FError(FakeU2FError.DEVICE_INELIGIBLE),
                "security key response",
            ],
        ),
        pytest.warns(DeprecationWarning, match="pyu2f is deprecated"),
    ):
        assert challenge.obtain_challenge_input(metadata) == {
            "securityKey": "security key response"
        }
        assert [call[0] for call in FakeCompositeAuthenticator.calls] == [
            "security_key_relying_party_id",
            "security_key_application_id",
        ]

    metadata["securityKey"]["relyingPartyId"] = "security_key_application_id"
    with (
        mock.patch.object(
            challenge,
            "_get_fido2_classes",
            side_effect=ImportError("fido2"),
        ),
        use_fake_pyu2f(side_effects=[FakeU2FError(FakeU2FError.DEVICE_INELIGIBLE)]),
        pytest.warns(DeprecationWarning, match="pyu2f is deprecated"),
    ):
        assert challenge.obtain_challenge_input(metadata) is None

    with (
        mock.patch.object(
            challenge,
            "_get_fido2_classes",
            side_effect=ImportError("fido2"),
        ),
        use_fake_pyu2f(side_effects=[FakeU2FError(FakeU2FError.TIMEOUT)]),
        pytest.warns(DeprecationWarning, match="pyu2f is deprecated"),
    ):
        assert challenge.obtain_challenge_input(metadata) is None

    with (
        mock.patch.object(
            challenge,
            "_get_fido2_classes",
            side_effect=ImportError("fido2"),
        ),
        use_fake_pyu2f(side_effects=[FakePluginError("plugin error")]),
        pytest.warns(DeprecationWarning, match="pyu2f is deprecated"),
    ):
        assert challenge.obtain_challenge_input(metadata) is None

    with (
        mock.patch.object(
            challenge,
            "_get_fido2_classes",
            side_effect=ImportError("fido2"),
        ),
        use_fake_pyu2f(side_effects=[FakeNoDeviceFoundError()]),
        pytest.warns(DeprecationWarning, match="pyu2f is deprecated"),
    ):
        assert challenge.obtain_challenge_input(metadata) is None

    with (
        mock.patch.object(
            challenge,
            "_get_fido2_classes",
            side_effect=ImportError("fido2"),
        ),
        use_fake_pyu2f(side_effects=[FakeU2FError(FakeU2FError.BAD_REQUEST)]),
        pytest.warns(DeprecationWarning, match="pyu2f is deprecated"),
    ):
        with pytest.raises(FakeU2FError):
            challenge.obtain_challenge_input(metadata)

    real_import = __import__

    def block_fido2(name, *args, **kwargs):
        if name == "fido2" or name.startswith("fido2."):
            raise ImportError(name)
        return real_import(name, *args, **kwargs)

    assert block_fido2("json") is json

    with mock.patch("builtins.__import__", side_effect=block_fido2):
        with pytest.raises(ImportError):
            challenge._get_fido2_classes()

    def block_security_key_imports(name, *args, **kwargs):
        if (
            name == "fido2"
            or name.startswith("fido2.")
            or name == "pyu2f"
            or name.startswith("pyu2f.")
        ):
            raise ImportError(name)
        return real_import(name, *args, **kwargs)

    assert block_security_key_imports("json") is json

    with mock.patch("builtins.__import__", side_effect=block_security_key_imports):
        with pytest.raises(exceptions.ReauthFailError) as excinfo:
            challenge.obtain_challenge_input(metadata)
        assert excinfo.match(r"fido2 dependency is required")


def test_security_key_webauthn():
    metadata = {
        "status": "READY",
        "challengeId": 2,
        "challengeType": "SECURITY_KEY",
        "securityKey": {
            "applicationId": "security_key_application_id",
            "challenges": [
                {
                    "keyHandle": "some_key",
                    "challenge": base64.urlsafe_b64encode(
                        "some_challenge".encode("ascii")
                    ).decode("ascii"),
                }
            ],
            "relyingPartyId": "security_key_application_id",
        },
    }

    challenge = challenges.SecurityKeyChallenge()

    sk = metadata["securityKey"]
    sk_challenges = sk["challenges"]

    application_id = sk["applicationId"]

    allow_credentials = []
    for sk_challenge in sk_challenges:
        allow_credentials.append(
            PublicKeyCredentialDescriptor(id=sk_challenge["keyHandle"])
        )

    extension = AuthenticationExtensionsClientInputs(appid=application_id)

    get_request = GetRequest(
        origin=challenges.REAUTH_ORIGIN,
        rpid=application_id,
        challenge=challenge._unpadded_urlsafe_b64recode(sk_challenge["challenge"]),
        timeout_ms=challenges.WEBAUTHN_TIMEOUT_MS,
        allow_credentials=allow_credentials,
        user_verification="preferred",
        extensions=extension,
    )

    assertion_resp = AuthenticatorAssertionResponse(
        client_data_json="clientDataJSON",
        authenticator_data="authenticatorData",
        signature="signature",
        user_handle="userHandle",
    )
    get_response = GetResponse(
        id="id",
        response=assertion_resp,
        authenticator_attachment="authenticatorAttachment",
        client_extension_results="clientExtensionResults",
    )
    response = {
        "clientData": get_response.response.client_data_json,
        "authenticatorData": get_response.response.authenticator_data,
        "signatureData": get_response.response.signature,
        "applicationId": "security_key_application_id",
        "keyHandle": get_response.id,
        "securityKeyReplyType": 2,
    }

    mock_handler = mock.Mock()
    mock_handler.get.return_value = get_response

    # Test success case
    assert challenge._obtain_challenge_input_webauthn(metadata, mock_handler) == {
        "securityKey": response
    }
    mock_handler.get.assert_called_with(get_request)

    # Test exceptions

    # Missing Values
    sk = metadata["securityKey"]
    metadata["securityKey"] = None
    with pytest.raises(exceptions.InvalidValue):
        challenge._obtain_challenge_input_webauthn(metadata, mock_handler)
    metadata["securityKey"] = sk

    c = metadata["securityKey"]["challenges"]
    metadata["securityKey"]["challenges"] = None
    with pytest.raises(exceptions.InvalidValue):
        challenge._obtain_challenge_input_webauthn(metadata, mock_handler)
    metadata["securityKey"]["challenges"] = []
    with pytest.raises(exceptions.InvalidValue):
        challenge._obtain_challenge_input_webauthn(metadata, mock_handler)
    metadata["securityKey"]["challenges"] = c

    aid = metadata["securityKey"]["applicationId"]
    metadata["securityKey"]["applicationId"] = None
    with pytest.raises(exceptions.InvalidValue):
        challenge._obtain_challenge_input_webauthn(metadata, mock_handler)
    metadata["securityKey"]["applicationId"] = aid

    rpi = metadata["securityKey"]["relyingPartyId"]
    metadata["securityKey"]["relyingPartyId"] = None
    with pytest.raises(exceptions.InvalidValue):
        challenge._obtain_challenge_input_webauthn(metadata, mock_handler)
    metadata["securityKey"]["relyingPartyId"] = rpi

    kh = metadata["securityKey"]["challenges"][0]["keyHandle"]
    metadata["securityKey"]["challenges"][0]["keyHandle"] = None
    with pytest.raises(exceptions.InvalidValue):
        challenge._obtain_challenge_input_webauthn(metadata, mock_handler)
    metadata["securityKey"]["challenges"][0]["keyHandle"] = kh

    ch = metadata["securityKey"]["challenges"][0]["challenge"]
    metadata["securityKey"]["challenges"][0]["challenge"] = None
    with pytest.raises(exceptions.InvalidValue):
        challenge._obtain_challenge_input_webauthn(metadata, mock_handler)
    metadata["securityKey"]["challenges"][0]["challenge"] = ch

    # Handler Exceptions
    mock_handler.get.side_effect = exceptions.MalformedError
    with pytest.raises(exceptions.MalformedError):
        challenge._obtain_challenge_input_webauthn(metadata, mock_handler)

    mock_handler.get.side_effect = exceptions.InvalidResource
    with pytest.raises(exceptions.InvalidResource):
        challenge._obtain_challenge_input_webauthn(metadata, mock_handler)

    mock_handler.get.side_effect = exceptions.ReauthFailError
    with pytest.raises(exceptions.ReauthFailError):
        challenge._obtain_challenge_input_webauthn(metadata, mock_handler)


@mock.patch("getpass.getpass", return_value="foo")
def test_password_challenge(getpass_mock):
    challenge = challenges.PasswordChallenge()

    with mock.patch("getpass.getpass", return_value="foo"):
        assert challenge.is_locally_eligible
        assert challenge.name == "PASSWORD"
        assert challenges.PasswordChallenge().obtain_challenge_input({}) == {
            "credential": "foo"
        }

    with mock.patch("getpass.getpass", return_value=None):
        assert challenges.PasswordChallenge().obtain_challenge_input({}) == {
            "credential": " "
        }


def test_saml_challenge():
    challenge = challenges.SamlChallenge()
    assert challenge.is_locally_eligible
    assert challenge.name == "SAML"
    with pytest.raises(exceptions.ReauthSamlChallengeFailError):
        challenge.obtain_challenge_input(None)
