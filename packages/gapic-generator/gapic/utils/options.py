# Copyright 2019 Google LLC
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

from collections import defaultdict
from os import path
from typing import Any, DefaultDict, Dict, FrozenSet, List, Optional, Tuple

import dataclasses
import json
import os
import warnings
import yaml

from gapic.samplegen_utils import utils as samplegen_utils


@dataclasses.dataclass(frozen=True)
class Options:
    """A representation of CLI options passed through protoc.

    To maximize interoperability with other languages, we are permissive
    on unrecognized arguments (essentially, we throw them away, but we do
    warn if it looks like it was meant for us).
    """

    name: str = ""
    namespace: Tuple[str, ...] = dataclasses.field(default=())
    warehouse_package_name: str = ""
    retry: Optional[Dict[str, Any]] = None
    sample_configs: Tuple[str, ...] = dataclasses.field(default=())
    autogen_snippets: bool = True
    templates: Tuple[str, ...] = dataclasses.field(default=("DEFAULT",))
    lazy_import: bool = False
    old_naming: bool = False
    add_iam_methods: bool = False
    metadata: bool = False
    # TODO(yon-mg): should there be an enum for transport type?
    transport: List[str] = dataclasses.field(default_factory=lambda: [])
    service_yaml_config: Dict[str, Any] = dataclasses.field(default_factory=dict)
    rest_numeric_enums: bool = False
    proto_plus_deps: Tuple[str, ...] = dataclasses.field(default=("",))
    gapic_version: str = "0.0.0"
    resource_name_aliases: Dict[str, str] = dataclasses.field(default_factory=dict)
    resumable_upload_prefix: str = "resumable/upload"

    # Class constants
    PYTHON_GAPIC_PREFIX: str = "python-gapic-"
    OPT_FLAGS: FrozenSet[str] = frozenset(
        (
            "add-iam-methods",  # microgenerator implementation for `reroute_to_grpc_interface`
            "lazy-import",
            "metadata",  # generate GAPIC metadata JSON file
            "old-naming",  # TODO(dovs): Come up with a better comment
            "retry-config",  # takes a path
            "service-yaml",  # takes a path
            "samples",  # output dir
            "autogen-snippets",  # produce auto-generated snippets
            # transport type(s) delineated by '+' (i.e. grpc, rest, custom.[something], etc?)
            "transport",
            "warehouse-package-name",  # change the package name on PyPI
            # when transport includes "rest", request that response enums be JSON-encoded as numbers
            "rest-numeric-enums",
            # proto plus dependencies delineated by '+'
            # For example, 'google.cloud.api.v1+google.cloud.anotherapi.v2'
            "proto-plus-deps",
            "gapic-version",  # A version string following https://peps.python.org/pep-0440,
            # Resolves method name collisions by mapping a fully qualified 
            # resource path to a custom TitleCase alias.
            # Format: resource.path/Name:AliasName
            "resource-name-alias",
            # Prefix for resumable upload requests
            "resumable-upload-prefix",
        )
    )

    @classmethod
    def build(cls, opt_string: str) -> "Options":
        """Build an Options instance based on a protoc opt string.

        Args:
            opt_string (str): A string, as passed from the protoc interface
                (through ``--python_gapic_opt``). If multiple options are
                passed, then protoc joins the values with ``,``.
                By convention, we use ``key=value`` strings for such
                options, with an absent value defaulting to ``True``.

        Returns:
            ~.Options: The Options instance.

        Raises:
            gapic.samplegen_utils.types.InvalidConfig:
                If paths to files or directories that should contain sample
                configs are passed and no valid sample config is found.
        """
        # Parse out every option beginning with `python-gapic`
        opts: DefaultDict[str, List[str]] = defaultdict(list)
        for opt in opt_string.split(","):
            opt = opt.strip()
            # Parse out the key and value.
            value = "true"
            if "=" in opt:
                opt, value = opt.split("=")

            # Save known, expected keys.
            if opt in cls.OPT_FLAGS:
                opts[opt].append(value)

            # Throw away other options not meant for us.
            if not opt.startswith(cls.PYTHON_GAPIC_PREFIX):
                continue

            # Set the option, using a key with the "python-gapic-" prefix
            # stripped.
            #
            # Just assume everything is a list at this point, and the
            # final instantiation step can de-list-ify where appropriate.
            opts[opt[len(cls.PYTHON_GAPIC_PREFIX) :]].append(value)

        # If templates are specified, one of the specified directories
        # may be our default; perform that replacement.
        default_token = "DEFAULT"
        templates = opts.pop("templates", [default_token])
        pwd = path.join(path.dirname(__file__), "..")
        default_path = path.realpath(path.join(pwd, "templates"))

        def tweak_path(p):
            if p == default_token:
                return default_path

            if path.isabs(p):
                return path.normpath(p)

            return path.normpath(path.join(pwd, p))

        templates = [tweak_path(p) for p in templates]

        retry_cfg = None
        retry_paths = opts.pop("retry-config", None)
        if retry_paths:
            # Just use the last config specified.
            with open(retry_paths[-1]) as f:
                retry_cfg = json.load(f)

        service_yaml_config = {}
        service_yaml_paths = opts.pop("service-yaml", None)
        if service_yaml_paths:
            # Just use the last file specified.
            with open(service_yaml_paths[-1]) as f:
                service_yaml_config = yaml.safe_load(f)
        # The yaml service files typically have this field,
        # but it is not a field in the gogle.api.Service proto.
        service_yaml_config.pop("type", None)

        # Build the options instance.
        sample_paths = opts.pop("samples", [])

        # autogen-snippets is True by default, so make sure users can disable
        # by passing `autogen-snippets=false`
        autogen_snippets = opts.pop("autogen-snippets", ["True"])[0] in (
            "True",
            "true",
            "T",
            "t",
            "TRUE",
        )

        # `rest-numeric-enums` is False by default. Make sure users can also disable
        # it by passing `rest-numeric-enums=False`.
        rest_numeric_enums = opts.pop("rest-numeric-enums", ["False"])[0] in (
            "True",
            "true",
            "T",
            "t",
            "TRUE",
        )

        # NOTE: Snippets are not currently correct for the alternative (Ads) templates
        # so always disable snippetgen in that case
        # https://github.com/googleapis/gapic-generator-python/issues/1052
        old_naming = bool(opts.pop("old-naming", False))
        if old_naming:
            autogen_snippets = False

        proto_plus_deps = tuple(opts.pop("proto-plus-deps", ""))
        if len(proto_plus_deps):
            proto_plus_deps = tuple(proto_plus_deps[0].split("+"))

        # Parse the resource name aliases dictionary (Format: "path/to/Resource:AliasName")
        resource_name_aliases = {}
        raw_aliases = opts.pop("resource-name-alias", [])
            
        # Parse explicitly and safely
        for mapping in raw_aliases:
            if not mapping:
                # We only need to check `not mapping` because the top-level 
                # opt_string parser already stripped trailing whitespaces
                continue
                
            try:
                # split(":", 1) ensures we only split on the FIRST colon 
                res_path, alias_name = mapping.split(":", 1)
                
                clean_path = res_path.strip()
                clean_alias = alias_name.strip()
                
                if not clean_path or not clean_alias:
                    raise ValueError()
                    
                resource_name_aliases[clean_path] = clean_alias
                
            except ValueError:
                warnings.warn(
                    f"Ignored malformed resource-name-alias: '{mapping}'. "
                    "Expected format is 'resource.path/Name:AliasName'."
                )

        resumable_upload_prefix = opts.pop("resumable-upload-prefix", ["resumable/upload"]).pop()

        answer = Options(
            name=opts.pop("name", [""]).pop(),
            namespace=tuple(opts.pop("namespace", [])),
            warehouse_package_name=opts.pop("warehouse-package-name", [""]).pop(),
            retry=retry_cfg,
            sample_configs=tuple(
                cfg_path
                for s in sample_paths
                for cfg_path in samplegen_utils.generate_all_sample_fpaths(s)
            ),
            autogen_snippets=autogen_snippets,
            templates=tuple(path.expanduser(i) for i in templates),
            lazy_import=bool(opts.pop("lazy-import", False)),
            old_naming=old_naming,
            add_iam_methods=bool(opts.pop("add-iam-methods", False)),
            metadata=bool(opts.pop("metadata", False)),
            # transport should include desired transports delimited by '+', e.g. transport='grpc+rest'
            transport=opts.pop("transport", ["grpc"])[0].split("+"),
            service_yaml_config=service_yaml_config,
            rest_numeric_enums=rest_numeric_enums,
            proto_plus_deps=proto_plus_deps,
            gapic_version=opts.pop("gapic-version", ["0.0.0"]).pop(),
            resource_name_aliases=resource_name_aliases,
            resumable_upload_prefix=resumable_upload_prefix,
        )

        # Note: if we ever need to recursively check directories for sample
        # configs, check that at least _one_ config is read in.

        # If there are any options remaining, then we failed to recognize
        # them -- complain.
        for key in opts.keys():
            warnings.warn(f"Unrecognized option: `python-gapic-{key}`.")

        # Done; return the built options.
        return answer
