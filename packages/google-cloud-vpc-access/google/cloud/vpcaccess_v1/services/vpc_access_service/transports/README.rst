
transport inheritance structure
_______________________________

``VpcAccessServiceTransport`` is the ABC for all transports.

- public child ``VpcAccessServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``VpcAccessServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseVpcAccessServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``VpcAccessServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
