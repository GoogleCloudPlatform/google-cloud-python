
transport inheritance structure
_______________________________

``BareMetalSolutionTransport`` is the ABC for all transports.

- public child ``BareMetalSolutionGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``BareMetalSolutionGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseBareMetalSolutionRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``BareMetalSolutionRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
