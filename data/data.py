from abc import ABC, abstractmethod


class Data(ABC):

    @abstractmethod
    def get_key(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def __gt__(self, other):
        raise NotImplementedError()

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError()
    