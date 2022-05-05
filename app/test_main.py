from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

valid_payload = {
        'uid': '123',
        'message': 'hello {name}',
        'variables': [{'name': 'alice'}, {'name': 'bob'}],
        'paper_type': 'foo',
        'paper_size': 'foo',
        'paper_orientation': 'foo',
        }

missing_key = {
        'uid': '123',
        'message': 'hello {name}',
        'variables': [{'name': 'alice'}, {'name': 'bob'}],
        'paper_type': 'foo',
        'paper_orientation': 'foo',
        }

def test_valid_payload():
    response = client.post("/api/v1/create/", json=valid_payload)
    assert response.status_code == 200


def test_invalid_payload():
    response = client.post("/api/v1/create/", json=missing_key)
    assert response.status_code == 200

