
transport inheritance structure
_______________________________

``CloudDeployTransport`` is the ABC for all transports.

- public child ``CloudDeployGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudDeployGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudDeployRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudDeployRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
