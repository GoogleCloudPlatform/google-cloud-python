
transport inheritance structure
_______________________________

``AcceleratorInterconnectMemberInstancesTransport`` is the ABC for all transports.

- public child ``AcceleratorInterconnectMemberInstancesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AcceleratorInterconnectMemberInstancesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAcceleratorInterconnectMemberInstancesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AcceleratorInterconnectMemberInstancesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
