# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.calculate_price200_response import CalculatePrice200Response
from openapi_server.models.calculate_price_request import CalculatePriceRequest


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def calculate_price(
        self,
        calculate_price_request: CalculatePriceRequest,
    ) -> CalculatePrice200Response:
        ...
