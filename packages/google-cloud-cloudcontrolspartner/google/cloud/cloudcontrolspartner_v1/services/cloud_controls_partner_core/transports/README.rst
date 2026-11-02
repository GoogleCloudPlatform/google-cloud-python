
transport inheritance structure
_______________________________

``CloudControlsPartnerCoreTransport`` is the ABC for all transports.

- public child ``CloudControlsPartnerCoreGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudControlsPartnerCoreGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudControlsPartnerCoreRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudControlsPartnerCoreRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
