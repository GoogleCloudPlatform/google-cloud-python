# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
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
#

"""Observability environment variable and client options resolution helpers."""

import os
import warnings
from typing import Any

# We import ClientOptions for type hinting
from google.api_core.client_options import ClientOptions

# Allowed truthy and falsy patterns for environment variables
_TRUTHY_VALUES = ("y", "yes", "t", "true", "on", "1")
_FALSY_VALUES = ("n", "no", "f", "false", "off", "0")


class FeatureGatingError(ValueError):
    """Raised when feature gating resolution fails or is misconfigured."""

    pass


def _strtobool(val: str) -> bool | None:
    """Convert a string representation of truth to a boolean."""
    clean_val = val.lower().strip()
    if not clean_val:
        return None
    if clean_val in _TRUTHY_VALUES:
        return True
    if clean_val in _FALSY_VALUES:
        return False
    raise ValueError(f"Invalid truth value: {val!r}")


def _get_env_bool(name: str) -> bool | None:
    """Retrieve the boolean value of an environment variable."""
    val = os.getenv(name)
    if val is None:
        return None
    try:
        return _strtobool(val)
    except ValueError as e:
        warnings.warn(f"Ignored invalid value for {name}: {e}", RuntimeWarning)
        return None


def _has_feature_key(
    *, configuration: ClientOptions | dict[str, Any] | None, feature_key: str
) -> bool:
    """Checks if a specific feature key is present and not None in configuration."""
    if configuration is None:
        return False

    if feature_key.startswith("__"):
        return False

    if isinstance(configuration, dict):
        return configuration.get(feature_key) is not None

    return getattr(configuration, feature_key, None) is not None


def resolve_feature_flags(
    *,
    env_var: str,
    feature_key: str,
    configuration: ClientOptions | dict[str, Any] | None = None,
) -> bool:
    """Determines if a feature is enabled based on environment variables and configuration.

    Behavior depends on whether the `env_var` name contains "EXPERIMENTAL":

    - **Experimental Path** (env_var contains "EXPERIMENTAL"):
      Strict control. Requires the environment variable to be explicitly 'true'.
      If a programmatic feature key is passed but the environment variable is not 'true',
      raises FeatureGatingError (Fail Fast).

    - **GA Path** (env_var does not contain "EXPERIMENTAL"):
      Standard precedence. Enabled if a programmatic feature key is passed,
      otherwise falls back to the environment variable value.

    Args:
        env_var: The name of the environment variable controlling this feature.
        feature_key: The key in configuration/attributes for the programmatic configuration.
        configuration: Optional. A dictionary or object containing client configuration.

    Returns:
        bool: True if the feature is resolved to enabled, False otherwise.

    Raises:
        FeatureGatingError: If a feature key is provided for an experimental feature without enabling the experimental environment variable.
    """

    # Check for programmatic feature configuration
    has_feature_key = _has_feature_key(
        configuration=configuration, feature_key=feature_key
    )

    # Read environment variable
    env_var_setting = _get_env_bool(env_var)

    # EXPERIMENTAL PATH:
    # Resolution Hierarchy:
    #   1. EXPERIMENTAL Environment Variable
    #   2. Fail Fast if Feature Key present but EXPERIMENTAL Environment Variable is not enabled
    if "EXPERIMENTAL" in env_var:
        # Fail Fast if feature key present but experimental environment variable is not enabled
        if env_var_setting is not True and has_feature_key:
            raise FeatureGatingError(
                f"Experimental feature requires {env_var} to be set to 'true' to use programmatic configuration."
            )

        return bool(env_var_setting)

    # GENERAL AVAILABILITY PATH:
    # Resolution Hierarchy:
    #   1. Programmatic Configuration (Feature Key)
    #   2. Environment Variable

    # Check Programmatic Configuration
    if has_feature_key:
        return True

    # Check Environment Variable
    return bool(env_var_setting)
