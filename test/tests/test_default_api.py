# coding: utf-8

from fastapi.testclient import TestClient




def test_pets_get(client: TestClient):
    """Test case for pets_get

    List all pets
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/pets",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

