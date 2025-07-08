# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.calculate_price200_response import CalculatePrice200Response  # noqa: F401
from openapi_server.models.calculate_price_request import CalculatePriceRequest  # noqa: F401


def test_calculate_price(client: TestClient):
    """Test case for calculate_price

    Calculates the suggested price.
    """
    calculate_price_request = openapi_server.CalculatePriceRequest()

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/getPrice",
    #    headers=headers,
    #    json=calculate_price_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

