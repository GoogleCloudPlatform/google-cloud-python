
transport inheritance structure
_______________________________

``MobileDeviceSubmodelServiceTransport`` is the ABC for all transports.

- public child ``MobileDeviceSubmodelServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``MobileDeviceSubmodelServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseMobileDeviceSubmodelServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``MobileDeviceSubmodelServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
