
transport inheritance structure
_______________________________

``ProposalServiceTransport`` is the ABC for all transports.

- public child ``ProposalServiceGrpcTransport`` for sync gRPC transport (defined in ``grpc.py``).
- public child ``ProposalServiceGrpcAsyncIOTransport`` for async gRPC transport (defined in ``grpc_asyncio.py``).
- private child ``_BaseProposalServiceRestTransport`` for base REST transport with inner classes ``_BaseMETHOD`` (defined in ``rest_base.py``).
- public child ``ProposalServiceRestTransport`` for sync REST transport with inner classes ``METHOD`` derived from the parent's corresponding ``_BaseMETHOD`` classes (defined in ``rest.py``).
