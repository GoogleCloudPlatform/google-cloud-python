# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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

from google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory import (
    SpannerMetricsTracerFactory,
)

pytest.importorskip("opentelemetry")


class TestSpannerMetricsTracerFactory:
    def test_new_instance_creation(self):
        factory1 = SpannerMetricsTracerFactory(enabled=True)
        factory2 = SpannerMetricsTracerFactory(enabled=True)
        assert factory1 is factory2  # Should return the same instance

    def test_generate_client_uid_format(self):
        client_uid = SpannerMetricsTracerFactory._generate_client_uid()
        assert isinstance(client_uid, str)
        assert len(client_uid.split("@")) == 3  # Should contain uuid, pid, and hostname

    def test_generate_client_hash(self):
        client_uid = "123e4567-e89b-12d3-a456-426614174000@1234@hostname"
        client_hash = SpannerMetricsTracerFactory._generate_client_hash(client_uid)
        assert isinstance(client_hash, str)
        assert len(client_hash) == 6  # Should be a 6-digit hex string

    def test_get_instance_config(self):
        instance_config = SpannerMetricsTracerFactory._get_instance_config()
        assert instance_config == "unknown"  # As per the current implementation

    def test_get_client_name(self):
        client_name = SpannerMetricsTracerFactory._get_client_name()
        assert isinstance(client_name, str)

    def test_singleton_enabled_toggle(self):
        factory = SpannerMetricsTracerFactory(enabled=True)
        assert factory.enabled is True
        factory_disabled = SpannerMetricsTracerFactory(enabled=False)
        assert factory_disabled is factory
        assert factory.enabled is False
        factory_re_enabled = SpannerMetricsTracerFactory(enabled=True)
        assert factory_re_enabled is factory
        assert factory.enabled is True

    def test_generate_client_hash_empty(self):
        assert SpannerMetricsTracerFactory._generate_client_hash("") == "000000"

    def test_generate_client_uid_exception(self, monkeypatch):
        import os

        monkeypatch.setattr(
            os, "uname", lambda: (_ for _ in ()).throw(RuntimeError("uname fail"))
        )
        assert SpannerMetricsTracerFactory._generate_client_uid() == ""

    def test_context_var_methods(self):
        mock_tracer = object()
        token = SpannerMetricsTracerFactory.set_current_tracer(mock_tracer)
        try:
            assert SpannerMetricsTracerFactory.get_current_tracer() is mock_tracer
        finally:
            SpannerMetricsTracerFactory.reset_current_tracer(token)
        assert SpannerMetricsTracerFactory.get_current_tracer() is None

    def test_without_opentelemetry(self, monkeypatch):
        import google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory as mod

        monkeypatch.setattr(mod, "HAS_OPENTELEMETRY_INSTALLED", False)
        SpannerMetricsTracerFactory._metrics_tracer_factory = None
        factory = SpannerMetricsTracerFactory(enabled=True)
        assert factory is not None
