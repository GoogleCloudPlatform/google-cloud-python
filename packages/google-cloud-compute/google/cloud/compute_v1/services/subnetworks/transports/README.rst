
transport inheritance structure
_______________________________

``SubnetworksTransport`` is the ABC for all transports.

- public child ``SubnetworksGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SubnetworksGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSubnetworksRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SubnetworksRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
