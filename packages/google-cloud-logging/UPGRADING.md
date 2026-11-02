# 3.0.0 Migration Guide

The v3.0.0 release of `google-cloud-logging` improves usability of the library,
particularly on serverless environments.

If you experience technical issues or have questions, please file an [issue](https://github.com/googleapis/python-logging/issues).

## Primary Changes

### Handler deprecations ([#310](https://github.com/googleapis/python-logging/pull/310))

> **WARNING**: Breaking change

We have changed our design policy to support more generic `Handler` classes instead of product-specific classes:

- [`CloudLoggingHandler`](https://github.com/googleapis/python-logging/blob/v2.7.0/google/cloud/logging_v2/handlers/handlers.py)
  - Sends logs over the network (using gRPC or HTTP API calls)
  - Replaces `AppEngineHandler`
- [`StructuredLogHandler`](https://github.com/googleapis/python-logging/blob/v2.7.0/google/cloud/logging_v2/handlers/structured_log.py)
  - Exports logs in JSON format through standard out, to be parsed by an agent
  - Replaces `ContainerEngineHandler`

As of v3.0.0, [`AppEngineHandler`](https://github.com/googleapis/python-logging/blob/v2.7.0/google/cloud/logging_v2/handlers/app_engine.py) 
and [`ContainerEngineHandler`](https://github.com/googleapis/python-logging/blob/v2.7.0/google/cloud/logging_v2/handlers/container_engine.py)
are deprecated and won't be updated. These handlers might be removed from the library in a future update.

### Full JSON log support in standard library integration ([#316](https://github.com/googleapis/python-logging/pull/316), [#339](https://github.com/googleapis/python-logging/pull/339), [#447](https://github.com/googleapis/python-logging/pull/447))

You can now log JSON data using the Python `logging` standard library integration. 
To log JSON data, do one of the following:

1. Use  `json_fields` `extra` argument:

```py
import logging

data_dict = {"hello": "world"}
logging.info("message field", extra={"json_fields": data_dict})
```

2. Log a JSON-parsable string:

```py
import logging
import json

data_dict = {"hello": "world"}
logging.info(json.dumps(data_dict))
```

### Metadata autodetection ([#315](https://github.com/googleapis/python-logging/pull/315))

> **WARNING**: Breaking change

Logs emitted by the library must be associated with a [montored-resource type](https://cloud.google.com/monitoring/api/resources)
that indicates the compute environment the log originated from. 
- Prior to 3.0.0, when a log doesn't specify a monitored resource, that field is set to ["global"](https://cloud.google.com/monitoring/api/resources#tag_global).
- With 3.0.0,  when a log doesn't specify a monitored resource, the library attempts to identify the resource. If a resource can't be detected, the field will still default to ["global"](https://cloud.google.com/monitoring/api/resources#tag_global).

### New `Logger.log` method ([#316](https://github.com/googleapis/python-logging/pull/316))

In v3.0.0, the library adds a generic `log()` method that will attempt to infer and log any type:

```py
logger.log("hello world")
```

v3.0.0 also supports the Logging class methods from previous releases:

```py
logger.log_text("hello world")
logger.log_struct({"hello": "world"})
logger.log_proto(proto_message)
logger.log_empty()
```

### More permissive arguments ([#422](https://github.com/googleapis/python-logging/pull/422))

> **WARNING**: Breaking change

In v3.0.0, the library supports a wider variety of input formats:

```py
# lowercase severity strings will be accepted
logger.log("hello world", severity="warning")
```

```py
# a severity will be pulled out of the JSON payload if not otherwise set
logger.log({"hello": "world", "severity":"warning"})
```

```py
# resource data can be passed as a dict instead of a Resource object
logger.log("hello world", resource={"type":"global", "labels":[]})
```

### Allow reading from non-project resources ([#444](https://github.com/googleapis/python-logging/pull/444))

Prior to v3.0.0, there was a crashing bug when attempting to read logs from non-project resources:

- `organizations/[ORGANIZATION_ID]/logs/[LOG_ID]`
- `billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]`
- `folders/[FOLDER_ID]/logs/[LOG_ID]`

The v3.0.0 update fixes this issue.

### Internal Gapic and HTTP implementation changes ([#375](https://github.com/googleapis/python-logging/pull/375))

> **WARNING**: Breaking change

The library supports sending logs using two network protocols: gRPC and HTTP. Prior to v3.0.0, there was an
inconsistency in the implementations, resulting in unexpected behavior when in HTTP mode.

### Max_size argument when listing entries ([#375](https://github.com/googleapis/python-logging/pull/375))

v3.0.0 introduces a new `max_size` argument to `list_entries` calls, which can be used to specify an upper bound
on how many logs should be returned:

```py
from google.cloud import logging_v2

client = logging_v2.Client()
client.list_entries(max_size=5)
```

---

# 2.0.0 Migration Guide

The 2.0 release of the `google-cloud-logging` client is a significant upgrade based on a [next-gen code generator](https://github.com/googleapis/gapic-generator-python), and includes substantial interface changes. Existing code written for earlier versions of this library will likely require updates to use this version. This document describes the changes that have been made, and what you need to do to update your usage.

If you experience issues or have questions, please file an [issue](https://github.com/googleapis/python-logging/issues).

## Supported Python Versions

> **WARNING**: Breaking change

The 2.0.0 release requires Python 3.6+.


## Primary Changes

This section lists the most relevant changes in `google.cloud.logging`.
See 'Changes in GAPIC Layer' if you were directly using `google.cloud.logging_v2.proto` or `google.cloud.logging_v2.gapic`.


### Optional arguments *must* be passed as keyword arguments.

Optional arguments are keyword-only arguments and *must* be passed by name.
See [PEP 3102](https://www.python.org/dev/peps/pep-3102/).

```diff
from google.cloud import logging

filter_ = "severity>=CRITICAL"
destination = "storage.googleapis.com/{bucket}".format(bucket=destination_bucket)
logging_client = logging.Client()
-sink = logging_client.sink(sink_name, filter_, destination)
+sink = logging_client.sink(sink_name, filter_=filter_, destination=destination)
```

### Support for non-project resources

Where appropriate, the library supports additional resource names. https://google.aip.dev/122

**Valid Resource Names**:

* `"projects/[PROJECT_ID]"`
* `"organizations/[ORGANIZATION_ID]"`
* `"billingAccounts/[BILLING_ACCOUNT_ID]"`
* `"folders/[FOLDER_ID]"`


#### `google.cloud.logging_v2.client.Client`


> **WARNING**: Breaking change

`list_entries` accepts an optional `resource_names` parameter. `projects` has been removed.


```diff
from google.cloud import logging_v2

client = logging_v2.Client()
-client.list_entries(projects="myProject"])
+client.list_entries(resource_names=["projects/myProject", "folders/myFolder"])
client.list_entries()  # defaults to project bound to client
```

`list_sinks` accepts an optional `parent` parameter.

```py
from google.cloud import logging_v2

client = logging_v2.Client()
client.list_sinks()  # lists sinks in current project
client.list_sinks(parent="folders/myFolder")  # specify a different parent resource
```

#### `google.cloud.logging_v2.logger.Logger`

> **WARNING**: Breaking change

`list_entries` accepts an optional `resource_names` parameter. `projects` has been removed.

```diff
from google.cloud import logging_v2

client = logging_v2.Client()
logger = logging_v2.Logger("myLog", client)
- logger.list_entries(projects="myProject"])
+ logger.list_entries(resource_names=["projects/myProject", "folders/myFolder"])
logger.list_entries()  # defaults to project bound to client
```

#### `google.cloud.logging_v2.sinks.Sink`

> **WARNING**: Breaking change
* Sinks no longer have a `project` property. The attribute is replaced by `parent`.

```diff
from google.cloud import logging

client = logging_v2.Client(project="myProject")
sink = logging.Sink("mySink", client=client)
-project = sink.project  # myProject
+parent = sink.parent  # projects/myProject
```


### `google.cloud.logging` is an alias for `google.cloud.logging_v2`

> **WARNING**: Breaking change

All library code has been moved to `google.cloud.logging_v2`.
`google.cloud.logging` serves as a default alias for `google.cloud.logging_v2`.




## Changes in GAPIC layer

This section describes changes in the GAPIC layer (produced by the generator) that previously lived in  `google.cloud.logging_v2.proto` / `google.cloud.logging_v2.gapic`.

> **NOTE**: Most users are unlikely to have been using this layer directly.

### Import path

> **WARNING**: Breaking change

The generated client is no longer exposed at `google.cloud.logging_v2`. This is because we expect most users to use the handwritten surface exposed at `google.cloud.logging_v2`. See the [Cloud Logging How-to Guides](https://cloud.google.com/logging/docs/how-to).

If you would like to continue using the generated surface, adjust your imports:

**Before**
```py
from google.cloud import logging_v2
logging_client = logging_v2.LoggingServiceV2Client()
```

**After**

```py
from google.cloud.logging_v2.services.logging_service_v2 import LoggingServiceV2Client
from google.cloud.logging_v2.types import LogSink

logging_client = LoggingServiceV2Client()
sink = LogSink()
```
### Method Calls

> **WARNING**: Breaking change

Methods expect request objects. We provide a script that will convert most common use cases. This script will *only* convert code written for the generated clients previously exposed at `google.cloud.logging_v2` like `LoggingServiceV2Client`.

* Install the library and `libcst`. `libcst` is required to run the fixup script.

```py
python3 -m pip install google-cloud-logging libcst
```

* The script `fixup_logging_v2_keywords.py` is shipped with the library. It expects
an input directory (with the code to convert) and an empty destination directory.

```sh
$ fixup_logging_v2_keywords.py --input-directory .samples/ --output-directory samples/
```

**Before:**
```py
from google.cloud import logging_v2

client = logging_v2.LoggingServiceV2Client()
client.list_log_entries(["projects/myProject"], filter_ = "severity>=CRITICAL")
```


**After:**
```py
from google.cloud.logging_v2.services.logging_service_v2 import LoggingServiceV2Client

client = LoggingServiceV2Client()
client.list_log_entries({"resource_names": ["projects/myProject"], "filter": "severity>=CRITICAL"})
```

#### More Details

In `google-cloud-logging<2.0.0`, parameters required by the API were positional parameters and optional parameters were keyword parameters.

**Before:**
```py
    def list_log_entries(
        self,
        resource_names,
        project_ids=None,
        filter_=None,
        order_by=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
```

In the 2.0.0 release, all methods have a single positional parameter `request`. Method docstrings indicate whether a parameter is required or optional.

Some methods have additional keyword only parameters. The available parameters depend on the [`google.api.method_signature` annotation](https://github.com/googleapis/googleapis/blob/2db5725bf898b544a0cf951e1694d3b0fce5eda3/google/cloud/automl/v1/prediction_service.proto#L86) specified by the API producer.


**After:**
```py
    def list_log_entries(
        self,
        request: logging.ListLogEntriesRequest = None,
        *,
        resource_names: Sequence[str] = None,
        filter: str = None,
        order_by: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListLogEntriesPager:
```

> **NOTE:** The `request` parameter and flattened keyword parameters for the API are mutually exclusive.
> Passing both will result in an error.


Both of these calls are valid:

```py
response = client.list_log_entries(
    request={
        "resource_names": resource_names,
        "filter": filter_,
        "order_by": order_by,
    }
)
```

```py
response = client.list_log_entries(
    resource_names=resource_names,
    filter=filter_,
    order_by=order_by,
)
```

This call is invalid because it mixes `request` with a keyword argument `order_by`. Executing this code will result in an error.

```py
response = client.list_log_entries(
    request={
        "resource_names": resource_names,
        "filter": filter_,
    }
    order_by=order_by
)
```

### `filter` parameter

Methods that took parameter `filter_` now expect `filter`.

**Before**
```py
from google.cloud import logging_v2

client = logging_v2.LoggingServiceV2Client()
client.list_log_entries(["projects/myProject"], filter_="severity>=CRITICAL")
```


**After**
```py
from google.cloud.logging_v2.services.logging_service_v2 import LoggingServiceV2Client

client = LoggingServiceV2Client()
client.list_log_entries(resource_names=["projects/myProject"], filter="severity>=CRITICAL")
```

### Enums


> **WARNING**: Breaking change

The submodule `enums` has been removed. Enums can be accessed under `types`.

**Before:**
```py
from google.cloud import logging_v2

severity = logging_v2.enums.LifecycleState.ACTIVE
```


**After:**
```py
from google.cloud import logging_v2

severity = logging_v2.types.LifecycleState.ACTIVE
```


### Resource Path Helper Methods

The following resource name helpers have been removed. Please construct the strings manually.

```py
billing_account = "my-billing-account"
folder = "my-folder"
organization = "my-organization"
log = "my-log"

exclusion = "exclusion"
sink = "my-sink"

# LoggingServiceV2Client
billing_log_path = f"billingAccounts/{billing_account}/logs/{log}"
folder_log_path = f"folders/{folder}/logs/{log}"
organization_log_path = f"organizations/{organization}/logs/{log}"

# ConfigServiceV2Client
billing_exclusion_path = f"billingAccounts/{billing_account}/exclusions/{exclusion}"
billing_sink_path = f"billingAccounts/{billing_account}/sinks/{sink}"
exclusion_path = f"projects/{project}/exclusions/{exclusion}"
folder_exclusion_path = f"folders/{folder}/exclusions/{exclusion}"
folder_sink_path = f"folders/{folder}/sinks/{sink}"
organization_exclusion_path = f"organizations/{organization}/exclusions/{exclusion}"
organization_sink_path = f"organizations/{organization}/sinks/{sink}"
```

The following resource name helpers have been renamed.

**All Clients**
* `billing_path` -> `common_billing_account_path`
* `folder_path` -> `common_folder_path`
* `organization_path` -> `common_organization_path`
* `project_path` -> `common_project_path`

**`ConfigServiceV2Client`**
* `sink_path` -> `log_sink_path`
* `exclusion_path` -> `log_exclusion_path`
