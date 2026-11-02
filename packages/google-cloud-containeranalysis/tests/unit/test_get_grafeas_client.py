import pytest
from google.auth import credentials

from google.cloud.devtools.containeranalysis_v1.services.container_analysis import (
    ContainerAnalysisAsyncClient,
    ContainerAnalysisClient,
)


def test_get_grafeas_client():
    client = ContainerAnalysisClient(credentials=credentials.AnonymousCredentials())
    client.get_grafeas_client()


@pytest.mark.asyncio
async def test_get_grafeas_client_async():
    async_client = ContainerAnalysisAsyncClient(
        credentials=credentials.AnonymousCredentials()
    )
    async_client.get_grafeas_client()
