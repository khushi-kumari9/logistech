# storage_bin.py

from src.storage_unit import StorageUnit

class StorageBin(StorageUnit):
    def __init__(self, bin_id, capacity, location_code):
        super().__init__(capacity)
        self.bin_id = bin_id
        self.capacity = capacity
        self.location_code = location_code
        self.used_space = 0

    def __lt__(self, other):
        # Allows sorting bins by capacity for binary search
        return self.capacity < other.capacity

    def is_available(self, package_size):
        return (self.capacity - self.used_space) >= package_size

    def occupy_space(self, amount):
        if self.is_available(amount):
            self.used_space += amount
            return True
        return False

    def free_space(self):
        self.used_space = 0
