from abc import ABC, abstractmethod


class TableTripMixin(ABC):

    @classmethod
    @abstractmethod
    def create(cls, record, schema):
        pass

    @classmethod
    @abstractmethod
    def retreive(cls, id):
        pass

    @classmethod
    @abstractmethod
    def update(cls, record, delta):
        pass

    @classmethod
    @abstractmethod
    def delete(cls, id):
        pass