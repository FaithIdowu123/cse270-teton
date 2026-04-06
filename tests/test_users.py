# test_users.py

import requests

def test_users_endpoint_empty_response():
    url = "http://127.0.0.1:8000/users/"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    response = requests.get(url, params=params)

    # Verify HTTP status code is 200
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    # Verify response body is empty
    assert response.text.strip() == "", f"Expected empty response, got: {response.text}"

def test_users_endpoint_unauthorized():
    url = "http://127.0.0.1:8000/users/"
    params = {
        "username": "admin",
        "password": "admin"  # incorrect password
    }

    response = requests.get(url, params=params)

    # Verify HTTP status code is 401
    assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"

    # Verify response body is empty
    assert response.text.strip() == "", f"Expected empty response, got: {response.text}"