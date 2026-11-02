
transport inheritance structure
_______________________________

``SipTrunksTransport`` is the ABC for all transports.

- public child ``SipTrunksGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``SipTrunksGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseSipTrunksRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``SipTrunksRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
