# tests/test_bins.py
import sys

from src.storage_bin import StorageBin
from src.algorithm import find_best_fit_bin
from src.package import Package


def test_bin_sorting():
    b1 = StorageBin(1, 50, "A1")
    b2 = StorageBin(2, 20, "B1")
    b3 = StorageBin(3, 100, "C1")

    bins = [b1, b2, b3]
    bins.sort()

    assert [b.bin_id for b in bins] == [2, 1, 3]


def test_best_fit_bin():
    bins = [
        StorageBin(1, 10, "A1"),
        StorageBin(2, 20, "B1"),
        StorageBin(3, 30, "C1"),
    ]
    bins.sort()

    pkg = Package("T123", 18, "NY")

    best_bin = find_best_fit_bin(bins, pkg.size)
    assert best_bin.bin_id == 2
