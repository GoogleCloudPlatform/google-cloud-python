
transport inheritance structure
_______________________________

``GkeInferenceQuickstartTransport`` is the ABC for all transports.

- public child ``GkeInferenceQuickstartGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``GkeInferenceQuickstartGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseGkeInferenceQuickstartRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``GkeInferenceQuickstartRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
