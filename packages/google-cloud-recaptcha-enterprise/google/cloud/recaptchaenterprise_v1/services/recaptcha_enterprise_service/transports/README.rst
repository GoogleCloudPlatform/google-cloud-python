
transport inheritance structure
_______________________________

``RecaptchaEnterpriseServiceTransport`` is the ABC for all transports.

- public child ``RecaptchaEnterpriseServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``RecaptchaEnterpriseServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseRecaptchaEnterpriseServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``RecaptchaEnterpriseServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
