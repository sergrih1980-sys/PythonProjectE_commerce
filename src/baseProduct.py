from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_base_product(cls, *args, **kwargs):
        pass
