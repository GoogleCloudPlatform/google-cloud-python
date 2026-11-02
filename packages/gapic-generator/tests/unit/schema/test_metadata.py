# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import typing

from google.protobuf import descriptor_pb2

from test_utils.test_utils import make_doc_meta

from gapic.schema import metadata
from gapic.schema import naming
from gapic.utils import RESERVED_NAMES


def test_address_str():
    addr = metadata.Address(package=("foo", "bar"), module="baz", name="Bacon")
    assert str(addr) == "baz.Bacon"


def test_address_str_with_context():
    addr = metadata.Address(
        package=("foo", "bar"),
        module="baz",
        name="Bacon",
    ).with_context(collisions=frozenset({"baz"}))
    assert str(addr) == "fb_baz.Bacon"


def test_address_str_parent():
    addr = metadata.Address(
        package=("foo", "bar"), module="baz", name="Bacon", parent=("spam", "eggs")
    )
    assert str(addr) == "baz.spam.eggs.Bacon"


def test_address_str_different_proto_package():
    addr = metadata.Address(
        package=("google", "iam", "v1"),
        module="options",
        name="GetPolicyOptions",
        api_naming=naming.NewNaming(proto_package="foo.bar.baz.v1"),
    )
    assert str(addr) == "options_pb2.GetPolicyOptions"


def test_address_str_different_proto_package_with_collision():
    addr = metadata.Address(
        package=("google", "rpc"),
        module="status",
        name="Status",
        api_naming=naming.NewNaming(proto_package="foo.bar.baz.v1"),
    ).with_context(collisions=frozenset({"status"}))
    # the module alias should be ignored for _pb2 types
    assert str(addr) == "status_pb2.Status"


def test_address_proto():
    addr = metadata.Address(package=("foo", "bar"), module="baz", name="Bacon")
    assert addr.proto == "foo.bar.Bacon"
    assert addr.proto_package == "foo.bar"


def test_proto_package_version_parsing():
    addr = metadata.Address(package=("baa"))
    assert addr.convert_to_versioned_package() == ("baa")

    addr = metadata.Address(package=("bab", "v1"))
    assert addr.convert_to_versioned_package() == ("bab_v1",)

    addr = metadata.Address(package=("bac", "v10"))
    assert addr.convert_to_versioned_package() == ("bac_v10",)

    addr = metadata.Address(package=("bad", "v2beta"))
    assert addr.convert_to_versioned_package() == ("bad_v2beta",)

    addr = metadata.Address(package=("bae", "v2beta20"))
    assert addr.convert_to_versioned_package() == ("bae_v2beta20",)

    addr = metadata.Address(package=("baf", "v20beta"))
    assert addr.convert_to_versioned_package() == ("baf_v20beta",)

    addr = metadata.Address(package=("bag", "v20p1"))
    assert addr.convert_to_versioned_package() == ("bag_v20p1",)

    addr = metadata.Address(package=("bah", "v20p1alpha3p5"))
    assert addr.convert_to_versioned_package() == ("bah_v20p1alpha3p5",)

    addr = metadata.Address(package=("bai", "v20p1"))
    assert addr.convert_to_versioned_package() == ("bai_v20p1",)

    addr = metadata.Address(package=("bah", "v20p1", "baj", "v3"))
    assert addr.convert_to_versioned_package() == ("bah", "v20p1", "baj_v3")

    addr = metadata.Address(package=("bab", "v1"))
    assert addr.proto_package_versioned == "bab_v1"

    addr = metadata.Address(package=("bah", "v20p1", "baj", "v3"))
    assert addr.proto_package_versioned == "bah.v20p1.baj_v3"


def test_address_child_no_parent():
    addr = metadata.Address(package=("foo", "bar"), module="baz")
    child = addr.child("Bacon", path=(4, 0))
    assert child.name == "Bacon"
    assert child.parent == ()
    assert child.module_path == (4, 0)


def test_address_child_with_parent():
    addr = metadata.Address(package=("foo", "bar"), module="baz")
    child = addr.child("Bacon", path=(4, 0))
    grandchild = child.child("Ham", path=(2, 0))
    assert grandchild.parent == ("Bacon",)
    assert grandchild.name == "Ham"
    assert grandchild.module_path == (4, 0, 2, 0)


def test_address_rel():
    addr = metadata.Address(package=("foo", "bar"), module="baz", name="Bacon")
    assert (
        addr.rel(
            metadata.Address(package=("foo", "bar"), module="baz"),
        )
        == "'Bacon'"
    )


def test_address_rel_other():
    addr = metadata.Address(package=("foo", "bar"), module="baz", name="Bacon")
    assert (
        addr.rel(
            metadata.Address(package=("foo", "not_bar"), module="baz"),
        )
        == "baz.Bacon"
    )
    assert (
        addr.rel(
            metadata.Address(package=("foo", "bar"), module="not_baz"),
        )
        == "baz.Bacon"
    )


def test_address_rel_later():
    addr = metadata.Address(
        module="baz",
        module_path=(4, 1),
        name="Bacon",
        package=("foo", "bar"),
    )
    other = metadata.Address(
        module="baz",
        module_path=(4, 0),
        name="Ham",
        package=("foo", "bar"),
    )
    assert addr.rel(other) == "'Bacon'"


def test_address_rel_nested_sibling():
    addr = metadata.Address(
        module="baz", name="Bacon", package=("foo", "bar"), parent=("Spam",)
    )
    other = metadata.Address(
        module="baz", name="Ham", package=("foo", "bar"), parent=("Spam",)
    )
    assert addr.rel(other) == "'Spam.Bacon'"


def test_address_rel_nested_sibling_later():
    addr = metadata.Address(
        module="baz",
        name="Bacon",
        module_path=(4, 0, 3, 1),
        package=("foo", "bar"),
        parent=("Spam",),
    )
    other = metadata.Address(
        module="baz",
        name="Ham",
        module_path=(4, 0, 3, 0),
        package=("foo", "bar"),
        parent=("Spam",),
    )
    assert addr.rel(other) == "'Spam.Bacon'"


def test_address_rel_nested_parent():
    parent = metadata.Address(module="baz", name="Ham", package=("foo", "bar"))
    child = metadata.Address(
        module="baz", name="Bacon", package=("foo", "bar"), parent=("Ham",)
    )
    assert child.rel(parent) == "Bacon"


def test_address_resolve():
    addr = metadata.Address(package=("foo", "bar"), module="baz", name="Qux")
    assert addr.resolve("Bacon") == "foo.bar.Bacon"
    assert addr.resolve("foo.bar.Bacon") == "foo.bar.Bacon"
    assert addr.resolve("google.example.Bacon") == "google.example.Bacon"


def test_address_subpackage():
    addr = metadata.Address(
        package=("foo", "bar", "baz", "v1", "spam", "eggs"),
        api_naming=naming.NewNaming(proto_package="foo.bar.baz.v1"),
    )
    assert addr.subpackage == ("spam", "eggs")


def test_address_subpackage_no_version():
    addr = metadata.Address(
        package=("foo", "bar", "baz", "spam", "eggs"),
        api_naming=naming.NewNaming(proto_package="foo.bar.baz"),
    )
    assert addr.subpackage == ("spam", "eggs")


def test_address_subpackage_empty():
    addr = metadata.Address(
        package=("foo", "bar", "baz", "v1"),
        api_naming=naming.NewNaming(proto_package="foo.bar.baz.v1"),
    )
    assert addr.subpackage == ()


def test_metadata_with_context():
    meta = metadata.Metadata()
    collisions = (
        meta.with_context(
            collisions={"foo", "bar"},
        ).address.collisions
        - RESERVED_NAMES
    )
    assert collisions == {"foo", "bar"}


def test_address_name_builtin_keyword():
    addr_builtin = metadata.Address(
        name="Any",
        module="any",
        package=("google", "protobuf"),
        api_naming=naming.NewNaming(proto_package="foo.bar.baz.v1"),
    )
    assert addr_builtin.module_alias == "gp_any"

    addr_kword = metadata.Address(
        name="Class",
        module="class",
        package=("google", "protobuf"),
        api_naming=naming.NewNaming(proto_package="foo.bar.baz.v1"),
    )
    assert addr_kword.module_alias == "gp_class"

    addr_kword = metadata.Address(
        name="Class",
        module="class",
        package=("google", "appengine_admin"),
        api_naming=naming.NewNaming(proto_package="foo.bar.baz.v1"),
    )
    assert addr_kword.module_alias == "gaa_class"


def test_doc_nothing():
    meta = metadata.Metadata()
    assert meta.doc == ""


def test_doc_leading_trumps_all():
    meta = make_doc_meta(leading="foo", trailing="bar", detached=["baz"])
    assert meta.doc == "foo"


def test_doc_trailing_trumps_detached():
    meta = make_doc_meta(trailing="spam", detached=["eggs"])
    assert meta.doc == "spam"


def test_doc_detached_joined():
    meta = make_doc_meta(detached=["foo", "bar"])
    assert meta.doc == "foo\n\nbar"
