
transport inheritance structure
_______________________________

``DeploymentTransport`` is the ABC for all transports.

- public child ``DeploymentGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``DeploymentGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseDeploymentRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``DeploymentRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
