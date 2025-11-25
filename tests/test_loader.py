import sys


from src.controller import WarehouseController
from src.package import Package


def test_queue_operations():
    c = WarehouseController()

    p1 = Package("A1", 10, "DEL")
    p2 = Package("A2", 20, "MUM")

    c.add_package_to_queue(p1)
    c.add_package_to_queue(p2)

    assert c.get_next_package().tracking_id == "A1"
    assert c.get_next_package().tracking_id == "A2"


def test_stack_operations():
    c = WarehouseController()

    p1 = Package("B1", 5, "BLR")
    p2 = Package("B2", 7, "HYD")

    c.load_truck(p1)
    c.load_truck(p2)

    removed = c.rollback_load()
    assert removed.tracking_id == "B2"

