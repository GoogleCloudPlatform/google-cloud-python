
transport inheritance structure
_______________________________

``AddressValidationTransport`` is the ABC for all transports.

- public child ``AddressValidationGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AddressValidationGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAddressValidationRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AddressValidationRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
