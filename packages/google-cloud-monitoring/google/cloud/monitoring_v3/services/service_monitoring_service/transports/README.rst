
transport inheritance structure
_______________________________

``ServiceMonitoringServiceTransport`` is the ABC for all transports.

- public child ``ServiceMonitoringServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ServiceMonitoringServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseServiceMonitoringServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ServiceMonitoringServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
