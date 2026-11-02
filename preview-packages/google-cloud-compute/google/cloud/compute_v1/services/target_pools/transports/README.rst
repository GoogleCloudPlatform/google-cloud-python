
transport inheritance structure
_______________________________

``TargetPoolsTransport`` is the ABC for all transports.

- public child ``TargetPoolsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TargetPoolsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTargetPoolsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TargetPoolsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
