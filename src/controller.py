# src/controller.py
# Main WarehouseController Singleton combining all components

from src.algorithm import find_best_fit_bin, can_fit_packages
from src.package import Package
from src.storage_bin import StorageBin
from database.database import Database   # because database is a separate folder


class WarehouseController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized") and self._initialized:
            return
        self._initialized = True

        # Components
        self.bin_inventory = []   # sorted list of StorageBin
        self.conveyor_queue = []  # FIFO queue
        self.loading_stack = []   # LIFO stack

        # Database
        self.db = Database()
        self.db.create_tables()

    # --------------------------------------------------
    # System Initialization
    # --------------------------------------------------
    def initialize_system(self):
        print("Warehouse System Online ✔")

    # --------------------------------------------------
    # Queue Operations (FIFO)
    # --------------------------------------------------
    def add_package_to_queue(self, package):
        self.conveyor_queue.append(package)

    def get_next_package(self):
        if self.conveyor_queue:
            return self.conveyor_queue.pop(0)
        return None

    # --------------------------------------------------
    # Stack Operations (LIFO)
    # --------------------------------------------------
    def load_truck(self, package):
        self.loading_stack.append(package)

    def rollback_load(self):
        if self.loading_stack:
            return self.loading_stack.pop()
        return None

    # --------------------------------------------------
    # Bin Allocation
    # --------------------------------------------------
    def assign_bin(self, package):
        bin_obj = find_best_fit_bin(self.bin_inventory, package.size)
        if not bin_obj:
            print("❌ No bin available for", package)
            return None

        if bin_obj.occupy_space(package.size):
            print(f"✔ Package {package.tracking_id} stored in bin {bin_obj.bin_id}")
            self.db.log_event(package.tracking_id, bin_obj.bin_id, "STORED")
            return bin_obj
        else:
            print("❌ Bin found but insufficient free space.")
            return None

    # --------------------------------------------------
    # Helper: Add new bins
    # --------------------------------------------------
    def add_storage_bin(self, bin_id, capacity, location):
        new_bin = StorageBin(bin_id, capacity, location)
        self.bin_inventory.append(new_bin)

        # Keep bins sorted for binary search
        self.bin_inventory.sort()
        return new_bin

    # --------------------------------------------------
    # Shipment Planner
    # --------------------------------------------------
    def check_truck_fit(self, packages, space):
        return can_fit_packages(packages, space)

    # --------------------------------------------------
    # Shutdown
    # --------------------------------------------------
    def shutdown(self):
        self.db.close()
        print("System shutting down...")
if __name__ == "__main__":
    controller = WarehouseController()
    controller.initialize_system()
 
