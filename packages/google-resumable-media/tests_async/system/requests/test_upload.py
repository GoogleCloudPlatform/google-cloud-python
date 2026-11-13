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

import asyncio
import base64
import hashlib
import http.client
import io
import os
import urllib.parse

import mock
import pytest  # type: ignore

import google._async_resumable_media.requests as resumable_requests
from google import _async_resumable_media
from google.resumable_media import _helpers, common
from tests.system import utils

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(CURR_DIR, "..", "..", "data")
ICO_FILE = os.path.realpath(os.path.join(DATA_DIR, "favicon.ico"))
IMAGE_FILE = os.path.realpath(os.path.join(DATA_DIR, "image1.jpg"))
ICO_CONTENT_TYPE = "image/x-icon"
JPEG_CONTENT_TYPE = "image/jpeg"
BYTES_CONTENT_TYPE = "application/octet-stream"
BAD_CHUNK_SIZE_MSG = (
    b"Invalid request.  The number of bytes uploaded is required to be equal "
    b"or greater than 262144, except for the final request (it's recommended "
    b"to be the exact multiple of 262144).  The received request contained "
    b"1024 bytes, which does not meet this requirement."
)


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
async def cleanup():
    to_delete = []

    async def add_cleanup(blob_name, transport):
        to_delete.append((blob_name, transport))

    yield add_cleanup

    for blob_name, transport in to_delete:
        metadata_url = utils.METADATA_URL_TEMPLATE.format(blob_name=blob_name)
        response = await transport.request("DELETE", metadata_url)
        assert response.status == http.client.NO_CONTENT


@pytest.fixture
def img_stream():
    """Open-file as a fixture.

    This is so that an entire test can execute in the context of
    the context manager without worrying about closing the file.
    """
    with open(IMAGE_FILE, "rb") as file_obj:
        yield file_obj


def get_md5(data):
    hash_obj = hashlib.md5(data)
    return base64.b64encode(hash_obj.digest())


def get_upload_id(upload_url):
    parse_result = urllib.parse.urlparse(upload_url)
    parsed_query = urllib.parse.parse_qs(parse_result.query)
    # NOTE: We are unpacking here, so asserting exactly one match.
    (upload_id,) = parsed_query["upload_id"]
    return upload_id


def get_num_chunks(total_bytes, chunk_size):
    expected_chunks, remainder = divmod(total_bytes, chunk_size)
    if remainder > 0:
        expected_chunks += 1
    return expected_chunks


async def check_response(
    response,
    blob_name,
    actual_contents=None,
    total_bytes=None,
    metadata=None,
    content_type=ICO_CONTENT_TYPE,
):
    assert response.status == http.client.OK

    json_response = await response.json()
    assert json_response["bucket"] == utils.BUCKET_NAME
    assert json_response["contentType"] == content_type
    if actual_contents is not None:
        md5_hash = json_response["md5Hash"].encode("ascii")
        assert md5_hash == get_md5(actual_contents)
        total_bytes = len(actual_contents)
    assert json_response["metageneration"] == "1"
    assert json_response["name"] == blob_name
    assert json_response["size"] == "{:d}".format(total_bytes)
    assert json_response["storageClass"] == "STANDARD"
    if metadata is None:
        assert "metadata" not in json_response
    else:
        assert json_response["metadata"] == metadata


async def check_content(blob_name, expected_content, transport, headers=None):
    media_url = utils.DOWNLOAD_URL_TEMPLATE.format(blob_name=blob_name)
    download = resumable_requests.Download(media_url, headers=headers)
    response = await download.consume(transport)
    content = await response.content.read()
    assert response.status == http.client.OK
    assert content == expected_content


async def check_tombstoned(upload, transport, *args):
    assert upload.finished
    basic_types = (resumable_requests.SimpleUpload, resumable_requests.MultipartUpload)

    if isinstance(upload, basic_types):
        with pytest.raises(ValueError):
            await upload.transmit(transport, *args)
    else:
        with pytest.raises(ValueError):
            await upload.transmit_next_chunk(transport, *args)


async def check_does_not_exist(transport, blob_name):
    metadata_url = utils.METADATA_URL_TEMPLATE.format(blob_name=blob_name)
    # Make sure we are creating a **new** object.
    response = await transport.request("GET", metadata_url)
    assert response.status == http.client.NOT_FOUND


async def check_initiate(response, upload, stream, transport, metadata):
    assert response.status == http.client.OK
    content = await response.content.read()
    assert content == b""
    upload_id = get_upload_id(upload.resumable_url)
    assert response.headers["x-guploader-uploadid"] == upload_id
    assert stream.tell() == 0
    # Make sure the upload cannot be re-initiated.
    with pytest.raises(ValueError) as exc_info:
        await upload.initiate(transport, stream, metadata, JPEG_CONTENT_TYPE)

    exc_info.match("This upload has already been initiated.")


async def check_bad_chunk(upload, transport):
    with pytest.raises(_async_resumable_media.InvalidResponse) as exc_info:
        await upload.transmit_next_chunk(transport)
    error = exc_info.value
    response = error.response
    assert response.status == http.client.BAD_REQUEST
    content = await response.content.read()
    assert content == BAD_CHUNK_SIZE_MSG


async def transmit_chunks(
    upload, transport, blob_name, metadata, num_chunks=0, content_type=JPEG_CONTENT_TYPE
):
    while not upload.finished:
        num_chunks += 1
        response = await upload.transmit_next_chunk(transport)
        if upload.finished:
            assert upload.bytes_uploaded == upload.total_bytes
            await check_response(
                response,
                blob_name,
                total_bytes=upload.total_bytes,
                metadata=metadata,
                content_type=content_type,
            )
        else:
            assert upload.bytes_uploaded == num_chunks * upload.chunk_size
            assert response.status == http.client.PERMANENT_REDIRECT

    return num_chunks


@pytest.mark.asyncio
async def test_simple_upload(authorized_transport, bucket, cleanup):
    with open(ICO_FILE, "rb") as file_obj:
        actual_contents = file_obj.read()

    blob_name = os.path.basename(ICO_FILE)
    # Make sure to clean up the uploaded blob when we are done.

    await cleanup(blob_name, authorized_transport)
    await check_does_not_exist(authorized_transport, blob_name)

    # Create the actual upload object.
    upload_url = utils.SIMPLE_UPLOAD_TEMPLATE.format(blob_name=blob_name)
    upload = resumable_requests.SimpleUpload(upload_url)
    # Transmit the resource.
    response = await upload.transmit(
        authorized_transport, actual_contents, ICO_CONTENT_TYPE
    )
    await check_response(response, blob_name, actual_contents=actual_contents)
    # Download the content to make sure it's "working as expected".
    await check_content(blob_name, actual_contents, authorized_transport)
    # Make sure the upload is tombstoned.
    await check_tombstoned(
        upload, authorized_transport, actual_contents, ICO_CONTENT_TYPE
    )


@pytest.mark.asyncio
async def test_simple_upload_with_headers(authorized_transport, bucket, cleanup):
    blob_name = "some-stuff.bin"
    # Make sure to clean up the uploaded blob when we are done.
    await cleanup(blob_name, authorized_transport)
    await check_does_not_exist(authorized_transport, blob_name)

    # Create the actual upload object.
    upload_url = utils.SIMPLE_UPLOAD_TEMPLATE.format(blob_name=blob_name)
    headers = utils.get_encryption_headers()
    upload = resumable_requests.SimpleUpload(upload_url, headers=headers)
    # Transmit the resource.
    data = b"Binary contents\x00\x01\x02."
    response = await upload.transmit(authorized_transport, data, BYTES_CONTENT_TYPE)
    await check_response(
        response, blob_name, actual_contents=data, content_type=BYTES_CONTENT_TYPE
    )
    # Download the content to make sure it's "working as expected".
    await check_content(blob_name, data, authorized_transport, headers=headers)
    # Make sure the upload is tombstoned.
    await check_tombstoned(upload, authorized_transport, data, BYTES_CONTENT_TYPE)


@pytest.mark.asyncio
async def test_multipart_upload(authorized_transport, bucket, cleanup):
    with open(ICO_FILE, "rb") as file_obj:
        actual_contents = file_obj.read()

    blob_name = os.path.basename(ICO_FILE)
    # Make sure to clean up the uploaded blob when we are done.
    await cleanup(blob_name, authorized_transport)
    await check_does_not_exist(authorized_transport, blob_name)

    # Create the actual upload object.
    upload_url = utils.MULTIPART_UPLOAD
    upload = resumable_requests.MultipartUpload(upload_url)
    # Transmit the resource.
    metadata = {"name": blob_name, "metadata": {"color": "yellow"}}
    response = await upload.transmit(
        authorized_transport, actual_contents, metadata, ICO_CONTENT_TYPE
    )
    await check_response(
        response,
        blob_name,
        actual_contents=actual_contents,
        metadata=metadata["metadata"],
    )
    # Download the content to make sure it's "working as expected".
    await check_content(blob_name, actual_contents, authorized_transport)
    # Make sure the upload is tombstoned.
    await check_tombstoned(
        upload, authorized_transport, actual_contents, metadata, ICO_CONTENT_TYPE
    )


@pytest.mark.parametrize("checksum", ["md5", "crc32c"])
@pytest.mark.asyncio
async def test_multipart_upload_with_bad_checksum(
    authorized_transport, checksum, bucket
):
    with open(ICO_FILE, "rb") as file_obj:
        actual_contents = file_obj.read()

    blob_name = os.path.basename(ICO_FILE)
    await check_does_not_exist(authorized_transport, blob_name)

    # Create the actual upload object.
    upload_url = utils.MULTIPART_UPLOAD
    upload = resumable_requests.MultipartUpload(upload_url, checksum=checksum)
    # Transmit the resource.
    metadata = {"name": blob_name, "metadata": {"color": "yellow"}}
    fake_checksum_object = _helpers._get_checksum_object(checksum)
    fake_checksum_object.update(b"bad data")
    fake_prepared_checksum_digest = _helpers.prepare_checksum_digest(
        fake_checksum_object.digest()
    )
    with mock.patch.object(
        _helpers, "prepare_checksum_digest", return_value=fake_prepared_checksum_digest
    ):
        with pytest.raises(common.InvalidResponse) as exc_info:
            await upload.transmit(
                authorized_transport, actual_contents, metadata, ICO_CONTENT_TYPE
            )
    response = exc_info.value.response
    message = await response.text()
    # Attempt to verify that this is a checksum mismatch error.
    assert checksum.upper() in message
    assert fake_prepared_checksum_digest in message

    # Make sure the upload is tombstoned.
    await check_tombstoned(
        upload, authorized_transport, actual_contents, metadata, ICO_CONTENT_TYPE
    )


@pytest.mark.asyncio
async def test_multipart_upload_with_headers(authorized_transport, bucket, cleanup):
    blob_name = "some-multipart-stuff.bin"
    # Make sure to clean up the uploaded blob when we are done.
    await cleanup(blob_name, authorized_transport)
    await check_does_not_exist(authorized_transport, blob_name)

    # Create the actual upload object.
    upload_url = utils.MULTIPART_UPLOAD
    headers = utils.get_encryption_headers()
    upload = resumable_requests.MultipartUpload(upload_url, headers=headers)
    # Transmit the resource.
    metadata = {"name": blob_name}
    data = b"Other binary contents\x03\x04\x05."
    response = await upload.transmit(
        authorized_transport, data, metadata, BYTES_CONTENT_TYPE
    )
    await check_response(
        response, blob_name, actual_contents=data, content_type=BYTES_CONTENT_TYPE
    )
    # Download the content to make sure it's "working as expected".
    await check_content(blob_name, data, authorized_transport, headers=headers)
    # Make sure the upload is tombstoned.
    await check_tombstoned(
        upload, authorized_transport, data, metadata, BYTES_CONTENT_TYPE
    )


async def _resumable_upload_helper(
    authorized_transport, stream, cleanup, checksum=None, headers=None
):
    blob_name = os.path.basename(stream.name)
    # Make sure to clean up the uploaded blob when we are done.
    await cleanup(blob_name, authorized_transport)
    await check_does_not_exist(authorized_transport, blob_name)
    # Create the actual upload object.
    chunk_size = _async_resumable_media.UPLOAD_CHUNK_SIZE
    upload = resumable_requests.ResumableUpload(
        utils.RESUMABLE_UPLOAD, chunk_size, headers=headers, checksum=checksum
    )
    # Initiate the upload.
    metadata = {"name": blob_name, "metadata": {"direction": "north"}}
    response = await upload.initiate(
        authorized_transport, stream, metadata, JPEG_CONTENT_TYPE
    )
    # Make sure ``initiate`` succeeded and did not mangle the stream.
    await check_initiate(response, upload, stream, authorized_transport, metadata)
    # Actually upload the file in chunks.
    num_chunks = await transmit_chunks(
        upload, authorized_transport, blob_name, metadata["metadata"]
    )
    assert num_chunks == get_num_chunks(upload.total_bytes, chunk_size)
    # Download the content to make sure it's "working as expected".
    stream.seek(0)
    actual_contents = stream.read()
    await check_content(
        blob_name, actual_contents, authorized_transport, headers=headers
    )
    # Make sure the upload is tombstoned.
    await check_tombstoned(upload, authorized_transport)


@pytest.mark.asyncio
async def test_resumable_upload(authorized_transport, img_stream, bucket, cleanup):
    await _resumable_upload_helper(authorized_transport, img_stream, cleanup)


@pytest.mark.asyncio
async def test_resumable_upload_with_headers(
    authorized_transport, img_stream, bucket, cleanup
):
    headers = utils.get_encryption_headers()
    await _resumable_upload_helper(
        authorized_transport, img_stream, cleanup, headers=headers
    )


@pytest.mark.parametrize("checksum", ["md5", "crc32c"])
@pytest.mark.asyncio
async def test_resumable_upload_with_bad_checksum(
    authorized_transport, img_stream, bucket, cleanup, checksum
):
    fake_checksum_object = _helpers._get_checksum_object(checksum)
    fake_checksum_object.update(b"bad data")
    fake_prepared_checksum_digest = _helpers.prepare_checksum_digest(
        fake_checksum_object.digest()
    )
    with mock.patch.object(
        _helpers, "prepare_checksum_digest", return_value=fake_prepared_checksum_digest
    ):
        with pytest.raises(common.DataCorruption) as exc_info:
            await _resumable_upload_helper(
                authorized_transport, img_stream, cleanup, checksum=checksum
            )
    expected_checksums = {"md5": "1bsd83IYNug8hd+V1ING3Q==", "crc32c": "YQGPxA=="}
    expected_message = (
        _async_resumable_media._upload._UPLOAD_CHECKSUM_MISMATCH_MESSAGE.format(
            checksum.upper(),
            fake_prepared_checksum_digest,
            expected_checksums[checksum],
        )
    )
    assert exc_info.value.args[0] == expected_message


@pytest.mark.asyncio
async def test_resumable_upload_bad_chunk_size(authorized_transport, img_stream):
    blob_name = os.path.basename(img_stream.name)
    # Create the actual upload object.
    upload = resumable_requests.ResumableUpload(
        utils.RESUMABLE_UPLOAD, _async_resumable_media.UPLOAD_CHUNK_SIZE
    )
    # Modify the ``upload`` **after** construction so we can
    # use a bad chunk size.
    upload._chunk_size = 1024
    assert upload._chunk_size < _async_resumable_media.UPLOAD_CHUNK_SIZE
    # Initiate the upload.
    metadata = {"name": blob_name}
    response = await upload.initiate(
        authorized_transport, img_stream, metadata, JPEG_CONTENT_TYPE
    )
    # Make sure ``initiate`` succeeded and did not mangle the stream.
    await check_initiate(response, upload, img_stream, authorized_transport, metadata)
    # Make the first request and verify that it fails.
    await check_bad_chunk(upload, authorized_transport)
    # Reset the chunk size (and the stream) and verify the "resumable"
    # URL is unusable.
    upload._chunk_size = _async_resumable_media.UPLOAD_CHUNK_SIZE
    img_stream.seek(0)
    upload._invalid = False
    await check_bad_chunk(upload, authorized_transport)


async def sabotage_and_recover(upload, stream, transport, chunk_size):
    assert upload.bytes_uploaded == chunk_size
    assert stream.tell() == chunk_size
    # "Fake" that the instance is in an invalid state.
    upload._invalid = True
    stream.seek(0)  # Seek to the wrong place.
    upload._bytes_uploaded = 0  # Make ``bytes_uploaded`` wrong as well.
    # Recover the (artifically) invalid upload.
    response = await upload.recover(transport)
    assert response.status == http.client.PERMANENT_REDIRECT
    assert not upload.invalid
    assert upload.bytes_uploaded == chunk_size
    assert stream.tell() == chunk_size


async def _resumable_upload_recover_helper(authorized_transport, cleanup, headers=None):
    blob_name = "some-bytes.bin"
    chunk_size = _async_resumable_media.UPLOAD_CHUNK_SIZE
    data = b"123" * chunk_size  # 3 chunks worth.
    # Make sure to clean up the uploaded blob when we are done.
    await cleanup(blob_name, authorized_transport)
    await check_does_not_exist(authorized_transport, blob_name)
    # Create the actual upload object.
    upload = resumable_requests.ResumableUpload(
        utils.RESUMABLE_UPLOAD, chunk_size, headers=headers
    )
    # Initiate the upload.
    metadata = {"name": blob_name}
    stream = io.BytesIO(data)
    response = await upload.initiate(
        authorized_transport, stream, metadata, BYTES_CONTENT_TYPE
    )
    # Make sure ``initiate`` succeeded and did not mangle the stream.
    await check_initiate(response, upload, stream, authorized_transport, metadata)
    # Make the first request.
    response = await upload.transmit_next_chunk(authorized_transport)
    assert response.status == http.client.PERMANENT_REDIRECT
    # Call upload.recover().
    await sabotage_and_recover(upload, stream, authorized_transport, chunk_size)
    # Now stream what remains.
    num_chunks = await transmit_chunks(
        upload,
        authorized_transport,
        blob_name,
        None,
        num_chunks=1,
        content_type=BYTES_CONTENT_TYPE,
    )
    assert num_chunks == 3
    # Download the content to make sure it's "working as expected".
    actual_contents = stream.getvalue()
    await check_content(
        blob_name, actual_contents, authorized_transport, headers=headers
    )
    # Make sure the upload is tombstoned.
    await check_tombstoned(upload, authorized_transport)


@pytest.mark.asyncio
async def test_resumable_upload_recover(authorized_transport, bucket, cleanup):
    await _resumable_upload_recover_helper(authorized_transport, cleanup)


@pytest.mark.asyncio
async def test_resumable_upload_recover_with_headers(
    authorized_transport, bucket, cleanup
):
    headers = utils.get_encryption_headers()
    await _resumable_upload_recover_helper(
        authorized_transport, cleanup, headers=headers
    )


class TestResumableUploadUnknownSize(object):
    @staticmethod
    def _check_range_sent(response, start, end, total):
        headers_sent = response.request_info.headers
        if start is None and end is None:
            expected_content_range = "bytes */{:d}".format(total)
        else:
            # Allow total to be an int or a string "*"
            expected_content_range = "bytes {:d}-{:d}/{}".format(start, end, total)

        assert headers_sent["content-range"] == expected_content_range

    @staticmethod
    def _check_range_received(response, size):
        assert response.headers["range"] == "bytes=0-{:d}".format(size - 1)

    async def _check_partial(self, upload, response, chunk_size, num_chunks):
        start_byte = (num_chunks - 1) * chunk_size
        end_byte = num_chunks * chunk_size - 1

        assert not upload.finished
        assert upload.bytes_uploaded == end_byte + 1
        assert response.status == http.client.PERMANENT_REDIRECT
        content = await response.content.read()
        assert content == b""

        self._check_range_sent(response, start_byte, end_byte, "*")
        self._check_range_received(response, end_byte + 1)

    @pytest.mark.asyncio
    async def test_smaller_than_chunk_size(self, authorized_transport, bucket, cleanup):
        blob_name = os.path.basename(ICO_FILE)
        chunk_size = _async_resumable_media.UPLOAD_CHUNK_SIZE
        # Make sure to clean up the uploaded blob when we are done.
        await cleanup(blob_name, authorized_transport)
        await check_does_not_exist(authorized_transport, blob_name)
        # Make sure the blob is smaller than the chunk size.
        total_bytes = os.path.getsize(ICO_FILE)
        assert total_bytes < chunk_size
        # Create the actual upload object.
        upload = resumable_requests.ResumableUpload(utils.RESUMABLE_UPLOAD, chunk_size)
        # Initiate the upload.
        metadata = {"name": blob_name}
        with open(ICO_FILE, "rb") as stream:
            response = await upload.initiate(
                authorized_transport,
                stream,
                metadata,
                ICO_CONTENT_TYPE,
                stream_final=False,
            )
            # Make sure ``initiate`` succeeded and did not mangle the stream.
            await check_initiate(
                response, upload, stream, authorized_transport, metadata
            )
            # Make sure total bytes was never set.
            assert upload.total_bytes is None
            # Make the **ONLY** request.
            response = await upload.transmit_next_chunk(authorized_transport)
            self._check_range_sent(response, 0, total_bytes - 1, total_bytes)
            await check_response(response, blob_name, total_bytes=total_bytes)
            # Download the content to make sure it's "working as expected".
            stream.seek(0)
            actual_contents = stream.read()
            await check_content(blob_name, actual_contents, authorized_transport)
            # Make sure the upload is tombstoned.
            await check_tombstoned(upload, authorized_transport)

    @pytest.mark.asyncio
    async def test_finish_at_chunk(self, authorized_transport, bucket, cleanup):
        blob_name = "some-clean-stuff.bin"
        chunk_size = _async_resumable_media.UPLOAD_CHUNK_SIZE
        # Make sure to clean up the uploaded blob when we are done.
        await cleanup(blob_name, authorized_transport)
        await check_does_not_exist(authorized_transport, blob_name)
        # Make sure the blob size is an exact multiple of the chunk size.
        data = b"ab" * chunk_size
        total_bytes = len(data)
        stream = io.BytesIO(data)
        # Create the actual upload object.
        upload = resumable_requests.ResumableUpload(utils.RESUMABLE_UPLOAD, chunk_size)
        # Initiate the upload.
        metadata = {"name": blob_name}
        response = await upload.initiate(
            authorized_transport,
            stream,
            metadata,
            BYTES_CONTENT_TYPE,
            stream_final=False,
        )
        # Make sure ``initiate`` succeeded and did not mangle the stream.
        await check_initiate(response, upload, stream, authorized_transport, metadata)
        # Make sure total bytes was never set.
        assert upload.total_bytes is None
        # Make three requests.
        response0 = await upload.transmit_next_chunk(authorized_transport)
        await self._check_partial(upload, response0, chunk_size, 1)

        response1 = await upload.transmit_next_chunk(authorized_transport)
        await self._check_partial(upload, response1, chunk_size, 2)

        response2 = await upload.transmit_next_chunk(authorized_transport)
        assert upload.finished
        # Verify the "clean-up" request.
        assert upload.bytes_uploaded == 2 * chunk_size
        await check_response(
            response2,
            blob_name,
            actual_contents=data,
            total_bytes=total_bytes,
            content_type=BYTES_CONTENT_TYPE,
        )
        self._check_range_sent(response2, None, None, 2 * chunk_size)

    @staticmethod
    def _add_bytes(stream, data):
        curr_pos = stream.tell()
        stream.write(data)
        # Go back to where we were before the write.
        stream.seek(curr_pos)

    @pytest.mark.asyncio
    async def test_interleave_writes(self, authorized_transport, bucket, cleanup):
        blob_name = "some-moar-stuff.bin"
        chunk_size = _async_resumable_media.UPLOAD_CHUNK_SIZE
        # Make sure to clean up the uploaded blob when we are done.
        await cleanup(blob_name, authorized_transport)
        await check_does_not_exist(authorized_transport, blob_name)
        # Start out the blob as a single chunk (but we will add to it).
        stream = io.BytesIO(b"Z" * chunk_size)
        # Create the actual upload object.
        upload = resumable_requests.ResumableUpload(utils.RESUMABLE_UPLOAD, chunk_size)
        # Initiate the upload.
        metadata = {"name": blob_name}
        response = await upload.initiate(
            authorized_transport,
            stream,
            metadata,
            BYTES_CONTENT_TYPE,
            stream_final=False,
        )
        # Make sure ``initiate`` succeeded and did not mangle the stream.
        await check_initiate(response, upload, stream, authorized_transport, metadata)
        # Make sure total bytes was never set.
        assert upload.total_bytes is None
        # Make three requests.
        response0 = await upload.transmit_next_chunk(authorized_transport)
        await self._check_partial(upload, response0, chunk_size, 1)
        # Add another chunk before sending.
        self._add_bytes(stream, b"K" * chunk_size)
        response1 = await upload.transmit_next_chunk(authorized_transport)
        await self._check_partial(upload, response1, chunk_size, 2)
        # Add more bytes, but make sure less than a full chunk.
        last_chunk = 155
        self._add_bytes(stream, b"r" * last_chunk)
        response2 = await upload.transmit_next_chunk(authorized_transport)
        assert upload.finished
        # Verify the "clean-up" request.
        total_bytes = 2 * chunk_size + last_chunk
        assert upload.bytes_uploaded == total_bytes
        await check_response(
            response2,
            blob_name,
            actual_contents=stream.getvalue(),
            total_bytes=total_bytes,
            content_type=BYTES_CONTENT_TYPE,
        )
        self._check_range_sent(response2, 2 * chunk_size, total_bytes - 1, total_bytes)
