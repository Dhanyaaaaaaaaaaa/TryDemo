# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.customer import Customer  # noqa: F401
from openapi_server.models.customer_create import CustomerCreate  # noqa: F401
from openapi_server.models.customer_update import CustomerUpdate  # noqa: F401


def test_customers_customer_id_delete(client: TestClient):
    """Test case for customers_customer_id_delete

    Delete a customer
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/customers/{customerId}".format(customerId='customer_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_customers_customer_id_get(client: TestClient):
    """Test case for customers_customer_id_get

    Get customer details
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/customers/{customerId}".format(customerId='customer_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_customers_customer_id_put(client: TestClient):
    """Test case for customers_customer_id_put

    Update a customer
    """
    customer_update = {"phone":"phone","name":"name","email":"email"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/customers/{customerId}".format(customerId='customer_id_example'),
    #    headers=headers,
    #    json=customer_update,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_customers_get(client: TestClient):
    """Test case for customers_get

    Get a list of customers
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/customers",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_customers_post(client: TestClient):
    """Test case for customers_post

    Create a new customer
    """
    customer_create = {"phone":"phone","name":"name","email":"email"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/customers",
    #    headers=headers,
    #    json=customer_create,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

