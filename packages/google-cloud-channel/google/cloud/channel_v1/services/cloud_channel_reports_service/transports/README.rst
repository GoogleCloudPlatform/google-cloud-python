
transport inheritance structure
_______________________________

``CloudChannelReportsServiceTransport`` is the ABC for all transports.

- public child ``CloudChannelReportsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudChannelReportsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudChannelReportsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudChannelReportsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
