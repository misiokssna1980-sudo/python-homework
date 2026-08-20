from encodings import cp1006

import pytest
import uuid
from api_client import YougileProjectAPI

@pytest.fixture(scope="session")
def api_client():
    base_url = "https://ru.yougile.com/api-v2"
    token = "89993c00-8586-4cd3-89da-b1564df1bb87"
    return YougileProjectAPI(base_url, token)

@pytest.fixture
def unique_title():
    return f"ГосУслуги_{uuid.uuid4().hex[:8]}"