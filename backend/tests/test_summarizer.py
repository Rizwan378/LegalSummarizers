import pytest
from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

def test_summarize_endpoint_invalid_file():
    response = client.post("/api/v1/summarize", files={"file": ("test.txt", b"invalid content")})
    assert response.status_code == 400
    assert "Only CSV files are allowed" in response.json()["detail"]

def test_summarize_endpoint_empty_file():
    """Test summarizer with empty CSV file."""
    response = client.post("/api/v1/summarize", files={"file": ("empty.csv", b"")})
    assert response.status_code == 400
    assert "Invalid CSV content" in response.json()["detail"]
    logger.info("Tested empty file upload successfully")

def test_summarize_endpoint_empty_file():
    """Test summarizer with empty CSV file."""
    response = client.post("/api/v1/summarize", files={"file": ("empty.csv", b"")})
    assert response.status_code == 400
    assert "Invalid CSV content" in response.json()["detail"]
    logger.info("Tested empty file upload successfully")
