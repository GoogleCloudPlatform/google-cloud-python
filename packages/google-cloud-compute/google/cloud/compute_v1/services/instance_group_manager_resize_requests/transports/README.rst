
transport inheritance structure
_______________________________

``InstanceGroupManagerResizeRequestsTransport`` is the ABC for all transports.

- public child ``InstanceGroupManagerResizeRequestsGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``InstanceGroupManagerResizeRequestsGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseInstanceGroupManagerResizeRequestsRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``InstanceGroupManagerResizeRequestsRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
