
transport inheritance structure
_______________________________

``CloudFunctionsServiceTransport`` is the ABC for all transports.

- public child ``CloudFunctionsServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudFunctionsServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudFunctionsServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudFunctionsServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
