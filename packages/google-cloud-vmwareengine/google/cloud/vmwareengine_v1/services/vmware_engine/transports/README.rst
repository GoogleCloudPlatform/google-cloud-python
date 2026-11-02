
transport inheritance structure
_______________________________

``VmwareEngineTransport`` is the ABC for all transports.

- public child ``VmwareEngineGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``VmwareEngineGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseVmwareEngineRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``VmwareEngineRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
