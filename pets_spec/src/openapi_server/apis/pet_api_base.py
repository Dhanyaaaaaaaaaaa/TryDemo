# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.api_response import ApiResponse
from openapi_server.models.pet import Pet
from openapi_server.security_api import get_token_petstore_auth, get_token_api_key

class BasePetApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePetApi.subclasses = BasePetApi.subclasses + (cls,)
    async def add_pet(
        self,
        pet: Pet,
    ) -> Pet:
        """Add a new pet to the store"""
        ...


    async def delete_pet(
        self,
        petId: int,
        api_key: str,
    ) -> None:
        """delete a pet"""
        ...


    async def find_pets_by_status(
        self,
        status: str,
    ) -> List[Pet]:
        """Multiple status values can be provided with comma separated strings"""
        ...


    async def find_pets_by_tags(
        self,
        tags: List[str],
    ) -> List[Pet]:
        """Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing."""
        ...


    async def get_pet_by_id(
        self,
        petId: int,
    ) -> Pet:
        """Returns a single pet"""
        ...


    async def update_pet(
        self,
        pet: Pet,
    ) -> Pet:
        """Update an existing pet by Id"""
        ...


    async def update_pet_with_form(
        self,
        petId: int,
        name: str,
        status: str,
    ) -> None:
        """"""
        ...


    async def upload_file(
        self,
        petId: int,
        additional_metadata: str,
        body: str,
    ) -> ApiResponse:
        """"""
        ...
