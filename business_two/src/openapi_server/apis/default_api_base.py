# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.customer import Customer
from openapi_server.models.customer_create import CustomerCreate
from openapi_server.models.customer_update import CustomerUpdate


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def customers_customer_id_delete(
        self,
        customerId: str,
    ) -> None:
        """Remove a customer from the system by ID."""
        ...


    async def customers_customer_id_get(
        self,
        customerId: str,
    ) -> Customer:
        """Retrieve details for a specific customer by ID."""
        ...


    async def customers_customer_id_put(
        self,
        customerId: str,
        customer_update: CustomerUpdate,
    ) -> Customer:
        """Update details for a specific customer."""
        ...


    async def customers_get(
        self,
    ) -> List[Customer]:
        """Retrieve a list of all customers in the system."""
        ...


    async def customers_post(
        self,
        customer_create: CustomerCreate,
    ) -> Customer:
        """Add a new customer to the system."""
        ...
