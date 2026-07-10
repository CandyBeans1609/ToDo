from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/users/register",
        json={
            "username": "akanksha",
            "email": "ak@example.com",
            "password": "Password123"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "akanksha"
    assert data["email"] == "ak@example.com"