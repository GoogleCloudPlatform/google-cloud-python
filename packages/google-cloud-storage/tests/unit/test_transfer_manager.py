# Copyright 2022 Google LLC
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

import concurrent.futures
import io
import os
import pickle
import tempfile
import threading

import mock
import pytest
from google.api_core import exceptions

from google.cloud.storage import Blob, Client, transfer_manager
from google.cloud.storage.exceptions import DataCorruption
from google.cloud.storage.retry import DEFAULT_RETRY

BLOB_TOKEN_STRING = "blob token"
FAKE_CONTENT_TYPE = "text/fake"
UPLOAD_KWARGS = {"content-type": FAKE_CONTENT_TYPE}
FAKE_RESULT = "nothing to see here"
FAKE_ENCODING = "fake_gzip"
DOWNLOAD_KWARGS = {"accept-encoding": FAKE_ENCODING}
CHUNK_SIZE = 8
HOSTNAME = "https://example.com"
URL = "https://example.com/bucket/blob"
USER_AGENT = "agent"
EXPECTED_UPLOAD_KWARGS = {
    "command": "tm.upload_many",
    **UPLOAD_KWARGS,
}
EXPECTED_DOWNLOAD_KWARGS = {
    "command": "tm.download_many",
    **DOWNLOAD_KWARGS,
}


# Used in subprocesses only, so excluded from coverage
def _validate_blob_token_in_subprocess(
    maybe_pickled_blob, method_name, path_or_file, **kwargs
):  # pragma: NO COVER
    assert pickle.loads(maybe_pickled_blob) == BLOB_TOKEN_STRING
    assert "filename" in method_name
    assert path_or_file.startswith("file")
    assert kwargs == EXPECTED_UPLOAD_KWARGS or kwargs == EXPECTED_DOWNLOAD_KWARGS
    return FAKE_RESULT


def test_upload_many_with_filenames():
    FILE_BLOB_PAIRS = [
        ("file_a.txt", mock.Mock(spec=Blob)),
        ("file_b.txt", mock.Mock(spec=Blob)),
    ]
    expected_upload_kwargs = EXPECTED_UPLOAD_KWARGS.copy()
    expected_upload_kwargs["if_generation_match"] = 0

    for _, blob_mock in FILE_BLOB_PAIRS:
        blob_mock._handle_filename_and_upload.return_value = FAKE_RESULT

    results = transfer_manager.upload_many(
        FILE_BLOB_PAIRS,
        skip_if_exists=True,
        upload_kwargs=UPLOAD_KWARGS,
        worker_type=transfer_manager.THREAD,
    )
    for filename, mock_blob in FILE_BLOB_PAIRS:
        mock_blob._handle_filename_and_upload.assert_any_call(
            filename, **expected_upload_kwargs
        )
    for result in results:
        assert result == FAKE_RESULT


def test_upload_many_with_file_objs():
    FILE_BLOB_PAIRS = [
        (tempfile.TemporaryFile(), mock.Mock(spec=Blob)),
        (tempfile.TemporaryFile(), mock.Mock(spec=Blob)),
    ]
    expected_upload_kwargs = EXPECTED_UPLOAD_KWARGS.copy()
    expected_upload_kwargs["if_generation_match"] = 0

    for _, blob_mock in FILE_BLOB_PAIRS:
        blob_mock._prep_and_do_upload.return_value = FAKE_RESULT

    results = transfer_manager.upload_many(
        FILE_BLOB_PAIRS,
        skip_if_exists=True,
        upload_kwargs=UPLOAD_KWARGS,
        worker_type=transfer_manager.THREAD,
    )
    for file, mock_blob in FILE_BLOB_PAIRS:
        mock_blob._prep_and_do_upload.assert_any_call(file, **expected_upload_kwargs)
    for result in results:
        assert result == FAKE_RESULT


def test_upload_many_passes_concurrency_options():
    FILE_BLOB_PAIRS = [
        (tempfile.TemporaryFile(), mock.Mock(spec=Blob)),
        (tempfile.TemporaryFile(), mock.Mock(spec=Blob)),
    ]
    MAX_WORKERS = 7
    DEADLINE = 10
    with (
        mock.patch("concurrent.futures.ThreadPoolExecutor") as pool_patch,
        mock.patch("concurrent.futures.wait") as wait_patch,
    ):
        wait_patch.return_value = ({pool_patch.return_value.submit.return_value}, set())
        transfer_manager.upload_many(
            FILE_BLOB_PAIRS,
            deadline=DEADLINE,
            worker_type=transfer_manager.THREAD,
            max_workers=MAX_WORKERS,
        )
        pool_patch.assert_called_with(max_workers=MAX_WORKERS)
        wait_patch.assert_called_with(mock.ANY, timeout=DEADLINE, return_when=mock.ANY)


def test_threads_deprecation_with_upload():
    FILE_BLOB_PAIRS = [
        (tempfile.TemporaryFile(), mock.Mock(spec=Blob)),
        (tempfile.TemporaryFile(), mock.Mock(spec=Blob)),
    ]
    MAX_WORKERS = 7
    DEADLINE = 10
    with (
        mock.patch("concurrent.futures.ThreadPoolExecutor") as pool_patch,
        mock.patch("concurrent.futures.wait") as wait_patch,
    ):
        wait_patch.return_value = ({pool_patch.return_value.submit.return_value}, set())
        with pytest.warns():
            transfer_manager.upload_many(
                FILE_BLOB_PAIRS, deadline=DEADLINE, threads=MAX_WORKERS
            )
        pool_patch.assert_called_with(max_workers=MAX_WORKERS)
        wait_patch.assert_called_with(mock.ANY, timeout=DEADLINE, return_when=mock.ANY)


def test_threads_deprecation_conflict_with_upload():
    FILE_BLOB_PAIRS = [
        (tempfile.TemporaryFile(), mock.Mock(spec=Blob)),
        (tempfile.TemporaryFile(), mock.Mock(spec=Blob)),
    ]
    MAX_WORKERS = 7
    DEADLINE = 10
    with pytest.raises(ValueError):
        transfer_manager.upload_many(
            FILE_BLOB_PAIRS,
            deadline=DEADLINE,
            threads=5,
            worker_type=transfer_manager.THREAD,
            max_workers=MAX_WORKERS,
        )


def test_upload_many_suppresses_exceptions():
    FILE_BLOB_PAIRS = [
        ("file_a.txt", mock.Mock(spec=Blob)),
        ("file_b.txt", mock.Mock(spec=Blob)),
    ]
    for _, mock_blob in FILE_BLOB_PAIRS:
        mock_blob._handle_filename_and_upload.side_effect = ConnectionError()

    results = transfer_manager.upload_many(
        FILE_BLOB_PAIRS, worker_type=transfer_manager.THREAD
    )
    for result in results:
        assert isinstance(result, ConnectionError)


def test_upload_many_raises_exceptions():
    FILE_BLOB_PAIRS = [
        ("file_a.txt", mock.Mock(spec=Blob)),
        ("file_b.txt", mock.Mock(spec=Blob)),
    ]
    for _, mock_blob in FILE_BLOB_PAIRS:
        mock_blob._handle_filename_and_upload.side_effect = ConnectionError()

    with pytest.raises(ConnectionError):
        transfer_manager.upload_many(
            FILE_BLOB_PAIRS, raise_exception=True, worker_type=transfer_manager.THREAD
        )


def test_upload_many_raises_timeout_error_when_deadline_exceeded():
    stop = threading.Event()

    # Thread-mode: A stuck upload must not make upload_many hang past the deadline.
    def blocking_upload(*args, **kwargs):
        stop.wait(5)

    mock_blob = mock.Mock(spec=Blob)
    mock_blob._prep_and_do_upload.side_effect = blocking_upload

    try:
        with pytest.raises(concurrent.futures.TimeoutError):
            transfer_manager.upload_many(
                [(io.BytesIO(b"data"), mock_blob)],
                worker_type=transfer_manager.THREAD,
                deadline=0.1,
            )
    finally:
        stop.set()


def test_upload_many_terminates_process_workers_on_deadline():
    # Process-mode: A stuck upload must not make upload_many hang past the deadline.
    # After the deadline, the worker processes should be terminated.
    fake_processes = {1: mock.Mock(), 2: mock.Mock()}

    class FakeProcessPoolExecutor(concurrent.futures.ProcessPoolExecutor):
        def __init__(self, *args, **kwargs):
            self._processes = fake_processes

        def submit(self, *args, **kwargs):
            return concurrent.futures.Future()

        def shutdown(self, *args, **kwargs):
            pass

    with (
        mock.patch(
            "google.cloud.storage.transfer_manager._get_pool_class_and_requirements",
            return_value=(FakeProcessPoolExecutor, False),
        ),
        mock.patch("concurrent.futures.wait") as wait_patch,
    ):
        # A non-empty not_done set signals the deadline was exceeded.
        wait_patch.return_value = (set(), {concurrent.futures.Future()})
        with pytest.raises(concurrent.futures.TimeoutError):
            transfer_manager.upload_many(
                [("file_a.txt", mock.Mock(spec=Blob))],
                worker_type=transfer_manager.PROCESS,
                deadline=0.1,
            )

    for process in fake_processes.values():
        process.terminate.assert_called_once_with()


def test_upload_many_suppresses_412_with_skip_if_exists():
    FILE_BLOB_PAIRS = [
        ("file_a.txt", mock.Mock(spec=Blob)),
        ("file_b.txt", mock.Mock(spec=Blob)),
    ]
    for _, mock_blob in FILE_BLOB_PAIRS:
        mock_blob._handle_filename_and_upload.side_effect = (
            exceptions.PreconditionFailed("412")
        )
    results = transfer_manager.upload_many(
        FILE_BLOB_PAIRS,
        skip_if_exists=True,
        raise_exception=True,
        worker_type=transfer_manager.THREAD,
    )
    for result in results:
        assert isinstance(result, exceptions.PreconditionFailed)


def test_upload_many_with_processes():
    # Mocks are not pickleable, so we send token strings over the wire.
    FILE_BLOB_PAIRS = [
        ("file_a.txt", BLOB_TOKEN_STRING),
        ("file_b.txt", BLOB_TOKEN_STRING),
    ]

    with mock.patch(
        "google.cloud.storage.transfer_manager._call_method_on_maybe_pickled_blob",
        new=_validate_blob_token_in_subprocess,
    ):
        results = transfer_manager.upload_many(
            FILE_BLOB_PAIRS,
            upload_kwargs=UPLOAD_KWARGS,
            worker_type=transfer_manager.PROCESS,
            raise_exception=True,
        )
    for result in results:
        assert result == FAKE_RESULT


def test_upload_many_with_processes_rejects_file_obj():
    # Mocks are not pickleable, so we send token strings over the wire.
    FILE_BLOB_PAIRS = [
        ("file_a.txt", BLOB_TOKEN_STRING),
        (tempfile.TemporaryFile(), BLOB_TOKEN_STRING),
    ]

    with mock.patch(
        "google.cloud.storage.transfer_manager._call_method_on_maybe_pickled_blob",
        new=_validate_blob_token_in_subprocess,
    ):
        with pytest.raises(ValueError):
            transfer_manager.upload_many(
                FILE_BLOB_PAIRS,
                upload_kwargs=UPLOAD_KWARGS,
                worker_type=transfer_manager.PROCESS,
            )


def test_download_many_with_filenames():
    BLOB_FILE_PAIRS = [
        (mock.Mock(spec=Blob), "file_a.txt"),
        (mock.Mock(spec=Blob), "file_b.txt"),
    ]

    for blob_mock, _ in BLOB_FILE_PAIRS:
        blob_mock._handle_filename_and_download.return_value = FAKE_RESULT

    results = transfer_manager.download_many(
        BLOB_FILE_PAIRS,
        download_kwargs=DOWNLOAD_KWARGS,
        worker_type=transfer_manager.THREAD,
    )
    for mock_blob, file in BLOB_FILE_PAIRS:
        mock_blob._handle_filename_and_download.assert_any_call(
            file, **EXPECTED_DOWNLOAD_KWARGS
        )
    for result in results:
        assert result == FAKE_RESULT


def test_download_many_with_skip_if_exists():
    with tempfile.NamedTemporaryFile() as tf:
        BLOB_FILE_PAIRS = [
            (mock.Mock(spec=Blob), "file_a.txt"),
            (mock.Mock(spec=Blob), tf.name),
        ]

        for blob_mock, _ in BLOB_FILE_PAIRS:
            blob_mock._handle_filename_and_download.return_value = FAKE_RESULT

        results = transfer_manager.download_many(
            BLOB_FILE_PAIRS,
            download_kwargs=DOWNLOAD_KWARGS,
            worker_type=transfer_manager.THREAD,
            skip_if_exists=True,
        )
        mock_blob, file = BLOB_FILE_PAIRS[0]
        mock_blob._handle_filename_and_download.assert_any_call(
            file, **EXPECTED_DOWNLOAD_KWARGS
        )
        mock_blob, _ = BLOB_FILE_PAIRS[1]
        mock_blob._handle_filename_and_download.assert_not_called()
        for result in results:
            assert result == FAKE_RESULT


def test_download_many_with_file_objs():
    BLOB_FILE_PAIRS = [
        (mock.Mock(spec=Blob), tempfile.TemporaryFile()),
        (mock.Mock(spec=Blob), tempfile.TemporaryFile()),
    ]

    for blob_mock, _ in BLOB_FILE_PAIRS:
        blob_mock._prep_and_do_download.return_value = FAKE_RESULT

    results = transfer_manager.download_many(
        BLOB_FILE_PAIRS,
        download_kwargs=DOWNLOAD_KWARGS,
        worker_type=transfer_manager.THREAD,
    )
    for mock_blob, file in BLOB_FILE_PAIRS:
        mock_blob._prep_and_do_download.assert_any_call(file, **DOWNLOAD_KWARGS)
    for result in results:
        assert result == FAKE_RESULT


def test_download_many_passes_concurrency_options():
    BLOB_FILE_PAIRS = [
        (mock.Mock(spec=Blob), tempfile.TemporaryFile()),
        (mock.Mock(spec=Blob), tempfile.TemporaryFile()),
    ]
    MAX_WORKERS = 7
    DEADLINE = 10
    with (
        mock.patch("concurrent.futures.ThreadPoolExecutor") as pool_patch,
        mock.patch("concurrent.futures.wait") as wait_patch,
    ):
        transfer_manager.download_many(
            BLOB_FILE_PAIRS,
            deadline=DEADLINE,
            worker_type=transfer_manager.THREAD,
            max_workers=MAX_WORKERS,
        )
        pool_patch.assert_called_with(max_workers=MAX_WORKERS)
        wait_patch.assert_called_with(mock.ANY, timeout=DEADLINE, return_when=mock.ANY)


def test_download_many_suppresses_exceptions():
    BLOB_FILE_PAIRS = [
        (mock.Mock(spec=Blob), "file_a.txt"),
        (mock.Mock(spec=Blob), "file_b.txt"),
    ]
    for mock_blob, _ in BLOB_FILE_PAIRS:
        mock_blob._handle_filename_and_download.side_effect = ConnectionError()

    results = transfer_manager.download_many(
        BLOB_FILE_PAIRS, worker_type=transfer_manager.THREAD
    )
    for result in results:
        assert isinstance(result, ConnectionError)


def test_download_many_raises_exceptions():
    BLOB_FILE_PAIRS = [
        (mock.Mock(spec=Blob), "file_a.txt"),
        (mock.Mock(spec=Blob), "file_b.txt"),
    ]
    for mock_blob, _ in BLOB_FILE_PAIRS:
        mock_blob._handle_filename_and_download.side_effect = ConnectionError()

    with pytest.raises(ConnectionError):
        transfer_manager.download_many(
            BLOB_FILE_PAIRS, raise_exception=True, worker_type=transfer_manager.THREAD
        )


def test_download_many_with_processes():
    # Mocks are not pickleable, so we send token strings over the wire.
    BLOB_FILE_PAIRS = [
        (BLOB_TOKEN_STRING, "file_a.txt"),
        (BLOB_TOKEN_STRING, "file_b.txt"),
    ]

    with mock.patch(
        "google.cloud.storage.transfer_manager._call_method_on_maybe_pickled_blob",
        new=_validate_blob_token_in_subprocess,
    ):
        results = transfer_manager.download_many(
            BLOB_FILE_PAIRS,
            download_kwargs=DOWNLOAD_KWARGS,
            worker_type=transfer_manager.PROCESS,
        )
    for result in results:
        assert result == FAKE_RESULT


def test_download_many_with_processes_rejects_file_obj():
    # Mocks are not pickleable, so we send token strings over the wire.
    BLOB_FILE_PAIRS = [
        (BLOB_TOKEN_STRING, "file_a.txt"),
        (BLOB_TOKEN_STRING, tempfile.TemporaryFile()),
    ]

    with mock.patch(
        "google.cloud.storage.transfer_manager._call_method_on_maybe_pickled_blob",
        new=_validate_blob_token_in_subprocess,
    ):
        with pytest.raises(ValueError):
            transfer_manager.download_many(
                BLOB_FILE_PAIRS,
                download_kwargs=DOWNLOAD_KWARGS,
                worker_type=transfer_manager.PROCESS,
            )


def test_upload_many_from_filenames():
    bucket = mock.Mock()

    FILENAMES = ["file_a.txt", "file_b.txt"]
    ROOT = "mypath/"
    PREFIX = "myprefix/"
    KEY_NAME = "keyname"
    BLOB_CONSTRUCTOR_KWARGS = {"kms_key_name": KEY_NAME}
    UPLOAD_KWARGS = {"content-type": "text/fake"}
    MAX_WORKERS = 7
    DEADLINE = 10
    WORKER_TYPE = transfer_manager.THREAD

    EXPECTED_FILE_BLOB_PAIRS = [
        (os.path.join(ROOT, filename), mock.ANY) for filename in FILENAMES
    ]

    with mock.patch(
        "google.cloud.storage.transfer_manager.upload_many"
    ) as mock_upload_many:
        transfer_manager.upload_many_from_filenames(
            bucket,
            FILENAMES,
            source_directory=ROOT,
            blob_name_prefix=PREFIX,
            skip_if_exists=True,
            blob_constructor_kwargs=BLOB_CONSTRUCTOR_KWARGS,
            upload_kwargs=UPLOAD_KWARGS,
            deadline=DEADLINE,
            raise_exception=True,
            worker_type=WORKER_TYPE,
            max_workers=MAX_WORKERS,
        )

    mock_upload_many.assert_called_once_with(
        EXPECTED_FILE_BLOB_PAIRS,
        skip_if_exists=True,
        upload_kwargs=UPLOAD_KWARGS,
        deadline=DEADLINE,
        raise_exception=True,
        worker_type=WORKER_TYPE,
        max_workers=MAX_WORKERS,
    )
    bucket.blob.assert_any_call(PREFIX + FILENAMES[0], **BLOB_CONSTRUCTOR_KWARGS)
    bucket.blob.assert_any_call(PREFIX + FILENAMES[1], **BLOB_CONSTRUCTOR_KWARGS)


def test_upload_many_from_filenames_minimal_args():
    bucket = mock.Mock()

    FILENAMES = ["file_a.txt", "file_b.txt"]

    EXPECTED_FILE_BLOB_PAIRS = [(filename, mock.ANY) for filename in FILENAMES]

    with mock.patch(
        "google.cloud.storage.transfer_manager.upload_many"
    ) as mock_upload_many:
        transfer_manager.upload_many_from_filenames(
            bucket,
            FILENAMES,
        )

    mock_upload_many.assert_called_once_with(
        EXPECTED_FILE_BLOB_PAIRS,
        skip_if_exists=False,
        upload_kwargs=None,
        deadline=None,
        raise_exception=False,
        worker_type=transfer_manager.PROCESS,
        max_workers=8,
    )
    bucket.blob.assert_any_call(FILENAMES[0])
    bucket.blob.assert_any_call(FILENAMES[1])


def test_upload_many_from_filenames_additional_properties():
    bucket = mock.Mock()
    blob = mock.Mock()
    bucket_blob = mock.Mock(return_value=blob)
    blob.cache_control = None
    bucket.blob = bucket_blob

    FILENAME = "file_a.txt"
    ADDITIONAL_BLOB_ATTRIBUTES = {"cache_control": "no-cache"}
    EXPECTED_FILE_BLOB_PAIRS = [(FILENAME, mock.ANY)]

    with mock.patch(
        "google.cloud.storage.transfer_manager.upload_many"
    ) as mock_upload_many:
        transfer_manager.upload_many_from_filenames(
            bucket, [FILENAME], additional_blob_attributes=ADDITIONAL_BLOB_ATTRIBUTES
        )

    mock_upload_many.assert_called_once_with(
        EXPECTED_FILE_BLOB_PAIRS,
        skip_if_exists=False,
        upload_kwargs=None,
        deadline=None,
        raise_exception=False,
        worker_type=transfer_manager.PROCESS,
        max_workers=8,
    )

    for attrib, value in ADDITIONAL_BLOB_ATTRIBUTES.items():
        assert getattr(blob, attrib) == value


def test__resolve_path_raises_invalid_path_error_on_windows():
    from google.cloud.storage.transfer_manager import InvalidPathError, _resolve_path

    with mock.patch("os.name", "nt"):
        with pytest.raises(InvalidPathError) as exc_info:
            _resolve_path("C:\\target", "C:\\target\\file.txt")
        assert "cannot be downloaded into" in str(exc_info.value)

    # Test that it DOES NOT raise on non-windows
    with mock.patch("os.name", "posix"):
        # Should not raise
        _resolve_path("/target", "C:\\target\\file.txt")


def test_download_many_to_path_raises_invalid_path_error():
    bucket = mock.Mock()

    BLOBNAMES = ["C:\\target\\file.txt"]
    PATH_ROOT = "mypath/"
    BLOB_NAME_PREFIX = "myprefix/"
    DOWNLOAD_KWARGS = {"accept-encoding": "fake-gzip"}
    MAX_WORKERS = 7
    DEADLINE = 10
    WORKER_TYPE = transfer_manager.THREAD

    with mock.patch("os.name", "nt"):
        import warnings

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            results = transfer_manager.download_many_to_path(
                bucket,
                BLOBNAMES,
                destination_directory=PATH_ROOT,
                blob_name_prefix=BLOB_NAME_PREFIX,
                download_kwargs=DOWNLOAD_KWARGS,
                deadline=DEADLINE,
                create_directories=False,
                raise_exception=True,
                max_workers=MAX_WORKERS,
                worker_type=WORKER_TYPE,
                skip_if_exists=True,
            )

    invalid_path_warnings = [
        warning
        for warning in w
        if str(warning.message).startswith("The blob ")
        and "will **NOT** be downloaded" in str(warning.message)
    ]

    assert len(invalid_path_warnings) == 1, (
        f"Expected 1 invalid path warning, found {len(invalid_path_warnings)}. All warnings: {[str(warning.message) for warning in w]}"
    )

    assert len(results) == 1
    assert isinstance(results[0], UserWarning)


def test_download_many_to_path():
    bucket = mock.Mock()

    BLOBNAMES = ["file_a.txt", "file_b.txt", "dir_a/file_c.txt"]
    PATH_ROOT = "mypath/"
    BLOB_NAME_PREFIX = "myprefix/"
    DOWNLOAD_KWARGS = {"accept-encoding": "fake-gzip"}
    MAX_WORKERS = 7
    DEADLINE = 10
    WORKER_TYPE = transfer_manager.THREAD

    EXPECTED_BLOB_FILE_PAIRS = [
        (mock.ANY, os.path.join(os.getcwd(), PATH_ROOT, blobname))
        for blobname in BLOBNAMES
    ]

    with mock.patch(
        "google.cloud.storage.transfer_manager.download_many",
        return_value=[FAKE_RESULT] * len(BLOBNAMES),
    ) as mock_download_many:
        results = transfer_manager.download_many_to_path(
            bucket,
            BLOBNAMES,
            destination_directory=PATH_ROOT,
            blob_name_prefix=BLOB_NAME_PREFIX,
            download_kwargs=DOWNLOAD_KWARGS,
            deadline=DEADLINE,
            create_directories=False,
            raise_exception=True,
            max_workers=MAX_WORKERS,
            worker_type=WORKER_TYPE,
            skip_if_exists=True,
        )

    mock_download_many.assert_called_once_with(
        EXPECTED_BLOB_FILE_PAIRS,
        download_kwargs=DOWNLOAD_KWARGS,
        deadline=DEADLINE,
        raise_exception=True,
        max_workers=MAX_WORKERS,
        worker_type=WORKER_TYPE,
        skip_if_exists=False,
    )
    assert results == [FAKE_RESULT] * len(BLOBNAMES)
    for blobname in BLOBNAMES:
        bucket.blob.assert_any_call(BLOB_NAME_PREFIX + blobname)


def test_download_many_to_path_with_skip_if_exists():
    bucket = mock.Mock()

    BLOBNAMES = ["file_a.txt", "file_b.txt", "dir_a/file_c.txt"]
    PATH_ROOT = "mypath/"
    BLOB_NAME_PREFIX = "myprefix/"
    DOWNLOAD_KWARGS = {"accept-encoding": "fake-gzip"}
    MAX_WORKERS = 7
    DEADLINE = 10
    WORKER_TYPE = transfer_manager.THREAD

    from google.cloud.storage.transfer_manager import _resolve_path

    existing_file = str(_resolve_path(PATH_ROOT, "file_a.txt"))

    def isfile_side_effect(path):
        return path == existing_file

    EXPECTED_BLOB_FILE_PAIRS = [
        (mock.ANY, str(_resolve_path(PATH_ROOT, "file_b.txt"))),
        (mock.ANY, str(_resolve_path(PATH_ROOT, "dir_a/file_c.txt"))),
    ]

    with mock.patch("os.path.isfile", side_effect=isfile_side_effect):
        with mock.patch(
            "google.cloud.storage.transfer_manager.download_many",
            return_value=[FAKE_RESULT, FAKE_RESULT],
        ) as mock_download_many:
            results = transfer_manager.download_many_to_path(
                bucket,
                BLOBNAMES,
                destination_directory=PATH_ROOT,
                blob_name_prefix=BLOB_NAME_PREFIX,
                download_kwargs=DOWNLOAD_KWARGS,
                deadline=DEADLINE,
                create_directories=False,
                raise_exception=True,
                max_workers=MAX_WORKERS,
                worker_type=WORKER_TYPE,
                skip_if_exists=True,
            )

    mock_download_many.assert_called_once_with(
        EXPECTED_BLOB_FILE_PAIRS,
        download_kwargs=DOWNLOAD_KWARGS,
        deadline=DEADLINE,
        raise_exception=True,
        max_workers=MAX_WORKERS,
        worker_type=WORKER_TYPE,
        skip_if_exists=False,
    )

    assert len(results) == 3
    assert isinstance(results[0], UserWarning)
    assert (
        str(results[0])
        == "The blob file_a.txt is skipped because destination file already exists"
    )
    assert results[1] == FAKE_RESULT
    assert results[2] == FAKE_RESULT


@pytest.mark.parametrize(
    "blobname",
    [
        "../../local/target",
        "../mypath",
        "../escape.txt",
        "go/four/levels/deep/../../../../../somefile1",
        "go/four/levels/deep/../some_dir/../../../../../invalid/path1",
    ],
)
def test_download_many_to_path_skips_download(blobname):
    bucket = mock.Mock()
    BLOBNAMES = [blobname]

    PATH_ROOT = "mypath/"
    BLOB_NAME_PREFIX = "myprefix/"
    DOWNLOAD_KWARGS = {"accept-encoding": "fake-gzip"}
    MAX_WORKERS = 7
    DEADLINE = 10
    WORKER_TYPE = transfer_manager.THREAD

    import warnings

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        with mock.patch(
            "google.cloud.storage.transfer_manager.download_many",
            return_value=[],
        ) as mock_download_many:
            results = transfer_manager.download_many_to_path(
                bucket,
                BLOBNAMES,
                destination_directory=PATH_ROOT,
                blob_name_prefix=BLOB_NAME_PREFIX,
                download_kwargs=DOWNLOAD_KWARGS,
                deadline=DEADLINE,
                create_directories=False,
                raise_exception=True,
                max_workers=MAX_WORKERS,
                worker_type=WORKER_TYPE,
                skip_if_exists=True,
            )

    path_traversal_warnings = [
        warning
        for warning in w
        if str(warning.message).startswith("The blob ")
        and "will **NOT** be downloaded. The resolved destination_directory"
        in str(warning.message)
    ]
    assert len(path_traversal_warnings) == 1, "---".join(
        [str(warning.message) for warning in w]
    )

    mock_download_many.assert_called_once_with(
        [],
        download_kwargs=DOWNLOAD_KWARGS,
        deadline=DEADLINE,
        raise_exception=True,
        max_workers=MAX_WORKERS,
        worker_type=WORKER_TYPE,
        skip_if_exists=False,
    )
    assert len(results) == 1
    assert isinstance(results[0], UserWarning)


@pytest.mark.parametrize(
    "blobname",
    [
        "simple_blob",
        "data/file.txt",
        "data/../sibling.txt",
        "/etc/passwd",
        "/local/usr/a.txt",
        "dir/./file.txt",
        "go/four/levels/deep/../somefile2",
        "go/four/levels/deep/../some_dir/valid/path1",
        "go/four/levels/deep/../some_dir/../../../../valid/path2",
    ],
)
def test_download_many_to_path_downloads_within_dest_dir(blobname):
    bucket = mock.Mock()
    BLOBNAMES = [blobname]

    PATH_ROOT = "mypath/"
    BLOB_NAME_PREFIX = "myprefix/"
    DOWNLOAD_KWARGS = {"accept-encoding": "fake-gzip"}
    MAX_WORKERS = 7
    DEADLINE = 10
    WORKER_TYPE = transfer_manager.THREAD

    from google.cloud.storage.transfer_manager import _resolve_path

    EXPECTED_BLOB_FILE_PAIRS = [(mock.ANY, str(_resolve_path(PATH_ROOT, blobname)))]

    with mock.patch(
        "google.cloud.storage.transfer_manager.download_many",
        return_value=[FAKE_RESULT],
    ) as mock_download_many:
        results = transfer_manager.download_many_to_path(
            bucket,
            BLOBNAMES,
            destination_directory=PATH_ROOT,
            blob_name_prefix=BLOB_NAME_PREFIX,
            download_kwargs=DOWNLOAD_KWARGS,
            deadline=DEADLINE,
            create_directories=False,
            raise_exception=True,
            max_workers=MAX_WORKERS,
            worker_type=WORKER_TYPE,
            skip_if_exists=True,
        )

    mock_download_many.assert_called_once_with(
        EXPECTED_BLOB_FILE_PAIRS,
        download_kwargs=DOWNLOAD_KWARGS,
        deadline=DEADLINE,
        raise_exception=True,
        max_workers=MAX_WORKERS,
        worker_type=WORKER_TYPE,
        skip_if_exists=False,
    )
    assert results == [FAKE_RESULT]
    bucket.blob.assert_any_call(BLOB_NAME_PREFIX + blobname)


def test_download_many_to_path_creates_directories():
    bucket = mock.Mock()

    with tempfile.TemporaryDirectory() as tempdir:
        DIR_NAME = "dir_a/dir_b"
        BLOBNAMES = [
            "file_a.txt",
            "file_b.txt",
            os.path.join(DIR_NAME, "file_c.txt"),
        ]

        EXPECTED_BLOB_FILE_PAIRS = [
            (mock.ANY, os.path.join(tempdir, blobname)) for blobname in BLOBNAMES
        ]

        with mock.patch(
            "google.cloud.storage.transfer_manager.download_many"
        ) as mock_download_many:
            transfer_manager.download_many_to_path(
                bucket,
                BLOBNAMES,
                destination_directory=tempdir,
                create_directories=True,
                raise_exception=True,
            )

        mock_download_many.assert_called_once_with(
            EXPECTED_BLOB_FILE_PAIRS,
            download_kwargs=None,
            deadline=None,
            raise_exception=True,
            worker_type=transfer_manager.PROCESS,
            max_workers=8,
            skip_if_exists=False,
        )
        for blobname in BLOBNAMES:
            bucket.blob.assert_any_call(blobname)

        assert os.path.isdir(os.path.join(tempdir, DIR_NAME))


def test_download_chunks_concurrently():
    blob_mock = mock.Mock(spec=Blob)
    FILENAME = "file_a.txt"
    MULTIPLE = 4
    blob_mock.size = CHUNK_SIZE * MULTIPLE

    expected_download_kwargs = EXPECTED_DOWNLOAD_KWARGS.copy()
    expected_download_kwargs["command"] = "tm.download_sharded"
    expected_download_kwargs["checksum"] = None

    with mock.patch("google.cloud.storage.transfer_manager.open", mock.mock_open()):
        result = transfer_manager.download_chunks_concurrently(
            blob_mock,
            FILENAME,
            chunk_size=CHUNK_SIZE,
            download_kwargs=DOWNLOAD_KWARGS,
            worker_type=transfer_manager.THREAD,
            crc32c_checksum=False,
        )
    for x in range(MULTIPLE):
        blob_mock._prep_and_do_download.assert_any_call(
            mock.ANY,
            **expected_download_kwargs,
            start=x * CHUNK_SIZE,
            end=((x + 1) * CHUNK_SIZE) - 1,
        )
    assert blob_mock._prep_and_do_download.call_count == 4
    assert result is None


def test_download_chunks_concurrently_with_crc32c():
    blob_mock = mock.Mock(spec=Blob)
    FILENAME = "file_a.txt"
    MULTIPLE = 4
    BLOB_CHUNK = b"abcdefgh"
    BLOB_CONTENTS = BLOB_CHUNK * MULTIPLE
    blob_mock.size = len(BLOB_CONTENTS)
    blob_mock.crc32c = "eOVVVw=="

    def write_to_file(f, *args, **kwargs):
        f.write(BLOB_CHUNK)

    blob_mock._prep_and_do_download.side_effect = write_to_file

    with mock.patch("google.cloud.storage.transfer_manager.open", mock.mock_open()):
        transfer_manager.download_chunks_concurrently(
            blob_mock,
            FILENAME,
            chunk_size=CHUNK_SIZE,
            download_kwargs=DOWNLOAD_KWARGS,
            worker_type=transfer_manager.THREAD,
            crc32c_checksum=True,
        )


def test_download_chunks_concurrently_with_crc32c_failure():
    blob_mock = mock.Mock(spec=Blob)
    FILENAME = "file_a.txt"
    MULTIPLE = 4
    BLOB_CHUNK = b"abcdefgh"
    BLOB_CONTENTS = BLOB_CHUNK * MULTIPLE
    blob_mock.size = len(BLOB_CONTENTS)
    blob_mock.crc32c = "invalid"

    def write_to_file(f, *args, **kwargs):
        f.write(BLOB_CHUNK)

    blob_mock._prep_and_do_download.side_effect = write_to_file

    with mock.patch("google.cloud.storage.transfer_manager.open", mock.mock_open()):
        with pytest.raises(DataCorruption):
            transfer_manager.download_chunks_concurrently(
                blob_mock,
                FILENAME,
                chunk_size=CHUNK_SIZE,
                download_kwargs=DOWNLOAD_KWARGS,
                worker_type=transfer_manager.THREAD,
                crc32c_checksum=True,
            )


def test_download_chunks_concurrently_raises_on_invalid_kwargs():
    blob_mock = mock.Mock(spec=Blob)
    FILENAME = "file_a.txt"
    MULTIPLE = 4
    blob_mock.size = CHUNK_SIZE * MULTIPLE

    with mock.patch("google.cloud.storage.transfer_manager.open", mock.mock_open()):
        with pytest.raises(ValueError):
            transfer_manager.download_chunks_concurrently(
                blob_mock,
                FILENAME,
                chunk_size=CHUNK_SIZE,
                worker_type=transfer_manager.THREAD,
                download_kwargs={
                    "start": CHUNK_SIZE,
                },
            )
        with pytest.raises(ValueError):
            transfer_manager.download_chunks_concurrently(
                blob_mock,
                FILENAME,
                chunk_size=CHUNK_SIZE,
                worker_type=transfer_manager.THREAD,
                download_kwargs={
                    "end": (CHUNK_SIZE * (MULTIPLE - 1)) - 1,
                },
            )
        with pytest.raises(ValueError):
            transfer_manager.download_chunks_concurrently(
                blob_mock,
                FILENAME,
                chunk_size=CHUNK_SIZE,
                worker_type=transfer_manager.THREAD,
                download_kwargs={
                    "checksum": "crc32c",
                },
            )


def test_download_chunks_concurrently_passes_concurrency_options():
    blob_mock = mock.Mock(spec=Blob)
    FILENAME = "file_a.txt"
    MAX_WORKERS = 7
    DEADLINE = 10
    MULTIPLE = 4
    blob_mock.size = CHUNK_SIZE * MULTIPLE

    with (
        mock.patch("concurrent.futures.ThreadPoolExecutor") as pool_patch,
        mock.patch("concurrent.futures.wait") as wait_patch,
        mock.patch("google.cloud.storage.transfer_manager.open", mock.mock_open()),
    ):
        transfer_manager.download_chunks_concurrently(
            blob_mock,
            FILENAME,
            chunk_size=CHUNK_SIZE,
            deadline=DEADLINE,
            worker_type=transfer_manager.THREAD,
            max_workers=MAX_WORKERS,
            crc32c_checksum=False,
        )
        pool_patch.assert_called_with(max_workers=MAX_WORKERS)
        wait_patch.assert_called_with(mock.ANY, timeout=DEADLINE, return_when=mock.ANY)


def test_upload_chunks_concurrently():
    bucket = mock.Mock()
    bucket.name = "bucket"
    bucket.client = _PickleableMockClient(identify_as_client=True)
    transport = bucket.client._http
    bucket.user_project = None

    blob = Blob("blob", bucket)
    blob.content_type = FAKE_CONTENT_TYPE

    FILENAME = "file_a.txt"
    SIZE = 2048

    container_mock = mock.Mock()
    container_mock.upload_id = "abcd"
    part_mock = mock.Mock()
    ETAG = "efgh"
    part_mock.etag = ETAG

    with (
        mock.patch("os.path.getsize", return_value=SIZE),
        mock.patch(
            "google.cloud.storage.transfer_manager.XMLMPUContainer",
            return_value=container_mock,
        ),
        mock.patch(
            "google.cloud.storage.transfer_manager.XMLMPUPart", return_value=part_mock
        ),
    ):
        transfer_manager.upload_chunks_concurrently(
            FILENAME,
            blob,
            chunk_size=SIZE // 2,
            worker_type=transfer_manager.THREAD,
        )
        container_mock.initiate.assert_called_once_with(
            transport=transport, content_type=blob.content_type
        )
        container_mock.register_part.assert_any_call(1, ETAG)
        container_mock.register_part.assert_any_call(2, ETAG)
        container_mock.finalize.assert_called_once_with(bucket.client._http)

        part_mock.upload.assert_called_with(transport)


def test_upload_chunks_concurrently_quotes_urls():
    bucket = mock.Mock()
    bucket.name = "bucket"
    bucket.client = _PickleableMockClient(identify_as_client=True)
    transport = bucket.client._http
    bucket.user_project = None

    blob = Blob(b"../wrongbucket/blob", bucket)
    blob.content_type = FAKE_CONTENT_TYPE
    quoted_url = "https://example.com/bucket/..%2Fwrongbucket%2Fblob"

    FILENAME = "file_a.txt"
    SIZE = 2048

    container_mock = mock.Mock()
    container_mock.upload_id = "abcd"
    part_mock = mock.Mock()
    ETAG = "efgh"
    part_mock.etag = ETAG
    container_cls_mock = mock.Mock(return_value=container_mock)

    with (
        mock.patch("os.path.getsize", return_value=SIZE),
        mock.patch(
            "google.cloud.storage.transfer_manager.XMLMPUContainer",
            new=container_cls_mock,
        ),
        mock.patch(
            "google.cloud.storage.transfer_manager.XMLMPUPart", return_value=part_mock
        ),
    ):
        transfer_manager.upload_chunks_concurrently(
            FILENAME,
            blob,
            chunk_size=SIZE // 2,
            worker_type=transfer_manager.THREAD,
        )

        container_mock.initiate.assert_called_once_with(
            transport=transport, content_type=blob.content_type
        )
        container_mock.register_part.assert_any_call(1, ETAG)
        container_mock.register_part.assert_any_call(2, ETAG)
        container_mock.finalize.assert_called_once_with(bucket.client._http)

        container_cls_mock.assert_called_once_with(
            quoted_url, FILENAME, headers=mock.ANY, retry=DEFAULT_RETRY
        )

        part_mock.upload.assert_called_with(transport)


def test_upload_chunks_concurrently_passes_concurrency_options():
    bucket = mock.Mock()
    bucket.name = "bucket"
    bucket.client = _PickleableMockClient(identify_as_client=True)
    transport = bucket.client._http
    bucket.user_project = None

    blob = Blob("blob", bucket)

    FILENAME = "file_a.txt"
    SIZE = 2048

    container_mock = mock.Mock()
    container_mock.upload_id = "abcd"

    MAX_WORKERS = 7
    DEADLINE = 10

    with (
        mock.patch("os.path.getsize", return_value=SIZE),
        mock.patch(
            "google.cloud.storage.transfer_manager.XMLMPUContainer",
            return_value=container_mock,
        ),
        mock.patch("concurrent.futures.ThreadPoolExecutor") as pool_patch,
        mock.patch("concurrent.futures.wait") as wait_patch,
    ):
        try:
            transfer_manager.upload_chunks_concurrently(
                FILENAME,
                blob,
                chunk_size=SIZE // 2,
                worker_type=transfer_manager.THREAD,
                max_workers=MAX_WORKERS,
                deadline=DEADLINE,
                retry=None,
            )
        except ValueError:
            pass  # The futures don't actually work, so we expect this to abort.
            # Conveniently, that gives us a chance to test the auto-delete
            # exception handling feature.
        container_mock.cancel.assert_called_once_with(transport)

        pool_patch.assert_called_with(max_workers=MAX_WORKERS)
        wait_patch.assert_called_with(mock.ANY, timeout=DEADLINE, return_when=mock.ANY)


def test_upload_chunks_concurrently_with_metadata_and_encryption():
    import datetime

    from google.cloud._helpers import _RFC3339_MICROS

    from google.cloud.storage._helpers import _UTC

    now = datetime.datetime.now(_UTC)
    now_str = now.strftime(_RFC3339_MICROS)

    custom_metadata = {"key_a": "value_a", "key_b": "value_b"}
    encryption_key = "b23ff11bba187db8c37077e6af3b25b8"
    kms_key_name = "sample_key_name"
    custom_headers = {
        "x-goog-custom-audit-foo": "bar",
    }

    METADATA = {
        "cache_control": "private",
        "content_disposition": "inline",
        "content_language": "en-US",
        "custom_time": now,
        "metadata": custom_metadata,
        "storage_class": "NEARLINE",
    }

    bucket = mock.Mock()
    bucket.name = "bucket"
    bucket.client = _PickleableMockClient(
        identify_as_client=True, extra_headers=custom_headers
    )
    transport = bucket.client._http
    user_project = "my_project"
    bucket.user_project = user_project

    blob = Blob("blob", bucket, kms_key_name=kms_key_name)
    blob.content_type = FAKE_CONTENT_TYPE

    for key, value in METADATA.items():
        setattr(blob, key, value)
    blob.metadata = {**custom_metadata}
    blob.encryption_key = encryption_key

    FILENAME = "file_a.txt"
    SIZE = 2048

    container_mock = mock.Mock()
    container_mock.upload_id = "abcd"
    part_mock = mock.Mock()
    ETAG = "efgh"
    part_mock.etag = ETAG
    container_cls_mock = mock.Mock(return_value=container_mock)

    invocation_id = "b9f8cbb0-6456-420c-819d-3f4ee3c0c455"

    with (
        mock.patch("os.path.getsize", return_value=SIZE),
        mock.patch(
            "google.cloud.storage.transfer_manager.XMLMPUContainer",
            new=container_cls_mock,
        ),
        mock.patch(
            "google.cloud.storage.transfer_manager.XMLMPUPart", return_value=part_mock
        ),
        mock.patch(
            "google.cloud.storage._helpers._get_invocation_id",
            return_value="gccl-invocation-id/" + invocation_id,
        ),
    ):
        transfer_manager.upload_chunks_concurrently(
            FILENAME,
            blob,
            chunk_size=SIZE // 2,
            worker_type=transfer_manager.THREAD,
        )
        expected_headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "agent",
            "x-goog-api-client": f"agent gccl-invocation-id/{invocation_id} gccl-gcs-cmd/tm.upload_sharded",
            "content-type": FAKE_CONTENT_TYPE,
            "x-upload-content-type": FAKE_CONTENT_TYPE,
            "X-Goog-Encryption-Algorithm": "AES256",
            "X-Goog-Encryption-Key": "YjIzZmYxMWJiYTE4N2RiOGMzNzA3N2U2YWYzYjI1Yjg=",
            "X-Goog-Encryption-Key-Sha256": "B25Y4hgVlNXDliAklsNz9ykLk7qvgqDrSbdds5iu8r4=",
            "Cache-Control": "private",
            "Content-Disposition": "inline",
            "Content-Language": "en-US",
            "x-goog-storage-class": "NEARLINE",
            "x-goog-custom-time": now_str,
            "x-goog-meta-key_a": "value_a",
            "x-goog-meta-key_b": "value_b",
            "x-goog-user-project": "my_project",
            "x-goog-encryption-kms-key-name": "sample_key_name",
            **custom_headers,
        }
        container_cls_mock.assert_called_once_with(
            URL, FILENAME, headers=expected_headers, retry=DEFAULT_RETRY
        )
        container_mock.initiate.assert_called_once_with(
            transport=transport, content_type=blob.content_type
        )
        container_mock.register_part.assert_any_call(1, ETAG)
        container_mock.register_part.assert_any_call(2, ETAG)
        container_mock.finalize.assert_called_once_with(transport)
        part_mock.upload.assert_called_with(blob.client._http)


class _PickleableMockBlob:
    def __init__(
        self,
        name="",
        size=None,
        generation=None,
        size_after_reload=None,
        generation_after_reload=None,
    ):
        self.name = name
        self.size = size
        self.generation = generation
        self._size_after_reload = size_after_reload
        self._generation_after_reload = generation_after_reload
        self.client = _PickleableMockClient()

    def reload(self):
        self.size = self._size_after_reload
        self.generation = self._generation_after_reload

    def _prep_and_do_download(self, *args, **kwargs):
        return "SUCCESS"


class _PickleableMockConnection:
    @staticmethod
    def get_api_base_url_for_mtls():
        return HOSTNAME

    user_agent = USER_AGENT


class _PickleableMockClient:
    def __init__(self, identify_as_client=False, extra_headers={}):
        self._http = "my_transport"  # used as an identifier for "called_with"
        self._connection = _PickleableMockConnection()
        self.identify_as_client = identify_as_client
        self._extra_headers = extra_headers

    @property
    def __class__(self):
        if self.identify_as_client:
            return Client
        else:
            return _PickleableMockClient


# Used in subprocesses only, so excluded from coverage
def _validate_blob_token_in_subprocess_for_chunk(
    maybe_pickled_blob, filename, **kwargs
):  # pragma: NO COVER
    blob = pickle.loads(maybe_pickled_blob)
    assert isinstance(blob, _PickleableMockBlob)
    assert filename.startswith("file")
    return FAKE_RESULT


def test_download_chunks_concurrently_with_processes():
    blob = _PickleableMockBlob(
        "file_a_blob", size_after_reload=24, generation_after_reload=100
    )
    FILENAME = "file_a.txt"

    with (
        mock.patch(
            "google.cloud.storage.transfer_manager._download_and_write_chunk_in_place",
            new=_validate_blob_token_in_subprocess_for_chunk,
        ),
        mock.patch("google.cloud.storage.transfer_manager.open", mock.mock_open()),
    ):
        result = transfer_manager.download_chunks_concurrently(
            blob,
            FILENAME,
            chunk_size=CHUNK_SIZE,
            download_kwargs=DOWNLOAD_KWARGS,
            worker_type=transfer_manager.PROCESS,
            crc32c_checksum=False,
        )
    assert result is None


def test__LazyClient():
    fake_cache = {}
    MOCK_ID = 9999
    with (
        mock.patch(
            "google.cloud.storage.transfer_manager._cached_clients", new=fake_cache
        ),
        mock.patch("google.cloud.storage.transfer_manager.Client"),
    ):
        lazyclient = transfer_manager._LazyClient(MOCK_ID)
        lazyclient_cached = transfer_manager._LazyClient(MOCK_ID)
        assert lazyclient is lazyclient_cached
        assert len(fake_cache) == 1


def test__pickle_client():
    # This test nominally has coverage, but doesn't assert that the essential
    # copyreg behavior in _pickle_client works. Unfortunately there doesn't seem
    # to be a good way to check that without actually creating a Client, which
    # will spin up HTTP connections undesirably. This is more fully checked in
    # the system tests.
    pkl = transfer_manager._pickle_client(FAKE_RESULT)
    assert pickle.loads(pkl) == FAKE_RESULT


def test__download_and_write_chunk_in_place():
    pickled_mock = pickle.dumps(_PickleableMockBlob())
    FILENAME = "file_a.txt"
    with mock.patch("google.cloud.storage.transfer_manager.open", mock.mock_open()):
        result = transfer_manager._download_and_write_chunk_in_place(
            pickled_mock, FILENAME, 0, 8, {}, False
        )
    assert result is not None


def test__upload_part():
    from google.cloud.storage.retry import DEFAULT_RETRY

    pickled_mock = pickle.dumps(_PickleableMockClient())
    FILENAME = "file_a.txt"
    UPLOAD_ID = "abcd"
    ETAG = "efgh"

    part = mock.Mock()
    part.etag = ETAG
    with mock.patch(
        "google.cloud.storage.transfer_manager.XMLMPUPart", return_value=part
    ):
        result = transfer_manager._upload_part(
            pickled_mock,
            URL,
            UPLOAD_ID,
            FILENAME,
            0,
            256,
            1,
            None,
            {"key", "value"},
            retry=DEFAULT_RETRY,
        )
        part.upload.assert_called_once()

        assert result == (1, ETAG)


def test__get_pool_class_and_requirements_error():
    with pytest.raises(ValueError):
        transfer_manager._get_pool_class_and_requirements("garbage")


def test__reduce_client():
    fake_cache = {}
    client = mock.Mock()
    custom_headers = {
        "x-goog-custom-audit-foo": "bar",
    }
    client._extra_headers = custom_headers
    client._enable_metrics = True
    client._enable_debug_metrics = True

    with (
        mock.patch(
            "google.cloud.storage.transfer_manager._cached_clients", new=fake_cache
        ),
        mock.patch("google.cloud.storage.transfer_manager.Client") as mock_client_cls,
    ):
        replicated_client, args = transfer_manager._reduce_client(client)
        assert replicated_client is not None
        assert custom_headers in args
        assert args[-2:] == (True, True)
        replicated_client(*args)
        mock_client_cls.assert_called_once_with(
            *args[1:6],
            extra_headers=custom_headers,
            enable_metrics=True,
            enable_debug_metrics=True,
        )

        # Verify compatibility when only enable_metrics is present (len(args) == 7 after id)
        fake_cache.clear()
        mock_client_cls.reset_mock()
        replicated_client(*args[:-1])
        mock_client_cls.assert_called_once_with(
            *args[1:6],
            extra_headers=custom_headers,
            enable_metrics=True,
        )

        # Verify compatibility when only extra_headers is present (len(args) == 6 after id)
        fake_cache.clear()
        mock_client_cls.reset_mock()
        replicated_client(*args[:-2])
        mock_client_cls.assert_called_once_with(
            *args[1:6],
            extra_headers=custom_headers,
        )


def test__call_method_on_maybe_pickled_blob():
    blob = mock.Mock(spec=Blob)
    blob._prep_and_do_download.return_value = "SUCCESS"
    result = transfer_manager._call_method_on_maybe_pickled_blob(
        blob, "_prep_and_do_download"
    )
    assert result == "SUCCESS"

    pickled_blob = pickle.dumps(_PickleableMockBlob())
    result = transfer_manager._call_method_on_maybe_pickled_blob(
        pickled_blob, "_prep_and_do_download"
    )
    assert result == "SUCCESS"


def test__ChecksummingSparseFileWrapper():
    FILENAME = "file_a.txt"
    import google_crc32c

    with mock.patch(
        "google.cloud.storage.transfer_manager.open", mock.mock_open()
    ) as open_mock:
        # test no checksumming
        wrapper = transfer_manager._ChecksummingSparseFileWrapper(FILENAME, 0, False)
        wrapper.write(b"abcdefgh")
        handle = open_mock()
        handle.write.assert_called_with(b"abcdefgh")
        wrapper.write(b"ijklmnop")
        assert wrapper.crc is None
        handle.write.assert_called_with(b"ijklmnop")

    with mock.patch(
        "google.cloud.storage.transfer_manager.open", mock.mock_open()
    ) as open_mock:
        wrapper = transfer_manager._ChecksummingSparseFileWrapper(FILENAME, 0, True)
        wrapper.write(b"abcdefgh")
        handle = open_mock()
        handle.write.assert_called_with(b"abcdefgh")
        wrapper.write(b"ijklmnop")
        assert wrapper.crc == google_crc32c.value(b"abcdefghijklmnop")
        handle.write.assert_called_with(b"ijklmnop")
