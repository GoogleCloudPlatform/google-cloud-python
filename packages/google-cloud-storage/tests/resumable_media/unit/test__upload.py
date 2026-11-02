# Copyright 2017 Google Inc.
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

import http.client
import io
import sys
import tempfile
from unittest import mock

import pytest  # type: ignore

from google.cloud.storage._media import _helpers, _upload
from google.cloud.storage.exceptions import DataCorruption, InvalidResponse
from google.cloud.storage.retry import DEFAULT_RETRY

URL_PREFIX = "https://www.googleapis.com/upload/storage/v1/b/{BUCKET}/o"
SIMPLE_URL = URL_PREFIX + "?uploadType=media&name={OBJECT}"
MULTIPART_URL = URL_PREFIX + "?uploadType=multipart"
RESUMABLE_URL = URL_PREFIX + "?uploadType=resumable"
ONE_MB = 1024 * 1024
BASIC_CONTENT = "text/plain"
JSON_TYPE = "application/json; charset=UTF-8"
JSON_TYPE_LINE = b"content-type: application/json; charset=UTF-8\r\n"
EXAMPLE_XML_UPLOAD_URL = "https://test-project.storage.googleapis.com/test-bucket"
EXAMPLE_HEADERS = {"example-key": "example-content"}
EXAMPLE_XML_MPU_INITIATE_TEXT_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<InitiateMultipartUploadResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Bucket>travel-maps</Bucket>
  <Key>paris.jpg</Key>
  <UploadId>{upload_id}</UploadId>
</InitiateMultipartUploadResult>
"""
UPLOAD_ID = "VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA"
PARTS = {1: "39a59594290b0f9a30662a56d695b71d", 2: "00000000290b0f9a30662a56d695b71d"}
FILE_DATA = b"testdata" * 128
CHECKSUM_MISMATCH_ERROR_MSG_XML_TEMPLATE = """<?xml version='1.0' encoding='UTF-8'?>
<Error>
    <Code>{ERROR_CODE}</Code>
    <Message>The MD5 you specified in Content-MD5 or x-goog-hash was invalid.</Message>
    <Details>Invalid MD5 value: dfdfdfd==</Details>
</Error>"""
INVALID_MD5_XML_RESPONSE = CHECKSUM_MISMATCH_ERROR_MSG_XML_TEMPLATE.format(
    ERROR_CODE="InvalidDigest"
)
INVALID_CRC32C_XML_RESPONSE = CHECKSUM_MISMATCH_ERROR_MSG_XML_TEMPLATE.format(
    ERROR_CODE="BadDigest"
)
INCORRECT_LENGTH_CRC32C_XML_RESPONSE = CHECKSUM_MISMATCH_ERROR_MSG_XML_TEMPLATE.format(
    ERROR_CODE="CrcMismatch"
)


@pytest.fixture(scope="session")
def filename():
    with tempfile.NamedTemporaryFile() as f:
        f.write(FILE_DATA)
        f.flush()
        yield f.name


class TestUploadBase(object):
    def test_constructor_defaults(self):
        upload = _upload.UploadBase(SIMPLE_URL)
        assert upload.upload_url == SIMPLE_URL
        assert upload._headers == {}
        assert not upload._finished
        _check_retry_strategy(upload)

    def test_constructor_explicit(self):
        headers = {"spin": "doctors"}
        upload = _upload.UploadBase(SIMPLE_URL, headers=headers)
        assert upload.upload_url == SIMPLE_URL
        assert upload._headers is headers
        assert not upload._finished
        _check_retry_strategy(upload)

    def test_finished_property(self):
        upload = _upload.UploadBase(SIMPLE_URL)
        # Default value of @property.
        assert not upload.finished

        # Make sure we cannot set it on public @property.
        with pytest.raises(AttributeError):
            upload.finished = False

        # Set it privately and then check the @property.
        upload._finished = True
        assert upload.finished

    def test__process_response_bad_status(self):
        upload = _upload.UploadBase(SIMPLE_URL)
        _fix_up_virtual(upload)

        # Make sure **not finished** before.
        assert not upload.finished
        status_code = http.client.SERVICE_UNAVAILABLE
        response = _make_response(status_code=status_code)
        with pytest.raises(InvalidResponse) as exc_info:
            upload._process_response(response)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 4
        assert error.args[1] == status_code
        assert error.args[3] == http.client.OK
        # Make sure **finished** after (even in failure).
        assert upload.finished

    def test__process_response(self):
        upload = _upload.UploadBase(SIMPLE_URL)
        _fix_up_virtual(upload)

        # Make sure **not finished** before.
        assert not upload.finished
        response = _make_response()
        ret_val = upload._process_response(response)
        assert ret_val is None
        # Make sure **finished** after.
        assert upload.finished

    def test__get_status_code(self):
        with pytest.raises(NotImplementedError) as exc_info:
            _upload.UploadBase._get_status_code(None)

        exc_info.match("virtual")

    def test__get_headers(self):
        with pytest.raises(NotImplementedError) as exc_info:
            _upload.UploadBase._get_headers(None)

        exc_info.match("virtual")

    def test__get_body(self):
        with pytest.raises(NotImplementedError) as exc_info:
            _upload.UploadBase._get_body(None)

        exc_info.match("virtual")


class TestSimpleUpload(object):
    def test__prepare_request_already_finished(self):
        upload = _upload.SimpleUpload(SIMPLE_URL)
        upload._finished = True
        with pytest.raises(ValueError) as exc_info:
            upload._prepare_request(b"", None)

        exc_info.match("An upload can only be used once.")

    def test__prepare_request_non_bytes_data(self):
        upload = _upload.SimpleUpload(SIMPLE_URL)
        assert not upload.finished
        with pytest.raises(TypeError) as exc_info:
            upload._prepare_request("", None)

        exc_info.match("must be bytes")

    def test__prepare_request(self):
        upload = _upload.SimpleUpload(SIMPLE_URL)
        content_type = "image/jpeg"
        data = b"cheetos and eetos"
        method, url, payload, headers = upload._prepare_request(data, content_type)

        assert method == "POST"
        assert url == SIMPLE_URL
        assert payload == data
        assert headers == {"content-type": content_type}

    def test__prepare_request_with_headers(self):
        headers = {"x-goog-cheetos": "spicy"}
        upload = _upload.SimpleUpload(SIMPLE_URL, headers=headers)
        content_type = "image/jpeg"
        data = b"some stuff"
        method, url, payload, new_headers = upload._prepare_request(data, content_type)

        assert method == "POST"
        assert url == SIMPLE_URL
        assert payload == data
        assert new_headers is headers
        expected = {"content-type": content_type, "x-goog-cheetos": "spicy"}
        assert headers == expected

    def test_transmit(self):
        upload = _upload.SimpleUpload(SIMPLE_URL)
        with pytest.raises(NotImplementedError) as exc_info:
            upload.transmit(None, None, None)

        exc_info.match("virtual")


class TestMultipartUpload(object):
    def test_constructor_defaults(self):
        upload = _upload.MultipartUpload(MULTIPART_URL)
        assert upload.upload_url == MULTIPART_URL
        assert upload._headers == {}
        assert upload._checksum_type == "crc32c"  # converted from "auto"
        assert not upload._finished
        _check_retry_strategy(upload)

    def test_constructor_explicit(self):
        headers = {"spin": "doctors"}
        upload = _upload.MultipartUpload(MULTIPART_URL, headers=headers, checksum="md5")
        assert upload.upload_url == MULTIPART_URL
        assert upload._headers is headers
        assert upload._checksum_type == "md5"
        assert not upload._finished
        _check_retry_strategy(upload)

    def test_constructor_explicit_auto(self):
        headers = {"spin": "doctors"}
        upload = _upload.MultipartUpload(
            MULTIPART_URL, headers=headers, checksum="auto"
        )
        assert upload.upload_url == MULTIPART_URL
        assert upload._headers is headers
        assert upload._checksum_type == "crc32c"
        assert not upload._finished
        _check_retry_strategy(upload)

    def test__prepare_request_already_finished(self):
        upload = _upload.MultipartUpload(MULTIPART_URL)
        upload._finished = True
        with pytest.raises(ValueError):
            upload._prepare_request(b"Hi", {}, BASIC_CONTENT)

    def test__prepare_request_non_bytes_data(self):
        data = "Nope not bytes."
        upload = _upload.MultipartUpload(MULTIPART_URL)
        with pytest.raises(TypeError):
            upload._prepare_request(data, {}, BASIC_CONTENT)

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==3=="
    )
    def _prepare_request_helper(
        self,
        mock_get_boundary,
        headers=None,
        checksum=None,
        expected_checksum=None,
        test_overwrite=False,
    ):
        upload = _upload.MultipartUpload(
            MULTIPART_URL, headers=headers, checksum=checksum
        )
        data = b"Hi"
        if test_overwrite and checksum:
            # Deliberately set metadata that conflicts with the chosen checksum.
            # This should be fully overwritten by the calculated checksum, so
            # the output should not change even if this is set.
            if checksum == "md5":
                metadata = {"md5Hash": "ZZZZZZZZZZZZZZZZZZZZZZ=="}
            else:
                metadata = {"crc32c": "ZZZZZZ=="}
        else:
            # To simplify parsing the response, omit other test metadata if a
            # checksum is specified.
            metadata = {"Some": "Stuff"} if not checksum else {}
        content_type = BASIC_CONTENT
        method, url, payload, new_headers = upload._prepare_request(
            data, metadata, content_type
        )

        assert method == "POST"
        assert url == MULTIPART_URL

        preamble = b"--==3==\r\n" + JSON_TYPE_LINE + b"\r\n"

        if checksum == "md5" and expected_checksum:
            metadata_payload = '{{"md5Hash": "{}"}}\r\n'.format(
                expected_checksum
            ).encode("utf8")
        elif checksum == "crc32c" and expected_checksum:
            metadata_payload = '{{"crc32c": "{}"}}\r\n'.format(
                expected_checksum
            ).encode("utf8")
        else:
            metadata_payload = b'{"Some": "Stuff"}\r\n'
        remainder = b"--==3==\r\ncontent-type: text/plain\r\n\r\nHi\r\n--==3==--"
        expected_payload = preamble + metadata_payload + remainder

        assert payload == expected_payload
        multipart_type = b'multipart/related; boundary="==3=="'
        mock_get_boundary.assert_called_once_with()

        return new_headers, multipart_type

    def test__prepare_request(self):
        headers, multipart_type = self._prepare_request_helper()
        assert headers == {"content-type": multipart_type}

    def test__prepare_request_with_headers(self):
        headers = {"best": "shirt", "worst": "hat"}
        new_headers, multipart_type = self._prepare_request_helper(headers=headers)
        assert new_headers is headers
        expected_headers = {
            "best": "shirt",
            "content-type": multipart_type,
            "worst": "hat",
        }
        assert expected_headers == headers

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__prepare_request_with_checksum(self, checksum):
        checksums = {
            "md5": "waUpj5Oeh+j5YqXt/CBpGA==",
            "crc32c": "ihY6wA==",
        }
        headers, multipart_type = self._prepare_request_helper(
            checksum=checksum, expected_checksum=checksums[checksum]
        )
        assert headers == {
            "content-type": multipart_type,
        }

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__prepare_request_with_checksum_overwrite(self, checksum):
        checksums = {
            "md5": "waUpj5Oeh+j5YqXt/CBpGA==",
            "crc32c": "ihY6wA==",
        }
        headers, multipart_type = self._prepare_request_helper(
            checksum=checksum,
            expected_checksum=checksums[checksum],
            test_overwrite=True,
        )
        assert headers == {
            "content-type": multipart_type,
        }

    def test_transmit(self):
        upload = _upload.MultipartUpload(MULTIPART_URL)
        with pytest.raises(NotImplementedError) as exc_info:
            upload.transmit(None, None, None, None)

        exc_info.match("virtual")


class TestResumableUpload(object):
    def test_constructor(self):
        chunk_size = ONE_MB
        upload = _upload.ResumableUpload(RESUMABLE_URL, chunk_size)
        assert upload.upload_url == RESUMABLE_URL
        assert upload._headers == {}
        assert not upload._finished
        _check_retry_strategy(upload)
        assert upload._chunk_size == chunk_size
        assert upload._stream is None
        assert upload._content_type is None
        assert upload._bytes_uploaded == 0
        assert upload._bytes_checksummed == 0
        assert upload._checksum_object is None
        assert upload._total_bytes is None
        assert upload._resumable_url is None
        assert upload._checksum_type == "crc32c"  # converted from "auto"

    def test_constructor_bad_chunk_size(self):
        with pytest.raises(ValueError):
            _upload.ResumableUpload(RESUMABLE_URL, 1)

    def test_invalid_property(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        # Default value of @property.
        assert not upload.invalid

        # Make sure we cannot set it on public @property.
        with pytest.raises(AttributeError):
            upload.invalid = False

        # Set it privately and then check the @property.
        upload._invalid = True
        assert upload.invalid

    def test_chunk_size_property(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        # Default value of @property.
        assert upload.chunk_size == ONE_MB

        # Make sure we cannot set it on public @property.
        with pytest.raises(AttributeError):
            upload.chunk_size = 17

        # Set it privately and then check the @property.
        new_size = 102
        upload._chunk_size = new_size
        assert upload.chunk_size == new_size

    def test_resumable_url_property(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        # Default value of @property.
        assert upload.resumable_url is None

        # Make sure we cannot set it on public @property.
        new_url = "http://test.invalid?upload_id=not-none"
        with pytest.raises(AttributeError):
            upload.resumable_url = new_url

        # Set it privately and then check the @property.
        upload._resumable_url = new_url
        assert upload.resumable_url == new_url

    def test_bytes_uploaded_property(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        # Default value of @property.
        assert upload.bytes_uploaded == 0

        # Make sure we cannot set it on public @property.
        with pytest.raises(AttributeError):
            upload.bytes_uploaded = 1024

        # Set it privately and then check the @property.
        upload._bytes_uploaded = 128
        assert upload.bytes_uploaded == 128

    def test_total_bytes_property(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        # Default value of @property.
        assert upload.total_bytes is None

        # Make sure we cannot set it on public @property.
        with pytest.raises(AttributeError):
            upload.total_bytes = 65536

        # Set it privately and then check the @property.
        upload._total_bytes = 8192
        assert upload.total_bytes == 8192

    def _prepare_initiate_request_helper(
        self, upload_url=RESUMABLE_URL, upload_headers=None, **method_kwargs
    ):
        data = b"some really big big data."
        stream = io.BytesIO(data)
        metadata = {"name": "big-data-file.txt"}

        upload = _upload.ResumableUpload(upload_url, ONE_MB, headers=upload_headers)
        orig_headers = upload._headers.copy()
        # Check ``upload``-s state before.
        assert upload._stream is None
        assert upload._content_type is None
        assert upload._total_bytes is None
        # Call the method and check the output.
        method, url, payload, headers = upload._prepare_initiate_request(
            stream, metadata, BASIC_CONTENT, **method_kwargs
        )
        assert payload == b'{"name": "big-data-file.txt"}'
        # Make sure the ``upload``-s state was updated.
        assert upload._stream == stream
        assert upload._content_type == BASIC_CONTENT
        if method_kwargs == {"stream_final": False}:
            assert upload._total_bytes is None
        else:
            assert upload._total_bytes == len(data)
        # Make sure headers are untouched.
        assert headers is not upload._headers
        assert upload._headers == orig_headers
        assert method == "POST"
        assert url == upload.upload_url
        # Make sure the stream is still at the beginning.
        assert stream.tell() == 0

        return data, headers

    def test__prepare_initiate_request(self):
        data, headers = self._prepare_initiate_request_helper()
        expected_headers = {
            "content-type": JSON_TYPE,
            "x-upload-content-length": "{:d}".format(len(data)),
            "x-upload-content-type": BASIC_CONTENT,
        }
        assert headers == expected_headers

    def test_prepare_initiate_request_with_signed_url(self):
        signed_urls = [
            "https://storage.googleapis.com/b/o?x-goog-signature=123abc",
            "https://storage.googleapis.com/b/o?X-Goog-Signature=123abc",
        ]
        for signed_url in signed_urls:
            data, headers = self._prepare_initiate_request_helper(
                upload_url=signed_url,
            )
            expected_headers = {
                "content-type": BASIC_CONTENT,
                "x-upload-content-length": "{:d}".format(len(data)),
            }
            assert headers == expected_headers

    def test__prepare_initiate_request_with_headers(self):
        # content-type header should be overwritten, the rest should stay
        headers = {
            "caviar": "beluga",
            "top": "quark",
            "content-type": "application/xhtml",
        }
        data, new_headers = self._prepare_initiate_request_helper(
            upload_headers=headers
        )
        expected_headers = {
            "caviar": "beluga",
            "content-type": JSON_TYPE,
            "top": "quark",
            "x-upload-content-length": "{:d}".format(len(data)),
            "x-upload-content-type": BASIC_CONTENT,
        }
        assert new_headers == expected_headers

    def test__prepare_initiate_request_known_size(self):
        total_bytes = 25
        data, headers = self._prepare_initiate_request_helper(total_bytes=total_bytes)
        assert len(data) == total_bytes
        expected_headers = {
            "content-type": "application/json; charset=UTF-8",
            "x-upload-content-length": "{:d}".format(total_bytes),
            "x-upload-content-type": BASIC_CONTENT,
        }
        assert headers == expected_headers

    def test__prepare_initiate_request_unknown_size(self):
        _, headers = self._prepare_initiate_request_helper(stream_final=False)
        expected_headers = {
            "content-type": "application/json; charset=UTF-8",
            "x-upload-content-type": BASIC_CONTENT,
        }
        assert headers == expected_headers

    def test__prepare_initiate_request_already_initiated(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        # Fake that the upload has been started.
        upload._resumable_url = "http://test.invalid?upload_id=definitely-started"

        with pytest.raises(ValueError):
            upload._prepare_initiate_request(io.BytesIO(), {}, BASIC_CONTENT)

    def test__prepare_initiate_request_bad_stream_position(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)

        stream = io.BytesIO(b"data")
        stream.seek(1)
        with pytest.raises(ValueError):
            upload._prepare_initiate_request(stream, {}, BASIC_CONTENT)

        # Also test a bad object (i.e. non-stream)
        with pytest.raises(AttributeError):
            upload._prepare_initiate_request(None, {}, BASIC_CONTENT)

    def test__process_initiate_response_non_200(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        _fix_up_virtual(upload)

        response = _make_response(403)
        with pytest.raises(InvalidResponse) as exc_info:
            upload._process_initiate_response(response)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 5
        assert error.args[1] == 403
        assert error.args[3] == 200
        assert error.args[4] == 201

    def test__process_initiate_response(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        _fix_up_virtual(upload)

        headers = {"location": "http://test.invalid?upload_id=kmfeij3234"}
        response = _make_response(headers=headers)
        # Check resumable_url before.
        assert upload._resumable_url is None
        # Process the actual headers.
        ret_val = upload._process_initiate_response(response)
        assert ret_val is None
        # Check resumable_url after.
        assert upload._resumable_url == headers["location"]

    def test_initiate(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        with pytest.raises(NotImplementedError) as exc_info:
            upload.initiate(None, None, {}, BASIC_CONTENT)

        exc_info.match("virtual")

    def test__prepare_request_already_finished(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        assert not upload.invalid
        upload._finished = True
        with pytest.raises(ValueError) as exc_info:
            upload._prepare_request()

        assert exc_info.value.args == ("Upload has finished.",)

    def test__prepare_request_invalid(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        assert not upload.finished
        upload._invalid = True
        with pytest.raises(ValueError) as exc_info:
            upload._prepare_request()

        assert exc_info.match("invalid state")
        assert exc_info.match("recover()")

    def test__prepare_request_not_initiated(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        assert not upload.finished
        assert not upload.invalid
        assert upload._resumable_url is None
        with pytest.raises(ValueError) as exc_info:
            upload._prepare_request()

        assert exc_info.match("upload has not been initiated")
        assert exc_info.match("initiate()")

    def test__prepare_request_invalid_stream_state(self):
        stream = io.BytesIO(b"some data here")
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        upload._stream = stream
        upload._resumable_url = "http://test.invalid?upload_id=not-none"
        # Make stream.tell() disagree with bytes_uploaded.
        upload._bytes_uploaded = 5
        assert upload.bytes_uploaded != stream.tell()
        with pytest.raises(ValueError) as exc_info:
            upload._prepare_request()

        assert exc_info.match("Bytes stream is in unexpected state.")

    @staticmethod
    def _upload_in_flight(data, headers=None, checksum=None):
        upload = _upload.ResumableUpload(
            RESUMABLE_URL, ONE_MB, headers=headers, checksum=checksum
        )
        upload._stream = io.BytesIO(data)
        upload._content_type = BASIC_CONTENT
        upload._total_bytes = len(data)
        upload._resumable_url = "http://test.invalid?upload_id=not-none"
        return upload

    def _prepare_request_helper(self, headers=None, checksum=None):
        data = b"All of the data goes in a stream."
        upload = self._upload_in_flight(data, headers=headers, checksum=checksum)
        method, url, payload, new_headers = upload._prepare_request()
        # Check the response values.
        assert method == "PUT"
        assert url == upload.resumable_url
        assert payload == data
        # Make sure headers are **NOT** updated
        assert upload._headers != new_headers

        return new_headers

    def test__prepare_request_success(self):
        headers = self._prepare_request_helper()
        expected_headers = {
            "content-range": "bytes 0-32/33",
            "content-type": BASIC_CONTENT,
        }
        assert headers == expected_headers

    def test__prepare_request_success_with_headers(self):
        headers = {"keep": "this"}
        new_headers = self._prepare_request_helper(headers)
        assert new_headers is not headers
        expected_headers = {
            "keep": "this",
            "content-range": "bytes 0-32/33",
            "content-type": BASIC_CONTENT,
        }
        assert new_headers == expected_headers

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__prepare_request_with_checksum(self, checksum):
        data = b"All of the data goes in a stream."
        upload = self._upload_in_flight(data, checksum=checksum)
        upload._prepare_request()
        assert upload._checksum_object is not None

        checksums = {"md5": "GRvfKbqr5klAOwLkxgIf8w==", "crc32c": "Qg8thA=="}
        checksum_digest = _helpers.prepare_checksum_digest(
            upload._checksum_object.digest()
        )
        assert checksum_digest == checksums[checksum]
        assert upload._bytes_checksummed == len(data)

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__update_checksum(self, checksum):
        data = b"All of the data goes in a stream."
        upload = self._upload_in_flight(data, checksum=checksum)
        start_byte, payload, _ = _upload.get_next_chunk(upload._stream, 8, len(data))
        upload._update_checksum(start_byte, payload)
        assert upload._bytes_checksummed == 8

        start_byte, payload, _ = _upload.get_next_chunk(upload._stream, 8, len(data))
        upload._update_checksum(start_byte, payload)
        assert upload._bytes_checksummed == 16

        # Continue to the end.
        start_byte, payload, _ = _upload.get_next_chunk(
            upload._stream, len(data), len(data)
        )
        upload._update_checksum(start_byte, payload)
        assert upload._bytes_checksummed == len(data)

        checksums = {"md5": "GRvfKbqr5klAOwLkxgIf8w==", "crc32c": "Qg8thA=="}
        checksum_digest = _helpers.prepare_checksum_digest(
            upload._checksum_object.digest()
        )
        assert checksum_digest == checksums[checksum]

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__update_checksum_rewind(self, checksum):
        data = b"All of the data goes in a stream."
        upload = self._upload_in_flight(data, checksum=checksum)
        start_byte, payload, _ = _upload.get_next_chunk(upload._stream, 8, len(data))
        upload._update_checksum(start_byte, payload)
        assert upload._bytes_checksummed == 8
        checksum_checkpoint = upload._checksum_object.digest()

        # Rewind to the beginning.
        upload._stream.seek(0)
        start_byte, payload, _ = _upload.get_next_chunk(upload._stream, 8, len(data))
        upload._update_checksum(start_byte, payload)
        assert upload._bytes_checksummed == 8
        assert upload._checksum_object.digest() == checksum_checkpoint

        # Rewind but not to the beginning.
        upload._stream.seek(4)
        start_byte, payload, _ = _upload.get_next_chunk(upload._stream, 8, len(data))
        upload._update_checksum(start_byte, payload)
        assert upload._bytes_checksummed == 12

        # Continue to the end.
        start_byte, payload, _ = _upload.get_next_chunk(
            upload._stream, len(data), len(data)
        )
        upload._update_checksum(start_byte, payload)
        assert upload._bytes_checksummed == len(data)

        checksums = {"md5": "GRvfKbqr5klAOwLkxgIf8w==", "crc32c": "Qg8thA=="}
        checksum_digest = _helpers.prepare_checksum_digest(
            upload._checksum_object.digest()
        )
        assert checksum_digest == checksums[checksum]

    def test__update_checksum_none(self):
        data = b"All of the data goes in a stream."
        upload = self._upload_in_flight(data, checksum=None)
        start_byte, payload, _ = _upload.get_next_chunk(upload._stream, 8, len(data))
        upload._update_checksum(start_byte, payload)
        assert upload._checksum_object is None

    def test__update_checksum_invalid(self):
        data = b"All of the data goes in a stream."
        upload = self._upload_in_flight(data, checksum="invalid")
        start_byte, payload, _ = _upload.get_next_chunk(upload._stream, 8, len(data))
        with pytest.raises(ValueError):
            upload._update_checksum(start_byte, payload)

    def test__make_invalid(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        assert not upload.invalid
        upload._make_invalid()
        assert upload.invalid

    def test__process_resumable_response_bad_status(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        _fix_up_virtual(upload)

        # Make sure the upload is valid before the failure.
        assert not upload.invalid
        response = _make_response(status_code=http.client.NOT_FOUND)
        with pytest.raises(InvalidResponse) as exc_info:
            upload._process_resumable_response(response, None)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 5
        assert error.args[1] == response.status_code
        assert error.args[3] == http.client.OK
        assert error.args[4] == http.client.PERMANENT_REDIRECT
        # Make sure the upload is invalid after the failure.
        assert upload.invalid

    def test__process_resumable_response_success(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB, checksum=None)
        _fix_up_virtual(upload)

        # Check / set status before.
        assert upload._bytes_uploaded == 0
        upload._bytes_uploaded = 20
        assert not upload._finished

        # Set the response body.
        bytes_sent = 158
        total_bytes = upload._bytes_uploaded + bytes_sent
        response_body = '{{"size": "{:d}"}}'.format(total_bytes)
        response_body = response_body.encode("utf-8")
        response = mock.Mock(
            content=response_body,
            status_code=http.client.OK,
            spec=["content", "status_code"],
        )
        ret_val = upload._process_resumable_response(response, bytes_sent)
        assert ret_val is None
        # Check status after.
        assert upload._bytes_uploaded == total_bytes
        assert upload._finished

    def test__process_resumable_response_partial_no_range(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        _fix_up_virtual(upload)

        response = _make_response(status_code=http.client.PERMANENT_REDIRECT)
        # Make sure the upload is valid before the failure.
        assert not upload.invalid
        with pytest.raises(InvalidResponse) as exc_info:
            upload._process_resumable_response(response, None)
        # Make sure the upload is invalid after the failure.
        assert upload.invalid

        # Check the error response.
        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 2
        assert error.args[1] == "range"

    def test__process_resumable_response_partial_bad_range(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        _fix_up_virtual(upload)

        # Make sure the upload is valid before the failure.
        assert not upload.invalid
        headers = {"range": "nights 1-81"}
        response = _make_response(
            status_code=http.client.PERMANENT_REDIRECT, headers=headers
        )
        with pytest.raises(InvalidResponse) as exc_info:
            upload._process_resumable_response(response, 81)

        # Check the error response.
        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 3
        assert error.args[1] == headers["range"]
        # Make sure the upload is invalid after the failure.
        assert upload.invalid

    def test__process_resumable_response_partial(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        _fix_up_virtual(upload)

        # Check status before.
        assert upload._bytes_uploaded == 0
        headers = {"range": "bytes=0-171"}
        response = _make_response(
            status_code=http.client.PERMANENT_REDIRECT, headers=headers
        )
        ret_val = upload._process_resumable_response(response, 172)
        assert ret_val is None
        # Check status after.
        assert upload._bytes_uploaded == 172

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__validate_checksum_success(self, checksum):
        data = b"All of the data goes in a stream."
        upload = self._upload_in_flight(data, checksum=checksum)
        _fix_up_virtual(upload)
        # Go ahead and process the entire data in one go for this test.
        start_byte, payload, _ = _upload.get_next_chunk(
            upload._stream, len(data), len(data)
        )
        upload._update_checksum(start_byte, payload)
        assert upload._bytes_checksummed == len(data)

        # This is only used by _validate_checksum for fetching metadata and
        # logging.
        metadata = {"md5Hash": "GRvfKbqr5klAOwLkxgIf8w==", "crc32c": "Qg8thA=="}
        response = _make_response(metadata=metadata)
        upload._finished = True

        assert upload._checksum_object is not None
        # Test passes if it does not raise an error (no assert needed)
        upload._validate_checksum(response)

    def test__validate_checksum_none(self):
        data = b"All of the data goes in a stream."
        upload = self._upload_in_flight(b"test", checksum=None)
        _fix_up_virtual(upload)
        # Go ahead and process the entire data in one go for this test.
        start_byte, payload, _ = _upload.get_next_chunk(
            upload._stream, len(data), len(data)
        )
        upload._update_checksum(start_byte, payload)

        # This is only used by _validate_checksum for fetching metadata and
        # logging.
        metadata = {"md5Hash": "GRvfKbqr5klAOwLkxgIf8w==", "crc32c": "Qg8thA=="}
        response = _make_response(metadata=metadata)
        upload._finished = True

        assert upload._checksum_object is None
        assert upload._bytes_checksummed == 0
        # Test passes if it does not raise an error (no assert needed)
        upload._validate_checksum(response)

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__validate_checksum_header_no_match(self, checksum):
        data = b"All of the data goes in a stream."
        upload = self._upload_in_flight(data, checksum=checksum)
        _fix_up_virtual(upload)
        # Go ahead and process the entire data in one go for this test.
        start_byte, payload, _ = _upload.get_next_chunk(
            upload._stream, len(data), len(data)
        )
        upload._update_checksum(start_byte, payload)
        assert upload._bytes_checksummed == len(data)

        # For this test, each checksum option will be provided with a valid but
        # mismatching remote checksum type.
        if checksum == "crc32c":
            metadata = {"md5Hash": "GRvfKbqr5klAOwLkxgIf8w=="}
        else:
            metadata = {"crc32c": "Qg8thA=="}
        # This is only used by _validate_checksum for fetching headers and
        # logging, so it doesn't need to be fleshed out with a response body.
        response = _make_response(metadata=metadata)
        upload._finished = True

        assert upload._checksum_object is not None
        with pytest.raises(InvalidResponse) as exc_info:
            upload._validate_checksum(response)

        error = exc_info.value
        assert error.response is response
        message = error.args[0]
        metadata_key = _helpers._get_metadata_key(checksum)
        assert (
            message
            == _upload._UPLOAD_METADATA_NO_APPROPRIATE_CHECKSUM_MESSAGE.format(
                metadata_key
            )
        )

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    def test__validate_checksum_mismatch(self, checksum):
        data = b"All of the data goes in a stream."
        upload = self._upload_in_flight(data, checksum=checksum)
        _fix_up_virtual(upload)
        # Go ahead and process the entire data in one go for this test.
        start_byte, payload, _ = _upload.get_next_chunk(
            upload._stream, len(data), len(data)
        )
        upload._update_checksum(start_byte, payload)
        assert upload._bytes_checksummed == len(data)

        metadata = {
            "md5Hash": "ZZZZZZZZZZZZZZZZZZZZZZ==",
            "crc32c": "ZZZZZZ==",
        }
        # This is only used by _validate_checksum for fetching headers and
        # logging, so it doesn't need to be fleshed out with a response body.
        response = _make_response(metadata=metadata)
        upload._finished = True

        assert upload._checksum_object is not None
        # Test passes if it does not raise an error (no assert needed)
        with pytest.raises(DataCorruption) as exc_info:
            upload._validate_checksum(response)

        error = exc_info.value
        assert error.response is response
        message = error.args[0]
        correct_checksums = {"crc32c": "Qg8thA==", "md5": "GRvfKbqr5klAOwLkxgIf8w=="}
        metadata_key = _helpers._get_metadata_key(checksum)
        assert message == _upload._UPLOAD_CHECKSUM_MISMATCH_MESSAGE.format(
            checksum.upper(), correct_checksums[checksum], metadata[metadata_key]
        )

    def test_transmit_next_chunk(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        with pytest.raises(NotImplementedError) as exc_info:
            upload.transmit_next_chunk(None)

        exc_info.match("virtual")

    def test__prepare_recover_request_not_invalid(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        assert not upload.invalid

        method, url, payload, headers = upload._prepare_recover_request()
        assert method == "PUT"
        assert url == upload.resumable_url
        assert payload is None
        assert headers == {"content-range": "bytes */*"}
        # Make sure headers are untouched.
        assert upload._headers == {}

    def test__prepare_recover_request(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        upload._invalid = True

        method, url, payload, headers = upload._prepare_recover_request()
        assert method == "PUT"
        assert url == upload.resumable_url
        assert payload is None
        assert headers == {"content-range": "bytes */*"}
        # Make sure headers are untouched.
        assert upload._headers == {}

    def test__prepare_recover_request_with_headers(self):
        headers = {"lake": "ocean"}
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB, headers=headers)
        upload._invalid = True

        method, url, payload, new_headers = upload._prepare_recover_request()
        assert method == "PUT"
        assert url == upload.resumable_url
        assert payload is None
        assert new_headers == {"content-range": "bytes */*"}
        # Make sure the ``_headers`` are not incorporated.
        assert "lake" not in new_headers
        # Make sure headers are untouched.
        assert upload._headers == {"lake": "ocean"}

    def test__process_recover_response_bad_status(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        _fix_up_virtual(upload)

        upload._invalid = True

        response = _make_response(status_code=http.client.BAD_REQUEST)
        with pytest.raises(InvalidResponse) as exc_info:
            upload._process_recover_response(response)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 4
        assert error.args[1] == response.status_code
        assert error.args[3] == http.client.PERMANENT_REDIRECT
        # Make sure still invalid.
        assert upload.invalid

    def test__process_recover_response_no_range(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        _fix_up_virtual(upload)

        upload._invalid = True
        upload._stream = mock.Mock(spec=["seek"])
        upload._bytes_uploaded = mock.sentinel.not_zero
        assert upload.bytes_uploaded != 0

        response = _make_response(status_code=http.client.PERMANENT_REDIRECT)
        ret_val = upload._process_recover_response(response)
        assert ret_val is None
        # Check the state of ``upload`` after.
        assert upload.bytes_uploaded == 0
        assert not upload.invalid
        upload._stream.seek.assert_called_once_with(0)

    def test__process_recover_response_bad_range(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        _fix_up_virtual(upload)

        upload._invalid = True
        upload._stream = mock.Mock(spec=["seek"])
        upload._bytes_uploaded = mock.sentinel.not_zero

        headers = {"range": "bites=9-11"}
        response = _make_response(
            status_code=http.client.PERMANENT_REDIRECT, headers=headers
        )
        with pytest.raises(InvalidResponse) as exc_info:
            upload._process_recover_response(response)

        error = exc_info.value
        assert error.response is response
        assert len(error.args) == 3
        assert error.args[1] == headers["range"]
        # Check the state of ``upload`` after (untouched).
        assert upload.bytes_uploaded is mock.sentinel.not_zero
        assert upload.invalid
        upload._stream.seek.assert_not_called()

    def test__process_recover_response_with_range(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        _fix_up_virtual(upload)

        upload._invalid = True
        upload._stream = mock.Mock(spec=["seek"])
        upload._bytes_uploaded = mock.sentinel.not_zero
        assert upload.bytes_uploaded != 0

        end = 11
        headers = {"range": "bytes=0-{:d}".format(end)}
        response = _make_response(
            status_code=http.client.PERMANENT_REDIRECT, headers=headers
        )
        ret_val = upload._process_recover_response(response)
        assert ret_val is None
        # Check the state of ``upload`` after.
        assert upload.bytes_uploaded == end + 1
        assert not upload.invalid
        upload._stream.seek.assert_called_once_with(end + 1)

    def test_recover(self):
        upload = _upload.ResumableUpload(RESUMABLE_URL, ONE_MB)
        with pytest.raises(NotImplementedError) as exc_info:
            upload.recover(None)

        exc_info.match("virtual")


@mock.patch("random.randrange", return_value=1234567890123456789)
def test_get_boundary(mock_rand):
    result = _upload.get_boundary()
    assert result == b"===============1234567890123456789=="
    mock_rand.assert_called_once_with(sys.maxsize)


class Test_construct_multipart_request(object):
    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==1=="
    )
    def test_binary(self, mock_get_boundary):
        data = b"By nary day tuh"
        metadata = {"name": "hi-file.bin"}
        content_type = "application/octet-stream"
        payload, multipart_boundary = _upload.construct_multipart_request(
            data, metadata, content_type
        )

        assert multipart_boundary == mock_get_boundary.return_value
        expected_payload = (
            b"--==1==\r\n" + JSON_TYPE_LINE + b"\r\n"
            b'{"name": "hi-file.bin"}\r\n'
            b"--==1==\r\n"
            b"content-type: application/octet-stream\r\n"
            b"\r\n"
            b"By nary day tuh\r\n"
            b"--==1==--"
        )
        assert payload == expected_payload
        mock_get_boundary.assert_called_once_with()

    @mock.patch(
        "google.cloud.storage._media._upload.get_boundary", return_value=b"==2=="
    )
    def test_unicode(self, mock_get_boundary):
        data_unicode = "\N{SNOWMAN}"
        # construct_multipart_request( ASSUMES callers pass bytes.
        data = data_unicode.encode("utf-8")
        metadata = {"name": "snowman.txt"}
        content_type = BASIC_CONTENT
        payload, multipart_boundary = _upload.construct_multipart_request(
            data, metadata, content_type
        )

        assert multipart_boundary == mock_get_boundary.return_value
        expected_payload = (
            b"--==2==\r\n" + JSON_TYPE_LINE + b"\r\n"
            b'{"name": "snowman.txt"}\r\n'
            b"--==2==\r\n"
            b"content-type: text/plain\r\n"
            b"\r\n"
            b"\xe2\x98\x83\r\n"
            b"--==2==--"
        )
        assert payload == expected_payload
        mock_get_boundary.assert_called_once_with()


def test_get_total_bytes():
    data = b"some data"
    stream = io.BytesIO(data)
    # Check position before function call.
    assert stream.tell() == 0
    assert _upload.get_total_bytes(stream) == len(data)
    # Check position after function call.
    assert stream.tell() == 0

    # Make sure this works just as well when not at beginning.
    curr_pos = 3
    stream.seek(curr_pos)
    assert _upload.get_total_bytes(stream) == len(data)
    # Check position after function call.
    assert stream.tell() == curr_pos


class Test_get_next_chunk(object):
    def test_exhausted_known_size(self):
        data = b"the end"
        stream = io.BytesIO(data)
        stream.seek(len(data))
        with pytest.raises(ValueError) as exc_info:
            _upload.get_next_chunk(stream, 1, len(data))

        exc_info.match("Stream is already exhausted. There is no content remaining.")

    def test_exhausted_known_size_zero(self):
        stream = io.BytesIO(b"")
        answer = _upload.get_next_chunk(stream, 1, 0)
        assert answer == (0, b"", "bytes */0")

    def test_exhausted_known_size_zero_nonempty(self):
        stream = io.BytesIO(b"not empty WAT!")
        with pytest.raises(ValueError) as exc_info:
            _upload.get_next_chunk(stream, 1, 0)
        exc_info.match("Stream specified as empty, but produced non-empty content.")

    def test_success_known_size_lt_stream_size(self):
        data = b"0123456789"
        stream = io.BytesIO(data)
        chunk_size = 3
        total_bytes = len(data) - 2

        # Splits into 3 chunks: 012, 345, 67
        result0 = _upload.get_next_chunk(stream, chunk_size, total_bytes)
        result1 = _upload.get_next_chunk(stream, chunk_size, total_bytes)
        result2 = _upload.get_next_chunk(stream, chunk_size, total_bytes)

        assert result0 == (0, b"012", "bytes 0-2/8")
        assert result1 == (3, b"345", "bytes 3-5/8")
        assert result2 == (6, b"67", "bytes 6-7/8")

    def test_success_known_size(self):
        data = b"0123456789"
        stream = io.BytesIO(data)
        total_bytes = len(data)
        chunk_size = 3
        # Splits into 4 chunks: 012, 345, 678, 9
        result0 = _upload.get_next_chunk(stream, chunk_size, total_bytes)
        result1 = _upload.get_next_chunk(stream, chunk_size, total_bytes)
        result2 = _upload.get_next_chunk(stream, chunk_size, total_bytes)
        result3 = _upload.get_next_chunk(stream, chunk_size, total_bytes)
        assert result0 == (0, b"012", "bytes 0-2/10")
        assert result1 == (3, b"345", "bytes 3-5/10")
        assert result2 == (6, b"678", "bytes 6-8/10")
        assert result3 == (9, b"9", "bytes 9-9/10")
        assert stream.tell() == total_bytes

    def test_success_unknown_size(self):
        data = b"abcdefghij"
        stream = io.BytesIO(data)
        chunk_size = 6
        # Splits into 4 chunks: abcdef, ghij
        result0 = _upload.get_next_chunk(stream, chunk_size, None)
        result1 = _upload.get_next_chunk(stream, chunk_size, None)
        assert result0 == (0, b"abcdef", "bytes 0-5/*")
        assert result1 == (chunk_size, b"ghij", "bytes 6-9/10")
        assert stream.tell() == len(data)

        # Do the same when the chunk size evenly divides len(data)
        stream.seek(0)
        chunk_size = len(data)
        # Splits into 2 chunks: `data` and empty string
        result0 = _upload.get_next_chunk(stream, chunk_size, None)
        result1 = _upload.get_next_chunk(stream, chunk_size, None)
        assert result0 == (0, data, "bytes 0-9/*")
        assert result1 == (len(data), b"", "bytes */10")
        assert stream.tell() == len(data)


class Test_get_content_range(object):
    def test_known_size(self):
        result = _upload.get_content_range(5, 10, 40)
        assert result == "bytes 5-10/40"

    def test_unknown_size(self):
        result = _upload.get_content_range(1000, 10000, None)
        assert result == "bytes 1000-10000/*"


def test_xml_mpu_container_constructor_and_properties(filename):
    container = _upload.XMLMPUContainer(EXAMPLE_XML_UPLOAD_URL, filename)
    assert container.upload_url == EXAMPLE_XML_UPLOAD_URL
    assert container.upload_id is None
    assert container._headers == {}
    assert container._parts == {}
    assert container._filename == filename

    container = _upload.XMLMPUContainer(
        EXAMPLE_XML_UPLOAD_URL,
        filename,
        headers=EXAMPLE_HEADERS,
        upload_id=UPLOAD_ID,
    )
    container._parts = PARTS
    assert container.upload_url == EXAMPLE_XML_UPLOAD_URL
    assert container.upload_id == UPLOAD_ID
    assert container._headers == EXAMPLE_HEADERS
    assert container._parts == PARTS
    assert container._filename == filename


def test_xml_mpu_container_initiate(filename):
    container = _upload.XMLMPUContainer(
        EXAMPLE_XML_UPLOAD_URL, filename, upload_id=UPLOAD_ID
    )
    with pytest.raises(ValueError):
        container._prepare_initiate_request(BASIC_CONTENT)

    container = _upload.XMLMPUContainer(
        EXAMPLE_XML_UPLOAD_URL, filename, headers=EXAMPLE_HEADERS
    )
    verb, url, body, headers = container._prepare_initiate_request(BASIC_CONTENT)
    assert verb == _upload._POST
    assert url == EXAMPLE_XML_UPLOAD_URL + _upload._MPU_INITIATE_QUERY
    assert not body
    assert headers == {**EXAMPLE_HEADERS, "content-type": BASIC_CONTENT}

    _fix_up_virtual(container)
    response = _make_xml_response(
        text=EXAMPLE_XML_MPU_INITIATE_TEXT_TEMPLATE.format(upload_id=UPLOAD_ID)
    )
    container._process_initiate_response(response)
    assert container.upload_id == UPLOAD_ID

    with pytest.raises(NotImplementedError):
        container.initiate(None, None)


def test_xml_mpu_container_finalize(filename):
    container = _upload.XMLMPUContainer(EXAMPLE_XML_UPLOAD_URL, filename)
    with pytest.raises(ValueError):
        container._prepare_finalize_request()

    container = _upload.XMLMPUContainer(
        EXAMPLE_XML_UPLOAD_URL,
        filename,
        headers=EXAMPLE_HEADERS,
        upload_id=UPLOAD_ID,
    )
    container._parts = PARTS
    verb, url, body, headers = container._prepare_finalize_request()
    assert verb == _upload._POST
    final_query = _upload._MPU_FINAL_QUERY_TEMPLATE.format(upload_id=UPLOAD_ID)
    assert url == EXAMPLE_XML_UPLOAD_URL + final_query
    assert headers == EXAMPLE_HEADERS
    assert b"CompleteMultipartUpload" in body
    for key, value in PARTS.items():
        assert str(key).encode("utf-8") in body
        assert value.encode("utf-8") in body

    _fix_up_virtual(container)
    response = _make_xml_response()
    container._process_finalize_response(response)
    assert container.finished

    with pytest.raises(NotImplementedError):
        container.finalize(None)


def test_xml_mpu_container_cancel(filename):
    container = _upload.XMLMPUContainer(EXAMPLE_XML_UPLOAD_URL, filename)
    with pytest.raises(ValueError):
        container._prepare_cancel_request()

    container = _upload.XMLMPUContainer(
        EXAMPLE_XML_UPLOAD_URL,
        filename,
        headers=EXAMPLE_HEADERS,
        upload_id=UPLOAD_ID,
    )
    container._parts = PARTS
    verb, url, body, headers = container._prepare_cancel_request()
    assert verb == _upload._DELETE
    final_query = _upload._MPU_FINAL_QUERY_TEMPLATE.format(upload_id=UPLOAD_ID)
    assert url == EXAMPLE_XML_UPLOAD_URL + final_query
    assert headers == EXAMPLE_HEADERS
    assert not body

    _fix_up_virtual(container)
    response = _make_xml_response(status_code=204)
    container._process_cancel_response(response)

    with pytest.raises(NotImplementedError):
        container.cancel(None)


def test_xml_mpu_part(filename):
    PART_NUMBER = 1
    START = 0
    END = 256
    ETAG = PARTS[1]

    part = _upload.XMLMPUPart(
        EXAMPLE_XML_UPLOAD_URL,
        UPLOAD_ID,
        filename,
        START,
        END,
        PART_NUMBER,
        headers=EXAMPLE_HEADERS,
        checksum="md5",
    )
    assert part.upload_url == EXAMPLE_XML_UPLOAD_URL
    assert part.upload_id == UPLOAD_ID
    assert part.filename == filename
    assert part.etag is None
    assert part.start == START
    assert part.end == END
    assert part.part_number == PART_NUMBER
    assert part._headers == EXAMPLE_HEADERS
    assert part._checksum_type == "md5"
    assert part._checksum_object is None

    part = _upload.XMLMPUPart(
        EXAMPLE_XML_UPLOAD_URL,
        UPLOAD_ID,
        filename,
        START,
        END,
        PART_NUMBER,
        headers=EXAMPLE_HEADERS,
        checksum="auto",
    )
    assert part.upload_url == EXAMPLE_XML_UPLOAD_URL
    assert part.upload_id == UPLOAD_ID
    assert part.filename == filename
    assert part.etag is None
    assert part.start == START
    assert part.end == END
    assert part.part_number == PART_NUMBER
    assert part._headers == EXAMPLE_HEADERS
    assert part._checksum_type == "crc32c"  # transformed from "auto"
    assert part._checksum_object is None

    part = _upload.XMLMPUPart(
        EXAMPLE_XML_UPLOAD_URL,
        UPLOAD_ID,
        filename,
        START,
        END,
        PART_NUMBER,
        headers=EXAMPLE_HEADERS,
        checksum=None,
    )
    verb, url, payload, headers = part._prepare_upload_request()
    assert verb == _upload._PUT
    assert url == EXAMPLE_XML_UPLOAD_URL + _upload._MPU_PART_QUERY_TEMPLATE.format(
        part=PART_NUMBER, upload_id=UPLOAD_ID
    )
    assert headers == EXAMPLE_HEADERS
    assert payload == FILE_DATA[START:END]

    _fix_up_virtual(part)
    response = _make_xml_response(headers={"etag": ETAG})
    part._process_upload_response(response)
    assert part.etag == ETAG


def test_xml_mpu_part_invalid_response(filename):
    PART_NUMBER = 1
    START = 0
    END = 256
    ETAG = PARTS[1]

    part = _upload.XMLMPUPart(
        EXAMPLE_XML_UPLOAD_URL,
        UPLOAD_ID,
        filename,
        START,
        END,
        PART_NUMBER,
        headers=EXAMPLE_HEADERS,
        checksum="md5",
    )
    _fix_up_virtual(part)
    response = _make_xml_response(headers={"etag": ETAG})
    with pytest.raises(InvalidResponse):
        part._process_upload_response(response)


@pytest.mark.parametrize(
    "error_scenarios",
    [
        INVALID_MD5_XML_RESPONSE,
        INVALID_CRC32C_XML_RESPONSE,
        INCORRECT_LENGTH_CRC32C_XML_RESPONSE,
    ],
)
def test_xml_mpu_part_checksum_failure(filename, error_scenarios):
    PART_NUMBER = 1
    START = 0
    END = 256
    ETAG = PARTS[1]

    part = _upload.XMLMPUPart(
        EXAMPLE_XML_UPLOAD_URL,
        UPLOAD_ID,
        filename,
        START,
        END,
        PART_NUMBER,
        headers=EXAMPLE_HEADERS,
        checksum="md5",
    )
    _fix_up_virtual(part)
    part._prepare_upload_request()
    response = _make_xml_response(
        status_code=http.client.BAD_REQUEST,
        headers={"etag": ETAG, "x-goog-hash": "md5=Ojk9c3dhfxgoKVVHYwFbHQ=="},
        text=error_scenarios,
    )  # Example md5 checksum but not the correct one
    with pytest.raises(DataCorruption):
        part._process_upload_response(response)


def test_xml_mpu_part_checksum_success(filename):
    PART_NUMBER = 1
    START = 0
    END = 256
    ETAG = PARTS[1]

    part = _upload.XMLMPUPart(
        EXAMPLE_XML_UPLOAD_URL,
        UPLOAD_ID,
        filename,
        START,
        END,
        PART_NUMBER,
        headers=EXAMPLE_HEADERS,
        checksum="md5",
    )
    _fix_up_virtual(part)
    part._prepare_upload_request()
    response = _make_xml_response(
        headers={"etag": ETAG, "x-goog-hash": "md5=pOUFGnohRRFFd24NztFuFw=="}
    )
    part._process_upload_response(response)
    assert part.etag == ETAG
    assert part.finished

    # Test error handling
    part = _upload.XMLMPUPart(
        EXAMPLE_XML_UPLOAD_URL,
        UPLOAD_ID,
        filename,
        START,
        END,
        PART_NUMBER,
        headers=EXAMPLE_HEADERS,
        checksum="md5",
    )
    with pytest.raises(NotImplementedError):
        part.upload(None)
    part._finished = True
    with pytest.raises(ValueError):
        part._prepare_upload_request()


def _make_response(status_code=http.client.OK, headers=None, metadata=None):
    headers = headers or {}
    return mock.Mock(
        headers=headers,
        status_code=status_code,
        json=mock.Mock(return_value=metadata),
        spec=["headers", "status_code"],
    )


def _make_xml_response(status_code=http.client.OK, headers=None, text=None):
    headers = headers or {}
    return mock.Mock(
        headers=headers,
        status_code=status_code,
        text=text,
        spec=["headers", "status_code", "text"],
    )


def _get_status_code(response):
    return response.status_code


def _get_headers(response):
    return response.headers


def _fix_up_virtual(upload):
    upload._get_status_code = _get_status_code
    upload._get_headers = _get_headers


def _check_retry_strategy(upload):
    assert upload._retry_strategy == DEFAULT_RETRY
