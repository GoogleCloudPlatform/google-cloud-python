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

import pytest

from google.api_core import _feature_gating_helpers
from google.api_core._feature_gating_helpers import (
    FeatureGatingError,
    _get_env_bool,
    _strtobool,
)


@pytest.mark.parametrize(
    "value,expected",
    [
        # Truthy values
        ("y", True),
        ("yes", True),
        ("t", True),
        ("true", True),
        ("on", True),
        ("1", True),
        ("  True  ", True),
        # Falsy values
        ("n", False),
        ("no", False),
        ("f", False),
        ("false", False),
        ("off", False),
        ("0", False),
        (" FALSE ", False),
        # Empty string
        ("", None),
    ],
)
def test_strtobool(value, expected):
    assert _strtobool(value) is expected


def test_strtobool_invalid():
    with pytest.raises(ValueError):
        _strtobool("invalid")


def test_get_env_bool(monkeypatch):
    monkeypatch.setenv("TEST_VAR", "true")
    assert _get_env_bool("TEST_VAR") is True

    monkeypatch.setenv("TEST_VAR", "invalid")
    import pytest

    with pytest.warns(RuntimeWarning, match="Ignored invalid value"):
        assert _get_env_bool("TEST_VAR") is None

    monkeypatch.delenv("TEST_VAR", raising=False)
    assert _get_env_bool("TEST_VAR") is None


def test_resolve_feature_flags_ga_enabled_via_env(monkeypatch):
    """Verify that a GA feature is enabled if its environment variable is True."""
    # Setup: We pass a GA environment variable set to True
    monkeypatch.setenv("GOOGLE_SDK_PYTHON_TRACING_ENABLED", "true")

    # Action
    result = _feature_gating_helpers.resolve_feature_flags(
        env_var="GOOGLE_SDK_PYTHON_TRACING_ENABLED",
        feature_key="tracer_provider",
        configuration=None,
    )

    # Assertion
    assert result is True


@pytest.mark.parametrize("exp_env_state", [None, "false"], ids=["missing", "disabled"])
def test_resolve_feature_flags_exp_blocked_with_feature_key_fails_fast(
    monkeypatch, exp_env_state
):
    """Verify that passing a feature_key to an experimental feature raises FeatureGatingError if the experimental environment variable is disabled or missing."""
    # Setup: Experimental env var is set to exp_env_state (None means not set)
    if exp_env_state is not None:
        monkeypatch.setenv(
            "GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", exp_env_state
        )
    else:
        monkeypatch.delenv(
            "GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", raising=False
        )
    configuration = {"tracer_provider": object()}

    # Action & Assertion
    with pytest.raises(FeatureGatingError, match="Experimental feature"):
        _feature_gating_helpers.resolve_feature_flags(
            env_var="GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED",
            feature_key="tracer_provider",
            configuration=configuration,
        )


def test_resolve_feature_flags_exp_enabled_with_feature_key(monkeypatch):
    """Verify that experimental feature is enabled if the experimental environment variable is enabled and a feature_key is provided."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")
    configuration = {"tracer_provider": object()}

    result = _feature_gating_helpers.resolve_feature_flags(
        env_var="GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED",
        feature_key="tracer_provider",
        configuration=configuration,
    )
    assert result is True


def test_resolve_feature_flags_exp_enabled_without_feature_key(monkeypatch):
    """Verify that experimental feature is enabled if the experimental environment variable is enabled and NO feature_key is provided."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    result = _feature_gating_helpers.resolve_feature_flags(
        env_var="GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED",
        feature_key="tracer_provider",
        configuration=None,
    )
    assert result is True


def test_resolve_feature_flags_exp_disabled_without_feature_key(monkeypatch):
    """Verify that experimental feature is disabled if the experimental environment variable is disabled and NO feature_key is provided."""
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "false")

    result = _feature_gating_helpers.resolve_feature_flags(
        env_var="GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED",
        feature_key="tracer_provider",
        configuration=None,
    )
    assert result is False


def test_resolve_feature_flags_ga_enabled_via_feature_key(monkeypatch):
    """Verify that a GA feature is enabled if a feature_key is provided, ignoring the environment variable."""
    # Env var is False, but feature_key is present in configuration
    monkeypatch.setenv("GOOGLE_SDK_PYTHON_TRACING_ENABLED", "false")
    configuration = {"tracer_provider": object()}

    result = _feature_gating_helpers.resolve_feature_flags(
        env_var="GOOGLE_SDK_PYTHON_TRACING_ENABLED",
        feature_key="tracer_provider",
        configuration=configuration,
    )
    assert result is True


@pytest.mark.parametrize(
    "env_val", [None, "false"], ids=["env_not_set", "env_explicit_false"]
)
def test_resolve_feature_flags_ga_fallback_to_false(monkeypatch, env_val):
    """Verify that a GA feature is disabled if neither a feature_key is provided nor the environment variable is enabled."""
    if env_val is not None:
        monkeypatch.setenv("GOOGLE_SDK_PYTHON_TRACING_ENABLED", env_val)
    else:
        monkeypatch.delenv("GOOGLE_SDK_PYTHON_TRACING_ENABLED", raising=False)
    result = _feature_gating_helpers.resolve_feature_flags(
        env_var="GOOGLE_SDK_PYTHON_TRACING_ENABLED",
        feature_key="tracer_provider",
        configuration=None,
    )
    assert result is False


class _MockOptions:
    def __init__(self):
        self.other_option = "value"


@pytest.mark.parametrize(
    "configuration",
    [
        {"other_option": "value"},
        _MockOptions(),
    ],
    ids=["dict_without_key", "object_without_key"],
)
def test_resolve_feature_flags_options_without_key(configuration):
    """Verify behavior when configuration is present but missing the feature key."""
    # GA Path: should fall through to env var / fallback
    result = _feature_gating_helpers.resolve_feature_flags(
        env_var="GOOGLE_SDK_PYTHON_TRACING_ENABLED",
        feature_key="tracer_provider",
        configuration=configuration,
    )
    assert result is False


def test_resolve_feature_flags_rejects_dunder_keys(monkeypatch):
    """Verify that dunder keys are rejected early in _has_feature_key."""
    # We use a dunder key that exists on all objects (__class__)
    # If the guardrail is missing, getattr might return it and return True
    configuration = {"__class__": "some_value"}

    result = _feature_gating_helpers.resolve_feature_flags(
        env_var="GOOGLE_SDK_PYTHON_TRACING_ENABLED",
        feature_key="__class__",
        configuration=configuration,
    )
    assert result is False

    class MockWithClass:
        __class__ = "some_value"

    result = _feature_gating_helpers.resolve_feature_flags(
        env_var="GOOGLE_SDK_PYTHON_TRACING_ENABLED",
        feature_key="__class__",
        configuration=MockWithClass(),
    )
    assert result is False
