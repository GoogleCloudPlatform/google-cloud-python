
transport inheritance structure
_______________________________

``NodeGroupControllerTransport`` is the ABC for all transports.

- public child ``NodeGroupControllerGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``NodeGroupControllerGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseNodeGroupControllerRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``NodeGroupControllerRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
