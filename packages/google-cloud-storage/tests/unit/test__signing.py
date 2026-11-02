# -*- coding: utf-8 -*-
#
# Copyright 2017 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import binascii
import calendar
import datetime
import json
import time
import unittest
import urllib.parse

import mock
import pytest

from google.cloud.storage._helpers import _UTC

from . import _read_local_json

_SERVICE_ACCOUNT_JSON = _read_local_json("url_signer_v4_test_account.json")
_CONFORMANCE_TESTS = _read_local_json("url_signer_v4_test_data.json")["signingV4Tests"]
_BUCKET_TESTS = [
    test for test in _CONFORMANCE_TESTS if "bucket" in test and not test.get("object")
]
_BLOB_TESTS = [
    test for test in _CONFORMANCE_TESTS if "bucket" in test and test.get("object")
]


def _utc_seconds(when):
    return int(calendar.timegm(when.timetuple()))


def _make_cet_timezone():
    from datetime import timedelta, timezone

    return timezone(timedelta(hours=1), name="CET")


class Test_get_expiration_seconds_v2(unittest.TestCase):
    @staticmethod
    def _call_fut(expiration):
        from google.cloud.storage._signing import get_expiration_seconds_v2

        return get_expiration_seconds_v2(expiration)

    def test_w_invalid_expiration_type(self):
        with self.assertRaises(TypeError):
            self._call_fut(object(), None)

    def test_w_expiration_none(self):
        with self.assertRaises(TypeError):
            self._call_fut(None)

    def test_w_expiration_int(self):
        self.assertEqual(self._call_fut(123), 123)

    def test_w_expiration_naive_datetime(self):
        expiration_no_tz = datetime.datetime(2004, 8, 19, 0, 0, 0, 0)
        utc_seconds = _utc_seconds(expiration_no_tz)
        self.assertEqual(self._call_fut(expiration_no_tz), utc_seconds)

    def test_w_expiration_utc_datetime(self):
        expiration_utc = datetime.datetime(2004, 8, 19, 0, 0, 0, 0, _UTC)
        utc_seconds = _utc_seconds(expiration_utc)
        self.assertEqual(self._call_fut(expiration_utc), utc_seconds)

    def test_w_expiration_other_zone_datetime(self):
        zone = _make_cet_timezone()
        expiration_other = datetime.datetime(2004, 8, 19, 0, 0, 0, 0, zone)
        utc_seconds = _utc_seconds(expiration_other)
        cet_seconds = utc_seconds - (60 * 60)  # CET one hour earlier than UTC
        self.assertEqual(self._call_fut(expiration_other), cet_seconds)

    def test_w_expiration_timedelta_seconds(self):
        fake_utcnow = datetime.datetime(2004, 8, 19, 0, 0, 0, 0, _UTC)
        utc_seconds = _utc_seconds(fake_utcnow)
        expiration_as_delta = datetime.timedelta(seconds=10)

        patch = mock.patch(
            "google.cloud.storage._signing._NOW", return_value=fake_utcnow
        )
        with patch as utcnow:
            result = self._call_fut(expiration_as_delta)

        self.assertEqual(result, utc_seconds + 10)
        utcnow.assert_called_once_with(datetime.timezone.utc)

    def test_w_expiration_timedelta_days(self):
        fake_utcnow = datetime.datetime(2004, 8, 19, 0, 0, 0, 0, _UTC)
        utc_seconds = _utc_seconds(fake_utcnow)
        expiration_as_delta = datetime.timedelta(days=1)

        patch = mock.patch(
            "google.cloud.storage._signing._NOW", return_value=fake_utcnow
        )
        with patch as utcnow:
            result = self._call_fut(expiration_as_delta)

        self.assertEqual(result, utc_seconds + 86400)
        utcnow.assert_called_once_with(datetime.timezone.utc)


class Test_get_expiration_seconds_v4(unittest.TestCase):
    @staticmethod
    def _call_fut(expiration):
        from google.cloud.storage._signing import get_expiration_seconds_v4

        return get_expiration_seconds_v4(expiration)

    def test_w_invalid_expiration_type(self):
        with self.assertRaises(TypeError):
            self._call_fut(object(), None)

    def test_w_expiration_none(self):
        with self.assertRaises(TypeError):
            self._call_fut(None)

    def test_w_expiration_int_gt_seven_days(self):
        fake_utcnow = datetime.datetime(2004, 8, 19, 0, 0, 0, 0)
        delta = datetime.timedelta(days=10)
        expiration_utc = fake_utcnow + delta
        expiration_seconds = _utc_seconds(expiration_utc)

        patch = mock.patch(
            "google.cloud.storage._signing._NOW", return_value=fake_utcnow
        )

        with patch as utcnow:
            with self.assertRaises(ValueError):
                self._call_fut(expiration_seconds)
        utcnow.assert_called_once_with(datetime.timezone.utc)

    def test_w_expiration_int(self):
        fake_utcnow = datetime.datetime(2004, 8, 19, 0, 0, 0, 0)
        expiration_seconds = 10

        patch = mock.patch(
            "google.cloud.storage._signing._NOW", return_value=fake_utcnow
        )

        with patch as utcnow:
            result = self._call_fut(expiration_seconds)

        self.assertEqual(result, expiration_seconds)
        utcnow.assert_called_once_with(datetime.timezone.utc)

    def test_w_expiration_naive_datetime(self):
        fake_utcnow = datetime.datetime(2004, 8, 19, 0, 0, 0, 0, _UTC)
        delta = datetime.timedelta(seconds=10)
        expiration_no_tz = fake_utcnow + delta

        patch = mock.patch(
            "google.cloud.storage._signing._NOW", return_value=fake_utcnow
        )
        with patch as utcnow:
            result = self._call_fut(expiration_no_tz)

        self.assertEqual(result, delta.seconds)
        utcnow.assert_called_once()

    def test_w_expiration_utc_datetime(self):
        fake_utcnow = datetime.datetime(2004, 8, 19, 0, 0, 0, 0, _UTC)
        delta = datetime.timedelta(seconds=10)
        expiration_utc = fake_utcnow + delta

        patch = mock.patch(
            "google.cloud.storage._signing._NOW", return_value=fake_utcnow
        )
        with patch as utcnow:
            result = self._call_fut(expiration_utc)

        self.assertEqual(result, delta.seconds)
        utcnow.assert_called_once_with(datetime.timezone.utc)

    def test_w_expiration_other_zone_datetime(self):
        zone = _make_cet_timezone()
        fake_utcnow = datetime.datetime(2004, 8, 19, 0, 0, 0, 0, _UTC)
        fake_cetnow = fake_utcnow.astimezone(zone)
        delta = datetime.timedelta(seconds=10)
        expiration_other = fake_cetnow + delta

        patch = mock.patch(
            "google.cloud.storage._signing._NOW", return_value=fake_utcnow
        )
        with patch as utcnow:
            result = self._call_fut(expiration_other)
        self.assertEqual(result, delta.seconds)
        utcnow.assert_called_once_with(datetime.timezone.utc)

    def test_w_expiration_timedelta(self):
        fake_utcnow = datetime.datetime(2004, 8, 19, 0, 0, 0, 0, _UTC)
        expiration_as_delta = datetime.timedelta(seconds=10)

        patch = mock.patch(
            "google.cloud.storage._signing._NOW", return_value=fake_utcnow
        )
        with patch as utcnow:
            result = self._call_fut(expiration_as_delta)

        self.assertEqual(result, expiration_as_delta.total_seconds())
        utcnow.assert_called_once_with(datetime.timezone.utc)


class Test_get_signed_query_params_v2(unittest.TestCase):
    @staticmethod
    def _call_fut(credentials, expiration, string_to_sign):
        from google.cloud.storage._signing import get_signed_query_params_v2

        return get_signed_query_params_v2(credentials, expiration, string_to_sign)

    def test_it(self):
        sig_bytes = b"DEADBEEF"
        account_name = mock.sentinel.service_account_email
        credentials = _make_credentials(signer_email=account_name)
        credentials.sign_bytes.return_value = sig_bytes
        expiration = 100
        string_to_sign = "fake_signature"
        result = self._call_fut(credentials, expiration, string_to_sign)

        expected = {
            "GoogleAccessId": account_name,
            "Expires": expiration,
            "Signature": base64.b64encode(sig_bytes),
        }
        self.assertEqual(result, expected)
        credentials.sign_bytes.assert_called_once_with(string_to_sign.encode("ascii"))


class Test_get_canonical_headers(unittest.TestCase):
    @staticmethod
    def _call_fut(*args, **kwargs):
        from google.cloud.storage._signing import get_canonical_headers

        return get_canonical_headers(*args, **kwargs)

    def test_w_none(self):
        headers = None
        expected_canonical = []
        expected_ordered = []
        canonical, ordered = self._call_fut(headers)
        self.assertEqual(canonical, expected_canonical)
        self.assertEqual(ordered, expected_ordered)

    def test_w_dict(self):
        headers = {"foo": "Foo 1.2.3", "Bar": " baz,bam,qux   "}
        expected_canonical = ["bar:baz,bam,qux", "foo:Foo 1.2.3"]
        expected_ordered = [tuple(item.split(":")) for item in expected_canonical]
        canonical, ordered = self._call_fut(headers)
        self.assertEqual(canonical, expected_canonical)
        self.assertEqual(ordered, expected_ordered)

    def test_w_list_and_multiples(self):
        headers = [
            ("foo", "Foo 1.2.3"),
            ("Bar", " baz"),
            ("Bar", "bam"),
            ("Bar", "qux   "),
        ]
        expected_canonical = ["bar:baz,bam,qux", "foo:Foo 1.2.3"]
        expected_ordered = [tuple(item.split(":")) for item in expected_canonical]
        canonical, ordered = self._call_fut(headers)
        self.assertEqual(canonical, expected_canonical)
        self.assertEqual(ordered, expected_ordered)

    def test_w_embedded_ws(self):
        headers = {"foo": "Foo\n1.2.3", "Bar": "   baz   bam   qux   "}
        expected_canonical = ["bar:baz bam qux", "foo:Foo 1.2.3"]
        expected_ordered = [tuple(item.split(":")) for item in expected_canonical]
        canonical, ordered = self._call_fut(headers)
        self.assertEqual(canonical, expected_canonical)
        self.assertEqual(ordered, expected_ordered)


class Test_canonicalize_v2(unittest.TestCase):
    @staticmethod
    def _call_fut(*args, **kwargs):
        from google.cloud.storage._signing import canonicalize_v2

        return canonicalize_v2(*args, **kwargs)

    def test_wo_headers_or_query_parameters(self):
        method = "GET"
        resource = "/bucket/blob"
        canonical = self._call_fut(method, resource, None, None)
        self.assertEqual(canonical.method, method)
        self.assertEqual(canonical.resource, resource)
        self.assertEqual(canonical.query_parameters, [])
        self.assertEqual(canonical.headers, [])

    def test_w_headers_and_resumable(self):
        method = "RESUMABLE"
        resource = "/bucket/blob"
        headers = [("x-goog-extension", "foobar")]
        canonical = self._call_fut(method, resource, None, headers)
        self.assertEqual(canonical.method, "POST")
        self.assertEqual(canonical.resource, resource)
        self.assertEqual(canonical.query_parameters, [])
        self.assertEqual(
            canonical.headers, ["x-goog-extension:foobar", "x-goog-resumable:start"]
        )

    def test_w_query_parameters(self):
        method = "GET"
        resource = "/bucket/blob"
        query_parameters = {"foo": "bar", "baz": "qux"}
        canonical = self._call_fut(method, resource, query_parameters, None)
        self.assertEqual(canonical.method, method)
        self.assertEqual(canonical.resource, f"{resource}?baz=qux&foo=bar")
        self.assertEqual(canonical.query_parameters, [("baz", "qux"), ("foo", "bar")])
        self.assertEqual(canonical.headers, [])


class Test_generate_signed_url_v2(unittest.TestCase):
    @staticmethod
    def _call_fut(*args, **kwargs):
        from google.cloud.storage._signing import generate_signed_url_v2

        return generate_signed_url_v2(*args, **kwargs)

    def _generate_helper(
        self,
        api_access_endpoint="",
        method="GET",
        content_md5=None,
        content_type=None,
        response_type=None,
        response_disposition=None,
        generation=None,
        headers=None,
        query_parameters=None,
    ):
        from urllib.parse import urlencode

        resource = "/name/path"
        credentials = _make_credentials(signer_email="service@example.com")
        credentials.sign_bytes.return_value = b"DEADBEEF"
        signed = base64.b64encode(credentials.sign_bytes.return_value)
        signed = signed.decode("ascii")

        expiration = 1000

        url = self._call_fut(
            credentials,
            resource,
            expiration=expiration,
            api_access_endpoint=api_access_endpoint,
            method=method,
            content_md5=content_md5,
            content_type=content_type,
            response_type=response_type,
            response_disposition=response_disposition,
            generation=generation,
            headers=headers,
            query_parameters=query_parameters,
            service_account_email=None,
            access_token=None,
        )

        # Check the mock was called.
        method = method.upper()

        if headers is None:
            headers = []
        elif isinstance(headers, dict):
            headers = sorted(headers.items())

        elements = []
        expected_resource = resource
        if method == "RESUMABLE":
            elements.append("POST")
            headers.append(("x-goog-resumable", "start"))
        else:
            elements.append(method)

        if query_parameters is not None:
            normalized_qp = {
                key.lower(): value and value.strip() or ""
                for key, value in query_parameters.items()
            }
            expected_qp = urlencode(sorted(normalized_qp.items()))
            expected_resource = f"{resource}?{expected_qp}"

        elements.append(content_md5 or "")
        elements.append(content_type or "")
        elements.append(str(expiration))
        elements.extend(["{}:{}".format(*header) for header in headers])
        elements.append(expected_resource)

        string_to_sign = "\n".join(elements)

        credentials.sign_bytes.assert_called_once_with(string_to_sign.encode("ascii"))

        scheme, netloc, path, qs, frag = urllib.parse.urlsplit(url)
        expected_scheme, expected_netloc, _, _, _ = urllib.parse.urlsplit(
            api_access_endpoint
        )
        self.assertEqual(scheme, expected_scheme)
        self.assertEqual(netloc, expected_netloc)
        self.assertEqual(path, resource)
        self.assertEqual(frag, "")

        # Check the URL parameters.
        params = dict(urllib.parse.parse_qsl(qs, keep_blank_values=True))

        self.assertEqual(params["GoogleAccessId"], credentials.signer_email)
        self.assertEqual(params["Expires"], str(expiration))
        self.assertEqual(params["Signature"], signed)

        if response_type is not None:
            self.assertEqual(params["response-content-type"], response_type)

        if response_disposition is not None:
            self.assertEqual(
                params["response-content-disposition"], response_disposition
            )

        if generation is not None:
            self.assertEqual(params["generation"], str(generation))

        if query_parameters is not None:
            for key, value in query_parameters.items():
                value = value.strip() if value else ""
                self.assertEqual(params[key].lower(), value)

    def test_w_expiration_int(self):
        self._generate_helper()

    def test_w_endpoint(self):
        api_access_endpoint = "https://api.example.com"
        self._generate_helper(api_access_endpoint=api_access_endpoint)

    def test_w_method(self):
        method = "POST"
        self._generate_helper(method=method)

    def test_w_method_resumable(self):
        method = "RESUMABLE"
        self._generate_helper(method=method)

    def test_w_response_type(self):
        response_type = "text/plain"
        self._generate_helper(response_type=response_type)

    def test_w_response_disposition(self):
        response_disposition = "attachment; filename=blob.png"
        self._generate_helper(response_disposition=response_disposition)

    def test_w_generation(self):
        generation = "123"
        self._generate_helper(generation=generation)

    def test_w_custom_headers_dict(self):
        self._generate_helper(headers={"x-goog-foo": "bar"})

    def test_w_custom_headers_list(self):
        self._generate_helper(headers=[("x-goog-foo", "bar")])

    def test_w_custom_query_parameters_w_string_value(self):
        self._generate_helper(query_parameters={"bar": "/"})

    def test_w_custom_query_parameters_w_none_value(self):
        self._generate_helper(query_parameters={"qux": None})

    def test_with_google_credentials(self):
        resource = "/name/path"
        credentials = _make_credentials()
        expiration = int(time.time() + 5)
        with self.assertRaises(AttributeError):
            self._call_fut(credentials, resource=resource, expiration=expiration)

    def test_with_access_token(self):
        resource = "/name/path"
        credentials = _make_credentials()
        expiration = int(time.time() + 5)
        email = mock.sentinel.service_account_email
        with mock.patch(
            "google.cloud.storage._signing._sign_message", return_value=b"DEADBEEF"
        ):
            self._call_fut(
                credentials,
                resource=resource,
                expiration=expiration,
                service_account_email=email,
                access_token="token",
            )


class Test_generate_signed_url_v4(unittest.TestCase):
    DEFAULT_EXPIRATION = 1000

    @staticmethod
    def _call_fut(*args, **kwargs):
        from google.cloud.storage._signing import generate_signed_url_v4

        return generate_signed_url_v4(*args, **kwargs)

    def _generate_helper(
        self,
        expiration=DEFAULT_EXPIRATION,
        api_access_endpoint="",
        method="GET",
        content_type=None,
        content_md5=None,
        response_type=None,
        response_disposition=None,
        generation=None,
        headers=None,
        query_parameters=None,
    ):
        now = datetime.datetime(2019, 2, 26, 19, 53, 27)
        resource = "/name/path"
        signer_email = "service@example.com"
        credentials = _make_credentials(signer_email=signer_email)
        credentials.sign_bytes.return_value = b"DEADBEEF"

        with mock.patch("google.cloud.storage._signing._NOW", lambda tz: now):
            url = self._call_fut(
                credentials,
                resource,
                expiration=expiration,
                api_access_endpoint=api_access_endpoint,
                method=method,
                content_type=content_type,
                content_md5=content_md5,
                response_type=response_type,
                response_disposition=response_disposition,
                generation=generation,
                headers=headers,
                query_parameters=query_parameters,
            )

        # Check the mock was called.
        credentials.sign_bytes.assert_called_once()

        scheme, netloc, path, qs, frag = urllib.parse.urlsplit(url)

        expected_scheme, expected_netloc, _, _, _ = urllib.parse.urlsplit(
            api_access_endpoint
        )
        self.assertEqual(scheme, expected_scheme)
        self.assertEqual(netloc, expected_netloc)
        self.assertEqual(path, resource)
        self.assertEqual(frag, "")

        # Check the URL parameters.
        params = dict(urllib.parse.parse_qsl(qs, keep_blank_values=True))
        self.assertEqual(params["X-Goog-Algorithm"], "GOOG4-RSA-SHA256")

        now_date = now.date().strftime("%Y%m%d")
        expected_cred = f"{signer_email}/{now_date}/auto/storage/goog4_request"
        self.assertEqual(params["X-Goog-Credential"], expected_cred)

        now_stamp = now.strftime("%Y%m%dT%H%M%SZ")
        self.assertEqual(params["X-Goog-Date"], now_stamp)
        self.assertEqual(params["X-Goog-Expires"], str(self.DEFAULT_EXPIRATION))

        signed = binascii.hexlify(credentials.sign_bytes.return_value).decode("ascii")
        self.assertEqual(params["X-Goog-Signature"], signed)

        if response_type is not None:
            self.assertEqual(params["response-content-type"], response_type)

        if response_disposition is not None:
            self.assertEqual(
                params["response-content-disposition"], response_disposition
            )

        if generation is not None:
            self.assertEqual(params["generation"], str(generation))

        if query_parameters is not None:
            for key, value in query_parameters.items():
                value = value.strip() if value else ""
                self.assertEqual(params[key].lower(), value)

    def test_w_expiration_too_long(self):
        with self.assertRaises(ValueError):
            self._generate_helper(expiration=datetime.timedelta(days=8))

    def test_w_defaults(self):
        self._generate_helper()

    def test_w_api_access_endpoint(self):
        self._generate_helper(api_access_endpoint="http://api.example.com")

    def test_w_method(self):
        self._generate_helper(method="PUT")

    def test_w_method_resumable(self):
        self._generate_helper(method="RESUMABLE")

    def test_w_content_type(self):
        self._generate_helper(content_type="text/plain")

    def test_w_content_md5(self):
        self._generate_helper(content_md5="FACEDACE")

    def test_w_response_type(self):
        self._generate_helper(response_type="application/octets")

    def test_w_response_disposition(self):
        self._generate_helper(response_disposition="attachment")

    def test_w_generation(self):
        self._generate_helper(generation=12345)

    def test_w_custom_host_header(self):
        self._generate_helper(headers={"Host": "api.example.com"})

    def test_w_custom_headers(self):
        self._generate_helper(headers={"x-goog-foo": "bar"})

    def test_w_custom_payload_hash_goog(self):
        self._generate_helper(headers={"x-goog-content-sha256": "DEADBEEF"})

    def test_w_custom_query_parameters_w_string_value(self):
        self._generate_helper(query_parameters={"bar": "/"})

    def test_w_custom_query_parameters_w_none_value(self):
        self._generate_helper(query_parameters={"qux": None})

    def test_with_access_token_and_service_account_email(self):
        resource = "/name/path"
        credentials = _make_credentials()
        email = mock.sentinel.service_account_email
        with mock.patch(
            "google.cloud.storage._signing._sign_message", return_value=b"DEADBEEF"
        ):
            self._call_fut(
                credentials,
                resource=resource,
                expiration=datetime.timedelta(days=5),
                service_account_email=email,
                access_token="token",
            )

    def test_with_access_token_and_service_account_email_and_signer_email(self):
        resource = "/name/path"
        signer_email = "service@example.com"
        credentials = _make_credentials(signer_email=signer_email)
        with mock.patch(
            "google.cloud.storage._signing._sign_message", return_value=b"DEADBEEF"
        ):
            self._call_fut(
                credentials,
                resource=resource,
                expiration=datetime.timedelta(days=5),
                service_account_email=signer_email,
                access_token="token",
            )

    def test_with_signer_email(self):
        resource = "/name/path"
        signer_email = "service@example.com"
        credentials = _make_credentials(signer_email=signer_email)
        credentials.sign_bytes.return_value = b"DEADBEEF"
        self._call_fut(
            credentials,
            resource=resource,
            expiration=datetime.timedelta(days=5),
        )

    def test_with_service_account_email_and_signer_email(self):
        resource = "/name/path"
        signer_email = "service@example.com"
        credentials = _make_credentials(signer_email=signer_email)
        credentials.sign_bytes.return_value = b"DEADBEEF"
        self._call_fut(
            credentials,
            resource=resource,
            expiration=datetime.timedelta(days=5),
            service_account_email=signer_email,
        )

    def test_with_token_and_signer_email(self):
        resource = "/name/path"
        signer_email = "service@example.com"
        credentials = _make_credentials(signer_email=signer_email)
        credentials.sign_bytes.return_value = b"DEADBEEF"
        self._call_fut(
            credentials,
            resource=resource,
            expiration=datetime.timedelta(days=5),
            access_token="token",
        )


class Test_sign_message(unittest.TestCase):
    @staticmethod
    def _call_fut(*args, **kwargs):
        from google.cloud.storage._signing import _sign_message

        return _sign_message(*args, **kwargs)

    def test_sign_bytes(self):
        signature = "DEADBEEF"
        data = {"signedBlob": signature}
        request = make_request(200, data)
        with mock.patch("google.auth.transport.requests.Request", return_value=request):
            returned_signature = self._call_fut(
                "123", service_account_email="service@example.com", access_token="token"
            )
            assert returned_signature == signature

    def test_sign_bytes_failure(self):
        from google.auth import exceptions

        request = make_request(401)
        with mock.patch("google.auth.transport.requests.Request", return_value=request):
            with pytest.raises(exceptions.TransportError):
                self._call_fut(
                    "123",
                    service_account_email="service@example.com",
                    access_token="token",
                )


class TestCustomURLEncoding(unittest.TestCase):
    def test_url_encode(self):
        from google.cloud.storage._signing import _url_encode

        # param1 includes safe symbol ~
        # param# includes symbols, which must be encoded
        query_params = {"param1": "value~1-2", "param#": "*value+value/"}

        self.assertEqual(
            _url_encode(query_params), "param%23=%2Avalue%2Bvalue%2F&param1=value~1-2"
        )


class TestQuoteParam(unittest.TestCase):
    def test_ascii_symbols(self):
        from google.cloud.storage._signing import _quote_param

        encoded_param = _quote_param("param")
        self.assertIsInstance(encoded_param, str)
        self.assertEqual(encoded_param, "param")

    def test_quoted_symbols(self):
        from google.cloud.storage._signing import _quote_param

        encoded_param = _quote_param("!#$%&'()*+,/:;=?@[]")
        self.assertIsInstance(encoded_param, str)
        self.assertEqual(
            encoded_param, "%21%23%24%25%26%27%28%29%2A%2B%2C%2F%3A%3B%3D%3F%40%5B%5D"
        )

    def test_unquoted_symbols(self):
        import string

        from google.cloud.storage._signing import _quote_param

        UNQUOTED = string.ascii_letters + string.digits + ".~_-"

        encoded_param = _quote_param(UNQUOTED)
        self.assertIsInstance(encoded_param, str)
        self.assertEqual(encoded_param, UNQUOTED)

    def test_unicode_symbols(self):
        from google.cloud.storage._signing import _quote_param

        encoded_param = _quote_param("ЁЙЦЯЩЯЩ")
        self.assertIsInstance(encoded_param, str)
        self.assertEqual(encoded_param, "%D0%81%D0%99%D0%A6%D0%AF%D0%A9%D0%AF%D0%A9")

    def test_bytes(self):
        from google.cloud.storage._signing import _quote_param

        encoded_param = _quote_param(b"bytes")
        self.assertIsInstance(encoded_param, str)
        self.assertEqual(encoded_param, "bytes")


class TestV4Stamps(unittest.TestCase):
    def test_get_v4_now_dtstamps(self):
        import datetime

        from google.cloud.storage._signing import get_v4_now_dtstamps

        with mock.patch(
            "google.cloud.storage._signing._NOW",
            return_value=datetime.datetime(2020, 3, 12, 13, 14, 15),
        ) as now_mock:
            timestamp, datestamp = get_v4_now_dtstamps()
            now_mock.assert_called_once()

        self.assertEqual(timestamp, "20200312T131415Z")
        self.assertEqual(datestamp, "20200312")


"""Conformance tests for v4 signed URLs."""

_FAKE_SERVICE_ACCOUNT = None


def fake_service_account():
    global _FAKE_SERVICE_ACCOUNT

    from google.oauth2.service_account import Credentials

    if _FAKE_SERVICE_ACCOUNT is None:
        _FAKE_SERVICE_ACCOUNT = Credentials.from_service_account_info(
            _SERVICE_ACCOUNT_JSON
        )

    return _FAKE_SERVICE_ACCOUNT


_API_ACCESS_ENDPOINT = "https://storage.googleapis.com"


def _run_conformance_test(
    resource, test_data, api_access_endpoint=_API_ACCESS_ENDPOINT
):
    credentials = fake_service_account()
    url = Test_generate_signed_url_v4._call_fut(
        credentials,
        resource,
        expiration=test_data["expiration"],
        api_access_endpoint=api_access_endpoint,
        method=test_data["method"],
        _request_timestamp=test_data["timestamp"],
        headers=test_data.get("headers"),
        query_parameters=test_data.get("queryParameters"),
    )

    assert url == test_data["expectedUrl"]


@pytest.mark.parametrize("test_data", _BUCKET_TESTS)
def test_conformance_bucket(test_data):
    global _API_ACCESS_ENDPOINT
    if "urlStyle" in test_data and test_data["urlStyle"] == "BUCKET_BOUND_HOSTNAME":
        _API_ACCESS_ENDPOINT = "{scheme}://{bucket_bound_hostname}".format(
            scheme=test_data["scheme"],
            bucket_bound_hostname=test_data["bucketBoundHostname"],
        )
        resource = "/"
        _run_conformance_test(resource, test_data, _API_ACCESS_ENDPOINT)
    else:
        resource = f"/{test_data['bucket']}"
        _run_conformance_test(resource, test_data)


@pytest.mark.parametrize("test_data", _BLOB_TESTS)
def test_conformance_blob(test_data):
    global _API_ACCESS_ENDPOINT
    if "urlStyle" in test_data:
        if test_data["urlStyle"] == "BUCKET_BOUND_HOSTNAME":
            _API_ACCESS_ENDPOINT = "{scheme}://{bucket_bound_hostname}".format(
                scheme=test_data["scheme"],
                bucket_bound_hostname=test_data["bucketBoundHostname"],
            )

        # For the VIRTUAL_HOSTED_STYLE
        else:
            _API_ACCESS_ENDPOINT = (
                f"{test_data['scheme']}://{test_data['bucket']}.storage.googleapis.com"
            )
        resource = f"/{test_data['object']}"
        _run_conformance_test(resource, test_data, _API_ACCESS_ENDPOINT)
    else:
        resource = f"/{test_data['bucket']}/{test_data['object']}"
        _run_conformance_test(resource, test_data)


def _make_credentials(signer_email=None):
    import google.auth.credentials

    if signer_email:
        credentials = mock.Mock(spec=google.auth.credentials.Signing)
        credentials.signer_email = signer_email
        return credentials
    else:
        return mock.Mock(spec=google.auth.credentials.Credentials)


def make_request(status, data=None):
    from google.auth import transport

    response = mock.create_autospec(transport.Response, instance=True)
    response.status = status
    if data is not None:
        response.data = json.dumps(data).encode("utf-8")

    request = mock.create_autospec(transport.Request)
    request.return_value = response
    return request
