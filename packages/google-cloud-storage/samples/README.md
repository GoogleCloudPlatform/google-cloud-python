
<img src="https://avatars2.githubusercontent.com/u/2810941?v=3&s=96" alt="Google Cloud Platform logo" title="Google Cloud Platform" align="right" height="96" width="96"/>

# Google Cloud Storage Python Samples

[![Open in Cloud Shell][shell_img]][shell_link]


This directory contains samples for Google Cloud Storage.
[Cloud Storage](https://cloud.google.com/storage/docs) allows world-wide
storage and retrieval of any amount of data at any time. You can use Google
Cloud Storage for a range of scenarios including serving website content,
storing data for archival and disaster recovery, or distributing large data
objects to users via direct download.

## Setup

### Before you begin

Before running the samples, make sure you've followed the steps outlined in
[Quick Start](https://github.com/googleapis/python-storage#quick-start).

### Authentication
Refer to the [Authentication Set Up Guide](https://cloud.google.com/storage/docs/reference/libraries#setting_up_authentication)
for more detailed instructions.

### Install Dependencies
1. Clone this repository and change to the sample directory you want to use.
    ```
    git clone https://github.com/googleapis/python-storage.git
    ```

2. Activate a venv if you have not already from the [Quick Start](https://github.com/googleapis/python-storage#quick-start).
    ```
    source <your-venv>/bin/activate
    ```
3. To run samples for [Rapid Buckets](https://github.com/googleapis/python-storage/tree/main/samples/snippets/zonal_buckets)

    ```
    pip install "google-cloud-storage[grpc]"
    python samples/snippets/zonal_buckets/storage_create_and_write_appendable_object.py --bucket_name <BUCKET_NAME> --object_name <OBJECT_NAME>

    ```

4. Install the dependencies needed to run the samples.
    ```
    cd samples/snippets
    pip install -r requirements.txt
    ```


## Running tests locally

Before running the tests, make sure you've followed the steps outlined in
[Setup](#setup).

### Install nox

We use [nox](https://nox.readthedocs.io/en/latest/) to instrument our tests.

```
pip install nox
```

### Set environment variables

You can run tests locally using your own gcs project or with a valid service account in project `python-docs-samples-tests`. This outlines the workflow of running tests locally using your own gcs project.

Refer to [`noxfile_config.py`](https://github.com/googleapis/python-storage/blob/main/samples/snippets/noxfile_config.py) and [a list of environment variables](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/testing/test-env.tmpl.sh) that can be set manually. Not every test needs all of these variables.
Below outlines some common environment variables used in the storage samples.
See [Other Resources](#other-resources) on how to create credentials, keys, and secrets.

    export GOOGLE_CLOUD_PROJECT=[your-project-name]
    export MAIN_GOOGLE_CLOUD_PROJECT=[your-project-name]
    export BUILD_SPECIFIC_GCLOUD_PROJECT=[your-project-name]
    export HMAC_KEY_TEST_SERVICE_ACCOUNT=[your-service-account]
    export CLOUD_KMS_KEY=[your-kms-key]
    export GOOGLE_APPLICATION_CREDENTIALS=[your-credentials]

If you are running a single test locally that does not use the environment variables, you can delete the `noxfile_config.py` file and simply set your `GOOGLE_CLOUD_PROJECT`

```
export GOOGLE_CLOUD_PROJECT=[your-project-name]
```


### Run tests with nox
```
nox -s lint
nox -s py-3.9 -- snippets_test.py
nox -s py-3.9 -- snippets_test.py::test_list_blobs
```

### Special test configurations
There are restrictions on the testing projects used in Kokoro. For instance,
we change the service account based on different test sessions to avoid
hitting the maximum limit of HMAC keys on a single service account.
Another example is `requester_pays_test.py` needs to use a different Storage bucket, and looks for an environment variable `REQUESTER_PAYS_TEST_BUCKET`.
Please refer to [`noxfile_config.py`](https://github.com/googleapis/python-storage/blob/main/samples/snippets/noxfile_config.py) , [kokoro configs](https://github.com/googleapis/python-storage/tree/main/.kokoro/samples), and test files to see if there are special test configurations required.


## Other Resources
* [Create Cloud KMS Keys](https://cloud.google.com/kms/docs/creating-keys)
* [Create HMAC Keys](https://cloud.google.com/storage/docs/authentication/managing-hmackeys)
* [Create Service Accounts](https://cloud.google.com/docs/authentication/getting-started#creating_a_service_account)

[shell_img]: https://gstatic.com/cloudssh/images/open-btn.png
[shell_link]: https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/README.md
[product-docs]: https://cloud.google.com/storage


-----

## Samples
<details>
    <summary><b>List of Samples</b></summary>

* [Activate HMAC Key](#activate-hmac-key)
* [Batch Request](#batch-request)
* [Add Bucket Conditional IAM Binding](#add-bucket-conditional-iam-binding)
* [Add Bucket Default Owner](#add-bucket-default-owner)
* [Add Bucket IAM Member](#add-bucket-iam-member)
* [Add Bucket Label](#add-bucket-label)
* [Add Bucket Owner](#add-bucket-owner)
* [Add File Owner](#add-file-owner)
* [Bucket Delete Default KMS Key](#bucket-delete-default-kms-key)
* [Change Default Storage Class](#change-default-storage-class)
* [Change File Storage Class](#change-file-storage-class)
* [Compose File](#compose-file)
* [Configure Retries](#configure-retries)
* [Copy File](#copy-file)
* [Copy File Archived Generation](#copy-file-archived-generation)
* [CORS Configuration](#cors-configuration)
* [Create Bucket](#create-bucket)
* [Create Bucket Class Location](#create-bucket-class-location)
* [Create Bucket Dual Region](#create-bucket-dual-region)
* [Create Bucket Notifications](#create-bucket-notifications)
* [Create Bucket Turbo Replication](#create-bucket-turbo-replication)
* [Create HMAC Key](#create-hmac-key)
* [Deactivate HMAC Key](#deactivate-hmac-key)
* [Define Bucket Website Configuration](#define-bucket-website-configuration)
* [Delete Bucket](#delete-bucket)
* [Delete Bucket Notification](#delete-bucket-notification)
* [Delete File](#delete-file)
* [Delete File Archived Generation](#delete-file-archived-generation)
* [Delete HMAC Key](#delete-hmac-key)
* [Disable Bucket Lifecycle Management](#disable-bucket-lifecycle-management)
* [Disable Default Event Based Hold](#disable-default-event-based-hold)
* [Disable Requester Pays](#disable-requester-pays)
* [Disable Uniform Bucket Level Access](#disable-uniform-bucket-level-access)
* [Disable Versioning](#disable-versioning)
* [Download Byte Range](#download-byte-range)
* [Download Encrypted File](#download-encrypted-file)
* [Download File](#download-file)
* [Download File Requester Pays](#download-file-requester-pays)
* [Download Into Memory](#download-into-memory)
* [Download Public File](#download-public-file)
* [Enable Bucket Lifecycle Management](#enable-bucket-lifecycle-management)
* [Enable Default Event Based Hold](#enable-default-event-based-hold)
* [Enable Requester Pays](#enable-requester-pays)
* [Enable Uniform Bucket Level Access](#enable-uniform-bucket-level-access)
* [Enable Versioning](#enable-versioning)
* [FileIO Write-Read](#fileio-write-read)
* [FileIO Pandas](#fileio-pandas)
* [Generate Encryption Key](#generate-encryption-key)
* [Generate Signed Post Policy V4](#generate-signed-post-policy-v4)
* [Generate Signed Url V2](#generate-signed-url-v2)
* [Generate Signed Url V4](#generate-signed-url-v4)
* [Generate Upload Signed Url V4](#generate-upload-signed-url-v4)
* [Get Bucket Labels](#get-bucket-labels)
* [Get Bucket Metadata](#get-bucket-metadata)
* [Get Default Event Based Hold](#get-default-event-based-hold)
* [Get HMAC Key](#get-hmac-key)
* [Get Metadata](#get-metadata)
* [Get Public Access Prevention](#get-public-access-prevention)
* [Get Requester Pays Status](#get-requester-pays-status)
* [Get Retention Policy](#get-retention-policy)
* [Get RPO](#get-rpo)
* [Get Service Account](#get-service-account)
* [Get Uniform Bucket Level Access](#get-uniform-bucket-level-access)
* [List Buckets](#list-buckets)
* [List Bucket Notifications](#list-bucket-notifications)
* [List File Archived Generations](#list-file-archived-generations)
* [List Files](#list-files)
* [List Files With Prefix](#list-files-with-prefix)
* [List HMAC Keys](#list-hmac-keys)
* [Lock Retention Policy](#lock-retention-policy)
* [Make Public](#make-public)
* [Move File](#move-file)
* [Object CSEK To CMEK](#object-csek-to-cmek)
* [Object Get KMS Key](#object-get-kms-key)
* [Print Bucket ACL](#print-bucket-acl)
* [Print Bucket ACL For User](#print-bucket-acl-for-user)
* [Print File ACL](#print-file-acl)
* [Print File ACL For User](#print-file-acl-for-user)
* [Print PubSub Bucket Notification](#print-pubsub-bucket-notification)
* [Release Event Based Hold](#release-event-based-hold)
* [Release Temporary Hold](#release-temporary-hold)
* [Remove Bucket Conditional IAM Binding](#remove-bucket-conditional-iam-binding)
* [Remove Bucket Default Owner](#remove-bucket-default-owner)
* [Remove Bucket IAM Member](#remove-bucket-iam-member)
* [Remove Bucket Label](#remove-bucket-label)
* [Remove Bucket Owner](#remove-bucket-owner)
* [Remove Cors Configuration](#remove-cors-configuration)
* [Remove File Owner](#remove-file-owner)
* [Remove Retention Policy](#remove-retention-policy)
* [Rename File](#rename-file)
* [Rotate Encryption Key](#rotate-encryption-key)
* [Set Bucket Default KMS Key](#set-bucket-default-kms-key)
* [Set Bucket Public IAM](#set-bucket-public-iam)
* [Set Event Based Hold](#set-event-based-hold)
* [Set Metadata](#set-metadata)
* [Set Public Access Prevention Enforced](#set-public-access-prevention-enforced)
* [Set Public Access Prevention Inherited](#set-public-access-prevention-inherited)
* [Set RPO Async Turbo](#set-rpo-async-turbo)
* [Set RPO Default](#set-rpo-default)
* [Set Retention Policy](#set-retention-policy)
* [Set Temporary Hold](#set-temporary-hold)
* [Upload Encrypted File](#upload-encrypted-file)
* [Upload File](#upload-file)
* [Upload From Memory](#upload-from-memory)
* [Upload With KMS Key](#upload-with-kms-key)
* [View Bucket IAM Members](#view-bucket-iam-members)

</details>

-----
### Activate HMAC Key
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_activate_hmac_key.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_activate_hmac_key.py). To run this sample:


`python storage_activate_hmac_key.py <ACCESS_ID> <PROJECT_ID>`

-----
### Batch Request
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_batch_request.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_batch_request.py). To run this sample:


`python storage_batch_request.py <BUCKET_NAME> <PREFIX>`

-----

### Add Bucket Conditional IAM Binding
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_add_bucket_conditional_iam_binding.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_add_bucket_conditional_iam_binding.py). To run this sample:


`python storage_add_bucket_conditional_iam_binding.py <BUCKET_NAME> <ROLE> <TITLE> <DESCRIPTION> <EXPRESSION> <MEMBERS>`

-----
### Add Bucket Default Owner
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_add_bucket_default_owner.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_add_bucket_default_owner.py). To run this sample:


`python storage_add_bucket_default_owner.py <BUCKET_NAME> <USER_EMAIL>`

-----
### Add Bucket IAM Member
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_add_bucket_iam_member.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_add_bucket_iam_member.py). To run this sample:


`python storage_add_bucket_iam_member.py <BUCKET_NAME> <ROLE> <MEMBER>`

-----
### Add Bucket Label
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_add_bucket_label.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_add_bucket_label.py). To run this sample:


`python storage_add_bucket_label.py <BUCKET_NAME>`

-----
### Add Bucket Owner
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_add_bucket_owner.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_add_bucket_owner.py). To run this sample:


`python storage_add_bucket_owner.py <BUCKET_NAME> <USER_EMAIL>`

-----
### Add File Owner
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_add_file_owner.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_add_file_owner.py). To run this sample:


`python storage_add_file_owner.py <BUCKET_NAME> <BLOB_NAME> <USER_EMAIL>`

-----
### Bucket Delete Default KMS Key
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_bucket_delete_default_kms_key.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_bucket_delete_default_kms_key.py). To run this sample:


`python storage_bucket_delete_default_kms_key.py <BUCKET_NAME>`

-----
### Change Default Storage Class
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_change_default_storage_class.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_change_default_storage_class.py). To run this sample:


`python storage_change_default_storage_class.py <BUCKET_NAME>`

-----
### Change File Storage Class
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_change_file_storage_class.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_change_file_storage_class.py). To run this sample:


`python storage_change_file_storage_class.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Compose File
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_compose_file.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_compose_file.py). To run this sample:


`python storage_compose_file.py <BUCKET_NAME> <FIRST_BLOB_NAME> <SECOND_BLOB_NAME> <DESTINATION_BLOB_NAME>`

-----
### Configure Retries
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_configure_retries.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_configure_retries.py). To run this sample:


`python storage_configure_retries.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Copy File
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_copy_file.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_copy_file.py). To run this sample:


`python storage_copy_file.py <BUCKET_NAME> <BLOB_NAME> <DESTINATION_BUCKET_NAME> <DESTINATION_BLOB_NAME>`

-----
### Copy File Archived Generation
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_copy_file_archived_generation.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_copy_file_archived_generation.py). To run this sample:


`python storage_copy_file_archived_generation.py <BUCKET_NAME> <BLOB_NAME> <DESTINATION_BUCKET_NAME> <DESTINATION_BLOB_NAME> <GENERATION>`

-----
### CORS Configuration
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_cors_configuration.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_cors_configuration.py). To run this sample:


`python storage_cors_configuration.py <BUCKET_NAME>`

-----
### Create Bucket
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_create_bucket.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_create_bucket.py). To run this sample:


`python storage_create_bucket.py <BUCKET_NAME>`

-----
### Create Bucket Class Location
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_create_bucket_class_location.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_create_bucket_class_location.py). To run this sample:


`python storage_create_bucket_class_location.py <BUCKET_NAME>`

-----
### Create Bucket Dual Region
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_create_bucket_dual_region.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_create_bucket_dual_region.py). To run this sample:


`python storage_create_bucket_dual_region.py <BUCKET_NAME> <LOCATION> <REGION_1> <REGION_2>`

-----
### Create Bucket Notifications
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_create_bucket_notifications.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_create_bucket_notifications.py). To run this sample:


`python storage_create_bucket_notifications.py <BUCKET_NAME> <TOPIC_NAME>`

-----
### Create Bucket Turbo Replication
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_create_bucket_turbo_replication.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_create_bucket_turbo_replication.py). To run this sample:


`python storage_create_bucket_turbo_replication.py <BUCKET_NAME>`

-----
### Create HMAC Key
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_create_hmac_key.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_create_hmac_key.py). To run this sample:


`python storage_create_hmac_key.py <PROJECT_ID> <SERVICE_ACCOUNT_EMAIL>`

-----
### Deactivate HMAC Key
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_deactivate_hmac_key.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_deactivate_hmac_key.py). To run this sample:


`python storage_deactivate_hmac_key.py <ACCESS_ID> <PROJECT_ID>`

-----
### Define Bucket Website Configuration
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_define_bucket_website_configuration.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_define_bucket_website_configuration.py). To run this sample:


`python storage_define_bucket_website_configuration.py <BUCKET_NAME> <MAIN_PAGE_SUFFIX> <NOT_FOUND_PAGE>`

-----
### Delete Bucket
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_delete_bucket.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_delete_bucket.py). To run this sample:


`python storage_delete_bucket.py <BUCKET_NAME>`

-----
### Delete Bucket Notification
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_delete_bucket_notification.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_delete_bucket_notification.py). To run this sample:


`python storage_delete_bucket_notification.py <BUCKET_NAME> <NOTIFICATION_ID>`

-----
### Delete File
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_delete_file.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_delete_file.py). To run this sample:


`python storage_delete_file.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Delete File Archived Generation
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_delete_file_archived_generation.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_delete_file_archived_generation.py). To run this sample:


`python storage_delete_file_archived_generation.py <BUCKET_NAME> <BLOB_NAME> <GENERATION>`

-----
### Delete HMAC Key
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_delete_hmac_key.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_delete_hmac_key.py). To run this sample:


`python storage_delete_hmac_key.py <ACCESS_ID> <PROJECT_ID>`

-----
### Disable Bucket Lifecycle Management
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_disable_bucket_lifecycle_management.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_disable_bucket_lifecycle_management.py). To run this sample:


`python storage_disable_bucket_lifecycle_management.py <BUCKET_NAME>`

-----
### Disable Default Event Based Hold
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_disable_default_event_based_hold.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_disable_default_event_based_hold.py). To run this sample:


`python storage_disable_default_event_based_hold.py <BUCKET_NAME>`

-----
### Disable Requester Pays
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_disable_requester_pays.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_disable_requester_pays.py). To run this sample:


`python storage_disable_requester_pays.py <BUCKET_NAME>`

-----
### Disable Uniform Bucket Level Access
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_disable_uniform_bucket_level_access.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_disable_uniform_bucket_level_access.py). To run this sample:


`python storage_disable_uniform_bucket_level_access.py <BUCKET_NAME>`

-----
### Disable Versioning
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_disable_versioning.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_disable_versioning.py). To run this sample:


`python storage_disable_versioning.py <BUCKET_NAME>`

-----
### Download Byte Range
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_download_byte_range.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_download_byte_range.py). To run this sample:


`python storage_download_byte_range.py <BUCKET_NAME> <SOURCE_BLOB_NAME> <START_BYTE> <END_BYTE> <DESTINATION_FILE_NAME> <>BASE64_ENCRYPTION_KEY`

-----
### Download Encrypted File
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_download_encrypted_file.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_download_encrypted_file.py). To run this sample:


`python storage_download_encrypted_file.py <BUCKET_NAME> <SOURCE_BLOB_NAME> <DESTINATION_FILE_NAME> <>BASE64_ENCRYPTION_KEY`

-----
### Download File
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_download_file.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_download_file.py). To run this sample:


`python storage_download_file.py <BUCKET_NAME> <SOURCE_BLOB_NAME> <DESTINATION_FILE_NAME>`

-----
### Download File Requester Pays
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_download_file_requester_pays.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_download_file_requester_pays.py). To run this sample:


`python storage_download_file_requester_pays.py <BUCKET_NAME> <PROJECT_ID> <SOURCE_BLOB_NAME> <DESTINATION_FILE_NAME>`

-----
### Download Into Memory
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_download_into_memory.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_download_into_memory.py). To run this sample:


`python storage_download_into_memory.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Download Public File
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_download_public_file.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_download_public_file.py). To run this sample:


`python storage_download_public_file.py <BUCKET_NAME> <SOURCE_BLOB_NAME> <DESTINATION_FILE_NAME>`

-----
### Enable Bucket Lifecycle Management
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_enable_bucket_lifecycle_management.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_enable_bucket_lifecycle_management.py). To run this sample:


`python storage_enable_bucket_lifecycle_management.py <BUCKET_NAME>`

-----
### Enable Default Event Based Hold
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_enable_default_event_based_hold.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_enable_default_event_based_hold.py). To run this sample:


`python storage_enable_default_event_based_hold.py <BUCKET_NAME>`

-----
### Enable Requester Pays
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_enable_requester_pays.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_enable_requester_pays.py). To run this sample:


`python storage_enable_requester_pays.py <BUCKET_NAME>`

-----
### Enable Uniform Bucket Level Access
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_enable_uniform_bucket_level_access.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_enable_uniform_bucket_level_access.py). To run this sample:


`python storage_enable_uniform_bucket_level_access.py <BUCKET_NAME>`

-----
### Enable Versioning
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_enable_versioning.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_enable_versioning.py). To run this sample:


`python storage_enable_versioning.py <BUCKET_NAME>`

-----
### FileIO Write-Read
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_fileio_write_read.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_fileio_write_read.py). To run this sample:


`python storage_fileio_write_read.py <BUCKET_NAME> <BLOB_NAME>`

-----
### FileIO Pandas
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_fileio_pandas.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_fileio_pandas.py). To run this sample:


`python storage_fileio_pandas.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Generate Encryption Key
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_generate_encryption_key.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_generate_encryption_key.py). To run this sample:


`python storage_generate_encryption_key.py`

-----
### Generate Signed Post Policy V4
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_generate_signed_post_policy_v4.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_generate_signed_post_policy_v4.py). To run this sample:


`python storage_generate_signed_post_policy_v4.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Generate Signed Url V2
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_generate_signed_url_v2.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_generate_signed_url_v2.py). To run this sample:


`python storage_generate_signed_url_v2.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Generate Signed Url V4
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_generate_signed_url_v4.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_generate_signed_url_v4.py). To run this sample:


`python storage_generate_signed_url_v4.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Generate Upload Signed Url V4
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_generate_upload_signed_url_v4.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_generate_upload_signed_url_v4.py). To run this sample:


`python storage_generate_upload_signed_url_v4.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Get Bucket Labels
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_get_bucket_labels.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_bucket_labels.py). To run this sample:


`python storage_get_bucket_labels.py <BUCKET_NAME>`

-----
### Get Bucket Metadata
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_get_bucket_metadata.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_bucket_metadata.py). To run this sample:


`python storage_get_bucket_metadata.py <BUCKET_NAME>`

-----
### Get Default Event Based Hold
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_get_default_event_based_hold.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_default_event_based_hold.py). To run this sample:


`python storage_get_default_event_based_hold.py <BUCKET_NAME>`

-----
### Get HMAC Key
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_get_hmac_key.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_hmac_key.py). To run this sample:


`python storage_get_hmac_key.py <ACCESS_ID> <PROJECT_ID>`

-----
### Get Metadata
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_get_metadata.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_metadata.py). To run this sample:


`python storage_get_metadata.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Get Public Access Prevention
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_get_public_access_prevention.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_public_access_prevention.py). To run this sample:


`python storage_get_public_access_prevention.py <BUCKET_NAME>`

-----
### Get Requester Pays Status
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_get_requester_pays_status.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_requester_pays_status.py). To run this sample:


`python storage_get_requester_pays_status.py <BUCKET_NAME>`

-----
### Get Retention Policy
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_get_retention_policy.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_retention_policy.py). To run this sample:


`python storage_get_retention_policy.py <BUCKET_NAME>`

-----
### Get RPO
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_get_rpo.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_rpo.py). To run this sample:


`python storage_get_rpo.py <BUCKET_NAME>`

-----
### Get Service Account
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_get_service_account.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_service_account.py). To run this sample:


`python storage_get_service_account.py`

-----
### Get Uniform Bucket Level Access
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_get_uniform_bucket_level_access.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_get_uniform_bucket_level_access.py). To run this sample:


`python storage_get_uniform_bucket_level_access.py <BUCKET_NAME>`

-----
### List Buckets
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_list_buckets.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_list_buckets.py). To run this sample:


`python storage_list_buckets.py`

-----
### List Bucket Notifications
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_list_bucket_notifications.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_list_bucket_notifications.py). To run this sample:


`python storage_list_bucket_notifications.py <BUCKET_NAME>`

-----
### List File Archived Generations
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_list_file_archived_generations.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_list_file_archived_generations.py). To run this sample:


`python storage_list_file_archived_generations.py <BUCKET_NAME>`

-----
### List Files
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_list_files.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_list_files.py). To run this sample:


`python storage_list_files.py <BUCKET_NAME>`

-----
### List Files With Prefix
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_list_files_with_prefix.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_list_files_with_prefix.py). To run this sample:


`python storage_list_files_with_prefix.py <BUCKET_NAME> <PREFIX>`

-----
### List HMAC Keys
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_list_hmac_keys.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_list_hmac_keys.py). To run this sample:


`python storage_list_hmac_keys.py <PROJECT_ID>`

-----
### Lock Retention Policy
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_lock_retention_policy.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_lock_retention_policy.py). To run this sample:


`python storage_lock_retention_policy.py <BUCKET_NAME>`

-----
### Make Public
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_make_public.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_make_public.py). To run this sample:


`python storage_make_public.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Move File
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_move_file.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_move_file.py). To run this sample:


`python storage_move_file.py <BUCKET_NAME> <BLOB_NAME> <DESTINATION_BUCKET_NAME> <DESTINATION_BLOB_NAME>`

-----
### Object CSEK To CMEK
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_object_csek_to_cmek.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_object_csek_to_cmek.py). To run this sample:


`python storage_object_csek_to_cmek.py <BUCKET_NAME> <BLOB_NAME> <ENCRYPTION_KEY> <KMS_KEY_NAME>`

-----
### Object Get KMS Key
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_object_get_kms_key.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_object_get_kms_key.py). To run this sample:


`python storage_object_get_kms_key.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Print Bucket ACL
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_print_bucket_acl.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_print_bucket_acl.py). To run this sample:


`python storage_print_bucket_acl.py <BUCKET_NAME>`

-----
### Print Bucket ACL For User
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_print_bucket_acl_for_user.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_print_bucket_acl_for_user.py). To run this sample:


`python storage_print_bucket_acl_for_user.py <BUCKET_NAME> <USER_EMAIL>`

-----
### Print File ACL
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_print_file_acl.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_print_file_acl.py). To run this sample:


`python storage_print_file_acl.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Print File ACL For User
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_print_file_acl_for_user.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_print_file_acl_for_user.py). To run this sample:


`python storage_print_file_acl_for_user.py <BUCKET_NAME> <BLOB_NAME> <USER_EMAIL>`

-----
### Print PubSub Bucket Notification
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_print_pubsub_bucket_notification.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_print_pubsub_bucket_notification.py). To run this sample:


`python storage_print_pubsub_bucket_notification.py <BUCKET_NAME> <NOTIFICATION_ID>`

-----
### Release Event Based Hold
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_release_event_based_hold.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_release_event_based_hold.py). To run this sample:


`python storage_release_event_based_hold.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Release Temporary Hold
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_release_temporary_hold.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_release_temporary_hold.py). To run this sample:


`python storage_release_temporary_hold.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Remove Bucket Conditional IAM Binding
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_remove_bucket_conditional_iam_binding.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_remove_bucket_conditional_iam_binding.py). To run this sample:


`python storage_remove_bucket_conditional_iam_binding.py <BUCKET_NAME> <ROLE> <TITLE> <DESCRIPTION> <EXPRESSION>`

-----
### Remove Bucket Default Owner
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_remove_bucket_default_owner.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_remove_bucket_default_owner.py). To run this sample:


`python storage_remove_bucket_default_owner.py <BUCKET_NAME> <USER_EMAIL>`

-----
### Remove Bucket IAM Member
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_remove_bucket_iam_member.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_remove_bucket_iam_member.py). To run this sample:


`python storage_remove_bucket_iam_member.py <BUCKET_NAME> <ROLE> <MEMBER>`

-----
### Remove Bucket Label
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_remove_bucket_label.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_remove_bucket_label.py). To run this sample:


`python storage_remove_bucket_label.py <BUCKET_NAME>`

-----
### Remove Bucket Owner
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_remove_bucket_owner.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_remove_bucket_owner.py). To run this sample:


`python storage_remove_bucket_owner.py <BUCKET_NAME> <USER_EMAIL>`

-----
### Remove CORS Configuration
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_remove_cors_configuration.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_remove_cors_configuration.py). To run this sample:


`python storage_remove_cors_configuration.py <BUCKET_NAME>`

-----
### Remove File Owner
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_remove_file_owner.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_remove_file_owner.py). To run this sample:


`python storage_remove_file_owner.py <BUCKET_NAME> <BLOB_NAME> <USER_EMAIL>`

-----
### Remove Retention Policy
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_remove_retention_policy.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_remove_retention_policy.py). To run this sample:


`python storage_remove_retention_policy.py <BUCKET_NAME>`

-----
### Rename File
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_rename_file.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_rename_file.py). To run this sample:


`python storage_rename_file.py <BUCKET_NAME> <BLOB_NAME> <NEW_NAME>`

-----
### Rotate Encryption Key
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_rotate_encryption_key.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_rotate_encryption_key.py). To run this sample:


`python storage_rotate_encryption_key.py <BUCKET_NAME> <BLOB_NAME> <BASE64_ENCRYPTION_KEY> <BASE64_NEW_ENCRYPTION_KEY>`

-----
### Set Bucket Default KMS Key
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_set_bucket_default_kms_key.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_set_bucket_default_kms_key.py). To run this sample:


`python storage_set_bucket_default_kms_key.py <BUCKET_NAME> <KMS_KEY_NAME>`

-----
### Set Bucket Public IAM
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_set_bucket_public_iam.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_set_bucket_public_iam.py). To run this sample:


`python storage_set_bucket_public_iam.py <BUCKET_NAME>`

-----
### Set Event Based Hold
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_set_event_based_hold.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_set_event_based_hold.py). To run this sample:


`python storage_set_event_based_hold.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Set Metadata
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_set_metadata.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_set_metadata.py). To run this sample:


`python storage_set_metadata.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Set Public Access Prevention Enforced
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_set_public_access_prevention_enforced.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_set_public_access_prevention_enforced.py). To run this sample:


`python storage_set_public_access_prevention_enforced.py <BUCKET_NAME>`

-----
### Set Public Access Prevention Inherited
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_set_public_access_prevention_inherited.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_set_public_access_prevention_inherited.py). To run this sample:


`python storage_set_public_access_prevention_inherited.py <BUCKET_NAME>`

-----
### Set Retention Policy
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_set_retention_policy.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_set_retention_policy.py). To run this sample:


`python storage_set_retention_policy.py <BUCKET_NAME> <RETENTION_PERIOD>`


-----
### Set RPO Async Turbo
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_set_rpo_async_turbo.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_set_rpo_async_turbo.py). To run this sample:


`python storage_set_rpo_async_turbo.py <BUCKET_NAME>`

-----
### Set RPO Default
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_set_rpo_default.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_set_rpo_default.py). To run this sample:


`python storage_set_rpo_default.py <BUCKET_NAME>`

-----
### Set Temporary Hold
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_set_temporary_hold.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_set_temporary_hold.py). To run this sample:


`python storage_set_temporary_hold.py <BUCKET_NAME> <BLOB_NAME>`

-----
### Upload Encrypted File
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_upload_encrypted_file.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_upload_encrypted_file.py). To run this sample:


`python storage_upload_encrypted_file.py <BUCKET_NAME> <SOURCE_FILE_NAME> <DESTINATION_BLOB_NAME> <BASE64_ENCRYPTION_KEY>`

-----
### Upload File
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_upload_file.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_upload_file.py). To run this sample:


`python storage_upload_file.py <BUCKET_NAME> <SOURCE_FILE_NAME> <DESTINATION_BLOB_NAME>`

-----
### Upload From Memory
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_upload_from_memory.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_upload_from_memory.py). To run this sample:


`python storage_upload_from_memory.py <BUCKET_NAME> <CONTENTS> <DESTINATION_BLOB_NAME>`

-----
### Upload With KMS Key
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_upload_with_kms_key.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_upload_with_kms_key.py). To run this sample:


`python storage_upload_with_kms_key.py <BUCKET_NAME> <SOURCE_FILE_NAME> <DESTINATION_BLOB_NAME> <KMS_KEY_NAME>`

-----
### View Bucket IAM Members
[![Open in Cloud Shell][shell_img]](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/python-storage&page=editor&open_in_editor=samples/snippets/storage_view_bucket_iam_members.py,samples/README.md)

View the [source code](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_view_bucket_iam_members.py). To run this sample:


`python storage_view_bucket_iam_members.py <BUCKET_NAME>`

