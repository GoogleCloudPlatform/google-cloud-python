
transport inheritance structure
_______________________________

``TextSuggestionsServiceTransport`` is the ABC for all transports.

- public child ``TextSuggestionsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``TextSuggestionsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseTextSuggestionsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``TextSuggestionsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
