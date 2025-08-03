import pytest
import json
import os
from utils.api_client import APIClient

# Fixture for reusable API client instance
@pytest.fixture(scope="session")
def client():
    return APIClient()

# Fixture to load test data from JSON file once per session
@pytest.fixture(scope="session")
def test_data():
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "test_data.json")
    with open(data_path) as f:
        return json.load(f)

# Fixture to create a test item and automatically clean up after test
@pytest.fixture
def created_item(client, test_data):
    post_payload = test_data["post_item"]
    response = client.post("/objects", json=post_payload)
    assert response.status_code == 200
    item = response.json()
    yield item  # Provide the item to the test
    client.delete(f"/objects/{item['id']}")  # Teardown after test