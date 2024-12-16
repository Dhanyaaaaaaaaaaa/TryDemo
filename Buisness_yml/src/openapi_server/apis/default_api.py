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
from openapi_server.models.customer import Customer
from openapi_server.models.customer_create import CustomerCreate
from openapi_server.models.customer_update import CustomerUpdate


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/customers/{customerId}",
    responses={
        204: {"description": "Customer deleted successfully"},
        404: {"description": "Customer not found"},
    },
    tags=["default"],
    summary="Delete a customer",
    response_model_by_alias=True,
)
async def customers_customer_id_delete(
    customerId: str = Path(..., description="ID of the customer to delete"),
) -> None:
    """Remove a customer from the system by ID."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().customers_customer_id_delete(customerId)


@router.get(
    "/customers/{customerId}",
    responses={
        200: {"model": Customer, "description": "Customer details"},
        404: {"description": "Customer not found"},
    },
    tags=["default"],
    summary="Get customer details",
    response_model_by_alias=True,
)
async def customers_customer_id_get(
    customerId: str = Path(..., description="ID of the customer to retrieve"),
) -> Customer:
    """Retrieve details for a specific customer by ID."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().customers_customer_id_get(customerId)


@router.put(
    "/customers/{customerId}",
    responses={
        200: {"model": Customer, "description": "Customer updated successfully"},
        404: {"description": "Customer not found"},
    },
    tags=["default"],
    summary="Update a customer",
    response_model_by_alias=True,
)
async def customers_customer_id_put(
    customerId: str = Path(..., description="ID of the customer to update"),
    customer_update: CustomerUpdate = Body(None, description=""),
) -> Customer:
    """Update details for a specific customer."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().customers_customer_id_put(customerId, customer_update)


@router.get(
    "/customers",
    responses={
        200: {"model": List[Customer], "description": "A list of customers"},
    },
    tags=["default"],
    summary="Get a list of customers",
    response_model_by_alias=True,
)
async def customers_get(
) -> List[Customer]:
    """Retrieve a list of all customers in the system."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().customers_get()


@router.post(
    "/customers",
    responses={
        201: {"model": Customer, "description": "Customer created successfully"},
    },
    tags=["default"],
    summary="Create a new customer",
    response_model_by_alias=True,
)
async def customers_post(
    customer_create: CustomerCreate = Body(None, description=""),
) -> Customer:
    """Add a new customer to the system."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().customers_post(customer_create)
