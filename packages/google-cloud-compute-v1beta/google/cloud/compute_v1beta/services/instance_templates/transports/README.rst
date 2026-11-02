
transport inheritance structure
_______________________________

``InstanceTemplatesTransport`` is the ABC for all transports.

- public child ``InstanceTemplatesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``InstanceTemplatesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseInstanceTemplatesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``InstanceTemplatesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
