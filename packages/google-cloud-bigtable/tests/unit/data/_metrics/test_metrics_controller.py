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

import mock


class TestBigtableClientSideMetricsController:
    def _make_one(self, *args, **kwargs):
        from google.cloud.bigtable.data._metrics import (
            BigtableClientSideMetricsController,
        )

        return BigtableClientSideMetricsController(*args, **kwargs)

    def test_ctor_defaults(self):
        """
        should create instance with GCP Exporter handler by default
        """
        instance = self._make_one()
        assert len(instance.handlers) == 0

    def ctor_custom_handlers(self):
        """
        if handlers are passed to init, use those instead
        """
        custom_handler = object()
        custom_interceptor = object()
        controller = self._make_one(custom_interceptor, handlers=[custom_handler])
        assert controller.interceptor == custom_interceptor
        assert len(controller.handlers) == 1
        assert controller.handlers[0] is custom_handler

    def test_add_handler(self):
        """
        New handlers should be added to list
        """
        controller = self._make_one(handlers=[object()])
        initial_handler_count = len(controller.handlers)
        new_handler = object()
        controller.add_handler(new_handler)
        assert len(controller.handlers) == initial_handler_count + 1
        assert controller.handlers[-1] is new_handler

    def test_create_operation_mock(self):
        """
        All args should be passed through, as well as the handlers
        """
        from google.cloud.bigtable.data._metrics import ActiveOperationMetric

        controller = self._make_one(handlers=[object()])
        arg = object()
        kwargs = {"a": 1, "b": 2}
        with mock.patch(
            "google.cloud.bigtable.data._metrics.ActiveOperationMetric.__init__"
        ) as mock_op:
            mock_op.return_value = None
            op = controller.create_operation(arg, **kwargs)
            assert isinstance(op, ActiveOperationMetric)
            assert mock_op.call_count == 1
            mock_op.assert_called_with(arg, **kwargs, handlers=controller.handlers)

    def test_create_operation(self):
        from google.cloud.bigtable.data._metrics import ActiveOperationMetric

        handler = object()
        expected_type = object()
        expected_is_streaming = True
        expected_zone = object()
        controller = self._make_one(handlers=[handler])
        op = controller.create_operation(
            expected_type, is_streaming=expected_is_streaming, zone=expected_zone
        )
        assert isinstance(op, ActiveOperationMetric)
        assert op.op_type is expected_type
        assert op.is_streaming is expected_is_streaming
        assert op.zone is expected_zone
        assert len(op.handlers) == 1
        assert op.handlers[0] is handler

    def test_close(self):
        handlers = [mock.Mock() for _ in range(3)]
        controller = self._make_one(handlers=handlers)
        controller.close()
        for handler in handlers:
            handler.close.assert_called_once()
