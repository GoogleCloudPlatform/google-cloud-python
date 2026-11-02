import tempfile
import unittest
from pathlib import Path
from unittest import mock

from docutils import nodes
from parameterized import parameterized
from sphinx import addnodes
from yaml import Loader, load

from docfx_yaml import extension, markdown_utils, utils


class TestGenerate(unittest.TestCase):
    def test_finds_unique_name(self):
        entries = {}

        # Disambiguate with unique entries.
        schema_v1_entry = "google.cloud.aiplatform.v1.schema.predict.instance_v1.types"
        schema_v1beta2_entry = (
            "google.cloud.aiplatform.v1beta2.schema.predict.instance_v1.types"
        )
        for entry in [schema_v1_entry, schema_v1beta2_entry]:
            for word in entry.split("."):
                if word not in entries:
                    entries[word] = 1
                else:
                    entries[word] += 1

        unique_v1_name = extension.find_unique_name(schema_v1_entry.split("."), entries)
        unique_v1beta2_name = extension.find_unique_name(
            schema_v1beta2_entry.split("."), entries
        )

        self.assertEqual("v1.types", ".".join(unique_v1_name))
        self.assertEqual("v1beta2.types", ".".join(unique_v1beta2_name))

    test_entries = [
        [
            "tests/yaml_pre.yaml",
            "tests/yaml_post.yaml",
            {
                "google.cloud.spanner_admin_database_v1.types": "spanner_admin_database_v1.types",
                "google.cloud.spanner_admin_instance_v1.types": "spanner_admin_instance_v1.types",
                "google.cloud.spanner_v1.types": "spanner_v1.types",
            },
        ],
        [
            # Tests duplicate names
            "tests/yaml_pre_duplicate.yaml",
            "tests/yaml_post_duplicate.yaml",
            {
                "google.api_core.client_info": "client_info",
                "google.api_core.gapic_v1.client_info": "gapic_v1.client_info",
            },
        ],
        [
            # Tests repeated duplicates in a row. No changes expected.
            "tests/yaml_repeat_duplicate.yaml",
            "tests/yaml_repeat_duplicate.yaml",
            {},
        ],
    ]

    @parameterized.expand(test_entries)
    def test_disambiguates_toc_name(
        self,
        test_filename,
        expected_filename,
        expected_disambiguated_names,
    ):
        with open(test_filename, "r") as test_file:
            test_yaml = load(test_file, Loader=Loader)
        with open(expected_filename, "r") as expected_yaml_file:
            expected_yaml = load(expected_yaml_file, Loader=Loader)

        disambiguated_names = extension.disambiguate_toc_name(test_yaml)

        self.assertEqual(expected_yaml, test_yaml)
        self.assertEqual(expected_disambiguated_names, disambiguated_names)

    test_entries = [
        [
            """
If a ``stream`` is attached to this download, then the downloaded
resource will be written to the stream.

Args:
    transport (~google.cloud.requests.Session): A ``requests`` object which can
        make authenticated requests.

    timeout (Optional[Union[float, Tuple[float, float]]]):
        The number of seconds to wait for the server response.
        Depending on the retry strategy, a request may be repeated
        several times using the same timeout each time.

        Can also be passed as a tuple (connect_timeout, read_timeout).
        See :meth:`google.cloud.requests.Session.request` documentation for details.

Returns:
    ~google.cloud.requests.Response: The HTTP response returned by ``transport``.

Raises:
    ~google.cloud.resumable_media.common.DataCorruption: If the download"s
        checksum doesn't agree with server-computed checksum.
    ValueError: If the current :class:`Download` has already
        finished.
            """,
            """
If a ``stream`` is attached to this download, then the downloaded
resource will be written to the stream.

Args:
    transport (<xref uid="google.cloud.requests.Session">Session</xref>): A ``requests`` object which can
        make authenticated requests.

    timeout (Optional[Union[float, Tuple[float, float]]]):
        The number of seconds to wait for the server response.
        Depending on the retry strategy, a request may be repeated
        several times using the same timeout each time.

        Can also be passed as a tuple (connect_timeout, read_timeout).
        See <xref uid="google.cloud.requests.Session.request">request</xref> documentation for details.

Returns:
    <xref uid="google.cloud.requests.Response">Response</xref>: The HTTP response returned by ``transport``.

Raises:
    <xref uid="google.cloud.resumable_media.common.DataCorruption">DataCorruption</xref>: If the download"s
        checksum doesn't agree with server-computed checksum.
    ValueError: If the current `Download` has already
        finished.
            """,
            [
                "google.cloud.requests.Session",
                "google.cloud.requests.Session.request",
                "google.cloud.requests.Response",
                "google.cloud.resumable_media.common.DataCorruption",
            ],
        ],
        [
            """
If a ~dateutil.time.stream() is attached to this download, then the downloaded
resource will be written to the stream.

Args:
    transport (~google.cloud.requests.Session()): A ``requests`` object which can
        make authenticated requests.

    timeout (Optional[Union[float, Tuple[float, float]]]):
        The number of seconds to wait for the server response.
        Depending on the retry strategy, a request may be repeated
        several times using the same timeout each time.

        Can also be passed as a :func:`~google.cloud.requests.tuple()` (connect_timeout, read_timeout).
        See :meth:`google.cloud.requests.Session.request()` documentation for details.
            """,
            """
If a `dateutil.time.stream()` is attached to this download, then the downloaded
resource will be written to the stream.

Args:
    transport (<xref uid="google.cloud.requests.Session">Session()</xref>): A ``requests`` object which can
        make authenticated requests.

    timeout (Optional[Union[float, Tuple[float, float]]]):
        The number of seconds to wait for the server response.
        Depending on the retry strategy, a request may be repeated
        several times using the same timeout each time.

        Can also be passed as a <xref uid="google.cloud.requests.tuple">tuple()</xref> (connect_timeout, read_timeout).
        See <xref uid="google.cloud.requests.Session.request">request()</xref> documentation for details.
            """,
            [
                "google.cloud.requests.Session",
                "google.cloud.requests.tuple",
                "google.cloud.requests.Session.request",
            ],
        ],
    ]

    @parameterized.expand(test_entries)
    def test_resolves_references_in_summary(
        self,
        test_docstring,
        expected_content,
        expected_xrefs,
    ):
        xrefs_to_check = []
        # Resolve over different regular expressions for different types of reference patterns.
        content_to_resolve, xrefs = extension._resolve_reference_in_module_summary(
            extension.REF_PATTERN,
            test_docstring.split("\n"),
        )
        xrefs_to_check.extend(xrefs)

        resolved_content, xrefs = extension._resolve_reference_in_module_summary(
            extension.REF_PATTERN_LAST,
            content_to_resolve,
        )
        xrefs_to_check.extend(xrefs)

        self.assertEqual(resolved_content, expected_content.split("\n"))
        self.assertCountEqual(xrefs_to_check, expected_xrefs)

    test_entries = [
        [
            """Required.

The [name][google.cloud.kms.v1.KeyRing.name] of the [KeyRing][google.cloud.kms.v1.KeyRing] associated with the [ImportJobs][google.cloud.kms.v1.ImportJob].
            """,
            """Required.

The <xref uid="google.cloud.kms.v1.KeyRing.name">name</xref> of the <xref uid="google.cloud.kms.v1.KeyRing">KeyRing</xref> associated with the <xref uid="google.cloud.kms.v1.ImportJob">ImportJobs</xref>.
            """,
            [
                "google.cloud.kms.v1.KeyRing.name",
                "google.cloud.kms.v1.KeyRing",
                "google.cloud.kms.v1.ImportJob",
            ],
        ],
    ]

    @parameterized.expand(test_entries)
    def test_resolves_square_bracket_references(
        self,
        summary,
        expected_summary,
        expected_xrefs,
    ):
        resolved_summary, xrefs = extension._resolve_reference_in_module_summary(
            extension.REF_PATTERN_BRACKETS,
            summary.split("\n"),
        )

        self.assertEqual(resolved_summary, expected_summary.split("\n"))
        self.assertCountEqual(xrefs, expected_xrefs)

    def test_raises_error_for_invalid_references(self):
        with self.assertRaises(ValueError):
            extension._resolve_reference_in_module_summary(
                ".*",
                "not a valid ref line".split("\n"),
            )

    test_entries = [
        [
            """
Simple test for docstring.

Args:
    arg1(int): simple description.
    arg2(str): simple description for `arg2`.

Returns:
    str: simple description for return value.

Raises:
    AttributeError: if `condition x`.
            """,
            "\nSimple test for docstring.\n\n",
            {
                "variables": {
                    "arg1": {
                        "var_type": "int",
                        "description": "simple description.",
                    },
                    "arg2": {
                        "var_type": "str",
                        "description": "simple description for `arg2`.",
                    },
                },
                "returns": [
                    {
                        "var_type": "str",
                        "description": "simple description for return value.",
                    }
                ],
                "exceptions": [
                    {
                        "var_type": "AttributeError",
                        "description": "if `condition x`.",
                    }
                ],
            },
        ],
        [
            # Tests summary in mixed format
            """
Simple test for docstring.

:type arg1: int
:param arg1: simple description.
:param arg2: simple description for `arg2`.
:type arg2: str

:rtype: str
:returns: simple description for return value.

:raises AttributeError: if `condition x`.
            """,
            "\nSimple test for docstring.\n\n",
            {
                "variables": {
                    "arg1": {
                        "var_type": "int",
                        "description": "simple description.",
                    },
                    "arg2": {
                        "var_type": "str",
                        "description": "simple description for `arg2`.",
                    },
                },
                "returns": [
                    {
                        "var_type": "str",
                        "description": "simple description for return value.",
                    }
                ],
                "exceptions": [
                    {
                        "var_type": "AttributeError",
                        "description": "if `condition x`.",
                    }
                ],
            },
        ],
        [
            # Tests summary for docstring tokens and not custom fields
            """
Union[int, None]: Expiration time in milliseconds for a partition.

If :attr:`partition_expiration` is set and <xref:type_> is
not set, :attr:`type_` will default to
:attr:`~google.cloud.bigquery.table.TimePartitioningType.DAY`.
It could return :param: with :returns as well.
            """,
            """
Union[int, None]: Expiration time in milliseconds for a partition.

If :attr:`partition_expiration` is set and <xref:type_> is
not set, :attr:`type_` will default to
:attr:`~google.cloud.bigquery.table.TimePartitioningType.DAY`.
It could return :param: with :returns as well.
            """,
            {
                "variables": {},
                "returns": [],
                "exceptions": [],
            },
        ],
        [
            # Tests summary with xrefs
            """
Simple test for docstring.

:type arg1: <xref uid="google.spanner_v1.type.Type">Type</xref>
:param arg1: simple description.
:param arg2: simple description for `arg2`.
:type arg2: ~google.spanner_v1.type.dict

:rtype: <xref uid="Pair">Pair</xref>
:returns: simple description for return value.

:raises <xref uid="SpannerException">SpannerException</xref>: if `condition x`.
            """,
            "\nSimple test for docstring.\n\n",
            {
                "variables": {
                    "arg1": {
                        "var_type": '<xref uid="google.spanner_v1.type.Type">Type</xref>',
                        "description": "simple description.",
                    },
                    "arg2": {
                        "var_type": "~google.spanner_v1.type.dict",
                        "description": "simple description for `arg2`.",
                    },
                },
                "returns": [
                    {
                        "var_type": '<xref uid="Pair">Pair</xref>',
                        "description": "simple description for return value.",
                    }
                ],
                "exceptions": [
                    {
                        "var_type": '<xref uid="SpannerException">SpannerException</xref>',
                        "description": "if `condition x`.",
                    }
                ],
            },
        ],
        [
            # Tests docstring without a summary
            """
Args:
    arg1(int): simple description.
    arg2(str): simple description for `arg2`.

Returns:
    str: simple description for return value.

Raises:
    AttributeError: if `condition x`.
            """,
            "\n",
            {
                "variables": {
                    "arg1": {
                        "var_type": "int",
                        "description": "simple description.",
                    },
                    "arg2": {
                        "var_type": "str",
                        "description": "simple description for `arg2`.",
                    },
                },
                "returns": [
                    {
                        "var_type": "str",
                        "description": "simple description for return value.",
                    }
                ],
                "exceptions": [
                    {
                        "var_type": "AttributeError",
                        "description": "if `condition x`.",
                    }
                ],
            },
        ],
    ]

    @parameterized.expand(test_entries)
    def test_extracts_docstring_info(
        self, summary, expected_top_summary, expected_summary_info
    ):
        summary_info = {"variables": {}, "returns": [], "exceptions": []}

        top_summary = extension._extract_docstring_info(
            summary_info,
            summary,
            "",
        )

        self.assertEqual(top_summary, expected_top_summary)
        self.assertDictEqual(summary_info, expected_summary_info)

    test_entries = [
        [
            """
Description of docstring which should fail.

:returns:param:
            """,
            ValueError,
            "Error string",
        ],
        [
            """
Description of malformed docstring.

Raises:
    Error that should fail: if condition `x`.
            """,
            KeyError,
            "Malformed docstring",
        ],
    ]

    @parameterized.expand(test_entries)
    def test_raises_error_extracting_malformed_docstring(
        self,
        summary,
        error_type,
        error_string,
    ):
        with self.assertRaises(error_type):
            extension._extract_docstring_info({}, summary, error_string)

    test_entries = [
        [
            "google.cloud.spanner_v1beta2.services.admin_database_v1.types",
            "google.cloud.spanner_v1beta2",
        ],
    ]

    @parameterized.expand(test_entries)
    def test_finds_package_group(
        self,
        uid,
        expected_package_group,
    ):
        package_group = extension.find_package_group(uid)

        self.assertEqual(package_group, expected_package_group)

    test_entries = [
        [
            "google.cloud.spanner_v1beta2",
            "Spanner V1beta2",
        ],
    ]

    @parameterized.expand(test_entries)
    def test_finds_pretty_package_name(
        self,
        package_group,
        expected_package_name,
    ):
        package_name = extension.pretty_package_name(package_group)

        self.assertEqual(package_name, expected_package_name)

    test_entries = [
        [
            # toc_yaml entry
            [
                {
                    "name": "database_admin",
                    "uidname": "google.cloud.spanner_admin_database_v1.services.database_admin",
                    "items": [
                        {
                            "name": "Overview",
                            "uidname": "google.cloud.spanner_admin_database_v1.services.database_admin",
                            "uid": "google.cloud.spanner_admin_database_v1.services.database_admin",
                        },
                        {
                            "name": "ListBackupOperationsAsyncPager",
                            "uidname": "google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsAsyncPager",
                            "uid": "google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsAsyncPager",
                        },
                    ],
                },
                {
                    "name": "spanner_admin_database_v1.types",
                    "uidname": "google.cloud.spanner_admin_database_v1.types",
                    "items": [
                        {
                            "name": "Overview",
                            "uidname": "google.cloud.spanner_admin_database_v1.types",
                            "uid": "google.cloud.spanner_admin_database_v1.types",
                        },
                        {
                            "name": "BackupInfo",
                            "uidname": "google.cloud.spanner_admin_database_v1.types.BackupInfo",
                            "uid": "google.cloud.spanner_admin_database_v1.types.BackupInfo",
                        },
                    ],
                },
                {
                    "name": "pool",
                    "uidname": "google.cloud.spanner_v1.pool",
                    "items": [
                        {
                            "name": "Overview",
                            "uidname": "google.cloud.spanner_v1.pool",
                            "uid": "google.cloud.spanner_v1.pool",
                        },
                        {
                            "name": "AbstractSessionPool",
                            "uidname": "google.cloud.spanner_v1.pool.AbstractSessionPool",
                            "uid": "google.cloud.spanner_v1.pool.AbstractSessionPool",
                        },
                    ],
                },
            ],
            # expected_toc_yaml entry
            [
                {
                    "name": "Spanner Admin Database V1",
                    "uidname": "google.cloud.spanner_admin_database_v1",
                    "items": [
                        {
                            "name": "database_admin",
                            "uidname": "google.cloud.spanner_admin_database_v1.services.database_admin",
                            "items": [
                                {
                                    "name": "Overview",
                                    "uidname": "google.cloud.spanner_admin_database_v1.services.database_admin",
                                    "uid": "google.cloud.spanner_admin_database_v1.services.database_admin",
                                },
                                {
                                    "name": "ListBackupOperationsAsyncPager",
                                    "uidname": "google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsAsyncPager",
                                    "uid": "google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsAsyncPager",
                                },
                            ],
                        },
                        {
                            "name": "spanner_admin_database_v1.types",
                            "uidname": "google.cloud.spanner_admin_database_v1.types",
                            "items": [
                                {
                                    "name": "Overview",
                                    "uidname": "google.cloud.spanner_admin_database_v1.types",
                                    "uid": "google.cloud.spanner_admin_database_v1.types",
                                },
                                {
                                    "name": "BackupInfo",
                                    "uidname": "google.cloud.spanner_admin_database_v1.types.BackupInfo",
                                    "uid": "google.cloud.spanner_admin_database_v1.types.BackupInfo",
                                },
                            ],
                        },
                    ],
                },
                {
                    "name": "Spanner V1",
                    "uidname": "google.cloud.spanner_v1",
                    "items": [
                        {
                            "name": "pool",
                            "uidname": "google.cloud.spanner_v1.pool",
                            "items": [
                                {
                                    "name": "Overview",
                                    "uidname": "google.cloud.spanner_v1.pool",
                                    "uid": "google.cloud.spanner_v1.pool",
                                },
                                {
                                    "name": "AbstractSessionPool",
                                    "uidname": "google.cloud.spanner_v1.pool.AbstractSessionPool",
                                    "uid": "google.cloud.spanner_v1.pool.AbstractSessionPool",
                                },
                            ],
                        }
                    ],
                },
            ],
        ],
    ]

    @parameterized.expand(test_entries)
    def test_groups_by_package(
        self,
        toc_yaml,
        expected_toc_yaml,
    ):
        toc_yaml = extension.group_by_package(toc_yaml)

        self.assertCountEqual(toc_yaml, expected_toc_yaml)

    test_entries = [
        [
            (
                """


.. code-block:: python

\n    from google.api_core.client_options import ClientOptions
\n    from google.cloud.vision_v1 import ImageAnnotatorClient
\n    def get_client_cert():
\n        # code to load client certificate and private key.
\n        return client_cert_bytes, client_private_key_bytes
\n    options = ClientOptions(api_endpoint=\"foo.googleapis.com\",
\n        client_cert_source=get_client_cert)
\n    client = ImageAnnotatorClient(client_options=options)


You can also pass a mapping object.


\n.. code-block:: ruby

\n    from google.cloud.vision_v1 import ImageAnnotatorClient
\n    client = ImageAnnotatorClient(
\n        client_options={
\n            \"api_endpoint\": \"foo.googleapis.com\",
\n            \"client_cert_source\" : get_client_cert
\n        })
"""
            ),
            (
                """```python
from google.api_core.client_options import ClientOptions

from google.cloud.vision_v1 import ImageAnnotatorClient

def get_client_cert():

    # code to load client certificate and private key.

    return client_cert_bytes, client_private_key_bytes

options = ClientOptions(api_endpoint=\"foo.googleapis.com\",

    client_cert_source=get_client_cert)

client = ImageAnnotatorClient(client_options=options)
```

You can also pass a mapping object.

```ruby
from google.cloud.vision_v1 import ImageAnnotatorClient

client = ImageAnnotatorClient(

    client_options={

        \"api_endpoint\": \"foo.googleapis.com\",

        \"client_cert_source\" : get_client_cert

    })

```
"""
            ),
        ],
        [
            # Check that nothing changes for literalincludes.
            (
                """
.. literalinclude::
    note that these are not supported yet, so they will be ignored for now.

And any other documentation that the source code would have could go here.
"""
            ),
            (
                """
.. literalinclude::
    note that these are not supported yet, so they will be ignored for now.

And any other documentation that the source code would have could go here.

"""
            ),
        ],
        [
            # Tests notices are processed properly.
            (
                """
.. note::
\n    this is a note.


.. caution::
\n    another type of notice.


.. key-term::
\n    hyphenated term notice.
"""
            ),
            (
                """<aside class="note">
<b>Note:</b>
this is a note.
</aside>
<aside class="caution">
<b>Caution:</b>
another type of notice.
</aside>
<aside class="key-term">
<b>Key Term:</b>
hyphenated term notice.
</aside>"""
            ),
        ],
    ]

    @parameterized.expand(test_entries)
    def test_parses_docstring_summary(
        self,
        summary,
        expected_summary,
    ):
        parsed_summary, attributes, enums = extension._parse_docstring_summary(summary)
        self.assertEqual(parsed_summary, expected_summary)
        self.assertEqual(attributes, [])
        self.assertEqual(enums, [])

    test_entries = [
        [
            (
                """


.. code:: python

\nprint("This should throw an exception.")
\nfor i in range(10):
\n    print(i)
"""
            ),
            ValueError,
        ],
        [
            (
                """
.. warning::
this is not a properly formatted warning.
"""
            ),
            ValueError,
        ],
        [
            (
                """
Values:
BAD_FORMATTING (-1): this is not properly formatted enum.
"""
            ),
            ValueError,
        ],
    ]

    @parameterized.expand(test_entries)
    def test_raises_error_parsing_malformed_docstring(self, summary, error_type):
        with self.assertRaises(error_type):
            extension._parse_docstring_summary(summary)

    test_entries = [
        [
            (
                """


.. attribute:: simple name

\nsimple description

\n:type: str
"""
            ),
            [
                {
                    "id": "simple name",
                    "description": "simple description",
                    "var_type": "str",
                }
            ],
            [],
        ],
        [
            # Tests for multiple attributes.
            (
                """


.. attribute:: simple name

\nsimple description

\n:type: str


.. attribute:: table_insert_request

\nTable insert request.

\n:type: google.cloud.bigquery_logging_v1.types.TableInsertRequest
"""
            ),
            [
                {
                    "id": "simple name",
                    "description": "simple description",
                    "var_type": "str",
                },
                {
                    "id": "table_insert_request",
                    "description": "Table insert request.",
                    "var_type": "google.cloud.bigquery_logging_v1.types.TableInsertRequest",
                },
            ],
            [],
        ],
        [
            # Tests only attributes in valid format are parsed.
            (
                """


.. attribute:: table_insert_request

\nTable insert request.

\ntype: google.cloud.bigquery_logging_v1.types.TableInsertRequest


.. attribute:: proper name

\nproper description.

\n:type: str
"""
            ),
            [
                {
                    "id": "proper name",
                    "description": "proper description.",
                    "var_type": "str",
                }
            ],
            [],
        ],
        [
            # Tests enums are parsed.
            (
                """
Values:
    EMPLOYMENT_TYPE_UNSPECIFIED (0):
        The default value if the employment type isn't specified.
    FULL_TIME (1):
        The job requires working a number of hours that constitute full time
        employment, typically 40 or more hours per week.
    PART_TIME (2):
        The job entails working fewer hours than a full time job,
        typically less than 40 hours a week.
"""
            ),
            [],
            [
                {
                    "id": "EMPLOYMENT_TYPE_UNSPECIFIED",
                    "description": (
                        "The default value if the employment type isn't specified."
                    ),
                },
                {
                    "id": "FULL_TIME",
                    "description": (
                        "The job requires working a number of hours that"
                        " constitute full time employment, typically 40 or"
                        " more hours per week."
                    ),
                },
                {
                    "id": "PART_TIME",
                    "description": (
                        "The job entails working fewer hours than a full"
                        " time job, typically less than 40 hours a week."
                    ),
                },
            ],
        ],
    ]

    @parameterized.expand(test_entries)
    def test_parses_docstring_summary_for_attributes_and_enums(
        self,
        summary,
        expected_attributes,
        expected_enums,
    ):
        _, attributes, enums = extension._parse_docstring_summary(summary)

        self.assertCountEqual(attributes, expected_attributes)
        self.assertCountEqual(enums, expected_enums)

        for attribute, expected_attribute in zip(attributes, expected_attributes):
            self.assertDictEqual(attribute, expected_attribute)
        for enum, expected_enum in zip(enums, expected_enums):
            self.assertDictEqual(enum, expected_enum)

    def test_merges_markdown_and_package_toc(self):
        known_uids = {
            "acl",
            "batch",
            "blob",
            "client",
            "constants",
            "fileio",
            "hmac_key",
            "notification",
            "retry",
        }
        markdown_pages = {
            "storage": [
                {"name": "FileIO", "href": "fileio.md"},
                {"name": "Retry", "href": "retry.md"},
                {"name": "Notification", "href": "notification.md"},
                {"name": "HMAC Key Metadata", "href": "hmac_key.md"},
                {"name": "Batches", "href": "batch.md"},
                {"name": "Constants", "href": "constants.md"},
                {"name": "Storage Client", "href": "client.md"},
                {"name": "Blobs / Objects", "href": "blobs.md"},
            ],
            "acl": [
                {"name": "ACL", "href": "acl.md"},
                {"name": "ACL guide", "href": "acl_guide.md"},
            ],
            "/": [
                {"name": "Overview", "href": "index.md"},
                {"name": "Changelog", "href": "changelog.md"},
            ],
        }
        pkg_toc_yaml = [
            {
                "name": "Storage",
                "items": [
                    {
                        "name": "acl",
                        "uid": "google.cloud.storage.acl",
                        "items": [
                            {
                                "name": "Overview",
                                "uid": "google.cloud.storage.acl",
                            },
                        ],
                    },
                    {
                        "name": "batch",
                        "uid": "google.cloud.storage.batch",
                        "items": [
                            {
                                "name": "Overview",
                                "uid": "google.cloud.storage.batch",
                            },
                        ],
                    },
                    {
                        "name": "blob",
                        "uid": "google.cloud.storage.blob",
                        "items": [
                            {
                                "name": "Overview",
                                "uid": "google.cloud.storage.blob",
                            },
                        ],
                    },
                    {
                        "name": "bucket",
                        "uid": "google.cloud.storage.bucket",
                        "items": [
                            {
                                "name": "Overview",
                                "uid": "google.cloud.storage.bucket",
                            },
                        ],
                    },
                    {
                        "name": "client",
                        "uid": "google.cloud.storage.client",
                        "items": [
                            {
                                "name": "Overview",
                                "uid": "google.cloud.storage.client",
                            },
                        ],
                    },
                    {
                        "name": "constants",
                        "uid": "google.cloud.storage.constants",
                    },
                    {
                        "name": "fileio",
                        "uid": "google.cloud.storage.fileio",
                        "items": [
                            {
                                "name": "Overview",
                                "uid": "google.cloud.storage.fileio",
                            },
                        ],
                    },
                    {
                        "name": "hmac_key",
                        "uid": "google.cloud.storage.hmac_key",
                        "items": [
                            {
                                "name": "Overview",
                                "uid": "google.cloud.storage.hmac_key",
                            },
                        ],
                    },
                    {
                        "name": "notification",
                        "uid": "google.cloud.storage.notification",
                        "items": [
                            {
                                "name": "Overview",
                                "uid": "google.cloud.storage.notification",
                            },
                        ],
                    },
                    {
                        "name": "retry",
                        "uid": "google.cloud.storage.retry",
                        "items": [
                            {
                                "name": "Overview",
                                "uid": "google.cloud.storage.retry",
                            },
                        ],
                    },
                ],
            },
        ]

        added_pages, merged_pkg_toc_yaml = extension.merge_markdown_and_package_toc(
            pkg_toc_yaml, markdown_pages, known_uids
        )

        expected_merged_pkg_toc_yaml = [
            {"name": "Overview", "href": "index.md"},
            {"name": "Changelog", "href": "changelog.md"},
            {
                "name": "Storage",
                "items": [
                    {"name": "Blobs / Objects", "href": "blobs.md"},
                    {
                        "name": "acl",
                        "uid": "google.cloud.storage.acl",
                        "items": [
                            {"name": "ACL guide", "href": "acl_guide.md"},
                            {"name": "Overview", "uid": "google.cloud.storage.acl"},
                        ],
                    },
                    {
                        "name": "batch",
                        "uid": "google.cloud.storage.batch",
                        "items": [
                            {"name": "Overview", "uid": "google.cloud.storage.batch"}
                        ],
                    },
                    {
                        "name": "blob",
                        "uid": "google.cloud.storage.blob",
                        "items": [
                            {"name": "Overview", "uid": "google.cloud.storage.blob"}
                        ],
                    },
                    {
                        "name": "bucket",
                        "uid": "google.cloud.storage.bucket",
                        "items": [
                            {"name": "Overview", "uid": "google.cloud.storage.bucket"}
                        ],
                    },
                    {
                        "name": "client",
                        "uid": "google.cloud.storage.client",
                        "items": [
                            {"name": "Overview", "uid": "google.cloud.storage.client"}
                        ],
                    },
                    {"name": "constants", "uid": "google.cloud.storage.constants"},
                    {
                        "name": "fileio",
                        "uid": "google.cloud.storage.fileio",
                        "items": [
                            {"name": "Overview", "uid": "google.cloud.storage.fileio"}
                        ],
                    },
                    {
                        "name": "hmac_key",
                        "uid": "google.cloud.storage.hmac_key",
                        "items": [
                            {"name": "Overview", "uid": "google.cloud.storage.hmac_key"}
                        ],
                    },
                    {
                        "name": "notification",
                        "uid": "google.cloud.storage.notification",
                        "items": [
                            {
                                "name": "Overview",
                                "uid": "google.cloud.storage.notification",
                            }
                        ],
                    },
                    {
                        "name": "retry",
                        "uid": "google.cloud.storage.retry",
                        "items": [
                            {"name": "Overview", "uid": "google.cloud.storage.retry"}
                        ],
                    },
                ],
            },
        ]
        self.assertSetEqual(
            added_pages,
            {
                "index.md",
                "changelog.md",
                "blobs.md",
                "acl_guide.md",
            },
        )
        (
            self.assertListEqual(
                merged_pkg_toc_yaml,
                [
                    {"name": "Overview", "href": "index.md"},
                    {"name": "Changelog", "href": "changelog.md"},
                    {
                        "name": "Storage",
                        "items": [
                            {"name": "Blobs / Objects", "href": "blobs.md"},
                            {
                                "name": "acl",
                                "uid": "google.cloud.storage.acl",
                                "items": [
                                    {"name": "ACL guide", "href": "acl_guide.md"},
                                    {
                                        "name": "Overview",
                                        "uid": "google.cloud.storage.acl",
                                    },
                                ],
                            },
                            {
                                "name": "batch",
                                "uid": "google.cloud.storage.batch",
                                "items": [
                                    {
                                        "name": "Overview",
                                        "uid": "google.cloud.storage.batch",
                                    }
                                ],
                            },
                            {
                                "name": "blob",
                                "uid": "google.cloud.storage.blob",
                                "items": [
                                    {
                                        "name": "Overview",
                                        "uid": "google.cloud.storage.blob",
                                    }
                                ],
                            },
                            {
                                "name": "bucket",
                                "uid": "google.cloud.storage.bucket",
                                "items": [
                                    {
                                        "name": "Overview",
                                        "uid": "google.cloud.storage.bucket",
                                    }
                                ],
                            },
                            {
                                "name": "client",
                                "uid": "google.cloud.storage.client",
                                "items": [
                                    {
                                        "name": "Overview",
                                        "uid": "google.cloud.storage.client",
                                    }
                                ],
                            },
                            {
                                "name": "constants",
                                "uid": "google.cloud.storage.constants",
                            },
                            {
                                "name": "fileio",
                                "uid": "google.cloud.storage.fileio",
                                "items": [
                                    {
                                        "name": "Overview",
                                        "uid": "google.cloud.storage.fileio",
                                    }
                                ],
                            },
                            {
                                "name": "hmac_key",
                                "uid": "google.cloud.storage.hmac_key",
                                "items": [
                                    {
                                        "name": "Overview",
                                        "uid": "google.cloud.storage.hmac_key",
                                    }
                                ],
                            },
                            {
                                "name": "notification",
                                "uid": "google.cloud.storage.notification",
                                "items": [
                                    {
                                        "name": "Overview",
                                        "uid": "google.cloud.storage.notification",
                                    }
                                ],
                            },
                            {
                                "name": "retry",
                                "uid": "google.cloud.storage.retry",
                                "items": [
                                    {
                                        "name": "Overview",
                                        "uid": "google.cloud.storage.retry",
                                    }
                                ],
                            },
                        ],
                    },
                ],
            ),
        )

    def test_get_class_lines(self):
        source = (
            "class TopLevel:\n"  # line 1
            "    pass\n"
            "\n"
            "@dec1\n"  # line 4
            "@dec2\n"  # line 5
            "class Decorated:\n"  # line 6
            "    class Nested:\n"  # line 7
            "        pass\n"
            "\n"
            "    @nested_dec\n"  # line 10
            "    class DecoratedNested:\n"  # line 11
            "        pass\n"
            "\n"
            "def factory():\n"  # line 14
            "    class LocalClass:\n"  # line 15
            "        pass\n"
            "\n"
            "async def async_factory():\n"  # line 18
            "    @local_dec\n"  # line 19
            "    class AsyncLocalClass:\n"  # line 20
            "        pass\n"
        )
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False
        ) as tmp_file:
            tmp_file.write(source)
            tmp_path = tmp_file.name

        try:
            extension._get_class_lines.cache_clear()
            class_lines = extension._get_class_lines(tmp_path)
            self.assertEqual(
                class_lines,
                {
                    "TopLevel": 1,
                    "Decorated": 4,
                    "Decorated.Nested": 7,
                    "Decorated.DecoratedNested": 10,
                    "factory.<locals>.LocalClass": 15,
                    "async_factory.<locals>.AsyncLocalClass": 19,
                },
            )
            # Non-existent file returns empty dict without raising.
            self.assertEqual(
                extension._get_class_lines(tmp_path + ".missing"),
                {},
            )
        finally:
            Path(tmp_path).unlink(missing_ok=True)

    def test_transform_node_does_not_mutate_live_doctree_or_pending_xref(self):
        app = mock.MagicMock()

        def fake_resolve_references(doctree, fromdocname, builder):
            for xref in list(doctree.traverse(addnodes.pending_xref)):
                ref = nodes.reference("", "", refuri=xref["reftarget"])
                ref.append(nodes.Text(xref.astext()))
                xref.replace_self(ref)

        app.env.resolve_references.side_effect = fake_resolve_references

        # 1. Detached node without pending_xref skips resolve_references.
        plain_node = nodes.paragraph("", "Plain text")
        self.assertEqual(utils.transform_node(app, plain_node).strip(), "Plain text")
        app.env.resolve_references.assert_not_called()

        # 2. Live doctree node with nested pending_xref is deep-copied so
        # neither its parent pointer nor its nested pending_xref child is mutated.
        live_parent = nodes.section()
        live_para = nodes.paragraph("", "See ")
        live_xref = addnodes.pending_xref(
            "",
            nodes.literal("", "Client"),
            refdomain="py",
            reftype="class",
            reftarget="google.cloud.Client",
        )
        live_para.append(live_xref)
        live_parent.append(live_para)

        rendered = utils.transform_node(app, live_para)

        app.env.resolve_references.assert_called_once()
        self.assertIs(live_para.parent, live_parent)
        self.assertIn(live_xref, live_para.children)
        self.assertIs(live_xref.parent, live_para)
        self.assertEqual(rendered.strip(), "See <xref:google.cloud.Client>")

    def test_run_sphinx_markdown(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            html_outdir = Path(tmp_dir) / "html"
            html_outdir.mkdir()
            markdown_outdir = Path(tmp_dir) / "markdown"

            orig_builder = mock.MagicMock()
            orig_builder.outdir = str(html_outdir)

            app = mock.MagicMock()
            app.builder = orig_builder
            app.env.found_docs = {"b_doc", "a_doc"}

            doctree_a = mock.sentinel.doctree_a
            doctree_b = mock.sentinel.doctree_b
            app.env.get_and_resolve_doctree.side_effect = [doctree_a, doctree_b]

            observed_builders = []

            def record_builder(docname, doctree):
                observed_builders.append((docname, doctree, app.builder))

            with (
                mock.patch("os.getcwd", return_value="/tmp/work"),
                mock.patch(
                    "sphinx_markdown_builder.markdown_builder.MarkdownBuilder"
                ) as mock_md_builder_cls,
            ):
                mock_md_builder = mock_md_builder_cls.return_value
                mock_md_builder.write_doc.side_effect = record_builder

                markdown_utils.run_sphinx_markdown(app)

                mock_md_builder_cls.assert_called_once_with(app)
                self.assertEqual(mock_md_builder.outdir, str(markdown_outdir))
                mock_md_builder.set_environment.assert_called_once_with(app.env)
                mock_md_builder.init.assert_called_once_with()
                mock_md_builder.prepare_writing.assert_called_once_with(
                    ["a_doc", "b_doc"]
                )
                self.assertEqual(
                    observed_builders,
                    [
                        ("a_doc", doctree_a, mock_md_builder),
                        ("b_doc", doctree_b, mock_md_builder),
                    ],
                )
                # Original builder is restored after run_sphinx_markdown completes.
                self.assertIs(app.builder, orig_builder)

                # Subsequent call when markdown_outdir already exists is a no-op.
                mock_md_builder_cls.reset_mock()
                markdown_utils.run_sphinx_markdown(app)
                mock_md_builder_cls.assert_not_called()

    def test_convert_cross_references_fast_path_checks_both_ends(self):
        # All UIDs start with "google." and content has no "google." -> fast-path.
        all_google_uids = ["google.cloud.storage.Client", "google.api_core.Retry"]
        content_no_google = "Plain description with custom_pkg.Client reference."
        self.assertEqual(
            extension.convert_cross_references(
                content_no_google,
                "google.cloud.storage.Blob",
                all_google_uids,
            ),
            content_no_google,
        )

        # Mixed sorted list where known_uids[0] starts with "google." but
        # known_uids[-1] does not -> must NOT skip non-google references.
        mixed_uids = ["google.cloud.storage.Client", "custom_pkg.Client"]
        self.assertEqual(
            extension.convert_cross_references(
                content_no_google,
                "google.cloud.storage.Blob",
                mixed_uids,
            ),
            'Plain description with <xref uid="custom_pkg.Client">custom_pkg.Client</xref> reference.',
        )


if __name__ == "__main__":
    unittest.main()
