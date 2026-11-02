
transport inheritance structure
_______________________________

``InstanceGroupManagersTransport`` is the ABC for all transports.

- public child ``InstanceGroupManagersGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``InstanceGroupManagersGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseInstanceGroupManagersRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``InstanceGroupManagersRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
