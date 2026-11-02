
transport inheritance structure
_______________________________

``CloudShellServiceTransport`` is the ABC for all transports.

- public child ``CloudShellServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudShellServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudShellServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudShellServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
