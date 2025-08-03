import pytest

# ---------- CREATE ----------

def test_create_item(client, test_data):
    post_payload = test_data["post_item"]
    response = client.post("/objects", json=post_payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == post_payload["name"]
    assert data["data"] == post_payload["data"]
    # Teardown
    client.delete(f"/objects/{data['id']}")


# ---------- READ (GET) ----------

def test_get_item_by_id(client, test_data, created_item):
    item_id = created_item["id"]
    response = client.get(f"/objects/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == created_item["name"]
    assert data["data"] == created_item["data"]


# ---------- UPDATE (PUT) ----------

def test_update_item(client, test_data, created_item):
    item_id = created_item["id"]
    put_payload = test_data["put_item"]
    response = client.put(f"/objects/{item_id}", json=put_payload)
    assert response.status_code == 200
    updated = response.json()
    assert updated["name"] == put_payload["name"]
    assert updated["data"] == put_payload["data"]


# ---------- DELETE ----------

def test_delete_item(client, test_data):
    # First, create a new item
    post_payload = test_data["post_item"]
    response = client.post("/objects", json=post_payload)
    assert response.status_code == 200
    item = response.json()
    item_id = item["id"]

    # Then delete it
    delete_response = client.delete(f"/objects/{item_id}")
    assert delete_response.status_code == 200

    # Verify that it's gone
    get_response = client.get(f"/objects/{item_id}")
    assert get_response.status_code == 404