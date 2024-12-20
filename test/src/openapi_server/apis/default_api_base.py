# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401



class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def pets_get(
        self,
    ) -> List[str]:
        ...
