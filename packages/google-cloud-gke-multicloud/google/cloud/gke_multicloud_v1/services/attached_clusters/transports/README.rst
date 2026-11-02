
transport inheritance structure
_______________________________

``AttachedClustersTransport`` is the ABC for all transports.

- public child ``AttachedClustersGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AttachedClustersGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAttachedClustersRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AttachedClustersRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
