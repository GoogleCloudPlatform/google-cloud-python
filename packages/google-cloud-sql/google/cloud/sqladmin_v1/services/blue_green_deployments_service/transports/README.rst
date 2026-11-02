
transport inheritance structure
_______________________________

``BlueGreenDeploymentsServiceTransport`` is the ABC for all transports.

- public child ``BlueGreenDeploymentsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BlueGreenDeploymentsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBlueGreenDeploymentsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BlueGreenDeploymentsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
