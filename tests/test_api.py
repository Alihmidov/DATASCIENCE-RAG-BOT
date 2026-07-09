from fastapi.testclient import TestClient
from app.main import app
import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

client = TestClient(app)

@pytest.mark.skip_if_no_ollama
def test_end_point_exists():
    response = client.post("/chat",json={"query": "Hello"})
    assert response.status_code == 200
    
def test_query_type():
    response = client.post("/chat",json={"query": 12345})
    assert response.status_code == 422