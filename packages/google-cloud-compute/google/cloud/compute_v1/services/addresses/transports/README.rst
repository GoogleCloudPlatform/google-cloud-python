
transport inheritance structure
_______________________________

``AddressesTransport`` is the ABC for all transports.

- public child ``AddressesGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``AddressesGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseAddressesRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``AddressesRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
