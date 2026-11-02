<!--
Copyright 2020 Google LLC
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    https://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->


# 2.0.0 Migration Guide

The 2.0 release of the `google-cloud-spanner` client is a significant update based on a
[next-gen code generator](https://github.com/googleapis/gapic-generator-python).
It drops support for Python versions below 3.6.

The handwritten client surfaces have minor changes which may require minimal updates to existing user code.

The generated client surfaces have substantial interface changes. Existing user code which uses these surfaces directly
will require significant updates to use this version.

This document describes the changes that have been made, and what you need to do to update your usage.

If you experience issues or have questions, please file an
[issue](https://github.com/googleapis/python-spanner/issues).


## Supported Python Versions

> **WARNING**: Breaking change

The 2.0.0 release requires Python 3.6+.

## Handwritten Surface Changes

### Resource List Methods

> **WARNING**: Breaking change

The list methods will now return the resource protos rather than the handwritten interfaces.

Accessing properties will remain unchanged. However, calling methods will require creating the handwritten interface
from the proto.

**Before:**
```py
for instance in client.list_instances():
    if "test" in instance.name:
        instance.delete()
```
```py
for backup in instance.list_backups():
    if "test" in backup.name:
        backup.delete()
```
```py
for database in instance.list_databases():
    if "test" in database.name:
        database.delete()
```

**After:**
```py
for instance_pb in client.list_instances():
    if "test" in instance_pb.name:
        instance = Instance.from_pb(instance_pb, client)
        instance.delete()
```
```py
for backup_pb in instance.list_backups():
    if "test" in backup_pb.name:
        backup = Backup.from_pb(backup_pb, instance)
        backup.delete()
```
```py
for database_pb in instance.list_databases():
    if "test" in database_pb.name:
        database = Database.from_pb(database_pb, instance)
        database.delete()
```


### Resource List Pagination

> **WARNING**: Breaking change

The library now handles pages for the user. Previously, the library would return a page generator which required a user
to then iterate over each page to get the resource. Now, the library handles iterating over the pages and only returns
the resource protos.

**Before:**
```py
for page in client.list_instances(page_size=5):
    for instance in page:
        ...
```
```py
for page in instance.list_backups(page_size=5):
    for backup in page:
        ...
```
```py
for page in instance.list_databases(page_size=5):
    for database in page:
        ...
```

**After:**
```py
for instance_pb in client.list_instances(page_size=5):
    ...
```
```py
for backup_pb in instance.list_backups(page_size=5):
    ...
```
```py
for database_pb in instance.list_databases(page_size=5):
    ...
```

### Deprecated Method Arguments

> **WARNING**: Breaking change

Deprecated arguments have been removed.
If you use these arguments, they have no effect and can be removed without consequence.
`user_agent` can be specified using `client_info` instead.
Users should not be using `page_token` directly as the library handles pagination under the hood.

**Before:**
```py
client = Client(user_agent=user_agent)
```
```py
for instance in list_instances(page_token=page_token):
    ...
```
```py
for config in list_instance_configs(page_token=page_token):
    ...
```
```py
for database in list_databases(page_token=page_token):
    ...
```

**After:**
```py
client = Client()
```
```py
for instance_pb in client.list_instances():
    ...
```
```py
for instance_config_pb in client.list_instance_configs():
    ...
```
```py
for database_pb in instance.list_databases():
    ...
```


## Generated Surface Changes


### Method Calls

> **WARNING**: Breaking change

Methods expect request objects. We provide scripts that will convert most common use cases.

* Install the library with `libcst`.

```py
python3 -m pip install google-cloud-spanner[libcst]
```

* The scripts `fixup_spanner_v1_keywords.py`, `fixup_spanner_admin_database_v1_keywords.py`, and
`fixup_spanner_admin_instance_v1_keywords.py` are shipped with the library. They expect an input directory (with the
code to convert) and an empty destination directory.

```sh
$ fixup_spanner_v1_keywords.py --input-directory .samples/ --output-directory samples/
```

>**WARNING**: These scripts will change any calls that match one of the methods. This may cause issues if you also use
>the handwritten surfaces e.g. `client.list_instances()`

#### More details

 In `google-cloud-spanner<2.0.0`, parameters required by the API were positional parameters and optional parameters were
 keyword parameters.

 **Before:**
 ```py
def list_instances(
        self,
        parent,
        page_size=None,
        filter_=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
 ```

 In the 2.0.0 release, all methods have a single positional parameter `request`. Method docstrings indicate whether a
 parameter is required or optional.

 Some methods have additional keyword only parameters. The available parameters depend on the
 [`google.api.method_signature` annotation](https://github.com/googleapis/googleapis/blob/master/google/spanner/admin/instance/v1/spanner_instance_admin.proto#L86) specified by the API producer.


 **After:**
 ```py
def list_instances(
        self,
        request: spanner_instance_admin.ListInstancesRequest = None,
        *,
        parent: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListInstancesPager:
 ```

 > **NOTE:** The `request` parameter and flattened keyword parameters for the API are mutually exclusive.
 > Passing both will result in an error.


 Both of these calls are valid:

 ```py
 response = client.list_instances(
     request={
         "parent": project_name,
     }
 )
 ```

 ```py
 response = client.execute_sql(
     parent=project_name,
 )
 ```

 This call is invalid because it mixes `request` with a keyword argument `parent`. Executing this code
 will result in an error.

 ```py
 response = client.execute_sql(
     request={},
     parent=project_name,
 )
 ```

### Enum and protos

> **WARNING**: Breaking change

Generated GAPIC protos have been moved under `types`. Import paths need to be adjusted.

**Before:**
```py
from google.cloud.spanner_v1.proto import type_pb2

param_types = {
    "start_title": type_pb2.Type(code=type_pb2.STRING),
    "end_title": type_pb2.Type(code=type_pb2.STRING),
}
```
**After:**
```py
from google.cloud.spanner_v1 import Type
from google.cloud.spanner_v1 import TypeCode

param_types = {
    "start_title": Type(code=TypeCode.STRING),
    "end_title": Type(code=TypeCode.STRING),
}
```
**Preferred:**
```py
from google.cloud import spanner

param_types = {
    "start_title": spanner.param_types.STRING,
    "end_title": spanner.param_types.STRING,
}
```

Generated GAPIC enum types have also been moved under `types`. Import paths need to be adjusted.

**Before:**
```py
from google.cloud.spanner_admin_database_v1.gapic import enums

state = enums.Backup.State.READY
```
**After:**
```py
from google.cloud.spanner_admin_database_v1 import types

state = types.Backup.State.READY
```
**Preferred:**
```py
from google.cloud.spanner_admin_database_v1 import Backup

state = Backup.State.READY
```
