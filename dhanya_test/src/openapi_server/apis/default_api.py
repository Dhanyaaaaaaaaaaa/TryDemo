# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.calculate_price200_response import CalculatePrice200Response
from openapi_server.models.calculate_price_request import CalculatePriceRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/getPrice",
    responses={
        200: {"model": CalculatePrice200Response, "description": "Successful response"},
    },
    tags=["default"],
    summary="Calculates the suggested price.",
    response_model_by_alias=True,
)
async def calculate_price(
    calculate_price_request: CalculatePriceRequest = Body(None, description=""),
) -> CalculatePrice200Response:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().calculate_price(calculate_price_request)
