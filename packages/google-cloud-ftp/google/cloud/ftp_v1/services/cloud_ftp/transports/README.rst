
transport inheritance structure
_______________________________

``CloudFtpTransport`` is the ABC for all transports.

- public child ``CloudFtpGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``CloudFtpGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseCloudFtpRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``CloudFtpRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
