
transport inheritance structure
_______________________________

``CloudChannelServiceTransport`` is the ABC for all transports.

- public child ``CloudChannelServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudChannelServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudChannelServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudChannelServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
