
transport inheritance structure
_______________________________

``PhoneNumbersTransport`` is the ABC for all transports.

- public child ``PhoneNumbersGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``PhoneNumbersGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BasePhoneNumbersRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``PhoneNumbersRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
