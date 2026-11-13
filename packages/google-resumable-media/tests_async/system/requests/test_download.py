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
import copy
import hashlib
import http.client
import io
import os

import google.auth.transport._aiohttp_requests as tr_requests  # type: ignore
import multidict  # type: ignore
import pytest  # type: ignore
from google.auth._default_async import default_async  # type: ignore

import google._async_resumable_media.requests as resumable_requests
import google._async_resumable_media.requests.download as download_mod
from google.resumable_media import _helpers, common
from tests.system import utils

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(CURR_DIR, "..", "..", "data")
PLAIN_TEXT = "text/plain"
IMAGE_JPEG = "image/jpeg"
ENCRYPTED_ERR = b"The target object is encrypted by a customer-supplied encryption key."
NO_BODY_ERR = "The content for this response was already consumed"
NOT_FOUND_ERR = (
    b"No such object: " + utils.BUCKET_NAME.encode("utf-8") + b"/does-not-exist.txt"
)
SIMPLE_DOWNLOADS = (resumable_requests.Download, resumable_requests.RawDownload)


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


class CorruptingAuthorizedSession(tr_requests.AuthorizedSession):
    """A Requests Session class with credentials, which corrupts responses.

    This class is used for testing checksum validation.

    Args:
        credentials (google.auth.credentials.Credentials): The credentials to
            add to the request.
        refresh_status_codes (Sequence[int]): Which HTTP status codes indicate
            that credentials should be refreshed and the request should be
            retried.
        max_refresh_attempts (int): The maximum number of times to attempt to
            refresh the credentials and retry the request.
        kwargs: Additional arguments passed to the :class:`requests.Session`
            constructor.
    """

    EMPTY_MD5 = base64.b64encode(hashlib.md5(b"").digest()).decode("utf-8")
    crc32c = _helpers._get_crc32c_object()
    crc32c.update(b"")
    EMPTY_CRC32C = base64.b64encode(crc32c.digest()).decode("utf-8")

    async def request(self, method, url, data=None, headers=None, **kwargs):
        """Implementation of Requests' request."""
        response = await tr_requests.AuthorizedSession.request(
            self, method, url, data=data, headers=headers, **kwargs
        )

        temp = multidict.CIMultiDict(response.headers)
        temp[_helpers._HASH_HEADER] = "crc32c={},md5={}".format(
            self.EMPTY_CRC32C, self.EMPTY_MD5
        )
        response._headers = temp

        return response


def get_path(filename):
    return os.path.realpath(os.path.join(DATA_DIR, filename))


ALL_FILES = (
    {
        "path": get_path("image1.jpg"),
        "content_type": IMAGE_JPEG,
        "md5": "1bsd83IYNug8hd+V1ING3Q==",
        "crc32c": "YQGPxA==",
        "slices": (
            slice(1024, 16386, None),  # obj[1024:16386]
            slice(None, 8192, None),  # obj[:8192]
            slice(-256, None, None),  # obj[-256:]
            slice(262144, None, None),  # obj[262144:]
        ),
    },
    {
        "path": get_path("image2.jpg"),
        "content_type": IMAGE_JPEG,
        "md5": "gdLXJltiYAMP9WZZFEQI1Q==",
        "crc32c": "sxxEFQ==",
        "slices": (
            slice(1024, 16386, None),  # obj[1024:16386]
            slice(None, 8192, None),  # obj[:8192]
            slice(-256, None, None),  # obj[-256:]
            slice(262144, None, None),  # obj[262144:]
        ),
    },
    {
        "path": get_path("file.txt"),
        "content_type": PLAIN_TEXT,
        "md5": "XHSHAr/SpIeZtZbjgQ4nGw==",
        "crc32c": "MeMHoQ==",
        "slices": (),
    },
    {
        "path": get_path("gzipped.txt.gz"),
        "uncompressed": get_path("gzipped.txt"),
        "content_type": PLAIN_TEXT,
        "md5": "KHRs/+ZSrc/FuuR4qz/PZQ==",
        "crc32c": "/LIRNg==",
        "slices": (),
        "metadata": {"contentEncoding": "gzip"},
    },
)


def get_contents_for_upload(info):
    with open(info["path"], "rb") as file_obj:
        return file_obj.read()


def get_contents(info):
    full_path = info.get("uncompressed", info["path"])
    with open(full_path, "rb") as file_obj:
        return file_obj.read()


def get_raw_contents(info):
    full_path = info["path"]
    with open(full_path, "rb") as file_obj:
        return file_obj.read()


def get_blob_name(info):
    full_path = info.get("uncompressed", info["path"])
    return os.path.basename(full_path)


async def delete_blob(transport, blob_name):
    metadata_url = utils.METADATA_URL_TEMPLATE.format(blob_name=blob_name)
    response = await transport.request("DELETE", metadata_url)
    assert response.status == http.client.NO_CONTENT


@pytest.fixture(scope="module")
async def secret_file(authorized_transport, bucket):
    blob_name = "super-seekrit.txt"
    data = b"Please do not tell anyone my encrypted seekrit."

    upload_url = utils.SIMPLE_UPLOAD_TEMPLATE.format(blob_name=blob_name)
    headers = utils.get_encryption_headers()
    upload = resumable_requests.SimpleUpload(upload_url, headers=headers)
    response = await upload.transmit(authorized_transport, data, PLAIN_TEXT)
    assert response.status == http.client.OK

    yield blob_name, data, headers

    await delete_blob(authorized_transport, blob_name)


# Transport that returns corrupt data, so we can exercise checksum handling.
@pytest.fixture(scope="module")
async def corrupting_transport():
    credentials, _ = default_async(scopes=(utils.GCS_RW_SCOPE,))
    yield CorruptingAuthorizedSession(credentials)


@pytest.fixture(scope="module")
async def simple_file(authorized_transport, bucket):
    blob_name = "basic-file.txt"
    upload_url = utils.SIMPLE_UPLOAD_TEMPLATE.format(blob_name=blob_name)
    upload = resumable_requests.SimpleUpload(upload_url)
    data = b"Simple contents"
    response = await upload.transmit(authorized_transport, data, PLAIN_TEXT)
    assert response.status == http.client.OK

    yield blob_name, data

    await delete_blob(authorized_transport, blob_name)


@pytest.fixture(scope="module")
async def add_files(authorized_transport, bucket):
    blob_names = []
    for info in ALL_FILES:
        to_upload = get_contents_for_upload(info)
        blob_name = get_blob_name(info)

        blob_names.append(blob_name)
        if "metadata" in info:
            upload = resumable_requests.MultipartUpload(utils.MULTIPART_UPLOAD)
            metadata = copy.deepcopy(info["metadata"])
            metadata["name"] = blob_name
            response = await upload.transmit(
                authorized_transport, to_upload, metadata, info["content_type"]
            )
        else:
            upload_url = utils.SIMPLE_UPLOAD_TEMPLATE.format(blob_name=blob_name)
            upload = resumable_requests.SimpleUpload(upload_url)
            response = await upload.transmit(
                authorized_transport, to_upload, info["content_type"]
            )

        assert response.status == http.client.OK

    yield

    # Clean-up the blobs we created.
    for blob_name in blob_names:
        await delete_blob(authorized_transport, blob_name)


async def check_tombstoned(download, transport):
    assert download.finished
    if isinstance(download, SIMPLE_DOWNLOADS):
        with pytest.raises(ValueError) as exc_info:
            await download.consume(transport)
        assert exc_info.match("A download can only be used once.")
    else:
        with pytest.raises(ValueError) as exc_info:
            await download.consume_next_chunk(transport)
        assert exc_info.match("Download has finished.")


async def check_error_response(exc_info, status_code, message):
    error = exc_info.value
    response = error.response
    assert response.status == status_code
    content = await response.content.read()
    assert content.startswith(message)
    assert len(error.args) == 5
    assert error.args[1] == status_code
    assert error.args[3] == http.client.OK
    assert error.args[4] == http.client.PARTIAL_CONTENT


class TestDownload(object):
    @staticmethod
    def _get_target_class():
        return resumable_requests.Download

    def _make_one(self, media_url, **kw):
        return self._get_target_class()(media_url, **kw)

    @staticmethod
    def _get_contents(info):
        return get_contents(info)

    @staticmethod
    async def _read_response_content(response):
        content = await response.content()
        return content

    @pytest.mark.asyncio
    @pytest.mark.parametrize("checksum", ["md5", "crc32c", None])
    async def test_download_full(self, add_files, authorized_transport, checksum):
        for info in ALL_FILES:
            actual_contents = self._get_contents(info)
            blob_name = get_blob_name(info)

            # Create the actual download object.
            media_url = utils.DOWNLOAD_URL_TEMPLATE.format(blob_name=blob_name)
            download = self._make_one(media_url, checksum=checksum)
            # Consume the resource.
            response = await download.consume(authorized_transport)
            response = tr_requests._CombinedResponse(response)
            assert response.status == http.client.OK
            content = await self._read_response_content(response)
            assert content == actual_contents
            await check_tombstoned(download, authorized_transport)

    @pytest.mark.asyncio
    async def test_extra_headers(self, authorized_transport, secret_file):
        blob_name, data, headers = secret_file
        # Create the actual download object.
        media_url = utils.DOWNLOAD_URL_TEMPLATE.format(blob_name=blob_name)
        download = self._make_one(media_url, headers=headers)
        # Consume the resource.
        response = await download.consume(authorized_transport)
        assert response.status == http.client.OK
        content = await response.content.read()
        assert content == data
        await check_tombstoned(download, authorized_transport)

        # Attempt to consume the resource **without** the headers.

        download_wo = self._make_one(media_url)

        with pytest.raises(common.InvalidResponse) as exc_info:
            await download_wo.consume(authorized_transport)

        await check_error_response(exc_info, http.client.BAD_REQUEST, ENCRYPTED_ERR)
        await check_tombstoned(download_wo, authorized_transport)

    @pytest.mark.asyncio
    async def test_non_existent_file(self, authorized_transport, bucket):
        blob_name = "does-not-exist.txt"
        media_url = utils.DOWNLOAD_URL_TEMPLATE.format(blob_name=blob_name)
        download = self._make_one(media_url)

        # Try to consume the resource and fail.
        with pytest.raises(common.InvalidResponse) as exc_info:
            await download.consume(authorized_transport)
        await check_error_response(exc_info, http.client.NOT_FOUND, NOT_FOUND_ERR)
        await check_tombstoned(download, authorized_transport)

    @pytest.mark.asyncio
    async def test_bad_range(self, simple_file, authorized_transport):
        blob_name, data = simple_file
        # Make sure we have an invalid range.
        start = 32
        end = 63
        assert len(data) < start < end
        # Create the actual download object.
        media_url = utils.DOWNLOAD_URL_TEMPLATE.format(blob_name=blob_name)
        download = self._make_one(media_url, start=start, end=end)

        # Try to consume the resource and fail.
        with pytest.raises(common.InvalidResponse) as exc_info:
            await download.consume(authorized_transport)

        await check_error_response(
            exc_info,
            http.client.REQUESTED_RANGE_NOT_SATISFIABLE,
            b"Request range not satisfiable",
        )
        await check_tombstoned(download, authorized_transport)

    def _download_slice(self, media_url, slice_):
        assert slice_.step is None

        end = None
        if slice_.stop is not None:
            end = slice_.stop - 1

        return self._make_one(media_url, start=slice_.start, end=end)

    @pytest.mark.asyncio
    async def test_download_partial(self, add_files, authorized_transport):
        for info in ALL_FILES:
            actual_contents = self._get_contents(info)
            blob_name = get_blob_name(info)

            media_url = utils.DOWNLOAD_URL_TEMPLATE.format(blob_name=blob_name)
            for slice_ in info["slices"]:
                download = self._download_slice(media_url, slice_)
                response = await download.consume(authorized_transport)
                assert response.status == http.client.PARTIAL_CONTENT
                content = await response.content.read()
                assert content == actual_contents[slice_]
                with pytest.raises(ValueError):
                    await download.consume(authorized_transport)


class TestRawDownload(TestDownload):
    @staticmethod
    def _get_target_class():
        return resumable_requests.RawDownload

    @staticmethod
    def _get_contents(info):
        return get_raw_contents(info)

    @staticmethod
    async def _read_response_content(response):
        content = await tr_requests._CombinedResponse(response._response).raw_content()
        return content

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    @pytest.mark.asyncio
    async def test_corrupt_download(self, add_files, corrupting_transport, checksum):
        for info in ALL_FILES:
            blob_name = get_blob_name(info)

            # Create the actual download object.
            media_url = utils.DOWNLOAD_URL_TEMPLATE.format(blob_name=blob_name)
            stream = io.BytesIO()
            download = self._make_one(media_url, stream=stream, checksum=checksum)
            # Consume the resource.
            with pytest.raises(common.DataCorruption) as exc_info:
                await download.consume(corrupting_transport)

            assert download.finished

            if checksum == "md5":
                EMPTY_HASH = CorruptingAuthorizedSession.EMPTY_MD5
            else:
                EMPTY_HASH = CorruptingAuthorizedSession.EMPTY_CRC32C

            msg = download_mod._CHECKSUM_MISMATCH.format(
                download.media_url,
                EMPTY_HASH,
                info[checksum],
                checksum_type=checksum.upper(),
            )
            assert exc_info.value.args == (msg,)

    @pytest.mark.parametrize("checksum", ["md5", "crc32c"])
    @pytest.mark.asyncio
    async def test_corrupt_download_no_check(
        self, add_files, corrupting_transport, checksum
    ):
        for info in ALL_FILES:
            blob_name = get_blob_name(info)

            # Create the actual download object.
            media_url = utils.DOWNLOAD_URL_TEMPLATE.format(blob_name=blob_name)
            stream = io.BytesIO()
            download = self._make_one(media_url, stream=stream, checksum=None)
            # Consume the resource.
            await download.consume(corrupting_transport)

            assert download.finished


def get_chunk_size(min_chunks, total_bytes):
    # Make sure the number of chunks **DOES NOT** evenly divide.
    num_chunks = min_chunks
    while total_bytes % num_chunks == 0:
        num_chunks += 1

    chunk_size = total_bytes // num_chunks
    # Since we know an integer division has remainder, increment by 1.
    chunk_size += 1
    assert total_bytes < num_chunks * chunk_size

    return num_chunks, chunk_size


async def consume_chunks(download, authorized_transport, total_bytes, actual_contents):
    start_byte = download.start
    end_byte = download.end
    if end_byte is None:
        end_byte = total_bytes - 1

    num_responses = 0
    while not download.finished:
        response = await download.consume_next_chunk(authorized_transport)
        num_responses += 1

        next_byte = min(start_byte + download.chunk_size, end_byte + 1)
        assert download.bytes_downloaded == next_byte - download.start
        assert download.total_bytes == total_bytes
        assert response.status == http.client.PARTIAL_CONTENT
        # NOTE: Due to the consumption of the stream in the respone, the
        # response object for async requests will be EOF at this point. In
        # sync versions we could compare the content with the range of
        # actual contents. Since streams aren't reversible, we can't do that
        # here.
        assert response.content.at_eof()

        start_byte = next_byte

    return num_responses, response


class TestChunkedDownload(object):
    @staticmethod
    def _get_target_class():
        return resumable_requests.ChunkedDownload

    def _make_one(self, media_url, chunk_size, stream, **kw):
        return self._get_target_class()(media_url, chunk_size, stream, **kw)

    @staticmethod
    def _get_contents(info):
        return get_contents(info)

    @pytest.mark.asyncio
    async def test_chunked_download_partial(self, add_files, authorized_transport):
        for info in ALL_FILES:
            actual_contents = self._get_contents(info)
            blob_name = get_blob_name(info)

            media_url = utils.DOWNLOAD_URL_TEMPLATE.format(blob_name=blob_name)
            for slice_ in info["slices"]:
                # Manually replace a missing start with 0.
                start = 0 if slice_.start is None else slice_.start
                # Chunked downloads don't support a negative index.
                if start < 0:
                    continue

                # First determine how much content is in the slice and
                # use it to determine a chunking strategy.
                total_bytes = len(actual_contents)
                if slice_.stop is None:
                    end_byte = total_bytes - 1
                    end = None
                else:
                    # Python slices DO NOT include the last index, though a byte
                    # range **is** inclusive of both endpoints.
                    end_byte = slice_.stop - 1
                    end = end_byte

                num_chunks, chunk_size = get_chunk_size(7, end_byte - start + 1)
                # Create the actual download object.
                stream = io.BytesIO()
                download = self._make_one(
                    media_url, chunk_size, stream, start=start, end=end
                )
                # Consume the resource in chunks.
                num_responses, last_response = await consume_chunks(
                    download, authorized_transport, total_bytes, actual_contents
                )

                # Make sure the combined chunks are the whole slice.
                assert stream.getvalue() == actual_contents[slice_]
                # Check that we have the right number of responses.
                assert num_responses == num_chunks
                # Make sure the last chunk isn't the same size.
                content = await last_response.content.read()
                assert len(content) < chunk_size
                await check_tombstoned(download, authorized_transport)

    @pytest.mark.asyncio
    async def test_chunked_with_extra_headers(self, authorized_transport, secret_file):
        blob_name, data, headers = secret_file
        num_chunks = 4
        chunk_size = 12
        assert (num_chunks - 1) * chunk_size < len(data) < num_chunks * chunk_size
        # Create the actual download object.
        media_url = utils.DOWNLOAD_URL_TEMPLATE.format(blob_name=blob_name)
        stream = io.BytesIO()
        download = self._make_one(media_url, chunk_size, stream, headers=headers)
        # Consume the resource in chunks.
        num_responses, last_response = await consume_chunks(
            download, authorized_transport, len(data), data
        )
        # Make sure the combined chunks are the whole object.
        assert stream.getvalue() == data
        # Check that we have the right number of responses.
        assert num_responses == num_chunks
        # Make sure the last chunk isn't the same size.

        content = await last_response.read()
        assert len(content) < chunk_size

        await check_tombstoned(download, authorized_transport)
        # Attempt to consume the resource **without** the headers.
        stream_wo = io.BytesIO()
        download_wo = resumable_requests.ChunkedDownload(
            media_url, chunk_size, stream_wo
        )
        with pytest.raises(common.InvalidResponse) as exc_info:
            await download_wo.consume_next_chunk(authorized_transport)

        assert stream_wo.tell() == 0
        await check_error_response(exc_info, http.client.BAD_REQUEST, ENCRYPTED_ERR)
        assert download_wo.invalid


class TestRawChunkedDownload(TestChunkedDownload):
    @staticmethod
    def _get_target_class():
        return resumable_requests.RawChunkedDownload

    @staticmethod
    def _get_contents(info):
        return get_raw_contents(info)

    @pytest.mark.asyncio
    async def test_chunked_download_full(self, add_files, authorized_transport):
        for info in ALL_FILES:
            actual_contents = self._get_contents(info)
            blob_name = get_blob_name(info)

            total_bytes = len(actual_contents)
            num_chunks, chunk_size = get_chunk_size(7, total_bytes)
            # Create the actual download object.
            media_url = utils.DOWNLOAD_URL_TEMPLATE.format(blob_name=blob_name)
            stream = io.BytesIO()
            download = self._make_one(media_url, chunk_size, stream)
            # Consume the resource in chunks.
            num_responses, last_response = await consume_chunks(
                download, authorized_transport, total_bytes, actual_contents
            )
            # Make sure the combined chunks are the whole object.
            assert stream.getvalue() == actual_contents
            # Check that we have the right number of responses.
            assert num_responses == num_chunks
            # Make sure the last chunk isn't the same size.
            assert total_bytes % chunk_size != 0
            content = await last_response.content.read()
            assert len(content) < chunk_size
            await check_tombstoned(download, authorized_transport)
