
transport inheritance structure
_______________________________

``CssProductInputsServiceTransport`` is the ABC for all transports.

- public child ``CssProductInputsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CssProductInputsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCssProductInputsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CssProductInputsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
