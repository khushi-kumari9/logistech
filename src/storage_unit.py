from abc import ABC, abstractmethod

class StorageUnit(ABC):

    def __init__(self, capacity):
        self.capacity = capacity
        self.used = 0

    @abstractmethod
    def occupy_space(self, amount):
        pass

    @abstractmethod
    def free_space(self, amount):
        pass
