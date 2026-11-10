
transport inheritance structure
_______________________________

``ForecastAdjustmentServiceTransport`` is the ABC for all transports.

- public child ``ForecastAdjustmentServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ForecastAdjustmentServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseForecastAdjustmentServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ForecastAdjustmentServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
