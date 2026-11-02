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

"""Concurrent media operations. This is a PREVIEW FEATURE: API may change."""

import concurrent.futures
import tempfile

from google.api_core import exceptions

DEFAULT_CHUNK_SIZE = 200 * 1024 * 1024


def upload_many(
    file_blob_pairs,
    skip_if_exists=False,
    upload_kwargs=None,
    max_workers=None,
    deadline=None,
    raise_exception=False,
):
    """Upload many files concurrently via a worker pool.

    This function is a PREVIEW FEATURE: the API may change in a future version.

    :type file_blob_pairs: List(Tuple(IOBase or str, 'google.cloud.storage.blob.Blob'))
    :param file_blob_pairs:
        A list of tuples of a file or filename and a blob. Each file will be
        uploaded to the corresponding blob by using blob.upload_from_file() or
        blob.upload_from_filename() as appropriate.

    :type skip_if_exists: bool
    :param skip_if_exists:
        If True, blobs that already have a live version will not be overwritten.
        This is accomplished by setting "if_generation_match = 0" on uploads.
        Uploads so skipped will result in a 412 Precondition Failed response
        code, which will be included in the return value but not raised
        as an exception regardless of the value of raise_exception.

    :type upload_kwargs: dict
    :param upload_kwargs:
        A dictionary of keyword arguments to pass to the upload method. Refer
        to the documentation for blob.upload_from_file() or
        blob.upload_from_filename() for more information. The dict is directly
        passed into the upload methods and is not validated by this function.

    :type max_workers: int
    :param max_workers:
        The number of workers (effectively, the number of threads) to use in
        the worker pool. Refer to concurrent.futures.ThreadPoolExecutor
        documentation for details.

    :type deadline: int
    :param deadline:
        The number of seconds to wait for all threads to resolve. If the
        deadline is reached, all threads will be terminated regardless of their
        progress and concurrent.futures.TimeoutError will be raised. This can be
        left as the default of None (no deadline) for most use cases.

    :type raise_exception: bool
    :param raise_exception:
        If True, instead of adding exceptions to the list of return values,
        instead they will be raised. Note that encountering an exception on one
        operation will not prevent other operations from starting. Exceptions
        are only processed and potentially raised after all operations are
        complete in success or failure.

        If skip_if_exists is True, 412 Precondition Failed responses are
        considered part of normal operation and are not raised as an exception.

    :raises: :exc:`concurrent.futures.TimeoutError` if deadline is exceeded.

    :rtype: list
    :returns: A list of results corresponding to, in order, each item in the
        input list. If an exception was received, it will be the result
        for that operation. Otherwise, the return value from the successful
        upload method is used (typically, None).
    """
    if upload_kwargs is None:
        upload_kwargs = {}
    if skip_if_exists:
        upload_kwargs["if_generation_match"] = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for path_or_file, blob in file_blob_pairs:
            method = (
                blob.upload_from_filename
                if isinstance(path_or_file, str)
                else blob.upload_from_file
            )
            futures.append(executor.submit(method, path_or_file, **upload_kwargs))
    results = []
    concurrent.futures.wait(
        futures, timeout=deadline, return_when=concurrent.futures.ALL_COMPLETED
    )
    for future in futures:
        exp = future.exception()

        # If raise_exception is False, don't call future.result()
        if exp and not raise_exception:
            results.append(exp)
        # If skip_if_exists and the exception is PreconditionFailed, do same.
        elif exp and skip_if_exists and isinstance(exp, exceptions.PreconditionFailed):
            results.append(exp)
        # Get the real result. If there was an exception not handled above,
        # this will raise it.
        else:
            results.append(future.result())
    return results


def download_many(
    blob_file_pairs,
    download_kwargs=None,
    max_workers=None,
    deadline=None,
    raise_exception=False,
):
    """Download many blobs concurrently via a worker pool.

    This function is a PREVIEW FEATURE: the API may change in a future version.

    :type blob_file_pairs: List(Tuple('google.cloud.storage.blob.Blob', IOBase or str))
    :param blob_file_pairs:
        A list of tuples of blob and a file or filename. Each blob will be
        downloaded to the corresponding blob by using blob.download_to_file() or
        blob.download_to_filename() as appropriate.

        Note that blob.download_to_filename() does not delete the destination
        file if the download fails.

    :type download_kwargs: dict
    :param download_kwargs:
        A dictionary of keyword arguments to pass to the download method. Refer
        to the documentation for blob.download_to_file() or
        blob.download_to_filename() for more information. The dict is directly
        passed into the download methods and is not validated by this function.

    :type max_workers: int
    :param max_workers:
        The number of workers (effectively, the number of threads) to use in
        the worker pool. Refer to concurrent.futures.ThreadPoolExecutor
        documentation for details.

    :type deadline: int
    :param deadline:
        The number of seconds to wait for all threads to resolve. If the
        deadline is reached, all threads will be terminated regardless of their
        progress and concurrent.futures.TimeoutError will be raised. This can be
        left as the default of None (no deadline) for most use cases.

    :type raise_exception: bool
    :param raise_exception:
        If True, instead of adding exceptions to the list of return values,
        instead they will be raised. Note that encountering an exception on one
        operation will not prevent other operations from starting. Exceptions
        are only processed and potentially raised after all operations are
        complete in success or failure.

    :raises: :exc:`concurrent.futures.TimeoutError` if deadline is exceeded.

    :rtype: list
    :returns: A list of results corresponding to, in order, each item in the
        input list. If an exception was received, it will be the result
        for that operation. Otherwise, the return value from the successful
        download method is used (typically, None).
    """

    if download_kwargs is None:
        download_kwargs = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for blob, path_or_file in blob_file_pairs:
            method = (
                blob.download_to_filename
                if isinstance(path_or_file, str)
                else blob.download_to_file
            )
            futures.append(executor.submit(method, path_or_file, **download_kwargs))
    results = []
    concurrent.futures.wait(
        futures, timeout=deadline, return_when=concurrent.futures.ALL_COMPLETED
    )
    for future in futures:
        if not raise_exception:
            exp = future.exception()
            if exp:
                results.append(exp)
                continue
        results.append(future.result())
    return results


def download_chunks_concurrently_to_file(
    blob,
    file_obj,
    chunk_size=DEFAULT_CHUNK_SIZE,
    download_kwargs=None,
    max_workers=None,
    deadline=None,
):
    """Download a single blob in chunks, concurrently.

    This function is a PREVIEW FEATURE: the API may change in a future version.

    Use of this function, in cases where single threads are unable to fully
    saturate available network bandwidth, may improve download performance for
    large objects.

    The size of the blob must be known in order to calculate the number of
    chunks. If the size is not already set, blob.reload() will be called
    automatically to set it.

    :type blob: 'google.cloud.storage.blob.Blob'
    :param blob:
        The blob to download.

    :type file_obj: IOBase
    :param file_obj: The file object to which the downloaded chunks will be
        written. Chunks are written in order. While the current implementation
        of this function does not use seek(), a future version may use seek() to
        write chunks out of order to improve write performance.

    :type chunk_size: int
    :param chunk_size: The size of each chunk. An excessively small size may
        have a negative performance impact, as each chunk will be uploaded in a
        separate HTTP request.

    :type download_kwargs: dict
    :param download_kwargs:
        A dictionary of keyword arguments to pass to the download method. Refer
        to the documentation for blob.download_to_file() or
        blob.download_to_filename() for more information. The dict is directly
        passed into the download methods and is not validated by this function.

    :type max_workers: int
    :param max_workers:
        The number of workers (effectively, the number of threads) to use in
        the worker pool. Refer to concurrent.futures.ThreadPoolExecutor
        documentation for details.

    :type deadline: int
    :param deadline:
        The number of seconds to wait for all threads to resolve. If the
        deadline is reached, all threads will be terminated regardless of their
        progress and concurrent.futures.TimeoutError will be raised. This can be
        left as the default of None (no deadline) for most use cases.

    :raises: :exc:`concurrent.futures.TimeoutError` if deadline is exceeded.
    """

    if download_kwargs is None:
        download_kwargs = {}
    # We must know the size of the object, and the generation.
    if not blob.size or not blob.generation:
        blob.reload()

    def download_range_via_tempfile(blob, start, end, download_kwargs):
        tmp = tempfile.TemporaryFile()
        blob.download_to_file(tmp, start=start, end=end, **download_kwargs)
        return tmp

    futures = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        cursor = 0
        while cursor < blob.size:
            start = cursor
            cursor = min(cursor + chunk_size, blob.size)
            futures.append(
                executor.submit(
                    download_range_via_tempfile,
                    blob,
                    start=start,
                    end=cursor - 1,
                    download_kwargs=download_kwargs,
                )
            )

    # Wait until all futures are done and process them in order.
    concurrent.futures.wait(
        futures, timeout=deadline, return_when=concurrent.futures.ALL_COMPLETED
    )
    for future in futures:
        tmp = future.result()
        tmp.seek(0)
        file_obj.write(tmp.read())
        tmp.close()


def upload_many_from_filenames(
    bucket,
    filenames,
    root="",
    blob_name_prefix="",
    skip_if_exists=False,
    blob_constructor_kwargs=None,
    upload_kwargs=None,
    max_workers=None,
    deadline=None,
    raise_exception=False,
):
    """Upload many files concurrently by their filenames.

    This function is a PREVIEW FEATURE: the API may change in a future version.

    The destination blobs are automatically created, with blob names based on
    the source filenames and the blob_name_prefix.

    For example, if the `filenames` include "images/icon.jpg", `root` is
    "/home/myuser/", and `blob_name_prefix` is "myfiles/", then the file at
    "/home/myuser/images/icon.jpg" will be uploaded to a blob named
    "myfiles/images/icon.jpg".

    :type bucket: 'google.cloud.storage.bucket.Bucket'
    :param bucket:
        The bucket which will contain the uploaded blobs.

    :type filenames: list(str)
    :param filenames:
        A list of filenames to be uploaded. This may include part of the path.
        The full path to the file must be root + filename. The filename is
        separate from the root because the filename will also determine the
        name of the destination blob.

    :type root: str
    :param root:
        A string that will be prepended to each filename in the input list, in
        order to find the source file for each blob. Unlike the filename itself,
        the root string does not affect the name of the uploaded blob itself.
        The root string will usually end in "/" (or "\\" depending on platform)
        but is not required to do so.

        For instance, if the root string is "/tmp/img-" and a filename is
        "0001.jpg", with an empty blob_name_prefix, then the file uploaded will
        be "/tmp/img-0001.jpg" and the destination blob will be "0001.jpg".

        This parameter can be an empty string.

    :type blob_name_prefix: str
    :param blob_name_prefix:
        A string that will be prepended to each filename in the input list, in
        order to determine the name of the destination blob. Unlike the filename
        itself, the prefix string does not affect the location the library will
        look for the source data on the local filesystem.

        For instance, if the root is "/tmp/img-", the blob_name_prefix is
        "myuser/mystuff-" and a filename is "0001.jpg" then the file uploaded
        will be "/tmp/img-0001.jpg" and the destination blob will be
        "myuser/mystuff-0001.jpg".

        The blob_name_prefix can be blank (an empty string).

    :type skip_if_exists: bool
    :param skip_if_exists:
        If True, blobs that already have a live version will not be overwritten.
        This is accomplished by setting "if_generation_match = 0" on uploads.
        Uploads so skipped will result in a 412 Precondition Failed response
        code, which will be included in the return value but not raised
        as an exception regardless of the value of raise_exception.

    :type blob_constructor_kwargs: dict
    :param blob_constructor_kwargs:
        A dictionary of keyword arguments to pass to the blob constructor. Refer
        to the documentation for blob.Blob() for more information. The dict is
        directly passed into the constructor and is not validated by this
        function. `name` and `bucket` keyword arguments are reserved by this
        function and will result in an error if passed in here.

    :type upload_kwargs: dict
    :param upload_kwargs:
        A dictionary of keyword arguments to pass to the upload method. Refer
        to the documentation for blob.upload_from_file() or
        blob.upload_from_filename() for more information. The dict is directly
        passed into the upload methods and is not validated by this function.

    :type max_workers: int
    :param max_workers:
        The number of workers (effectively, the number of threads) to use in
        the worker pool. Refer to concurrent.futures.ThreadPoolExecutor
        documentation for details.

    :type deadline: int
    :param deadline:
        The number of seconds to wait for all threads to resolve. If the
        deadline is reached, all threads will be terminated regardless of their
        progress and concurrent.futures.TimeoutError will be raised. This can be
        left as the default of None (no deadline) for most use cases.

    :type raise_exception: bool
    :param raise_exception:
        If True, instead of adding exceptions to the list of return values,
        instead they will be raised. Note that encountering an exception on one
        operation will not prevent other operations from starting. Exceptions
        are only processed and potentially raised after all operations are
        complete in success or failure.

        If skip_if_exists is True, 412 Precondition Failed responses are
        considered part of normal operation and are not raised as an exception.

    :raises: :exc:`concurrent.futures.TimeoutError` if deadline is exceeded.

    :rtype: list
    :returns: A list of results corresponding to, in order, each item in the
        input list. If an exception was received, it will be the result
        for that operation. Otherwise, the return value from the successful
        upload method is used (typically, None).
    """
    if blob_constructor_kwargs is None:
        blob_constructor_kwargs = {}

    file_blob_pairs = []

    for filename in filenames:
        path = root + filename
        blob_name = blob_name_prefix + filename
        blob = bucket.blob(blob_name, **blob_constructor_kwargs)
        file_blob_pairs.append((path, blob))

    return upload_many(
        file_blob_pairs,
        skip_if_exists=skip_if_exists,
        upload_kwargs=upload_kwargs,
        max_workers=max_workers,
        deadline=deadline,
        raise_exception=raise_exception,
    )


def download_many_to_path(
    bucket,
    blob_names,
    path_root="",
    blob_name_prefix="",
    download_kwargs=None,
    max_workers=None,
    deadline=None,
    raise_exception=False,
):
    """Download many files concurrently by their blob names.

    This function is a PREVIEW FEATURE: the API may change in a future version.

    The destination files are automatically created, with filenames based on
    the source blob_names and the path_root.

    The destination files are not automatically deleted if their downloads fail,
    so please check the return value of this function for any exceptions, or
    enable `raise_exception=True`, and process the files accordingly.

    For example, if the `blob_names` include "icon.jpg", `path_root` is
    "/home/myuser/", and `blob_name_prefix` is "images/", then the blob named
    "images/icon.jpg" will be downloaded to a file named
    "/home/myuser/icon.jpg".

    :type bucket: 'google.cloud.storage.bucket.Bucket'
    :param bucket:
        The bucket which contains the blobs to be downloaded

    :type blob_names: list(str)
    :param blob_names:
        A list of blobs to be downloaded. The blob name in this string will be
        used to determine the destination file path as well.

        The full name to the blob must be blob_name_prefix + blob_name. The
        blob_name is separate from the blob_name_prefix because the blob_name
        will also determine the name of the destination blob. Any shared part of
        the blob names that need not be part of the destination path should be
        included in the blob_name_prefix.

    :type path_root: str
    :param path_root:
        A string that will be prepended to each blob_name in the input list,
        in order to determine the destination path for that blob. The path_root
        string will usually end in "/" (or "\\" depending on platform) but is
        not required to do so. For instance, if the path_root string is
        "/tmp/img-" and a blob_name is "0001.jpg", with an empty
        blob_name_prefix, then the source blob "0001.jpg" will be downloaded to
        destination "/tmp/img-0001.jpg" . This parameter can be an empty string.

    :type blob_name_prefix: str
    :param blob_name_prefix:
        A string that will be prepended to each blob_name in the input list, in
        order to determine the name of the source blob. Unlike the blob_name
        itself, the prefix string does not affect the destination path on the
        local filesystem. For instance, if the path_root is "/tmp/img-", the
        blob_name_prefix is "myuser/mystuff-" and a blob_name is "0001.jpg" then
        the source blob "myuser/mystuff-0001.jpg" will be downloaded to
        "/tmp/img-0001.jpg". The blob_name_prefix can be blank (an empty
        string).

    :type download_kwargs: dict
    :param download_kwargs:
        A dictionary of keyword arguments to pass to the download method. Refer
        to the documentation for blob.download_to_file() or
        blob.download_to_filename() for more information. The dict is directly
        passed into the download methods and is not validated by this function.

    :type max_workers: int
    :param max_workers:
        The number of workers (effectively, the number of threads) to use in
        the worker pool. Refer to concurrent.futures.ThreadPoolExecutor
        documentation for details.

    :type deadline: int
    :param deadline:
        The number of seconds to wait for all threads to resolve. If the
        deadline is reached, all threads will be terminated regardless of their
        progress and concurrent.futures.TimeoutError will be raised. This can be
        left as the default of None (no deadline) for most use cases.

    :type raise_exception: bool
    :param raise_exception:
        If True, instead of adding exceptions to the list of return values,
        instead they will be raised. Note that encountering an exception on one
        operation will not prevent other operations from starting. Exceptions
        are only processed and potentially raised after all operations are
        complete in success or failure. If skip_if_exists is True, 412
        Precondition Failed responses are considered part of normal operation
        and are not raised as an exception.

    :raises: :exc:`concurrent.futures.TimeoutError` if deadline is exceeded.

    :rtype: list
    :returns: A list of results corresponding to, in order, each item in the
        input list. If an exception was received, it will be the result
        for that operation. Otherwise, the return value from the successful
        download method is used (typically, None).
    """
    blob_file_pairs = []

    for blob_name in blob_names:
        full_blob_name = blob_name_prefix + blob_name
        path = path_root + blob_name
        blob_file_pairs.append((bucket.blob(full_blob_name), path))

    return download_many(
        blob_file_pairs,
        download_kwargs=download_kwargs,
        max_workers=max_workers,
        deadline=deadline,
        raise_exception=raise_exception,
    )
