# Copyright 2016 Google LLC
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

"""Testable usage examples for Google Cloud Storage API wrapper

Each example function takes a ``client`` argument (which must be an instance
of :class:`google.cloud.storage.client.Client`) and uses it to perform a task
with the API.

To facilitate running the examples as system tests, each example is also passed
a ``to_delete`` list;  the function adds to the list any objects created which
need to be deleted during teardown.
"""

from google.cloud import storage


def snippet(func):
    """Mark ``func`` as a snippet example function."""
    func._snippet = True
    return func


@snippet
def storage_get_started(to_delete):
    # START storage_get_started
    client = storage.Client()
    bucket = client.get_bucket("bucket-id-here")
    # Then do other things...
    blob = bucket.get_blob("/remote/path/to/file.txt")
    assert blob.download_as_string() == b"My old contents!"
    blob.upload_from_string("New contents!")
    blob2 = bucket.blob("/remote/path/storage.txt")
    blob2.upload_from_filename(filename="/local/path.txt")
    # END storage_get_started

    to_delete.append(bucket)


@snippet
def client_bucket_acl(client, to_delete):
    bucket_name = "system-test-bucket"
    client.create_bucket(bucket_name)

    # START client_bucket_acl
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    acl = bucket.acl
    # END client_bucket_acl
    to_delete.append(bucket)

    # START acl_user_settings
    acl.user("me@example.org").grant_read()
    acl.all_authenticated().grant_write()
    # END acl_user_settings

    # START acl_save
    acl.save()
    # END acl_save

    # START acl_revoke_write
    acl.all().grant_read()
    acl.all().revoke_write()
    # END acl_revoke_write

    # START acl_save_bucket
    bucket.acl.save(acl=acl)
    # END acl_save_bucket

    # START acl_print
    print(list(acl))
    # [{'role': 'OWNER', 'entity': 'allUsers'}, ...]
    # END acl_print


@snippet
def download_to_file(to_delete):
    # START download_to_file
    from google.cloud.storage import Blob

    client = storage.Client(project="my-project")
    bucket = client.get_bucket("my-bucket")
    encryption_key = "c7f32af42e45e85b9848a6a14dd2a8f6"
    blob = Blob("secure-data", bucket, encryption_key=encryption_key)
    blob.upload_from_string("my secret message.")
    with open("/tmp/my-secure-file", "wb") as file_obj:
        client.download_to_file(blob, file_obj)
    # END download_to_file

    to_delete.append(blob)


@snippet
def upload_from_file(to_delete):
    # START upload_from_file
    from google.cloud.storage import Blob

    client = storage.Client(project="my-project")
    bucket = client.get_bucket("my-bucket")
    encryption_key = "aa426195405adee2c8081bb9e7e74b19"
    blob = Blob("secure-data", bucket, encryption_key=encryption_key)
    with open("my-file", "rb") as my_file:
        blob.upload_from_file(my_file)
    # END upload_from_file

    to_delete.append(blob)


@snippet
def get_blob(to_delete):
    from google.cloud.storage.blob import Blob

    # START get_blob
    client = storage.Client()
    bucket = client.get_bucket("my-bucket")
    assert isinstance(bucket.get_blob("/path/to/blob.txt"), Blob)
    # <Blob: my-bucket, /path/to/blob.txt>
    assert not bucket.get_blob("/does-not-exist.txt")
    # None
    # END get_blob

    to_delete.append(bucket)


@snippet
def delete_blob(to_delete):
    # START delete_blob
    from google.cloud.exceptions import NotFound

    client = storage.Client()
    bucket = client.get_bucket("my-bucket")
    blobs = list(client.list_blobs(bucket))
    assert len(blobs) > 0
    # [<Blob: my-bucket, my-file.txt>]
    bucket.delete_blob("my-file.txt")
    try:
        bucket.delete_blob("doesnt-exist")
    except NotFound:
        pass
    # END delete_blob

    blob = None
    # START delete_blobs
    bucket.delete_blobs([blob], on_error=lambda blob: None)
    # END delete_blobs

    to_delete.append(bucket)


@snippet
def configure_website(to_delete):
    bucket_name = "test-bucket"
    # START configure_website
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    bucket.configure_website("index.html", "404.html")
    # END configure_website

    # START make_public
    bucket.make_public(recursive=True, future=True)
    # END make_public

    to_delete.append(bucket)


@snippet
def get_bucket(client, to_delete):
    import google

    # START get_bucket
    try:
        bucket = client.get_bucket("my-bucket")
    except google.cloud.exceptions.NotFound:
        print("Sorry, that bucket does not exist!")
    # END get_bucket
    to_delete.append(bucket)


@snippet
def add_lifecycle_delete_rule(client, to_delete):
    # START add_lifecycle_delete_rule
    bucket = client.get_bucket("my-bucket")
    bucket.add_lifecycle_delete_rule(age=2)
    bucket.patch()
    # END add_lifecycle_delete_rule
    to_delete.append(bucket)


@snippet
def add_lifecycle_set_storage_class_rule(client, to_delete):
    # START add_lifecycle_set_storage_class_rule
    bucket = client.get_bucket("my-bucket")
    bucket.add_lifecycle_set_storage_class_rule(
        "COLD_LINE", matches_storage_class=["NEARLINE"]
    )
    bucket.patch()
    # END add_lifecycle_set_storage_class_rule
    to_delete.append(bucket)


@snippet
def lookup_bucket(client, to_delete):
    from google.cloud.storage.bucket import Bucket

    # START lookup_bucket
    bucket = client.lookup_bucket("doesnt-exist")
    assert not bucket
    # None
    bucket = client.lookup_bucket("my-bucket")
    assert isinstance(bucket, Bucket)
    # <Bucket: my-bucket>
    # END lookup_bucket

    to_delete.append(bucket)


@snippet
def create_bucket(client, to_delete):
    from google.cloud.storage import Bucket

    # START create_bucket
    bucket = client.create_bucket("my-bucket")
    assert isinstance(bucket, Bucket)
    # <Bucket: my-bucket>
    # END create_bucket

    to_delete.append(bucket)


@snippet
def list_buckets(client, to_delete):
    # START list_buckets
    for bucket in client.list_buckets():
        print(bucket)
    # END list_buckets

    for bucket in client.list_buckets():
        to_delete.append(bucket)


@snippet
def policy_document(client):
    # pylint: disable=unused-argument
    # START policy_document
    bucket = client.bucket("my-bucket")
    conditions = [["starts-with", "$key", ""], {"acl": "public-read"}]

    policy = bucket.generate_upload_policy(conditions)

    # Generate an upload form using the form fields.
    policy_fields = "".join(
        f'<input type="hidden" name="{key}" value="{value}">'
        for key, value in policy.items()
    )

    upload_form = (
        '<form action="http://{bucket_name}.storage.googleapis.com"'
        '   method="post" enctype="multipart/form-data">'
        '<input type="text" name="key" value="my-test-key">'
        '<input type="hidden" name="bucket" value="{bucket_name}">'
        '<input type="hidden" name="acl" value="public-read">'
        '<input name="file" type="file">'
        '<input type="submit" value="Upload">'
        "{policy_fields}"
        "</form>"
    ).format(bucket_name=bucket.name, policy_fields=policy_fields)

    print(upload_form)
    # END policy_document


def _line_no(func):
    code = getattr(func, "__code__", None) or getattr(func, "func_code")
    return code.co_firstlineno


def _find_examples():
    funcs = [obj for obj in globals().values() if getattr(obj, "_snippet", False)]
    for func in sorted(funcs, key=_line_no):
        yield func


def _name_and_doc(func):
    return func.__name__, func.__doc__


def main():
    client = storage.Client()
    for example in _find_examples():
        to_delete = []
        name, doc = _name_and_doc(example)
        print(f"{name:>25}: {doc}")

        try:
            example(client, to_delete)
        except AssertionError as failure:
            print(f"   FAIL: {failure}")
        except Exception as error:  # pylint: disable=broad-except
            print(f"  ERROR: {error!r}")
        for item in to_delete:
            item.delete()


if __name__ == "__main__":
    main()
